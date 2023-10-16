from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver

import time
import random
import json
import zipfile
import os
import requests
import sys
import string
from datetime import datetime, timedelta
# lamanhug24

filechay = os.path.basename(sys.argv[0]).split('.')[0]

def getPlugin(proxy_host, proxy_port, proxy_user, proxy_pass):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    
    return pluginfile

def telegram_bot_sendtext(bot_message):

   bot_token = '6132854382:AAG4a4L9ndMuYMiTVulYQOlGH9uklhb8B-Q'
   bot_chatID = '-1001884739111'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

options = Options()
#options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=1')
options.add_argument('--log-level=3')
options.add_argument("--disable-renderer-backgrounding");
options.add_argument("--disable-background-timer-throttling");
options.add_argument("--disable-backgrounding-occluded-windows");
options.add_argument("--disable-client-side-phishing-detection");
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-oopr-debug-crash-dump");
options.add_argument("--no-crash-upload");
options.add_argument("--disable-low-res-tiling");
options.add_extension(getPlugin('161.123.152.194','6439','gcgtgfjm','xuzqwpo8yu87'))

# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chromeOptions)

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
options.add_argument('--ignore-gpu-blacklist')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-software-rasterizer")
options.add_argument('--disable-gpu')

options.add_argument("--ignore-certificate-errors-spki-list");
options.add_argument("--ignore-ssl-errors");

options.add_argument( '--disable-blink-features=AutomationControlled' )
options.add_argument(r"--user-data-dir=C:\profile"+"\\"+filechay)
#driver=webdriver.Chrome(executable_path=r'C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe', options=options)
#drivers = [webdriver.Chrome(executable_path=r'C:\Development\chromedriver.exe', options=options[0]), webdriver.Chrome(executable_path=r'C:\Development\chromedriver.exe', options=options[1])]


preferences = {
    "webrtc.ip_handling_policy" : "disable_non_proxied_udp",
    "webrtc.multiple_routes_enabled": False,
    "webrtc.nonproxied_udp_enabled" : False
}
options.add_experimental_option("prefs", preferences)

service=Service(r'C:\Users\Admin\Desktop\Aviso 3\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Google Inc. (Nvidia)",
      renderer="ANGLE(NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0)",
      fix_hairline=True,
      
  )


driver.get("https://aviso.bz/")
delay = random.randint(5,10)
delaylau = random.randint(5,60)
ramdomso = random.randint(1800, 3600)

print("***************Nhap phim ban ky************************")
xyz= input()
for x in range(1500):
    try:
        if(x<10):
            time.sleep(delay)
            driver.get('https://aviso.bz/work-serf')
            tentaikhoan = driver.find_element('xpath', '/html/body/table/tbody/tr[1]/td/div/div[2]/div[2]/div[1]/ul/li[2]/span[2]').text
            
            time.sleep(3)
            driver.execute_script("window.scrollTo(150, 500);")
            
            taikhoantien = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[1]/div/div[1]/a[2]/span[1]').text
            print("File running is: "+filechay+".py" )
            print("{a} {b} {c} {d} {e}".format(a='---------------Tài khoản', b=tentaikhoan.split(" ")[0], c='có', d=taikhoantien.split(" ")[0], e='RUB'))
            
            try:
                xemthoigian = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[4]/table/tbody/tr/td[3]/div/span[1]').text
            except:
                xemthoigian = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[3]/table/tbody/tr/td[3]/div/span[1]').text
                
            print('thời gian chạy task là:', xemthoigian.split(" ")[0])
            
            try:
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[4]/table/tbody/tr/td[2]/div[1]/a')
                xemvideo1.click()
            except:
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[3]/table/tbody/tr/td[2]/div[1]/a')
                xemvideo1.click()
            time.sleep(3)
            try:
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[4]/table/tbody/tr/td[2]/div[1]/a')
                xemvideo1.click()
            except:
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[3]/table/tbody/tr/td[2]/div[1]/a')
                xemvideo1.click()
            
            # xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[3]/table/tbody/tr/td[2]/div[1]/a')
            # xemvideo1.click()
        
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
        
            time.sleep(float(xemthoigian.split(" ")[0]) + 5)
            
            driver.switch_to.frame(driver.find_element('xpath', '/html/frameset/frame[1]'))
            
            clicksurf = driver.find_element('xpath', '/html/body/table/tbody/tr/td[2]/a');
            clicksurf.click()
            
            time.sleep(3)
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
                
            try:
                curr=driver.current_window_handle
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    if handle != curr:
                        driver.close()
            except:
                pass
        if(x>10):
            if(x==300):
                driver.get('https://google.com')
                time.sleep(ramdomso)
            if(x==600):
                driver.get('https://google.com')
                time.sleep(ramdomso)
            if(x==900):
                driver.get('https://google.com')
                time.sleep(ramdomso)
            if(x==1200):
                driver.get('https://google.com')
                time.sleep(ramdomso)
            time.sleep(delay)
            driver.get('https://aviso.bz/work-youtube')
            tentaikhoan = driver.find_element('xpath', '/html/body/table/tbody/tr[1]/td/div/div[2]/div[2]/div[1]/ul/li[2]/span[2]').text
            # print('tài khoản có là:', tentaikhoan.split(" ")[0], 'có tiền' , )

            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 200);")
            
            taikhoantien = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[1]/div/div[1]/a[2]/span[1]').text
            print("File running is: "+filechay+".py")
            print("{a} {b} {c} {d} {e}".format(a='---------------Tài khoản', b=tentaikhoan.split(" ")[0], c='có', d=taikhoantien.split(" ")[0], e='RUB'))

            if float(taikhoantien.split(" ")[0]) % 3 == 0:
                telegram_bot_sendtext("{a} {b} {c} {d} {e}".format(a='------------Tài khoản', b=tentaikhoan.split(" ")[0], c='có', d=taikhoantien.split(" ")[0], e='RUB'))
                time.sleep(delaylau)
            time.sleep(3)
            try:
                xemthoigian = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[3]/div/span[1]').text
                print('thời gian chạy task là:', xemthoigian.split(" ")[0])
                xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]')
                xemvideo.click()
            except:  
                print("Het video cho 10 phut")
                driver.get('https://google.com')
                time.sleep(600)
            #xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]')
            #xemvideo.click()
            time.sleep(delay)
            print('click tab để xem video rồi')
            try: 
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/span[1]')
                xemvideo1.click()
            except Clickagain: 
                xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]')
                xemvideo1.click()
            except:
                print("Het video cho 10 phut")
                driver.get('https://google.com')
                time.sleep(600)
            time.sleep(delay)
            driver.switch_to.window(driver.window_handles[-1])
            driver.switch_to.frame(driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td/iframe'))
                
            xemvideodi = driver.find_element('xpath', '/html/body/div[1]/div/div[4]/button');
            xemvideodi.click()
            time.sleep(float(xemthoigian.split(" ")[0]) + delay)
                
                #Xem 3s
            try:
                driver.switch_to.frame(driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td/iframe'))
                video3s = driver.find_element('xpath', '/html/body/div[1]/div/div[4]/button');
                video3s.click()
                time.sleep(delay)
                #driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                #driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  
                
                
            try:
                curr=driver.current_window_handle
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    if handle != curr:
                        driver.close()
            except:
                pass
            
    except:
        print('có lỗi xảy ra')
        driver.switch_to.window(driver.window_handles[0]) 
        driver.get('https://aviso.bz/work-youtube')
        pass
    
driver.close()