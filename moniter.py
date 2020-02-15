import requests
import time
dynamicset = set()
old=0
live_status_url = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=14222920"
dynamic_trigger_url = "你自己的链接"
live_trigger_url = "你自己的链接"
dynamic_url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?&host_uid=345819190&offset_dynamic_id=0&need_top=1"
r = requests.get(dynamic_url)
num = r.json()['data']['cards'][1]['desc']['dynamic_id']
dynamicset.add(num)
count = 2879
while(1):
    count = count +1
    try:
        live_status_response = requests.get(live_status_url)
        new = live_status_response.json()['data']['room_info']['live_status']
    except BaseException:
        print(live_status_response.json())
        time.sleep(120)
        continue
    try:
        r = requests.get(dynamic_url)
        num = r.json()['data']['cards'][1]['desc']['dynamic_id']
    except BaseException:
        print(r.json())
        time.sleep(120)
        continue
    if(count==2880):
        count=0
        data = {}
        try:    #这个的作用是提醒你自己程序是否还在运行
            data['value1']=str(new)
            data['value2']=str(num)
            purl= '你自己的链接'
            requests.post(purl,data)
        except BaseException:
            time.sleep(120)
            count-=1
            continue
    if(not num in dynamicset):
        try:
            print(num)
            requests.get(dynamic_trigger_url)
        except BaseException:
            time.sleep(120)
    if((new!=None)&(old!=1)&(new==1)):
        livetitle={}
        try:
            livetitle['value1'] = live_status_response.json()['data']['room_info']['title']
            r = requests.post(live_trigger_url,livetitle)
        except BaseException:
            time.sleep(120)  
    old = new
    time.sleep(30)
    dynamicset.add(num)
