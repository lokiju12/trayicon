from pystray import MenuItem as item
import pystray
from PIL import Image
import socket
import webbrowser
import subprocess
import os

# # ip 가져오기
# ip = (socket.gethostbyname(socket.gethostname()))
# print(ip)
# 경로 오류 방지
currentpath = os.getcwd()
print(currentpath)

# def call():
#     webbrowser.open(r'http://call.hjsc.co.kr')
# def hyperion():
#     webbrowser.open(r'https://hy.hjsc.co.kr')
# def erp():
#     webbrowser.open(r'https://hs.hjsc.co.kr/hs_out/index.jsp')
# def tel():
#     subprocess.Popen(currentpath+'\\tel.exe')
# def ip_change():
#     subprocess.Popen(currentpath+'\\ip_change.exe')
# def stop():
#     icon.stop()

image = Image.open(currentpath+'icon.ico')
print(image)
# menu = (item('1. 원격접속도우미', call),
#         item('2. Hyperion 2.0', hyperion),
#         item('3. HS - ERP', erp),
#         item('4. 전화번호 검색', tel),
#         item('5. IP 변경', ip_change),
#         item('종료하기', stop),
#         )



icon = pystray.Icon('', image)

icon.run()


