import pygame
import random
import time
from datetime import datetime

# sx, sy => 피사체의 가로길이, 세로길리
# x, y => 비행기의 가로길이, 세로길이


# 1. 게임초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400,900]
screen = pygame.display

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
        if address[-3::] == "png":
            self.img = pygame.image.load(address).convert_alpha()    
        else: 
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

    # 피사체의 그림 조정
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy)) # 그림의 크기를 조정한다.
        self.sx, self.sy = self.img.get_size()
    

    def show(self):
        screen.blit(self.img,(self.x,self,y))


# 충돌이 일어났는지 확인하는 함수!
# return 값이 boolean 타입임
def crash(a,b):
    # 여기 범위 안에있으면 충돌이 일어났다고 판단함!
    if(a.x-b.sx <= b.sx) and (b.x <= a.x + a.sx):
        if(a.y - b.sy <= b.y) and (b.y <= a.y + a.sy):
            return True
        else:
            return False
    else:
        return False





# 4-0. 메인 이벤트
SB=0
while SB==0:

    # 4-1. FPS 설정 
    # FPS를 60으로 설정함
    clock.tick(60)

    # 4-2. 각종 입력 감지 
    for event in pygame.event.get():  # 어떤 동작을 했을때 그 동작을 받아옴
        if event.type == pygame.QUIT# x버튼을 눌렀을때!
            SB=1 # SB 가 1이되면 while문을 빠져나오게 된다!
        if event.type == pygame.KEYDOWN: # 어떤 키를 눌렀을때!(키보드가 눌렸을 때)
            # 키를 누그로있는 상태 : True
            # 키를 떼고있는 상태 : False
            if event.key == pygame.K_LEFT:  # 만약 누른 키가 왼쪽 방향키 라면?
                left_go = True
            elif event.key == pygame.K_RIGHT:  # 만약 누른 키가 오른쪽 방향키 라면?
                right_go = True
            elif event.key == pygame.K_SPACE:  # 만약 누른키가 space키 라면?
                space_go = True
                # k=0
        
        elif event.type == pygame.KEYUP: # 키를 누르는것을 뗐을때!
            if evnet.type == pygame.K_LEFT: # 키를 뗐다면 그 키가 왼쪽 방향키 인가?
                left_go = False
            elif event.key == pygame.K_RIGHT: # 키를 뗐다면 그 키가 오른쪽 방향키 인가?
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False
        
    
    # 4-3. 입력과 시간에 따른 변화 
    # 4-4. 그리기 












# 5. 게임종료
pygame.quit()
