# python_pong_game

### 예시
![퐁게임](https://github.com/kgw08003/python_pong_game/assets/109195054/70b2b2e4-f214-4359-a207-397a96522b06)


### Turtle 모듈 불러오기:
import turtle: Turtle 모듈을 불러옵니다. 이 모듈을 사용하여 그래픽 기반의 게임 화면을 생성하고 조작합니다.

### 화면 설정:
turtle.Screen(): 게임 화면을 생성합니다.
win.title("Pong Game"): 게임의 제목을 설정합니다.
win.bgcolor("black"): 게임 배경색을 검은색으로 설정합니다.
win.setup(width=600, height=400): 게임 화면의 크기를 설정합니다.

### 패들과 공 생성:
왼쪽 패들(left_pad)과 오른쪽 패들(right_pad)을 생성합니다.
공(ball)을 생성합니다.
각각의 객체의 속도, 모양, 색상, 크기, 초기 위치를 설정합니다.

### 패들 이동 함수:
패들을 위로(left_pad_up, right_pad_up)와 아래로(left_pad_down, right_pad_down) 이동시키는 함수를 정의합니다.

### 키 바인딩:
win.listen(): 키 입력을 받을 준비를 합니다.
특정 키에 대한 이벤트 핸들러(win.onkeypress)를 설정하여 패들을 이동하는 함수와 연결합니다.

### 게임 루프:
while True:: 게임 루프를 시작합니다.
win.update(): 게임 화면을 업데이트합니다.
공의 위치를 갱신하고, 벽과 패들과의 충돌을 체크하여 공의 방향을 변경합니다.
승리 조건을 체크하여 게임이 종료되면 승자를 출력하고 루프를 종료합니다.
