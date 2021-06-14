## 2021-1-OSSPC-MUHIRYO-4
### Pygame을 이용한 Shooting Game

### Info
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://www.olis.or.kr/license/Detailselect.do?lId=1006)
![badges](https://img.shields.io/badge/OS-ubuntu,MacOs-red)
![Laguage](https://img.shields.io/badge/python-3.6.1-blue.svg)
![Laguage](https://img.shields.io/badge/pygame-2.0.1-lightgreen.svg)
![badges](https://img.shields.io/badge/pygame_menu-3.3.0-black) 

**TEAM 무히려 좋아**
  * **팀장** : 동국대학교 미디어커뮤니케이션학과 [고세열](https://github.com/rhtpduf15)
 
  * **팀원** : 동국대학교 산업시스템공학과 [박병현](https://github.com/park1997)
  
  * **팀원** : 동국대학교 산업시스템공학과 [임채균](https://github.com/Lim0613)

### 게임 소개
* 시작화면

  ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/startimg.PNG)
  * **Menu**
    * **Select Mode**

      ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/selectmode.PNG)
      
      모드에는 오아시스 와 아이스 두개의 모드가 존재합니다.
      
      * **Oasis**
      
        ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/oasis.png)
      
        오아시스 모드에는 비행체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/DesertLV1-1.png)이 미사일로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/MISSILE_2-1.png)이 파괴해야 하는 물체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/scorphion1-1.png) 파괴하지 말고 피해야 하는 물체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/Catus1.png)이 등장합니다.
        
      * **Ice**  
        
        ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/ice.png)
        
        아이스 모드에는 비행체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/santa-1.png)이 미사일로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/ice_missile-1.png)이 파괴해야 하는 물체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/penguin2-1.png)이 파괴하지 말고 피해야 하는 물체로![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/ship-1.png)이 등장합니다.
        
    * **Back**
    
      Select Mode 혹은 Help를 선택했을 시 나오는 Back은 이전 Menu를 다시 보여줍니다.
      
    * **Help**
 
       ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/howtoplay2.png)
       
       게임 방법을 설명해주는 이미지가 나옵니다. 키보드 상, 하, 좌, 우로 비행체를 조작할 수 있고 8방향        이동이 가능하며 스페이스바를 누를 시 미사일이 발사 됩니다.
    * **Quit**
      
      게임종료 버튼
* **게임 내 미사일 종류**
  
  ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/kind1.png)  ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/kind2.png)  ![image](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/kind3.png)
  
  미사일 종류는 점수에 따라 크게 세가지로 나뉩니다. 첫번째는 하나의 미사일만, 두번째는 200점이 넘어갔을 시에 두개의 미사일이, 세번째는 400점을 넘겼을 시 두개의 미사일이 불규칙한 형태로 발사됩니다.(아이스 모드 동일)
  
* [게임영상 다운로드](https://github.com/CSID-DGU/2021-1-OSSPC-MUHIRYO-4/blob/main/SourceCode/Image/gameplay.mp4)


### 실행 방법
#### 1. Python 3.8 설치
```
$ sudo apt get update
$ sudo apt install python3.6.1
```

#### 2. Pygame 2.0.1 설치
```
$ pip3 install pygame == 2.0.1
```

#### 3. Pygame_menu 3.3.0 설치
```
$ pip3 install pygame_menu == 2.0.1
```

#### 4. 프로젝트 폴더 접속
```
$ cd 2021-1-OSSPC-MUHIRYO-4
```

#### 5. 실행
```
$ cd SourceCode
$ python Main.py
```
