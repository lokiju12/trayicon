from pystray import MenuItem as item
from pystray import Menu
import pystray
from PIL import Image
import subprocess
import webbrowser
import os
import socket
# 웹/프로그램 연결
def call():
    webbrowser.open(r'http://call.hjsc.co.kr')
def hyperion():
    webbrowser.open(r'https://hy.hjsc.co.kr')
def erp():
    webbrowser.open(r'https://hs.hjsc.co.kr/hs_out/index.jsp')
def tel():
    subprocess.Popen(currentpath+'\\tel.exe')
def ip_change():
    subprocess.Popen(currentpath+'\\IP_Change.cmd')
# 현재 실행중인 trayicon.exe를 모두 삭제
def old_trayicon_shutdown():
    subprocess.Popen('taskkill /f /im trayicon.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
old_trayicon_shutdown()
# 경로 오류 방지
currentpath = os.getcwd()
print(currentpath)
# IP주소 확인
ip = (socket.gethostbyname(socket.gethostname()))
# 아이콘 이미지 설정 
image = Image.open('icon.ico')
# 메뉴 설정
menu = Menu(
    item('IP : '+ip, call),
    Menu.SEPARATOR,  # 구분선 추가
    item('원격접속도우미', call),
    Menu.SEPARATOR,  # 구분선 추가
    item('HYPERION', hyperion),
    item('HS - ERP', erp),
    item('전화번호부', tel),
    Menu.SEPARATOR,  # 구분선 추가
    item('IP변경하기', ip_change),
    Menu.SEPARATOR,  # 구분선 추가
    item('종료하기', lambda: icon.stop()),
    )
# 아이콘 설정
icon = pystray.Icon('', image, menu=pystray.Menu(*menu))
# 아이콘 마우스 오버 텍스트
icon.title = 'IP : '+ip 
icon.run()
