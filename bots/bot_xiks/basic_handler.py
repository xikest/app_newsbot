from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
# from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
# ================================================================================
# = 이벤트 작성
# ================================================================================

class BasicHandler:

    @staticmethod
    def start():
        def _start(update: Update, context: CallbackContext):
            update.message.reply_text(text="I'm a bot, please talk to me!")
        return CommandHandler('start', _start)
        
    @staticmethod
    def help():
        def _help(update: Update, context: CallbackContext):
            update.message.reply_text(text = """shiller_ratio - 쉴러 PE Ratio
market_pattern_w - market pattern_w
market_pattern_m - market pattern_m
cpi - 소비자 물가 지수
ppi - 생산자 물가 지수
ism - ISM 서비스 지수
diffusion_index_philadelphia - 필라델피아 기업 경기 전망 보고서
reatail_sales - 소매 판매 보고서
new_residential_sales - 신규 주택 판매
durable_goods - 내구주 수주
pce - 개인 소비 지출
employment_cost_index - 고용 비용 지수
gdp - GDP
jolt - 고용 이직 현황
adp_employment_report - ADP 고용 보고서
inventories_sales_ratio - 기업재고
fed - FED(자산, M2V, FED rate)
cfnai - 국가활동지수
empirestate_manufacturing - 엠파이어스테이트_제조업
existing_home_sales - 기존 주택
industrial_production_capacity - 산업 생산 및 설비 가동률
productivity - 생산성과 단위비용
initial_claims - 실업 청구
ecommerce - 전자 상거래 
import_export - 수출입
cass_freight_index - 캐스 화물 지수
new_housing - 신규 주택 착공
consumer_credit - 소비자 신용
cpi_bra - CPI 브라질
cpi_chn - CPI 중국
cpi_de - CPI 독일
cpi_inida - CPI 인도
cpi_jpn - CPI 일본
cpi_kr - CPI 한국
bs_stock - ticker를 입력해 주세요.""")
        return CommandHandler('help', _help)


    # def help():
    #     async def _help(update: Update, context: CallbackContext):
    #         await  update.message.reply_text(text = "shiller_ratio - 쉴러 PE Ratio\n market_pattern_w - market pattern_w\n market_pattern_m - market pattern_m\n cpi - 소비자 물가 지수\n ppi - 생산자 물가 지수\n ism - ISM 서비스 지수\n diffusion_index_philadelphia - 필라델피아 기업 경기 전망 보고서\n reatail_sales - 소매 판매 보고서\n new_residential_sales - 신규 주택 판매\n durable_goods - 내구주 수주 \n pce - 개인 소비 지출\n employment_cost_index - 고용 비용 지수\n gdp -gdp \n jolt - 고용 이직 현황 \n adp_employment_report - ADP 고용 보고서 \n inventories_sales_ratio - 기업재고 \n fed - FED \n cfnai - 국가활동지수\n empirestate_manufacturing - 엠파이어스테이트_제조업\n existing_home_sales - 기존 주택\n industrial_production_capacity - 산업 생산 및 설비 가동률\n productivity - 생산성과 단위비용\n bs_stock - ticker를 입력해 주세요.")
    #     return CommandHandler('help', _help)


 
  
    
    

    # @staticmethod
    # def echo():
    #     def _echo(update: Update, context: CallbackContext):
    #         update.message.reply_text(text=update.message.text)
    #     return MessageHandler(Filters.text & (~Filters.command), _echo)
    
    @staticmethod
    def caps():
        def _caps(update: Update, context: CallbackContext):
            text_caps = ' '.join(context.args).upper()
            update.message.reply_text(text=text_caps)
        return CommandHandler('caps', _caps)  
    
    
    @staticmethod  
    def inline_caps():
        def _inline_caps(update: Update, context: CallbackContext):
            query = update.inline_query.query
            if not query:
                return
            results = []
            results.append(
                InlineQueryResultArticle(
                    id=query.upper(),
                    title='Caps',
                    input_message_content=InputTextMessageContent(query.upper())
                )
            )
            context.bot.answer_inline_query(update.inline_query.id, results)
        return InlineQueryHandler(_inline_caps)

    # @staticmethod      
    # def unknown():
    #     def _unknown(update: Update, context: CallbackContext):
    #         update.message.reply_text(text="Sorry, I didn't understand that command.")
    #     return MessageHandler(Filters.command, _unknown)

    
    

        # # message reply function
        # @staticmethod
        # def get_message(update, context) :
        #     cont:Context
        #     user_text = update.message.text #
        #     if user_text == "안녕": 
        #         update.message.reply_text(text="안녕 하세요") 
        #     elif user_text == "일정": 
        #         update.message.reply_text(text="준비 중입니다.")
        #     # elif user_text == "shir": 
        #     #     update.message.reply_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop())
        #     # elif user_text == "mkptn": 
        #     #     update.message.reply_photo(photo=SrcMacro.Market.pattern().content.pop()) 
  
        #     else:
        #         update.message.reply_text('아직은 학습 중입니다.')

        # # help reply function
        # @staticmethod
        # def help_command(update, context) :
        #     update.message.reply_text("무엇을 도와드릴까요?")
          
           
        # # shri reply function
        # @staticmethod
        # def shri_command(update, context) :
        #         update.message.reply_text("잠시만 기다려주세요.")
        #         for content in SrcMacro.ShillerRatio.compareWithPrice():
        #             while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
        
        # # mkptn reply function
        # @staticmethod
        # def mkptn_command(update, context) :
        #         update.message.reply_text("잠시만 기다려주세요.")
        #         for content in SrcMacro.Market.pattern(): 
        #             while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
            
        # # cpi reply function
        # @staticmethod
        # def cpi_command(update, context) :
        #         update.message.reply_text("잠시만 기다려주세요.")
        #         for content in SrcMacro.Macro.cpi(): 
        #             while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
            
        # # reatailSales  reply function
        # @staticmethod
        # def reatailSales_command(update, context) :
        #         update.message.reply_text("잠시만 기다려주세요.")
        #         for content in SrcMacro.Macro.reatailSales(): 
        #             while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
                    
                    
                    
        # @staticmethod
        # def get_photo(update, context): 
        #     photo = context.bot.get_file(
        #                 update.message.photo[-1].file_id)
        #     photo.download()

        # # file reply function
        # @staticmethod
        # def get_file(update, context) :
        #     file_id_short = update.message.document.file_id
        #     file_url =update.message.document.file_name
        #     context.bot.getFile(file_id_short).download(file_url)
        #     update.message.reply_text('file saved')
            
        # @staticmethod
        # def btns_task(update, context):  #task 버튼을 추가하는 함수입니다.
        #     task_buttons = [
        #         [
        #             InlineKeyboardButton("Shiller Ratio", callback_data=1 ), InlineKeyboardButton("market pattern", callback_data=2 )
        #             ], 
        #         [
        #             InlineKeyboardButton("작업3", callback_data=3 ), InlineKeyboardButton("작업4", callback_data=4 )
        #             ], 
        #         [
        #             InlineKeyboardButton("종료", callback_data=9 )
        #             ]
        #         ]
        #     reply_markup = InlineKeyboardMarkup( task_buttons )
        #     context.bot.send_message(
        #         chat_id=update.message.chat_id,
        #         text="작업을 선택해주세요.",
        #         reply_markup=reply_markup
        #         )
            
        # @staticmethod
        # def btns_action(update, context): #버튼을 클릭했을 때 실행되는 함수
        #     query = update.callback_query
        #     data = query.data
            
        #     context.bot.send_chat_action(
        #         chat_id=update.effective_user.id,
        #         action=ChatAction.TYPING
        #         )
        #     if data == "9":
        #             context.bot.edit_message_text(text=f"작업이 종료되었습니다.",chat_id=query.message.chat_id, message_id=query.message.message_id)
        #         # elfif data == "2": context.bot.send_photo(text=f"작업이 종료되었습니다.",chat_id=query.message.chat_id, message_id=query.message.message_id)
        #     elif  data == "1": 
        #             context.bot.send_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop(), chat_id=query.message.chat_id)
                    
        #             # context.bot.send_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop(), chat_id=query.message.chat_id)
        #     elif data == "2": context.bot.send_photo(photo=SrcMacro.Market.pattern().content.pop(), chat_id=query.message.chat_id)
        #     else:
        #         context.bot.edit_message_text(
        #             text=f"[{data}] 작업을 완료하였습니다.",
        #             chat_id=query.message.chat_id,
        #             message_id=query.message.message_id
        #         )
