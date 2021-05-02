import pygame


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

# 4. 메인 이벤트
SB=0
# 4-1. FPS 설정
# 4-2. 각종 입력 감지
# 4-3 입력, 시간에 따른 변화
# 4-4 그리기
# 4-5 업데이트
# 5. 게임종료