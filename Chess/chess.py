import pygame #게임 라이브러리
from pygame.locals import * #변수
import copy #복사본을 만드는데 사용하는 라이브러리
import pickle #텍스트 파일에 저장하고 텍스트 파일에서 읽는 데 사용되는 라이브러리
import random #랜덤 함수
from collections import defaultdict #기본 데이터 형식으로 지정
from collections import Counter #리스트의 요소를 효율적으로 카운트
import threading #GUI가 보드를 채색하는 동안 동시에 AI가 생각할 수 있도록 하기 위한 import.


class GamePosition:
    def __init__(self,board,player,castling_rights,EnP_Target,HMC,history = {}):
        self.board = board
        self.player = player 
        self.castling = castling_rights 
        self.EnP = EnP_Target 
        self.HMC = HMC
        self.history = history
        
    def getboard(self):
        return self.board
    def setboard(self,board):
        self.board = board
    def getplayer(self):
        return self.player
    def setplayer(self,player):
        self.player = player
    def getCastleRights(self):
        return self.castling
    def setCastleRights(self,castling_rights):
        self.castling = castling_rights
    def getEnP(self):
        return self.EnP
    def setEnP(self, EnP_Target):
        self.EnP = EnP_Target
    def getHMC(self):
        return self.HMC
    def setHMC(self,HMC):
        self.HMC = HMC
    def checkRepition(self):
        #사전의 값중 3보다 크면 True를 반환
        return any(value>=3 for value in self.history.itervalues())
    def addtoHistory(self,position):
        #현재 위치에서 고유키 생성
        key = pos2key(position)
        self.history[key] = self.history.get(key,0) + 1
    def gethistory(self):
        return self.history
    def clone(self):
        #이 메서드는 동일한 현재 개체의 다른 인스턴스를 반환합니다.
        #매개변수가 있지만 현재 개체와 독립적입니다.
        clone = GamePosition(copy.deepcopy(self.board), #복사
                             self.player,
                             copy.deepcopy(self.castling), #복사
                             self.EnP,
                             self.HMC)
        return clone
class Shades:
    def __init__(self,image,coord):
        self.image = image
        self.pos = coord
    def getInfo(self):
        return [self.image,self.pos]
class Piece:
    def __init__(self,pieceinfo,chess_coord):
        #piecinfo는 'Qb'와 같은 문자열. Q는 퀸과 b를 나타낸다.
        #검은색이라는 사실을 확인.
        piece = pieceinfo[0]
        color = pieceinfo[1]
        #이 작품의 이미지가 저장된 위치에 대한 정보를 가져옴.
        #모든 조각과 함께 전체 스프라이트 이미지에 표시됨.
        #square_width 및 square_height는 칸의 크기를 나타낸다.
        if piece=='K':
            index = 0
        elif piece=='Q':
            index = 1
        elif piece=='B':
            index = 2
        elif piece == 'N':
            index = 3
        elif piece == 'R':
            index = 4
        elif piece == 'P':
            index = 5
        left_x = square_width*index
        if color == 'w':
            left_y = 0
        else:
            left_y = square_height
        
        self.pieceinfo = pieceinfo
        #subsection은 스프라이트 이미지의 일부를 정의
        self.subsection = (left_x,left_y,square_width,square_height)
        #피스의 위치는 두 가지 방법으로 정의된다.
        #보드 사용되는 기본값은 무언가를 저장하는 chess_cord입니다.
        #(3,2)와 같은 이것은 우리의 이미지가 있어야 하는 체스 좌표를 나타냄.
        #눈이 어둡다 반면 ispos는 기본값을 보유하지 않습니다.
        #(-1,-1)의 #, (-1,-1)을 나타내는 (460,360)과 같은 픽셀 좌표를 보유
        self.chess_coord = chess_coord
        self.pos = (-1,-1)

    def getInfo(self):
        return [self.chess_coord, self.subsection,self.pos]
    def setpos(self,pos):
        self.pos = pos
    def getpos(self):
        return self.pos
    def setcoord(self,coord):
        self.chess_coord = coord
    def __repr__(self):
        #useful for debugging
        return self.pieceinfo+'('+str(chess_coord[0])+','+str(chess_coord[1])+')'

##################################/////프로그램 함수\\\\########################
def drawText(board):
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k]==0:
                board[i][k] = 'Oo'
        print (board[i])
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k]=='Oo':
                board[i][k] = 0
def isOccupied(board,x,y):
    if board[y][x] == 0:
        return False
    return True
def isOccupiedby(board,x,y,color):
    if board[y][x]==0:
        return False
    if board[y][x][1] == color[0]:
        return True
    return False
def filterbyColor(board,listofTuples,color):
    filtered_list = []
    #각 좌표를 살펴 보면
    for pos in listofTuples:
        x = pos[0]
        y = pos[1]
        if x>=0 and x<=7 and y>=0 and y<=7 and not isOccupiedby(board,x,y,color):
            filtered_list.append(pos)
    return filtered_list
def lookfor(board,piece):
    listofLocations = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == piece:
                x = col
                y = row
                listofLocations.append((x,y))
    return listofLocations
def isAttackedby(position,target_x,target_y,color):
    board = position.getboard()
    color = color[0]
    listofAttackedSquares = []
    for x in range(8):
        for y in range(8):
            if board[y][x]!=0 and board[y][x][1]==color:
                listofAttackedSquares.extend(
                    findPossibleSquares(position,x,y,True))
    #표적 칸이 지정된 공격 범위 아래에 있는지 확인.
    return (target_x,target_y) in listofAttackedSquares             
def findPossibleSquares(position,x,y,AttackSearch=False):
    #위치 객체에서 개별 구성요소 데이터 가져오기    
    board = position.getboard()
    player = position.getplayer()
    castling_rights = position.getCastleRights()
    EnP_Target = position.getEnP()
    if len(board[y][x])!=2:
        return [] 
    piece = board[y][x][0] #폰, 록, 등등
    color = board[y][x][1] #흰색 or 검은색
    enemy_color = opp(color)
    listofTuples = [] 

    if piece == 'P': #폰.
        if color=='w': #흰색
            if not isOccupied(board,x,y-1) and not AttackSearch:
                listofTuples.append((x,y-1))
                
                if y == 6 and not isOccupied(board,x,y-2):
                    #만약 폰이 초기 위치에 있으면 두 칸을 이동할 수 있습니다.
                    listofTuples.append((x,y-2))
            
            if x!=0 and isOccupiedby(board,x-1,y-1,'black'):
                listofTuples.append((x-1,y-1))
            if x!=7 and isOccupiedby(board,x+1,y-1,'black'):
                listofTuples.append((x+1,y-1))
            if EnP_Target!=-1: 
                if EnP_Target == (x-1,y-1) or EnP_Target == (x+1,y-1):
                    listofTuples.append(EnP_Target)
            
        elif color=='b': #이 폰은 검은색이고, 위와 같지만 반대쪽.
            if not isOccupied(board,x,y+1) and not AttackSearch:
                listofTuples.append((x,y+1))
                if y == 1 and not isOccupied(board,x,y+2):
                    listofTuples.append((x,y+2))
            if x!=0 and isOccupiedby(board,x-1,y+1,'white'):
                listofTuples.append((x-1,y+1))
            if x!=7 and isOccupiedby(board,x+1,y+1,'white'):
                listofTuples.append((x+1,y+1))
            if EnP_Target == (x-1,y+1) or EnP_Target == (x+1,y+1):
                listofTuples.append(EnP_Target)

    elif piece == 'R': #록.
        #모든 수평 정사각형 가져오기
        for i in [-1,1]:
            #i는 +-1이다. 이 코드를 통하여 오른쪽과 왼쪽을 탐색이 가능하다.
            kx = x 
            while True:
                kx = kx + i #왼쪽인지 오른쪽인지 탐색
                if kx<=7 and kx>=0:
                    
                    if not isOccupied(board,kx,y):
                        listofTuples.append((kx,y))
                    else:
                        if isOccupiedby(board,kx,y,enemy_color):
                            listofTuples.append((kx,y))
                        break
                        
                else: 
                    break
        #동일한 방법을 사용하여 수직 칸을 구함.
        for i in [-1,1]:
            ky = y
            while True:
                ky = ky + i 
                if ky<=7 and ky>=0: 
                    if not isOccupied(board,x,ky):
                        listofTuples.append((x,ky))
                    else:
                        if isOccupiedby(board,x,ky,enemy_color):
                            listofTuples.append((x,ky))
                        break
                else:
                    break
        
    elif piece == 'N': #나이트.
        #X방향으로 움직이면 Y로 무조건 1칸 이동 해야함. 반대 상황도 마찬가지
        for dx in [-2,-1,1,2]:
            if abs(dx)==1:
                sy = 2
            else:
                sy = 1
            for dy in [-sy,+sy]:
                listofTuples.append((x+dx,y+dy))
        #유효한 칸만 존재하도록 튜플 목록을 필터링
        listofTuples = filterbyColor(board,listofTuples,color)
    elif piece == 'B': # 비숍.
        #비숍은 대각선으로 움직인다
        for dx in [-1,1]:
            for dy in [-1,1]: 
                kx = x 
                ky = y
                while True: 
                    kx = kx + dx
                    ky = ky + dy
                    if kx<=7 and kx>=0 and ky<=7 and ky>=0:
                        if not isOccupied(board,kx,ky):
                            listofTuples.append((kx,ky))
                        else:
                            if isOccupiedby(board,kx,ky,enemy_color):
                                listofTuples.append((kx,ky))
                            #비숍은 다른 말들을 뛰어 넘을 수 없음
                            break    
                    else:
                        break
    
    elif piece == 'Q': #퀸
        #퀸은 비숍과 록의 행동반경과 똑같음
        board[y][x] = 'R' + color
        list_rook = findPossibleSquares(position,x,y,True)
        board[y][x] = 'B' + color
        list_bishop = findPossibleSquares(position,x,y,True)
        #비숍의 이동과 록의 이동을 합체
        listofTuples = list_rook + list_bishop
        #합친걸 다시 퀸으로 변경
        board[y][x] = 'Q' + color
    elif piece == 'K': #왕
        #왕은 오직 한칸만 이동 가능
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                listofTuples.append((x+dx,y+dy))
        listofTuples = filterbyColor(board,listofTuples,color)
        if not AttackSearch:
            right = castling_rights[player]
            if (right[0] and 
            board[y][7]!=0 and 
            board[y][7][0]=='R' and 
            not isOccupied(board,x+1,y) and
            not isOccupied(board,x+2,y) and 
            not isAttackedby(position,x,y,enemy_color) and 
            not isAttackedby(position,x+1,y,enemy_color) and 
            not isAttackedby(position,x+2,y,enemy_color)):
                listofTuples.append((x+2,y))
            
            if (right[1] and 
            board[y][0]!=0 and 
            board[y][0][0]=='R' and 
            not isOccupied(board,x-1,y)and 
            not isOccupied(board,x-2,y)and 
            not isOccupied(board,x-3,y) and 
            not isAttackedby(position,x,y,enemy_color) and 
            not isAttackedby(position,x-1,y,enemy_color) and
            not isAttackedby(position,x-2,y,enemy_color)):
                listofTuples.append((x-2,y)) 

    #체크 상태일때 왕이 공격 받지 않는 칸으로 이동
    if not AttackSearch:
        new_list = []
        for tupleq in listofTuples:
            x2 = tupleq[0]
            y2 = tupleq[1]
            temp_pos = position.clone()
            makemove(temp_pos,x,y,x2,y2)
            if not isCheck(temp_pos,color):
                new_list.append(tupleq)
        listofTuples = new_list
    return listofTuples
def makemove(position,x,y,x2,y2):
    board = position.getboard()
    piece = board[y][x][0]
    color = board[y][x][1]
    player = position.getplayer()
    castling_rights = position.getCastleRights()
    EnP_Target = position.getEnP()
    half_move_clock = position.getHMC()
    if isOccupied(board,x2,y2) or piece=='P':
        half_move_clock = 0
    else:
        half_move_clock += 1

    board[y2][x2] = board[y][x]
    board[y][x] = 0
    
    if piece == 'K':
        castling_rights[player] = [False,False]
        if abs(x2-x) == 2:
            if color=='w':
                l = 7
            else:
                l = 0
            
            if x2>x:
                    board[l][5] = 'R'+color
                    board[l][7] = 0
            else:
                    board[l][3] = 'R'+color
                    board[l][0] = 0

    if piece=='R':
        if x==0 and y==0:
            castling_rights[1][1] = False
        elif x==7 and y==0:
            castling_rights[1][0] = False
        elif x==0 and y==7:
            castling_rights[0][1] = False
        elif x==7 and y==7:
            castling_rights[0][0] = False

    if piece == 'P':
        if EnP_Target == (x2,y2):
            if color=='w':
                board[y2+1][x2] = 0
            else:
                board[y2-1][x2] = 0
        if abs(y2-y)==2:
            EnP_Target = (x,(y+y2)/2)
        else:
            EnP_Target = -1
        if y2==0:
            board[y2][x2] = 'Qw'
        elif y2 == 7:
            board[y2][x2] = 'Qb'
    else:
        EnP_Target = -1

    player = 1 - player     
    position.setplayer(player)
    position.setCastleRights(castling_rights)
    position.setEnP(EnP_Target)
    position.setHMC(half_move_clock)
def opp(color):
    color = color[0]
    if color == 'w':
        oppcolor = 'b'
    else:
        oppcolor = 'w'
    return oppcolor
def isCheck(position,color):
    board = position.getboard()
    color = color[0]
    enemy = opp(color)
    piece = 'K' + color
    x,y = lookfor(board,piece)[0]
    return isAttackedby(position,x,y,enemy)
def isCheckmate(position,color=-1):
    
    if color==-1:
        return isCheckmate(position,'white') or isCheckmate(position,'b')
    color = color[0]
    if isCheck(position,color) and allMoves(position,color)==[]:
            return True
    return False
def isStalemate(position):
    player = position.getplayer()
    if player==0:
        color = 'w'
    else:
        color = 'b'
    if not isCheck(position,color) and allMoves(position,color)==[]:
        return True
    return False
def getallpieces(position,color):
    board = position.getboard()
    listofpos = []
    for j in range(8):
        for i in range(8):
            if isOccupiedby(board,i,j,color):
                listofpos.append((i,j))
    return listofpos
def allMoves(position, color):
    if color==1:
        color = 'white'
    elif color ==-1:
        color = 'black'
    color = color[0]
    listofpieces = getallpieces(position,color)
    moves = []
    for pos in listofpieces:
        targets = findPossibleSquares(position,pos[0],pos[1])
        for target in targets:
             moves.append([pos,target])
    return moves
def pos2key(position):
    board = position.getboard()
    boardTuple = []
    for row in board:
        boardTuple.append(tuple(row))
    boardTuple = tuple(boardTuple)
    rights = position.getCastleRights()
    tuplerights = (tuple(rights[0]),tuple(rights[1]))
    key = (boardTuple,position.getplayer(),
           tuplerights)
    return key

##############################////////GUI 함수\\\\\\\\\\\\\#############################
def chess_coord_to_pixels(chess_coord):
    x,y = chess_coord
    if isAI:
        if AIPlayer==0:
            #AI와 하고 있고, 검은색으로 플레이
            return ((7-x)*square_width, (7-y)*square_height)
        else:
            return (x*square_width, y*square_height)
    if not isFlip or player==0 ^ isTransition:
        return (x*square_width, y*square_height)
    else:
        return ((7-x)*square_width, (7-y)*square_height)
def pixel_coord_to_chess(pixel_coord):
    x,y = pixel_coord[0]/square_width, pixel_coord[1]/square_height
    if isAI:
        if AIPlayer==0:
            return (7-x,7-y)
        else:
            return (x,y)
    if not isFlip or player==0 ^ isTransition:
        return (x,y)
    else:
        return (7-x,7-y)
def getPiece(chess_coord):
    for piece in listofWhitePieces+listofBlackPieces:
        #piece.getInfo()[0]은 점유된 체스 좌표를 나타냄
        if piece.getInfo()[0] == chess_coord:
            return piece
def createPieces(board):
    listofWhitePieces = []
    listofBlackPieces = []
    for i in range(8):
        for k in range(8):
            if board[i][k]!=0:
                #칸이 비어 있지 않을때
                p = Piece(board[i][k],(k,i))
                #오브젝트에 대한 참조를 적절한 위치에 추가
                if board[i][k][1]=='w':
                    listofWhitePieces.append(p)
                else:
                    listofBlackPieces.append(p)

    return [listofWhitePieces,listofBlackPieces]
def createShades(listofTuples):
    global listofShades
    listofShades = []
    if isTransition:
        return
    if isDraw:
        coord = lookfor(board,'Kw')[0]
        shade = Shades(circle_image_yellow,coord)
        listofShades.append(shade)
        coord = lookfor(board,'Kb')[0]
        shade = Shades(circle_image_yellow,coord)
        listofShades.append(shade)
        return
    if chessEnded:
        #게임은 종료되었으며, 체크메이트가 될 수 없다.
        #승자 에게 녹색 동그라미를 수여
        coord = lookfor(board,'K'+winner)[0]
        shade = Shades(circle_image_green_big,coord)
        listofShades.append(shade)
    #만약 어떤 킹이 체크 상태이면 빨간 동그라미를 수여
    if isCheck(position,'white'):
        coord = lookfor(board,'Kw')[0]
        shade = Shades(circle_image_red,coord)
        listofShades.append(shade)
    if isCheck(position,'black'):
        coord = lookfor(board,'Kb')[0]
        shade = Shades(circle_image_red,coord)
        listofShades.append(shade)
    #입력된 모든 대상 제곱을 살펴봄
    for pos in listofTuples:
        if isOccupied(board,pos[0],pos[1]):
            img = circle_image_capture
        else:
            img = circle_image_green
        shade = Shades(img,pos)
        listofShades.append(shade)
def drawBoard():
    screen.blit(background,(0,0))
    #조각을 블리팅할 순서를 선택합니다.
    if player==1:
        order = [listofWhitePieces,listofBlackPieces]
    else:
        order = [listofBlackPieces,listofWhitePieces]
    if isTransition:
        order = list(reversed(order))
    #다음 세 가지 조건 동안 나타나는 음영은 다음과 같아야 한다.
    if isDraw or chessEnded or isAIThink:
        for shade in listofShades:
            img,chess_coord = shade.getInfo()
            pixel_coord = chess_coord_to_pixels(chess_coord)
            screen.blit(img,pixel_coord)
    #그림자를 만들어 이전 동작이 재생된 내용을 표시.
    if prevMove[0]!=-1 and not isTransition:
        x,y,x2,y2 = prevMove
        screen.blit(yellowbox_image,chess_coord_to_pixels((x,y)))
        screen.blit(yellowbox_image,chess_coord_to_pixels((x2,y2)))

    for piece in order[0]:
        
        chess_coord,subsection,pos = piece.getInfo()
        pixel_coord = chess_coord_to_pixels(chess_coord)
        if pos==(-1,-1):
            screen.blit(pieces_image,pixel_coord,subsection)
        else:
            screen.blit(pieces_image,pos,subsection)
    if not (isDraw or chessEnded or isAIThink):
        for shade in listofShades:
            img,chess_coord = shade.getInfo()
            pixel_coord = chess_coord_to_pixels(chess_coord)
            screen.blit(img,pixel_coord)
    for piece in order[1]:
        chess_coord,subsection,pos = piece.getInfo()
        pixel_coord = chess_coord_to_pixels(chess_coord)
        if pos==(-1,-1):
            screen.blit(pieces_image,pixel_coord,subsection)
        else:
            screen.blit(pieces_image,pos,subsection)

###########################////////AI 관련 기능\\\\\\\\\\############################

def negamax(position,depth,alpha,beta,colorsign,bestMoveReturn,root=True):
    #먼저 위치가 열려 있는 데이터베이스 사전에 이미 저장되어 있는지 확인
    if root:
        #현재 위치에서 키 생성
        key = pos2key(position)
        if key in openings:
            #최상의 이동을 반환
            bestMoveReturn[:] = random.choice(openings[key])
            return
    #이미 평가된 위치의 점수를 저장할 전역 변수에 액세스
    global searched
    if depth==0:
        return colorsign*evaluate(position)
    #재생할 수 있는 모든 이동 생성
    moves = allMoves(position, colorsign)
    #실행할 이동이 없는 경우 위치를 평가한 후 반환
    if moves==[]:
        return colorsign*evaluate(position)
    #루트 노드에 대한 최상의 이동 초기화
    if root:
        bestMove = moves[0]
    #최상의 이동 값을 초기화
    bestValue = -100000
    for move in moves:
        #현재 이동의 복제본을 만들고 해당 복제본에 대해 이동을 수행
        newpos = position.clone()
        makemove(newpos,move[0][0],move[0][1],move[1][0],move[1][1])
        #새 결과 위치에 대한 키를 생성
        key = pos2key(newpos)
        #이 위치가 이전에 이미 검색된 경우 해당 노드 값을 탐색
        if key in searched:
            value = searched[key]
        else:
            value = -negamax(newpos,depth-1, -beta,-alpha,-colorsign,[],False)
            searched[key] = value
        #이 움직임이 지금까지의 움직임 보다 더 나은 경우
        if value>bestValue:
            #저장
            bestValue = value
            #루트 노드에 있는 경우 이동을 최상의 이동으로 저장
            if root:
                bestMove = move
        #이 노드의 하한을 업데이트합니다.
        alpha = max(alpha,value)
        if alpha>=beta:
            #만약 우리의 하한이 이 노드의 상한보다 높다면, 더 이상의 움직임을 살펴볼 필요가 없음.  
            break
    #만약 루트 노드인 경우 최상의 이동을 반환
    if root:
        searched = {}
        bestMoveReturn[:] = bestMove
        return
    return bestValue
def evaluate(position):
    if isCheckmate(position,'white'):
        return -20000
    if isCheckmate(position,'black'):
        return 20000
    board = position.getboard()
    #더 빠른 계산을 위해 보드를 1D 배열로 평평하게 만든다.
    flatboard = [x for row in board for x in row]
    #각 조각의 수를 셀 카운터 개체를 만듬
    c = Counter(flatboard)
    Qw = c['Qw']
    Qb = c['Qb']
    Rw = c['Rw']
    Rb = c['Rb']
    Bw = c['Bw']
    Bb = c['Bb']
    Nw = c['Nw']
    Nb = c['Nb']
    Pw = c['Pw']
    Pb = c['Pb']

    whiteMaterial = 9*Qw + 5*Rw + 3*Nw + 3*Bw + 1*Pw
    blackMaterial = 9*Qb + 5*Rb + 3*Nb + 3*Bb + 1*Pb
    numofmoves = len(position.gethistory())
    gamephase = 'opening'
    if numofmoves>40 or (whiteMaterial<14 and blackMaterial<14):
        gamephase = 'ending'

    Dw = doubledPawns(board,'white')
    Db = doubledPawns(board,'black')
    Sw = blockedPawns(board,'white')
    Sb = blockedPawns(board,'black')
    Iw = isolatedPawns(board,'white')
    Ib = isolatedPawns(board,'black')
    #위 데이터를 기반으로 위치 평가
    evaluation1 = 900*(Qw - Qb) + 500*(Rw - Rb) +330*(Bw-Bb
                )+320*(Nw - Nb) +100*(Pw - Pb) +-30*(Dw-Db + Sw-Sb + Iw- Ib
                )
    #테이블을 기준으로 위치 평가
    evaluation2 = pieceSquareTable(flatboard,gamephase)
    evaluation = evaluation1 + evaluation2
    return evaluation
def pieceSquareTable(flatboard,gamephase):
    #점수 초기화
    score = 0

    for i in range(64):
        if flatboard[i]==0:
            continue
        piece = flatboard[i][0]
        color = flatboard[i][1]
        sign = +1
        #테이블이 있으므로 검은색 조각일 경우 인덱스 조정. 흰색을 위해 설계함
        if color=='b':
            i = (7-i/8)*8 + i%8
            sign = -1
        #점수 조정
        if piece=='P':
            score += sign*pawn_table[i]
        elif piece=='N':
            score+= sign*knight_table[i]
        elif piece=='B':
            score+=sign*bishop_table[i]
        elif piece=='R':
            score+=sign*rook_table[i]
        elif piece=='Q':
            score+=sign*queen_table[i]
        elif piece=='K':
            if gamephase=='opening':
                score+=sign*king_table[i]
            else:
                score+=sign*king_endgame_table[i]
    return score  
def doubledPawns(board,color):
    color = color[0]
    #폰 인덱스 가져오기
    listofpawns = lookfor(board,'P'+color)
    repeats = 0
    temp = []
    for pawnpos in listofpawns:
        if pawnpos[0] in temp:
            repeats = repeats + 1
        else:
            temp.append(pawnpos[0])
    return repeats
def blockedPawns(board,color):
    color = color[0]
    listofpawns = lookfor(board,'P'+color)
    blocked = 0
    for pawnpos in listofpawns:
        if ((color=='w' and isOccupiedby(board,pawnpos[0],pawnpos[1]-1,
                                       'black'))
            or (color=='b' and isOccupiedby(board,pawnpos[0],pawnpos[1]+1,
                                       'white'))):
            blocked = blocked + 1
    return blocked
def isolatedPawns(board,color):
    color = color[0]
    listofpawns = lookfor(board,'P'+color)
    #모든 폰의 좌표를 X개 가져옴
    xlist = [x for (x,y) in listofpawns]
    isolated = 0
    for x in xlist:
        if x!=0 and x!=7:
            #모서리가 아닌 경우
            if x-1 not in xlist and x+1 not in xlist:
                isolated+=1
        elif x==0 and 1 not in xlist:
            #왼쪽 모서리:
            isolated+=1
        elif x==7 and 6 not in xlist:
            #오른쪽 모서리
            isolated+=1
    return isolated

#########메인 함수####################################################
#보드 초기화
board = [ ['Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb'], #8
          ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'], #7
          [  0,    0,    0,    0,    0,    0,    0,    0],  #6
          [  0,    0,    0,    0,    0,    0,    0,    0],  #5
          [  0,    0,    0,    0,    0,    0,    0,    0],  #4
          [  0,    0,    0,    0,    0,    0,    0,    0],  #3
          ['Pw', 'Pw', 'Pw',  'Pw', 'Pw', 'Pw', 'Pw', 'Pw'], #2
          ['Rw', 'Nw', 'Bw',  'Qw', 'Kw', 'Bw', 'Nw', 'Rw'] ]#1
          # a      b     c     d     e     f     g     h

player = 0 #0은 흰색, 1은 검은색
castling_rights = [[True, True],[True, True]]
En_Passant_Target = -1 #이 변수는 다음과 같은 칸이 있을 경우 좌표를 저장
half_move_clock = 0 #이 변수는 지금까지 실행된 가역 이동 수를 저장. 위 데이터를 저장할 GamePosition 클래스의 인스턴스를 생성
position = GamePosition(board,player,castling_rights,En_Passant_Target
                        ,half_move_clock)
#pieceSquareTable() 함수를 통해 전역으로 액세스할 수 있도록 여기에 pieceSquareTable을 저장
pawn_table = [  0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]
knight_table = [-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-90,-30,-30,-30,-30,-90,-50]
bishop_table = [-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-90,-10,-10,-90,-10,-20]
rook_table = [0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0]
queen_table = [-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, 70, -5,-10,-10,-20]
king_table = [-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]
king_endgame_table = [-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50]

#GUI 만들기
#pygame 시작
pygame.init()
#임의의 크기로 화면을 로드
screen = pygame.display.set_mode((600,600))

#체스판 이미지 로드
background = pygame.image.load('Media\\board.png').convert()
#모든 조각이 있는 이미지를 로드
pieces_image = pygame.image.load('Media\\Chess_Pieces_Sprite.png').convert_alpha()
circle_image_green = pygame.image.load('Media\\green_circle_small.png').convert_alpha()
circle_image_capture = pygame.image.load('Media\\green_circle_neg.png').convert_alpha()
circle_image_red = pygame.image.load('Media\\red_circle_big.png').convert_alpha()
greenbox_image = pygame.image.load('Media\\green_box.png').convert_alpha()
circle_image_yellow = pygame.image.load('Media\\yellow_circle_big.png').convert_alpha()
circle_image_green_big = pygame.image.load('Media\\green_circle_big.png').convert_alpha()
yellowbox_image = pygame.image.load('Media\\yellow_box.png').convert_alpha()
#메뉴 사진:
withfriend_pic = pygame.image.load('Media\\withfriend.png').convert_alpha()
withAI_pic = pygame.image.load('Media\\withAI.png').convert_alpha()
playwhite_pic = pygame.image.load('Media\\playWhite.png').convert_alpha()
playblack_pic = pygame.image.load('Media\\playBlack.png').convert_alpha()
flipEnabled_pic = pygame.image.load('Media\\flipEnabled.png').convert_alpha()
flipDisabled_pic = pygame.image.load('Media\\flipDisabled.png').convert_alpha()

#배경 크기 가져오기:
size_of_bg = background.get_rect().size
#개별 칸크기 가져오기
square_width = size_of_bg[0]/8
square_height = size_of_bg[1]/8

#각 조각이 칸에 맞도록 이미지의 크기를 조정

pieces_image = pygame.transform.scale(pieces_image,
                                      (square_width*6,square_height*2))
circle_image_green = pygame.transform.scale(circle_image_green,
                                      (square_width, square_height))
circle_image_capture = pygame.transform.scale(circle_image_capture,
                                      (square_width, square_height))
circle_image_red = pygame.transform.scale(circle_image_red,
                                      (square_width, square_height))
greenbox_image = pygame.transform.scale(greenbox_image,
                                      (square_width, square_height))
yellowbox_image = pygame.transform.scale(yellowbox_image,
                                      (square_width, square_height))
circle_image_yellow = pygame.transform.scale(circle_image_yellow,
                                             (square_width, square_height))
circle_image_green_big = pygame.transform.scale(circle_image_green_big,
                                             (square_width, square_height))
withfriend_pic = pygame.transform.scale(withfriend_pic,
                                      (square_width*4,square_height*4))
withAI_pic = pygame.transform.scale(withAI_pic,
                                      (square_width*4,square_height*4))
playwhite_pic = pygame.transform.scale(playwhite_pic,
                                      (square_width*4,square_height*4))
playblack_pic = pygame.transform.scale(playblack_pic,
                                      (square_width*4,square_height*4))
flipEnabled_pic = pygame.transform.scale(flipEnabled_pic,
                                      (square_width*4,square_height*4))
flipDisabled_pic = pygame.transform.scale(flipDisabled_pic,
                                      (square_width*4,square_height*4))



#배경과 같은 크기의 창을 만들고 제목을 설정하고, 그 위에 배경 이미지를 로드
screen = pygame.display.set_mode(size_of_bg)
pygame.display.set_caption('Shallow Green')
screen.blit(background,(0,0))

#보드에 그려야 할 목록을 생성
listofWhitePieces,listofBlackPieces = createPieces(board)
#목록에는 클래스 Piece의 객체에 대한 참조가 포함
listofShades = []

clock = pygame.time.Clock() #게임의 fps를 제어하는 데 도움
isDown = False #마우스를 누르고 있는지 여부를 나타내는 변수
isClicked = False 
isTransition = False #작품이 애니메이션화되고 있는지 여부를 추적
isDraw = False #게임이 무승부로 끝난 경우 True를 저장
chessEnded = False #체크메이트, 교착 상태 등으로 체스 게임이 종료되면 True
isRecord = False 
isAIThink = False #인공지능이 가장 좋은 동작을 계산하고 있는지 여부를 저장
openings = defaultdict(list)
try:
    file_handle = open('openingTable.txt','r+')
    openings = pickle.loads(file_handle.read())
except:
    if isRecord:
        file_handle = open('openingTable.txt','w')

searched = {} #negamax가 다음을 포함하는 노드를 추적할 수 있는 전역 변수
prevMove = [-1,-1,-1,-1] 
ax,ay=0,0
numm = 0
isMenu = True
isAI = -1
isFlip = -1
AIPlayer = -1
#마지막으로 사용자가 종료할 때까지 false를 유지할 변수
gameEnded = False
#########################무한 LOOP#####################################
while not gameEnded:
    if isMenu:
        screen.blit(background,(0,0))
        if isAI==-1:
            screen.blit(withfriend_pic,(0,square_height*2))
            screen.blit(withAI_pic,(square_width*4,square_height*2))
        elif isAI==True:
            screen.blit(playwhite_pic,(0,square_height*2))
            screen.blit(playblack_pic,(square_width*4,square_height*2))
        elif isAI==False:
            screen.blit(flipDisabled_pic,(0,square_height*2))
            screen.blit(flipEnabled_pic,(square_width*4,square_height*2))
        if isFlip!=-1:
            drawBoard()
            isMenu = False
            if isAI and AIPlayer==0:
                colorsign=1
                bestMoveReturn = []
                move_thread = threading.Thread(target = negamax,
                            args = (position,3,-1000000,1000000,colorsign,bestMoveReturn))
                move_thread.start()
                isAIThink = True
            continue
        for event in pygame.event.get():
            if event.type==QUIT:
                gameEnded = True
                break
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[0]<square_width*4 and
                pos[1]>square_height*2 and
                pos[1]<square_height*6):
                    if isAI == -1:
                        isAI = False
                    elif isAI==True:
                        AIPlayer = 1
                        isFlip = False
                    elif isAI==False:
                        isFlip = False
                elif (pos[0]>square_width*4 and
                pos[1]>square_height*2 and
                pos[1]<square_height*6):
                    if isAI == -1:
                        isAI = True
                    elif isAI==True:
                        AIPlayer = 0
                        isFlip = False
                    elif isAI==False:
                        isFlip=True

        pygame.display.update()
        clock.tick(60)
        continue
    numm+=1
    if isAIThink and numm%6==0:
        ax+=1
        if ax==8:
            ay+=1
            ax=0
        if ay==8:
            ax,ay=0,0
        if ax%4==0:
            createShades([])
        if AIPlayer==0:
            listofShades.append(Shades(greenbox_image,(7-ax,7-ay)))
        else:
            listofShades.append(Shades(greenbox_image,(ax,ay)))
    
    for event in pygame.event.get():
        if event.type==QUIT:
            gameEnded = True
        
            break
        if chessEnded or isTransition or isAIThink:
            continue
        if not isDown and event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            chess_coord = pixel_coord_to_chess(pos)
            x = chess_coord[0]
            y = chess_coord[1]
            if not isOccupiedby(board,x,y,'wb'[player]):
                continue
            dragPiece = getPiece(chess_coord)
            listofTuples = findPossibleSquares(position,x,y)
            createShades(listofTuples)
            if ((dragPiece.pieceinfo[0]=='K') and
                (isCheck(position,'white') or isCheck(position,'black'))):
                None
            else:
                listofShades.append(Shades(greenbox_image,(x,y)))
            isDown = True       
        if (isDown or isClicked) and event.type == MOUSEBUTTONUP:
            isDown = False
            dragPiece.setpos((-1,-1))
            pos = pygame.mouse.get_pos()
            chess_coord = pixel_coord_to_chess(pos)
            x2 = chess_coord[0]
            y2 = chess_coord[1]
            isTransition = False
            if (x,y)==(x2,y2): 
                if not isClicked: 
                    isClicked = True
                    prevPos = (x,y) 
                else:
                    x,y = prevPos
                    if (x,y)==(x2,y2): 
                        isClicked = False
                        createShades([])
                    else:
                        if isOccupiedby(board,x2,y2,'wb'[player]):
                            isClicked = True
                            prevPos = (x2,y2)
                        else:
                            isClicked = False
                            createShades([])
                            isTransition = True 

            if not (x2,y2) in listofTuples:
                isTransition = False
                continue
            if isRecord:
                key = pos2key(position)
                if [(x,y),(x2,y2)] not in openings[key]: 
                    openings[key].append([(x,y),(x2,y2)])

            makemove(position,x,y,x2,y2)
            prevMove = [x,y,x2,y2]
            player = position.getplayer()
            position.addtoHistory(position)
            HMC = position.getHMC()
            if HMC>=100 or isStalemate(position) or position.checkRepition():
                isDraw = True
                chessEnded = True
            if isCheckmate(position,'white'):
                winner = 'b'
                chessEnded = True
            if isCheckmate(position,'black'):
                winner = 'w'
                chessEnded = True
            if isAI and not chessEnded:
                if player==0:
                    colorsign = 1
                else:
                    colorsign = -1
                bestMoveReturn = []
                move_thread = threading.Thread(target = negamax,
                            args = (position,3,-1000000,1000000,colorsign,bestMoveReturn))
                move_thread.start()
                isAIThink = True
            dragPiece.setcoord((x2,y2))
            if not isTransition:
                listofWhitePieces,listofBlackPieces = createPieces(board)
            else:
                movingPiece = dragPiece
                origin = chess_coord_to_pixels((x,y))
                destiny = chess_coord_to_pixels((x2,y2))
                movingPiece.setpos(origin)
                step = (destiny[0]-origin[0],destiny[1]-origin[1])
            createShades([])
    if isTransition:
        p,q = movingPiece.getpos()
        dx2,dy2 = destiny
        n= 30.0
        if abs(p-dx2)<=abs(step[0]/n) and abs(q-dy2)<=abs(step[1]/n):
            movingPiece.setpos((-1,-1))
            listofWhitePieces,listofBlackPieces = createPieces(board)
            isTransition = False
            createShades([])
        else:
            movingPiece.setpos((p+step[0]/n,q+step[1]/n))
    if isDown:
        m,k = pygame.mouse.get_pos()
        dragPiece.setpos((m-square_width/2,k-square_height/2))
    if isAIThink and not isTransition:
        if not move_thread.isAlive():
            isAIThink = False
            createShades([])
            [x,y],[x2,y2] = bestMoveReturn
            makemove(position,x,y,x2,y2)
            prevMove = [x,y,x2,y2]
            player = position.getplayer()
            HMC = position.getHMC()
            position.addtoHistory(position)
            if HMC>=100 or isStalemate(position) or position.checkRepition():
                isDraw = True
                chessEnded = True
            if isCheckmate(position,'white'):
                winner = 'b'
                chessEnded = True
            if isCheckmate(position,'black'):
                winner = 'w'
                chessEnded = True
            isTransition = True
            movingPiece = getPiece((x,y))
            origin = chess_coord_to_pixels((x,y))
            destiny = chess_coord_to_pixels((x2,y2))
            movingPiece.setpos(origin)
            step = (destiny[0]-origin[0],destiny[1]-origin[1])

    drawBoard()
    pygame.display.update()

    clock.tick(60)
pygame.quit()
if isRecord:
    file_handle.seek(0)
    pickle.dump(openings,file_handle)
    file_handle.truncate()
    file_handle.close()