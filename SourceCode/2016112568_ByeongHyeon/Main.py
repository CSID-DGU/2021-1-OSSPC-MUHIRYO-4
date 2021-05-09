import pygame
import random
import time
from datetime import datetime

# sx, sy => 피사체의 x위치 y 위치
# x, y => 비행기의 가로길이, 세로길이

# 1. 게임초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [600,900]
# size = [400,900]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()



class obj:
    def __init__(self):
        self.x =0
        self.y=0
        self.move =0

    def put_img(self,address):
        # png파일 일때
        # convert해줘야하는 문제가 있기때문에
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    # 피사체의 그림 조정
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy)) # 그림의 크기를 조정한다.
        self.sx, self.sy = self.img.get_size()


    def show(self):
        screen.blit(self.img,(self.x,self.y))


# 충돌이 일어났는지 확인하는 함수!
# return 값이 boolean 타입임
def crash(a,b):
    # 요 범위 안에 있을때 충돌이 일어남
    if (a.x-b.sx <=b.x) and (b.x<=a.x + a.sx):
        if(a.y-b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True
        else:
            return False

    else:
        return False

def crash2(a,b):
    # 미사일이 두번 맞았을때 사라지게끔!하는 함수

    pass


# 객체 생성
ss = obj()
# 우리들이 움직여야할 물체
ss.put_img("SourceCode/Image/pngtree-airplane-vector-illustration-png-image_332890.jpeg")
# 그림의 크기를 조정
ss.change_size(50,80)
# 비행체의 위치를 하단의 중앙으로 바꾸기위해!
# x값의 절반에서 피사체의 길이의 절반만큼 왼쪽으로 이동해야 정확히 가운데임
ss.x = round(size[0]/2 - ss.sx/2)
# 맨 밑에서 피사체의 y길이만큼 위로 올라와야함
ss.y = size[1] - ss.sy
# 비행체가 움직이는 속도를 결정함
ss.move = 5

k=0
left_go = False
right_go = False
up_go = False
down_go = False

right_up_go = False
left_up_go = False
right_down_go = False
left_down_go = False
space_go = False

# 미사일의 스피드
m_speed = 0 # 초기화
killed = 0

# 미사일의 크기 조정
min_size = 0
max_size = 40

# 미사일을 발사할때 미사일 객체가 저장되는 리스트 공간
m_list = []
# 피사체 출현시 피사체 객체가 저장되는 리스트 공산
a_list = []

# RGB
black = (0,0,0)
white = (255,255,255)
background_color = (210,105,30)
background_image_desert = pygame.image.load("SourceCode/Image/Desertmap.png")
# 피사체를 미사일로 맞추었을때 맞춘 피사체의 개수
kill = 0
# 피사체를 죽이지못하고 화면밖으로 놓친 피사체의 개수
loss = 0

# 현재 내가 획득한 점수
score = 0

# Game Over
GO = 0


# 4-0 게임 시작 대기 화면(작은 event)
SB=0
while SB==0:
    clock.tick(60)
    for event in pygame.event.get(): # 이벤트가 있다면
        if event.type == pygame.KEYDOWN: # 그 이벤트가 어떤 버튼을 누르는 것이라면
            if event.key == pygame.K_SPACE: # 그 버튼이 스페이스 버튼이라면?
                SB=1
    screen.fill(background_color)

    font = pygame.font.Font("SourceCode/Font/DXHanlgrumStd-Regular.otf",15)
    text_kill = font.render("PRESS \"SPACE\" KEY TO START THE GAME",True,(255,255,255)) # 폰트가지고 랜더링 하는데 표시할 내용, True는 글자가 잘 안깨지게 하는 거임 걍 켜두기, 글자의 색깔
    screen.blit(text_kill,(130,round((size[1]/2)-50))) # 이미지화 한 텍스트라 이미지를 보여준다고 생각하면 됨

    pygame.display.flip() # 그려왔던게 화면에 업데이트가 됨



# 4. 메인 이벤트
# 코드를 첫 실행한 시간 저장
start_time = datetime.now()
SB=0
while SB==0:

    # 4-1. FPS 설정
    # FPS를 60으로 설정함
    clock.tick(60)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():  # 어떤 동작을 했을때 그 동작을 받아옴
        if event.type == pygame.QUIT: # x버튼을 눌렀을때!
            SB=1 # SB 가 1이되면 while문을 빠져나오게 된다!
        if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
            # 키를 누르고있는 상태 : True
            # 키를 떼고있는 상태 : False
            if event.key == pygame.K_LEFT:  # 만약 누른 키가 왼쪽 방향키 라면?
                # if event.key == pygame.K_UP:
                #     left_up_go = True
                # elif event.key == pygame.K_DOWN:
                #     left_down_go = True
                left_go = True
            if event.key == pygame.K_RIGHT:  # 만약 누른 키가 오른쪽 방향키 라면?
                # if event.key == pygame.K_UP:
                #     right_up_go = True
                # elif event.key == pygame.K_DOWN:
                #     right_down_go = True
                right_go = True
            if event.key == pygame.K_SPACE:  # 만약 누른키가 space키 라면?
                space_go = True
                # 속도를 1/6으로 낮췄는데 누를때마다도 한번씩 발사하고싶어서 누르면 k=0으로 초기화시킴 -> while문 조건 통과하기위해
                k=0
            if event.key == pygame.K_UP :
                up_go = True
            if event.key == pygame.K_DOWN:
                down_go = True





        elif event.type == pygame.KEYUP: # 키를 누르는것을 뗐을때!
            if event.key == pygame.K_LEFT: # 키를 뗐다면 그 키가 왼쪽 방향키 인가?
                left_go = False
            elif event.key == pygame.K_RIGHT: # 키를 뗐다면 그 키가 오른쪽 방향키 인가?
                right_go = False
            elif event.key == pygame.K_SPACE: # 키를 뗐다면 그 키가 스페이스 키인가?
                space_go = False
            elif event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False



        # 4-3. 입력과 시간에 따른 변화
    now_time = datetime.now()
        # 코드실행 시점에서 현재시간과릐 차이를 초로 바꿈
    delta_time = (now_time - start_time).total_seconds()


    # 버튼을 꾹 길게 눌렀을때 움직이게 하기
    # 왼쪽 방향키를 눌렀을 때
    if left_go == True:
        ss.x -= ss.move
        # 물체가 왼쪽 끝 경계값으로 이동하면 더이상 나가지 않게끔 만듬!
        # 배경이 뭐냐에 따라 달라질 듯 !
        if ss.x < 0:
            # 더 이상 나가지 못하도록 0 으로 막아줌
            ss.x = 0
    # 오른쪽 방향키를 눌렀을 때
    elif right_go == True:
        ss.x += ss.move
        # 오른쪽 끝에서 비행선의 가로크기만큼 빼줘야한다
        if ss.x >= size[0] - ss.sx:
            # 더 이상 오른쪽 바깥으로 못나가게 오른쪽 끝값으로 초기화
            ss.x = size[0] - ss.sx
    # 윗 방향키를 눌렀을때
    # 윗 방향키를 elif에서 if로 시작
    # 좌우와 상하가 독립된 상태로 구분됨
    if up_go == True:
        ss.y -= ss.move
        # 게임화면 위쪽 화면으로 나가는 경우
        if ss.y < 0:
            # 더이상 나가지 못하게 위치값 고정
            ss.y = 0
    # 아래 방향키를 눌렀을때
    elif down_go == True:
        ss.y += ss.move
        # 게임화면 위쪽 화면으로 나가는 경우
        if ss.y >= size[1] - ss.sy:
            # 더이상 나가지 못하게 위치값 고정
            ss.y = size[1] - ss.sy

    # if right_up_go == True:
    #     ss.y -= ss.move
    #     ss.x += ss.move
    #     if ss.x >= size[0] - ss.sx:
    #         ss.x = size[0] - ss.sx
    #     if ss.y < 0:
    #         ss.y = 0

    # 미사일의 속도 조정
    m_speed = 30-(score//40)



    # 점수와 관련해서 미사일의 속도를 바꾸면 좋을듯 !
    # k%6 이면 미사일의 발생 확률을 1/6으로 낮춤!
    if (space_go == True) and k%m_speed == 0:
        # 미사일 객체 생성
        mm = obj()
        # 미사일의 사진
        mm.put_img("SourceCode/Image/pngtree-brass-bullet-shells-png-image_3258604.jpeg")
        # 미사일의 크기 조정
        mm.change_size(5,15)
        # 미사일의 x값 (위치)
        mm.x = round(ss.x + ss.sx/2 - mm.sx/2)
        # 미사일의 위치 = 비행기의 위치 - 미사일의 y크기
        mm.y = ss.y - mm.sy - 10
        # 미사일의 움직이는 속도를 결정함
        mm.move = 15
        # 미사일의 객체를 리스트에 저장한다.
        m_list.append(mm)
    k+=1

    # 피사체의 리스트를 초기화함
    # delete list
    d_list = []
    for i in range(len(m_list)):
        # i 번째 미사일
        m = m_list[i]
        # 미사일 속도만큼 미사일이 y축방향으로 빠져나간다.
        m.y -= m.move
        # 미사일의 사이즈만큼 나갔을때 지워준다.
        if m.y < -m.sx:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del m_list[d]

    # score 100점 마다 피사체의 사이즈 1씩 감소
    min_size = 30 - score//100

    # score 가 10점 증가함에따라 피사체 발생 개수 0.01확률 증가
    if random.random() > 0.98 -(score//100)*0.01:
        # 피사체 객체 생성
        aa = obj()
        aa.put_img("SourceCode/Image/png-clipart-alien-alien.png")
        # 피사체의 그림 크기 조정
        random_size = random.randrange(min_size,max_size)
        # 정사각형 모양의 피사체
        aa.change_size(random_size,random_size)
        # 0부터 오른쪽 끝까지의 랜덤변수인데 비행기크기보다 작으므로 미사일을 안맞는 외계인도 고려해야함(비행선크기/2 를 뺴줘야함)
        aa.x = random.randrange(0, size[0] - aa.sx - round(ss.sx/2))
        aa.y = 10
        aa.move = 2 + (score//300)
        a_list.append(aa)

    # 살생부 리스트 초기화
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        # 외계인이 화면 밖으로 나갔다면 지워준다.
        if a.y >= size[1]:
            d_list.append(i)

    # 메모리 효율을 위해 삭제
    # 앞에서 부터 지워지면 리스트가 앞당겨져서 오류가 일어나기때문에 reverse해주고 지워준다.
    d_list.reverse()
    for d in d_list:
        del a_list[d]
        # 외계인이 화면 밖으로 나간 횟수
        loss += 1

    dm_list = []
    da_list = []

    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m = m_list[i]
            a = a_list[j]
            if crash(m,a) is True:
                dm_list.append(i)
                da_list.append(j)

    # 미사일2개와 외계인 1개가 같이 만나는 경우가 있을 수도 있으니까 배제하기위해 중복제거를 해준다.
    dm_list = list(set(dm_list))
    da_list = list(set(da_list))
    # reverse 하지않고 지우면 앞에서 부터 지워지고 앞에서부터지워지면 index의 변화가 일어나서 reverse를 해야함
    dm_list.reverse()
    da_list.reverse()


    # del로 미사일과 외계인 삭제하기
    for dm in dm_list:
        del m_list[dm]
    for da in da_list:
        del a_list[da]
        # 피사체를 파괴한 횟수
        kill += 1

    for i in range(len(a_list)):
        a = a_list[i]
        # 만약 외계인이 ss 와 부딛치면 게임 종료
        if crash(a,ss) is True:
            # 1초뒤에 꺼지도록 함
            time.sleep(1)
            # while 문이 종료되도록 하는 key
            SB = 1
            # Go 가 0 인상태로 while문을 빠져나왔다면 x버튼으로 빠져나온것
            GO = 1
    # score 가 0 점이 되면 프로그램 종료
    if score < 0:
        SB = 1


    # 4-4. 그리기
    screen.fill(background_color)


    ss.show()
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()
    # 점수 산정
    score = (kill*5 - loss*8)

    font = pygame.font.Font("SourceCode/Font/DXHanlgrumStd-Regular.otf",20)
    text_kill = font.render("Killed : {} Loss : {}  Score : {}".format(kill,loss,score),True,(255,255,0)) # 폰트가지고 랜더링 하는데 표시할 내용, True는 글자가 잘 안깨지게 하는 거임 걍 켜두기, 글자의 색깔
    screen.blit(text_kill,(10,5)) # 이미지화 한 텍스트라 이미지를 보여준다고 생각하면 됨

    # 현재 흘러간 시간
    text_time = font.render("Time : {:.2f}".format(delta_time),True,(225,225,225))
    screen.blit(text_time,(size[0]-150,5))

    # 4-5. 업데이트
    pygame.display.flip() # 그려왔던게 화면에 업데이트가 됨



# 5. 게임종료(1. x키를 눌러서 게임이 종료된 경우, 2. 죽어서 게임이 종료된 경우)
# 이건 게임오버가 된 상황!
while GO==1:
    clock.tick(60)
    for event in pygame.event.get(): # 이벤트가 있다면
        if event.type == pygame.QUIT:
            GO=0

    font = pygame.font.Font("SourceCode/Font/DXHanlgrumStd-Regular.otf",40)
    text_kill = font.render("GAME OVER",True,(255,0,0)) # 폰트가지고 랜더링 하는데 표시할 내용, True는 글자가 잘 안깨지게 하는 거임 걍 켜두기, 글자의 색깔
    screen.blit(text_kill,(150,round((size[1]/2)-70))) # 이미지화 한 텍스트라 이미지를 보여준다고 생각하면 됨

    pygame.display.flip() # 그려왔던게 화면에 업데이트가 됨


pygame.quit()


# 텍스트 띄우는 방법(내용, 위치, 글자체, 크기, 색깔)
# 1. 폰트 설정
# font = pygame.font.Font(address,size)
# 2. Surface 생성(텍스트의 이미지화)
# text = font.render(contents,True,color)
# 3. Surface 화면에 표시
# screen.blit(text,position)


# 위 코드 세줄이 한 묶음으로 다니게 될것임






# 점수가 올라감에 따라 더 작은 피사체가 나올수도있게 끔 해보자 !
