# Computer Vision Project : deep learning & keras

## GPU 환경설정 설정

- 장치관리자 : NVIDIA grapic card 확인, 드라이버 업데이트
- CUDA Toolkit 10.0 설치 : [tensorflow gpu install guide > Software requirements 참조](https://www.tensorflow.org/install/gpu#software_requirements) > [CUDA Toolkit 10.0 Download](https://developer.nvidia.com/cuda-10.0-download-archive)
- 환경변수 확인하기 : 고급 시스템 설정 > 환경변수 > "CUDA_PATH" and "CUDA_PATH_V10_0" (두 변수 값이 동일함)
- CuDNN SDK 다운로드([CuDDN SDK Download](https://developer.nvidia.com/cudnn), 회원가입 필요) 후 압축 풀기 > cuda 폴더의 파일을 CUDA_PATH 아래에 동일한 명칭의 폴더에 복사하기

## python & package 설치

- windsows에 python 설치하고 가상환경 만들기 : [Python Download](https://www.python.org/downloads/)
  - pip install virtualenv
  - virtualenv computer-vision
- 가상환경 활성화 하기(windows) : computer-vision/Sctipts/activate
- tensorflow 설치하기 : pip install tensorflow-gpu
- keras 설치 : pip install keras
- jupyter 설치 : pip install jupyter
- jupyter notebook 설정(강의에서는 jupyter notebook과 pycharm을 editor로 사용)
  - 시작 directory 지정 : .jupyter 폴더에 jupyter_notebook_config.py 파일의 c.NotebookApp.notebook_dir에 폴더 지정
  - 글꼴 수정 : .jupyter 폴더 아래에 custom 폴더에 custom.css의 font-family, font-size 수정