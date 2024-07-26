from utils.policy_scraper import PolicyScraper
from utils.js_policy_counter import PolicyCounter
from utils.policy_writer import insert_into_table
from utils.create_database_and_table import create_database_and_table
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
import requests
import time
import random


def get_url(page, policy):
    cur_url = f'https://sousuo.www.gov.cn/search-gov/data?t=zhengcelibrary&q={policy}&timetype=timeqb&mintime=&maxtime' \
              f'=&sort=score&sortType=1&searchfield=title&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear' \
              f'=&puborg=&pcodeYear=&pcodeNum=&filetype=&p={page}&n=5&inpro=&bmfl=&dup=&orpro=&type=gwyzcwjk'
    response = requests.get(cur_url)
    soup = BeautifulSoup(response.text, "html.parser")
    link = re.findall(r'\b(?:https?://)?(?i:[a-z]+\.)+[^\s,]+\b', str(soup))
    return link


def get_num(i, total_page):
    current_num = current_status.policy_counter(i)
    m = current_num // 5
    n = current_num % 5
    result = [5 if i < m else n if i == m else 0 for i in range(total_page)]
    return result


if __name__ == "__main__":
    processed_policy1, processed_policy2, processed_policy3 = 0, 0, 0
    print("请输入关键字：")
    policy = quote(input())
    url = f'https://sousuo.www.gov.cn/zcwjk/policyDocumentLibrary?q={policy}&t=zhengcelibrary&orpro='
    current_status = PolicyCounter(url)
    current_total = current_status.policy_counter(1)
    page_total = current_status.page_counter()
    a = get_num(2, page_total)
    b = get_num(3, page_total)
    c = get_num(4, page_total)
    current_status.take_log()
    current_status.driver.quit()
    print(f"查询成功，共计{current_total}文章，共{page_total}页\n请输入数据库名：")
    dbname = input()
    create_database_and_table(dbname)
    policy_scraper = PolicyScraper()

    try:
        for page in range(page_total):
            print(f"已完成{page * 100 / page_total}%")
            policy_url_list = get_url(page + 1, policy)
            for num, policy_url in enumerate(policy_url_list):
                if requests.get(policy_url).status_code != 404:
                    if num < a[page]:
                        processed_policy1 += 1
                        policy_scraper.set_url(policy_url, processed_policy1)
                        insert_into_table("gwy_wj1", policy_scraper.get_info1(), dbname)
                    elif a[page] <= num < a[page] + b[page]:
                        processed_policy2 += 1
                        policy_scraper.set_url(policy_url, processed_policy2)
                        insert_into_table("gwy_wj2", policy_scraper.get_info2(), dbname)
                    elif a[page] + b[page] <= num < a[page] + b[page] + c[page]:
                        processed_policy3 += 1
                        policy_scraper.set_url(policy_url, processed_policy3)
                        insert_into_table("gwy_wj3", policy_scraper.get_info3(), dbname)
            time.sleep(random.randint(2, 5))
    finally:
        policy_scraper.driver.quit()

    print("\n爬取成功！！！！！")
