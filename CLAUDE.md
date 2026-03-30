# SD-OCT2 Industrial Defect Detection System

## Project Overview
SD-OCT(Spectral Domain Optical Coherence Tomography) 기반 산업용 접착층 결함 탐지 시스템.
sdoct 프로젝트의 후속 버전으로, Spectral Domain 방식의 OCT 신호 처리와 결함 탐지를 고도화한다.

## Tech Stack
- **Language**: Python 3.12
- **Detection**: YOLOv8 (ultralytics) - 결함 탐지 모델
- **GUI**: PySide6, PyQtGraph - 데스크톱 대시보드
- **Image Processing**: NumPy, OpenCV, SciPy - B-scan 이미지 처리
- **Visualization**: Matplotlib - 2D/3D 시각화
- **OCT Signal**: SciPy (FFT, Gaussian filter) - SD-OCT 간섭 신호 처리

## Directory Structure
```
sdoct2/
├── src/                          # 메인 애플리케이션 소스
│   ├── gui/                      # PySide6 GUI 모듈
│   ├── engine/                   # OCT 물리 엔진 & 신호 처리
│   └── detection/                # YOLO 기반 결함 탐지
├── ref/                          # 참조 스크립트 & 유틸리티
├── tests/                        # 테스트 코드
├── docs/                         # 문서
├── oct_industrial_dataset/       # 생성된 합성 데이터셋
│   ├── images/                   # B-scan 이미지 (512x512 grayscale)
│   ├── masks/                    # 세그멘테이션 마스크
│   └── multi_defect/             # 복합 결함 이미지
├── yolo_dataset/                 # YOLO 학습용 데이터셋 (train/val 80:20)
├── runs/                         # 학습 결과 & 리포트 출력
├── CLAUDE.md                     # 이 파일
└── requirements.txt              # Python 의존성
```

## Defect Types
| Class ID | Type          | Color | Description       |
|----------|---------------|-------|-------------------|
| 0        | bubble        | Red   | 기포 결함 (접착층 내 공기 포집) |
| 1        | delamination  | Blue  | 박리 결함 (층간 분리)          |
| 2        | inclusion     | Green | 이물질 결함 (외부 물질 혼입)    |

## Key Commands
```bash
# 환경 설정
pip install -r requirements.txt

# GUI 대시보드 실행
python src/gui/dashboard.py
```

## SD-OCT Conventions
- **이미지 크기**: 512x512 pixels, grayscale
- **마스크 포맷**: 255 = 결함 영역, 0 = 배경
- **OCT 파라미터**: 중심파장 1300nm, 대역폭 100nm, 깊이범위 ~3mm/512px
- **신호 처리**: 스펙트럼 간섭 → FFT → log 압축(dB) → 노이즈 모델링(Rayleigh speckle + Gaussian)
- **YOLO 학습**: yolov8n, imgsz=512, 30 epochs, batch=16
- **YOLO 라벨**: normalized center x, y, width, height
- **결함 색상 코드**: bubble=빨강, delamination=파랑, inclusion=초록

## Development Guidelines
- 한국어 주석 사용 가능 (코드 내 변수/함수명은 영문)
- 모든 이미지 처리 함수는 512x512 기준으로 작성
- GUI 코드와 로직 코드를 분리 (src/gui vs src/engine)
- 새로운 결함 유형 추가 시 Defect Types 테이블 업데이트
- 생성된 데이터셋 및 모델 가중치(.pt)는 git에 포함하지 않음
