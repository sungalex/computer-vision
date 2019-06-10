# 3차원 영상 처리

## 수동형 카메라 기법(Strereo Vision)

- 두개의 카메라 영상(두 카메라가 떨어진 거리 만큼 좌우 이동한 이미지)를 비교해서 각 픽셀의 깊이를 계산
- "광원 -> 영상(P) -> 실물(S)"의 관계
  - $P = k * \large \frac {S} {Z}$
  - P: 영상의 중심으로부터 픽셀 거리
  - S: 실물의 중심으로 부터 거리
  - Z: 광원으로 부터 실물까지의 직각 거리
  - k: 카메라 상수
- 이론적으로는 두개의 카메라를 이용하면, 카메라 간의 거리(S)와 두 카메라의 영상 이미지간의 거리변화(P)를 이용해서 실물까지의 거리(Z)를 구할 수 있음
  - $Z = k * \large \frac {S}{P}$
  - 두개의 이미지 간의 거리 변화는 optical flow 기법을 이용해 측정
  - 실제는 렌즈의 굴곡 등으로 인해 다양한 조정 기법이 필요함

## 능동형 카메라 기법

- 스테레오 비전 및 구조형 광 : 능동형 카메라 기법
- 레이저 삼각 측량 : 다양한 크기의 레이저 광원을 비추어서 패턴으로 픽셀 위치를 파악
- ToF(Time of Flight): 광원이 되돌아오는 시간 차를 이용한 거리 측정

## 사용되는 기술

- PCL(Point Cloud Library): 3차원 이미지 처리 라이브러리
- 3 depth camera & Vendor 제공 S/W
  - polygon model, registration, point cloud, surface reconstruction, polygon mesh
