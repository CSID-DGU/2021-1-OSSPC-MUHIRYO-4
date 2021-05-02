import pygame
import random
import time
from datetime import datetime



# 1. 게임초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400,900]
screen = pygame.display

title = "My Game"
pygame.display.set_caption(title) # 창의 제목 표시줄 옵션
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

#RGB 값 설정
black = (0,0,0)
white = (255,255,255)
k=0

class obj:
    def __init__(self):
        self.x =0
        self.y=0
        self.move =0
    

# 충돌이 일어났는지 확인하는 함수!
# return 값이 boolean 타입임
def crash(a,b):
    # 여기 범위 안에있으면 충돌이 일어났다고 판단함!
    if(a.x-b.sx <= b.sx) and (b.x)





# 4-0. 메인 이벤트
SB=0
# 4-1. FPS 설정
# 4-2. 각종 입력 감지
# 4-3 입력, 시간에 따른 변화
# 4-4 그리기
# 4-5 업데이트
# 5. 게임종료
pygame.quit()
