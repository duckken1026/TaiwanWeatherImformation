#import urllib.request as req#匯入套件
import requests
from datetime import datetime
import json
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import tkinter.ttk as ttk
from io import BytesIO

locationName=[]
maxT = []
minT = []
parameter = []
pop = []        #降雨機率
keys=[]

cityList = []
nerAirData = []

AQI = []
Status =[]
PM =[]
WIND_SPEED = []

def getTime():    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time) 確認時間
    tmp = current_time.split(":")
    index = 10
    hr = 0
    for i in range(2):
        hr += index * int(tmp[0][i])
        index /= 10
    #print(hr) #確認輸出
    return hr


def ok():
    option = en1.get()
    location = en2.get()
    opcode(option , location)
      
    
def UI_Window():
    window.geometry('800x1000')  #邊框
    window.minsize(width=500,height=625) #最小邊框
    window.maxsize(width=1920,height=1080) #最大邊框
    #window.iconbitmap("C:\\Users\\JIMBO\\OneDrive\\桌面\\Final_Project\\icon\\meow.ico") #標題圖示 only for .ico
    window.config(bg = "skyblue") #背景顏色
    window.attributes("-fullscreen", True) #把東西的屬性 (頁面置頂)
    #if(current_time.getTime() == hr): #抓時間去找要什麼資料
        
    lbl_intr = tk.Label(window, text="Hello User", bg='white', fg='#263238', font=('Arial', 18))
    lbl_intr.grid(column = 1, row = 0) #pack() , grid() 只能選一個用
    
    
    
    lb1 = tk.Label(window, text="請輸入您要的功能", bg='white', fg='#263238', font=('Arial', 16))
    lb1.grid(column = 0, row = 1) #pack() , grid() 只能選一個用
    

   
    
    
    lb2 = tk.Label(window, text="請輸入地點", bg='white', fg='#263238', font=('Arial', 16))
    lb2.grid(column = 0, row = 2) 
    
    
    
    bt_1 = tk.Button(window, text="enter", bg='red', fg='white', font=('Arial', 16), command = ok )
    bt_1['activebackground'] = 'red'
    bt_1['activeforeground'] = 'black'
    bt_1.grid(column = 1, row = 3) #botton不要包裝成函式，lable抓不到，包裝功能就好
    
    bt_2 = tk.Button(window, text="EXIT", bg='red', fg='white', font=('Arial', 20), command = window.destroy )
    bt_2['activebackground'] = 'red'
    bt_2['activeforeground'] = 'black'
    bt_2.place(x=1190, y=650, anchor='nw')
    
    

    #create_label_image()
    window.mainloop()
    

'''
    現有(提供)資訊: Wx(天氣現象) 、 MaxT(最高溫度) 、 MinT(最低溫度) 、 CI(舒適度) 、 PoP(降雨機率)
'''
def textData1(data):
    for i in range(4):
           if(i==0):
               text1.set(data[i])
               lb2_intr.grid(column = 2, row = 0) #pack() , grid() 只能選一個用
           elif(i == 1):
               text2.set(data[i])
               lb3_intr.grid(column = 3, row = 0) #pack() , grid() 只能選一個用 
           elif(i == 2):
               text3.set(data[i])
               lb4_intr.grid(column = 4, row = 0) #pack() , grid() 只能選一個用
           elif(i == 3):
               text4.set(data[i])
               lb5_intr.grid(column = 5, row = 0) #pack() , grid() 只能選一個用

def textData2(data1,data2,data3,data4,location,option):
    isRainy = 0
    airCondition = 0
        
    for i in range(22):
        if (location == locationName[i]):
            #printParameter = tk.Label(window, text= parameter[i], bg='white', fg='#263238', font=('Arial', 16))
            A = data1[i]
            text5.set(A)
            printMaxT.grid(column = 2, row = 1)
            text6.set(data2[i])
            printMinT.grid(column = 3, row = 1)
            text7.set(data3[i])
            if(option == "天氣"):
                textT = data4[i] + "%"
            else:
                textT = data4[i]
            text8.set(textT)
            printParameter.grid(column = 4, row = 1)
            if(option == "天氣"):
                if(pop[i]>='40' or pop[i] == '100'):
                    isRainy = 1     
                else:
                    imLabel = tk.Label(image = img1).place(x =170,y=180)
                
            if(option == "空汙"):
               if(A <= '50' and len(A) == 2):
                    airCondition = 1     
               elif((A <= "99" and len(A) == 2) or A == "100"):
                    airCondition = 2 
               elif(A <= "150"):
                    airCondition = 3
               elif(A <= "200"):
                    airCondition = 4
               elif(A <= "300"):
                    airCondition = 5
                    
                
            printPop.grid(column = 5, row = 1)
            break
    if(option == "天氣" and isRainy == 1):  
        imLabel = tk.Label(image = img).place(x =170,y=180)  #button函式內不可放入圖片初始化的圖片，只能有放置圖片的程式

    elif(option == "空汙" and airCondition == 1):
        imLabel1 = tk.Label(image = img2).place(x =170,y=400)
    elif(option == "空汙" and airCondition == 2):
        imLabel1 = tk.Label(image = img3).place(x =170,y=400)
    elif(option == "空汙" and airCondition == 3):
        imLabel1 = tk.Label(image = img4).place(x =170,y=400)
    elif(option == "空汙" and airCondition == 4):
        imLabel1 = tk.Label(image = img5).place(x =170,y=400)
    elif(option == "空汙" and airCondition == 5):
        imLabel1 = tk.Label(image = img6).place(x =170,y=400)

def opcode(option,location):

    if(option == '天氣'):
        textData1(weatherList)
        textData2(maxT,minT,parameter,pop,location,option)
    
    elif(option == "空汙"):
        textData1(AirList)
        textData2(AQI,Status,PM,WIND_SPEED,location,option)
    




def main():
    Weatherhtml = requests.get("https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-2690584E-1FFF-4D4D-8270-F361A33EB494&downloadType=WEB&format=JSON")
    Weatherhtml.encoding = "utf-8"        #氣象資料
    text = json.loads(Weatherhtml.text)
    
    Airhtml = requests.get("https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json")
    Airhtml.encoding = "utf-8"        #空汙資料
    AirText = json.loads(Airhtml.text)
    
    data = text['cwbopendata']['dataset']['location']#(0~21)共有22個index
    
    AirData = AirText['records']
    for i in range(22):     # weather loop
        locationName.append(data[i]['locationName'])#names of location
        maxT.append(data[i]['weatherElement'][1]['time'][0]['parameter']["parameterName"])#names of location   
        minT.append(data[i]['weatherElement'][2]['time'][0]['parameter']["parameterName"])#names of location
        parameter.append(data[i]['weatherElement'][3]['time'][0]['parameter']["parameterName"])#names of location
        pop.append(data[i]['weatherElement'][4]['time'][0]['parameter']["parameterName"])#names of location
        
    for i in range(84):     # air loop (initial)
        if(AirData[i]['County'] not in cityList):
           nerAirData.append(AirData[i]) 
        cityList.append(AirData[i]['County'])
    for i in range(22):     # air loop
        AQI.append(nerAirData[i]['AQI'])
        Status.append(nerAirData[i]['Status'])
        PM.append(nerAirData[i]['PM2.5'] + "μg/m3")
        WIND_SPEED.append(nerAirData[i]['WIND_SPEED'] + "m/s")
        #print(nerAirData[i]['County'], AQI, Status, PM, WIND_SPEED)
    '''
    print(locationName)
    print(maxT)
    print(minT)
    print(parameter)
    print(pop)
    #print(len(data[0]["weatherElement"]))
    '''
    for i in range(len(data[0]["weatherElement"])):
        for key in data[0]["weatherElement"][i].keys():
            #print(data[0]["weatherElement"][i])
            keys.append(key)
    #print(data[0]) #檢查data
    #print(keys) #檢查keys
    
    raderhtml = requests.get("https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=CWB-BD6EC57A-D622-4CA5-AF76-B59F0D047C6B&downloadType=WEB&format=JSON")
    raderhtml.encoding = "utf-8"        #雷達回波圖資料
    raderText = json.loads(raderhtml.text)
    raderData = raderText["cwbopendata"]["dataset"]["resource"]["uri"]  #雷達回波圖
    response = requests.get(raderData)
    im2 = Image.open(BytesIO(response.content))                #插入圖片
    img2 = ImageTk.PhotoImage(im2.resize((500,500)))        #修改圖片大小
    imLabel2 = tk.Label(image = img2).place(x =700,y=145)
    
    UI_Window()
    
    
window = tk.Tk()
window.title('天氣預報')
current_time = getTime()
en1 = ttk.Combobox(window, values=['天氣','空汙'],state="readonly") #使用者輸入
en1.grid(column = 1, row = 1)
en1.current(0)
en2 = ttk.Combobox(window, values=['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市', '基隆市', '新竹縣', '新竹市', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '嘉義市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣'],state="readonly") #使用者輸入
en2.grid(column = 1, row = 2)
en2.current(0)

im = Image.open("1.gif")                #插入圖片
img = ImageTk.PhotoImage(im.resize((200,200)))        #修改圖片大小

im1 = Image.open("0.gif")                #插入圖片
img1 = ImageTk.PhotoImage(im1.resize((200,200)))        #修改圖片大小

im2 = Image.open("n1.png")                #插入圖片
img2 = ImageTk.PhotoImage(im2.resize((342,212)))        #修改圖片大小

im3 = Image.open("n2.png")                #插入圖片
img3 = ImageTk.PhotoImage(im3.resize((342,212)))        #修改圖片大小

im4 = Image.open("n3.png")                #插入圖片
img4 = ImageTk.PhotoImage(im4.resize((342,212)))        #修改圖片大小

im5 = Image.open("n4.png")                #插入圖片
img5 = ImageTk.PhotoImage(im5.resize((342,212)))        #修改圖片大小

im6 = Image.open("n5.png")                #插入圖片
img6 = ImageTk.PhotoImage(im6.resize((342,212)))        #修改圖片大小
        

text1 = tk.StringVar()
text1.set('')

text2 = tk.StringVar()
text2.set('')

text3 = tk.StringVar()
text3.set('')

text4 = tk.StringVar()
text4.set('')

text5 = tk.StringVar()
text5.set('')

text6 = tk.StringVar()
text6.set('')

text7 = tk.StringVar()
text7.set('')

text8 = tk.StringVar()
text8.set('')

weatherList = ["最高溫度","最低溫度","天氣概況","降雨機率"]
AirList = ["AQI "," Status "," PM2.5 "," WIND_SPEED"]

lb2_intr = tk.Label(window, textvariable=text1, bg='white', fg='#263238', font=('Arial', 20))

lb3_intr = tk.Label(window, textvariable=text2, bg='white', fg='#263238', font=('Arial', 20))

lb4_intr = tk.Label(window, textvariable=text3, bg='white', fg='#263238', font=('Arial', 20))

lb5_intr = tk.Label(window, textvariable=text4, bg='white', fg='#263238', font=('Arial', 20))

printMaxT = tk.Label(window,textvariable=text5, bg='white', fg='#263238', font=('Arial', 20))

printMinT = tk.Label(window,textvariable = text6, bg='white', fg='#263238', font=('Arial', 20))

printParameter = tk.Label(window, textvariable=text7, bg='white', fg='#263238', font=('Arial', 16))

printPop = tk.Label(window,textvariable = text8, bg='white', fg='#263238', font=('Arial', 20))

main()
