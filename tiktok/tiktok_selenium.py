from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import TITOK_SESSIONID

import time
import json
import logging

browser_logger = logging.getLogger(
    'selenium.webdriver.remote.remote_connection')
browser_logger.setLevel(logging.ERROR)
driver_service = Service(ChromeDriverManager().install())

def upload_tiktok(title, vid_path, tags):
    for a in range(1, 6):
        try:
            print('This is Attempt# ', a)
            c_options = Options()
            c_options.add_argument("--headless")
            c_options.add_argument("--log-level=3")
            c_options.add_experimental_option(
                "excludeSwitches", ["enable-automation"])
            c_options.add_experimental_option('useAutomationExtension', False)
            c_options.add_argument(
                '--disable-blink-features=AutomationControlled')
            c_options.add_argument("--profile-directory=Default")

            driver = webdriver.Chrome(options=c_options, service=driver_service)
            driver.set_window_size(1920, 1080)
            driver.get("https://www.tiktok.com/login/phone-or-email/email")
            print('Logging in Tiktok')

            cookies = [{
                "domain": ".tiktok.com",
                "expiry": 1703079680,
                "httpOnly": True,
                "name": "sessionid",
                "path": "/",
                "sameSite": "Lax",
                "secure": True,
                "value": TITOK_SESSIONID
            }]

            for cookie in cookies:
                driver.add_cookie(cookie)

            driver.get('https://www.tiktok.com/upload?lang=en')
            print('Navigating For Upload')
            iframe = driver.find_element(
                By.XPATH, "/html/body/div/div/div[2]/div/iframe")
            driver.switch_to.frame(iframe)
            upload = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/input")))
            upload.send_keys(rf'{vid_path}')
            print('Uploading The Video')
            caption = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div")))
            post_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[8]/div[2]/button")))
            caption.send_keys(title)
            caption.send_keys(Keys.RETURN)
            caption.send_keys(Keys.RETURN)
            caption.send_keys(Keys.RETURN)


            print('Adding tags...')
            for tag in tags:
                caption.send_keys(f'#{tag}')
                time.sleep(2)
                caption.send_keys(Keys.RETURN)
            

            print('Waiting for upload to finish')
            for a in range(0, 300):
                if post_button.is_enabled():
                    driver.execute_script(
                        "arguments[0].scrollIntoView();", post_button)
                    time.sleep(2)
                    post_button.click()
                    print("VIDEO HAS BEEN UPLOADED")
                    print(f"Upload took {a*2} seconds")
                    time.sleep(10)
                    break
                else:
                    time.sleep(2)

            driver.close()
            break
        except Exception as e:
            print(
                f'\u2193\u2193\u2193\u2193\u2193 This Error Happened \u2193\u2193\u2193\u2193\u2193 \n \n{e}\n\nTRYING AGAIN')


def login():
    driver = webdriver.Chrome()
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    time.sleep(60)
    cookies = driver.get_cookies()
    print(cookies)
    print('cookies retrieved')
    with open('./tiktok/cookies.json', 'w') as file:
        file.write(json.dumps(cookies))
    driver.close()
