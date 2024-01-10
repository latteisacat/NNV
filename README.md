# XOR Neural Network Visualization

## About
***
 * XOR 기능을 수행하는 Neural Network를 시각적으로 살펴 보고 동작을 파악하기 위한 간단한 프로젝트입니다.

### V1
 * 하드 코딩으로 함수를 구현하여 matplotlib를 통해 그래프를 그렸습니다.
### 실행 조건 및 방법
 * matplotlib 3.8.2, numpy 1.26.3을 사용하였습니다.
 * 하드코딩 되어 있으므로 사용자가 조작할 필요 없이 실행 후 결과를 확인할 수 있습니다.

### V2

#### 목표
 * 사용자로부터 변수 개수, 변수 들의 값을 받아 visualization 하고자 합니다.
#### 생각해볼 점
 * V1에서는 입력이 단 2개, x1, x2 였기 때문에 2차원 그래프 내에 시각화 하기 매우 용이했습니다. 그러나 입력이 3개, 4개, 이미지의 경우 각 픽셀당 입력으로 들어오기 때문에 수 만개가 될 수도 있는 상황에서 이것을 2차원 평면에 시각화 하여 보여주는 방법을 고민 중입니다.
