import asyncio
import logging
import datetime
from typing import AsyncGenerator
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from bot.definition_obj import Context

async def get_page_content(session: aiohttp.ClientSession, url: str) -> tuple[str, str]:
    """
    주어진 URL에서 비동기적으로 웹 페이지의 제목과 본문 일부를 추출합니다.
    (주의: 본문 추출은 RSS 피드에 내용이 포함된 경우에 한정적으로 사용)
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        async with session.get(url, headers=headers, timeout=10) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            title = soup.find('title').text.strip() if soup.find('title') else 'No Title'
            
            # RSS 피드 내에 content가 있을 경우를 대비한 필드.
            # 웹 크롤링으로 본문을 가져오는 것은 사이트별 정책 확인이 필요.
            # 여기서는 공개된 RSS의 'content'나 'description' 필드를 활용하는 것을 가정.
            content = "" # 필요시 로직 추가
            
            return title, content
            
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        logging.warning(f"페이지 콘텐츠를 가져오는 데 실패했습니다: {url}, 오류: {e}")
        return "Failed to fetch title", ""
    except Exception as e:
        logging.error(f"페이지 처리 중 예기치 않은 오류 발생: {url}, 오류: {e}")
        return "Processing Error", ""


class NEWS:
    def __init__(self, chat_id:str, src:str, name:str, url:str, class_key:str, verbose:bool=False, *args, **kwargs):
        self.chat_id = chat_id
        self.src = src
        self.verbose = verbose
        self.name = name
        self.url = url
        self.class_key = class_key

    async def generator(self) -> AsyncGenerator:
        logging.info(f"'{self.name}' 피드 가져오기 시작: {datetime.datetime.now()}")
        try:
            if self.src == 'web':
                async with aiohttp.ClientSession() as session:
                    links = await WebScraper(session).get_links_general(
                        url=self.url,
                        class_key=self.class_key,
                        condition=lambda href: href and (href.startswith('http') or href.startswith('/'))
                    )
                    for link in links:
                        # 상대 경로일 경우 절대 경로로 변환
                        if link.startswith('/'):
                            parsed_uri = urlparse(self.url)
                            base_url = f'{parsed_uri.scheme}://{parsed_uri.netloc}'
                            article_link = base_url + link
                        else:
                            article_link = link
                            
                        title, _ = await get_page_content(session, article_link)
                        
                        if title and "Failed" not in title and "Error" not in title:
                            yield Context(label=f'{self.name}', title=title, link=article_link, bot_chat_id=self.chat_id, dtype='msg')

        except Exception as e:
            logging.error(f"'{self.name}' 피드 처리 중 심각한 오류 발생: {e}")
        finally:
            logging.info(f"'{self.name}' 피드 처리 완료: {datetime.datetime.now()}")


class WebScraper:
    def __init__(self, session: aiohttp.ClientSession, base_url=None):
        self.session = session
        self.base_url = base_url

    async def get_links_general(self, url, class_key: str, condition=lambda href: True):
        full_url = self.base_url + url if self.base_url and not url.startswith('http') else url
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            async with self.session.get(full_url, headers=headers, timeout=15) as response:
                response.raise_for_status()
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                elements = soup.find_all(attrs={'class': class_key})
                links = []
                for element in elements:
                    for link in element.find_all('a'):
                        href = link.attrs.get('href')
                        if condition(href):
                            links.append(href)
                return list(dict.fromkeys(links)) # 중복 제거
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            logging.warning(f"링크를 가져오는 데 실패했습니다: {url}, 오류: {e}")
            return []