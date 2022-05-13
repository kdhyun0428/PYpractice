# tkinter 모듈 가져오기
from tkinter import *

# 생성된 pyperclip 모듈을 복사하기 위해 pyperclip 모듈 가져오기
import pyperclip
import random

# tkinter 초기화
root = Tk()

# GUI의 폭 및 높이 설정
root.geometry("400x400")   

# 문자열 유형의 변수를 선언
passstr = StringVar()

#다음 작업에 사용할 정수 유형의 변수 선언
passlen = IntVar()

# 처음에 암호 길이를 0으로 설정
passlen.set(0)


#비밀번호 생성 함수
def generate():
    #비밀번호를 생성하는데 사용할 목록 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    # 빈 문자열 선언
    password = ""

    #입력한 길이의 임의 암호를 생성하는 루프
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # 항목 위젯에 암호 설정
    passstr.set(password)

# 클립보드에 암호를 복사하는 기능
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# 텍스트 레이블 위젯 작성
Label(root, text="Password Generator Application", font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)

#입력한 암호 길이를 사용하는 항목 위젯 만들기
Entry(root, textvariable=passlen).pack(pady=3)

# 생성 함수를 호출하는 버튼
Button(root, text="Generate Password", command=generate).pack(pady=7)

# 생성된 암호를 표시하는 항목 위젯
Entry(root, textvariable=passstr).pack(pady=3)

# Copy to clipboard 기능을 호출하는 버튼
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

root.mainloop