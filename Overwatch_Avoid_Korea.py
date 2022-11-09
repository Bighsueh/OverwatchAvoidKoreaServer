import os
import time

def command_exe(command_str):
    exe_result = os.popen(command_str)
    print(exe_result.read())

while True:
    print("")
    print("Overwatch遮擋韓國伺服器.exe")
    print("    Made By ss313021490")
    print("")
    print("Instagram：https://www.instagram.com/hsueh.0214/")
    print("")

    print()
    print("輸入1 開始遮擋OW韓國伺服器")
    print("輸入2 取消遮擋OW韓國伺服器")
    print("輸入0 結束程式")

    print()

    input_text = str(input())
    if(input_text == "0"): break
    print("執行結果：")

    if(input_text == "1"):
        command_exe("route add -p 34.64.0.0 mask 255.255.0.0 0.0.0.0")
    elif(input_text == "2"):
        command_exe("route delete 34.64.0.0")
    else:
        print("輸入錯誤，請重新輸入...")
        time.sleep(2)
        os.system('cls')
        continue

    print("執行完畢，若執行結果為「確定!」則代表執行成功")
    print("*提醒，遊戲結束後請將遮擋關閉，以免造成連線問題。")
    print()
    print("按下Enter結束程式...")
    input()
    break

        

