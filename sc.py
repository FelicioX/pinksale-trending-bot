from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os, zipfile, json
from fake_useragent import UserAgent
from multiprocessing import Process


try:
    ua = UserAgent()
    userAgent = ua.random 
except:
    ua = UserAgent()
    userAgent = ua.random 

with open('Config.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)


link = json_object['url']
py = json_object['proxy']
port = json_object['port']
user = json_object['user']
pasw = json_object['pasw']
coin = json_object['coin']
thread = int(json_object['thread'])

PROXY_HOST = py  # rotating proxy
PROXY_PORT = port
PROXY_USER = user 
PROXY_PASS = pasw


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
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

def get_chromedriver(use_proxy=False):
    s = Service(executable_path=os.path.join(os.curdir,'chromedriver.exe'))
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
        #chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    #chrome_options.add_extension("extension.crx")
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options,service=s)
    return driver


def main():
    try:
        driver = get_chromedriver(use_proxy=False)
        driver.maximize_window()
        driver.set_page_load_timeout(300)
        try:
            driver.get('https://www.pinksale.finance/launchpads?chain=BSC')
            driver.implicitly_wait(20)
            sleep(2)
            driver.find_element(By.CLASS_NAME,'ant-input').send_keys(link)
            sleep(2)
            driver.find_element(By.CLASS_NAME,'ant-spin-container').find_element(By.TAG_NAME,'button').click()
            sleep(2)

            # Infinity scrolling
            screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
            i = 1

            while True:
                # scroll one screen height each time
                driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
                i += 1
                sleep(2)
                # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
                scroll_height = driver.execute_script("return document.body.scrollHeight;")  
                # Break the loop when the height we need to scroll to is larger than the total scroll height
            
                if (screen_height) * i > scroll_height:
                    break
                
            #driver.refresh()

            AllLink = driver.find_element(By.CLASS_NAME,'content').find_elements(By.TAG_NAME,'a')
            for Link in AllLink:
                driver.execute_script("arguments[0].click();",Link)
                sleep(1)
                driver.switch_to.window(driver.window_handles[1])
                sleep(2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            
            li = driver.find_element(By.CLASS_NAME,'table-container').find_elements(By.TAG_NAME,'a')
            for l in li:
                driver.execute_script("arguments[0].click();",l)
                sleep(1)
                driver.switch_to.window(driver.window_handles[1])
                sleep(2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            driver.quit()
        except Exception as e:
            driver.quit()
        
    except Exception as e:
        driver.quit()


def runner():
    while True:
        try:
            main()
        except:
            sleep(10)
            main()


if __name__=='__main__':
    for _ in range(thread):
        process_obj = Process(target=runner)
        process_obj.start()


    for __ in range(thread):
       process_obj.join()
