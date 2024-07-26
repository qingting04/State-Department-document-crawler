from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import re
import os


class PolicyCounter:
    def __init__(self, url):
        self.url = url
        options = Options()
        options.add_argument("--headless")  # Ensure GUI is off
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                                       options=options)
        self.driver.get(url)

    def policy_counter(self, i):
        try:
            policy_count_element = (self.driver.find_element_by_xpath
                                    (f"/html/body/div/div/div[2]/div[3]/div[2]/div[2]/ul/li[{i}]/a/span"))
            policy_count_text = policy_count_element.text
            policy_count = int(re.findall(r"\d+", policy_count_text)[0])
            return policy_count
        except:
            return 0

    def page_counter(self):
        try:
            page_count = (self.driver.find_element_by_xpath
                          ("/html/body/div/div/div[2]/div[3]/div[2]/div[3]/div[3]/span[1]").text)
            page_count = int(re.findall(r"\d+", page_count)[0])
            return page_count
        except:
            return 0

    def take_log(self):
        if not os.path.exists('updating_log.txt'):
            file = open('updating_log.txt', 'w+')
        else:
            file = open('updating_log.txt', 'a')
        file.write(
            f'\n当前时间 {str(datetime.now())} 国务院文件共计 {self.page_counter()} 页，文件共计 {self.policy_counter(1)} 条')
        file.close()


