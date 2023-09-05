# turtle 모듈 불러오기
import turtle

# 화면 설정
win = turtle.Screen()   # 화면 객체 생성
win.title("Pong Game")  # 게임 제목 설정
win.bgcolor("black")    # 배경 색상 설정
win.setup(width=600, height=400)  # 화면 크기 설정

# 왼쪽 패들 생성
left_pad = turtle.Turtle()  # 거북이 객체 생성
left_pad.speed(0)           # 속도 설정 (0: 최고속도)
left_pad.shape("square")    # 모양 설정 (사각형)
left_pad.color("white")     # 색상 설정 (흰색)
left_pad.shapesize(stretch_wid=4.5, stretch_len=1)  # 크기 설정
left_pad.penup()            # 선 숨김
left_pad.goto(-250, 0)      # 좌표 설정

# 오른쪽 패들 생성
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=4.5, stretch_len=1)
right_pad.penup()
right_pad.goto(250, 0)

# 공 생성
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4    # x축 이동 속도
ball.dy = 4    # y축 이동 속도

# 왼쪽 패들 이동 함수
def left_pad_up():
    y = left_pad.ycor()   # 현재 y좌표 가져오기
    y += 20               # 20만큼 증가
    left_pad.sety(y)      # 새로운 y좌표 설정

def left_pad_down():
    y = left_pad.ycor()
    y -= 20               # 20만큼 감소
    left_pad.sety(y)

# 오른쪽 패들 이동 함수
def right_pad_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def right_pad_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# 키 바인딩
win.listen()                 # 입력 대기 상태
win.onkeypress(left_pad_up, "w")      # w 키 누를 때 left_pad_up() 함수 실행
win.onkeypress(left_pad_down, "s")    # s 키 누를 때 left_pad_down() 함수 실행
win.onkeypress(right_pad_up, "Up")    # ↑ 키 누를 때 right_pad_up() 함수 실행
win.onkeypress(right_pad_down, "Down")# ↓ 키 누를 때 right_pad_down() 함수 실행

# 게임 루프
while True:
    win.update()   # 화면 업데이트

    ball.setx(ball.xcor() + ball.dx) # 공의 x 좌표 업데이트
    ball.sety(ball.ycor() + ball.dy) # 공의 y 좌표 업데이트

    # 벽 충돌 체크
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1 # 공의 y 방향 반전

    # 패들 충돌 체크
    if ball.xcor() < -240 and left_pad.ycor() + 60 > ball.ycor() > left_pad.ycor() - 60:
        ball.dx *= -1 # 공의 x 방향 반전
    elif ball.xcor() > 240 and right_pad.ycor() + 60 > ball.ycor() > right_pad.ycor() - 60:
        ball.dx *= -1 # 공의 x 방향 반전

    # 승리 조건 체크
    if ball.xcor() > 290: # 왼쪽 선을 넘으면
        print("Left player wins!") # 왼쪽 선을 지키는 플레이어 승리
        break # 게임 루프 종료
    elif ball.xcor() < -290: # 오른쪽 선을 넘으면
        print("Right player wins!") # 오른쪽 선을 지키는 플레이어 승리
        break # 게임 루프 종료











# 위 코드는 키보드 이벤트 처리, 공의 이동, 충돌 검사 및 승리 조건 검사 등을 포함하는 간단한 Pong 게임의 코드입니다.
# 플레이어는 키보드의 w와 s 키를 사용하여 왼쪽 패들을 이동하고, 위와 아래 방향키를 사용하여 오른쪽 패들을 이동합니다.
# 공은 고정된 속도로 이동하고, 벽과 패들과 충돌할 때마다 방향을 반전시킵니다.
# 한 플레이어가 공을 너무 멀리 넘겨 상대방의 골대를 넘으면, 그 플레이어는 게임에서 패배합니다.