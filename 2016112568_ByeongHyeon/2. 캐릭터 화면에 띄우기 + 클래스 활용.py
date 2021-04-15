import pygame

# 1. 게임초기화 
pygame.init()

# 2. 게임창 옵션 설정
size=[400,900] # 게임창 크기
screen = pygame.display.set_mode(size)

title = "My game"
pygame.display.set_caption(title) # 창의 제목 표시줄 옵션


# 3. 게임 내 필요한 설정
clock = pygame.time.Clock() # 이걸로 FPS설정함


ss = pygame.image.load("/Users/byeonghyeon/Documents/GitHub/2021-1-OSSPC-MUHIRYO-4/2016112568_ByeongHyeon/Image/pngtree-airplane-vector-illustration-png-image_332890.jpeg").convert_alpha()


black=(0,0,0) # RGB임
white=(255,255,255)
k=0
# 4. 메인 이벤트
SB =0
while SB==0:
    
    # 4-1. FPS설정ㅈ
    clock.tick(60) # FPS를 60으로 설정함

    # 4-2. 각종 입력 감지
    for event in pygame.event.get(): #동작을 했을때 행동을 받아오게됨
        if event.type ==pygame.QUIT: # x버튼을 누르면 while문빠져나옴
            SB=1 # SB 가 1이되면 while 문을 벗어나오게 됨
            
    # 4-3. 입력, 시간에 따른 변화
    k+=1
    
    # 4-4 그리기
    screen.fill(black)
    screen.blit(ss,(0,0))
    # 4-5. 업데이트
    pygame.display.flip() # 그려왔던데 화면에 업데이트가 됨
# 5. 게임종료
pygame.quit()



