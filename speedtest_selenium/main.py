from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import os
import time

class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")
        self.down = 0
        self.up = 0
        self.wait = WebDriverWait(self.driver, 2)
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "start-button")))
    def get_internet_speed(self):
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button > a")
        go_button.click()
        wait = WebDriverWait(self.driver, 60)
        speed_container = self.driver.find_element(By.CLASS_NAME, "result-container-data")

        try:
            # Wait until the url changes and has "result" in it
            wait.until(ec.url_contains("result"))
        except Exception as e:
            print(f"Timeout: url has not been changed {e}")
        down = speed_container.find_element(By.CSS_SELECTOR, "span[class~='download-speed']")
        self.down = down.text
        up = speed_container.find_element(By.CSS_SELECTOR, "span[class~='upload-speed']")
        self.up = up.text
        print(f"Download speed is {self.down} Mbps and upload speed is {self.up} Mbps")
    def tweet_at_provider(self):
        print(f"Tweeted")

internet_speed_bot = InternetSpeedTwitterBot()
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()