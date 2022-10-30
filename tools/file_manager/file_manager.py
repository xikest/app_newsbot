import os
from pathlib import Path

class FileMgt():
  """
  #루트 경로 생성
  root_dir = '/content/drive/MyDrive/fmgt'
  fmgt = FileMgt(root_dir)
  
  #폴더 생성
  fmgt.mkdir('data')
  fmgt.mkdir('img')
  >>/content/drive/MyDrive/fmgt/data
  >>/content/drive/MyDrive/fmgt/img
  
  #하위 폴더 확인
  fmgt['root'].get_dir_list(only_name=True)
  >>['data', 'img']
  
  # 파일 다운로드
  url='https://data.nasdaq.com/api/v3/databases/MULTPL/metadata?api_key=FKTM3JuTxzCy-6cgwWwt'
  fmgt['data'].download_from_web(url, unzip=True)
  >>['MULTPL_metadata']
  
  # 폴더 내 파일 확인
  fmgt['data'].get_file_list(only_name=True)
  >>['MULTPL_metadata']
  
  fmgt['img'].get_dir_list(only_name=True)
  >>[]
  
  # 폴더 이동
  fmgt['data'].chdir()

  # 현재 폴더 경로 확인
  fmgt.getCwd
  >>/content/drive/MyDrive/fmgt/data
  
  # 현재 경로 얻어오기
  fmgt.getDir
  
  # 파일 열기
  fmgt['data'].open_file('sdsd.txt')
  
  # 모든 경로 보기
  fmgt()
  
  # pickle 데이터 저장
  save_to_pickle(data, file_name)
  
  # pickle 데이터 불러오기
  load_from_pickle(file_name)
  
  """

  def __init__(self, dir_root=None):
    self._path_dict = dict()
    self.mkDir(dir_root, key='root')
    self.getDir('root').chDir()
    
  def __call__(self):
    return self._path_dict
  
  def getDir(self, dir_key):
    self._dir = self._path_dict.get(dir_key)
    print(self._dir)
    return self
  
  def setDir(self, key, dir_path):
    self._path_dict[key] = dir_path
    return print(self._path_dict[key])
    
  
  def chDir(self):
    os.chdir(self._dir)
    return self
    
  def mkDir(self, dir_name:str=None, key:str=None):
      if dir_name is None: path = self.getCwd
      else: path = self.getCwd/dir_name
      if key is None: key = dir_name
      if not path.exists(): path.mkdir(parents=True)
      self.setDir(key, path)
      return self
    
  @property
  def getCwd(self):
    return Path.cwd()
  
  @property
  def getDataPath(self):
    return self._path_dict.get('data')
  

  def getFileList(self, pattern='*', only_name=False):
    if only_name is True : return [child.stem for child in self.getCwd.glob(pattern) if child.is_file()]
    else: return [child for child in self.getCwd.glob(pattern) if child.is_file()]

  def getDirList(self, pattern='*', only_name=False):
    if only_name is True :  return [child.stem for child in self.getCwd.glob(pattern) if child.is_dir()]
    else: return [child for child in self.getCwd.glob(pattern) if child.is_dir()]
