from selenium import webdriver


class PolicyScraper:
    def __init__(self):
        self.num = None
        self.url = None
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
            options=options)

    def set_url(self, url, num):
        self.url = url
        self.num = num
        self.driver.get(url)

    def get_info1(self):
        link = {}
        try:
            link['seq_id'] = self.num  # 序列ID，从0—现有的文件数
            link['pub_url'] = self.url  # 原文链接
            link['index_id'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[2]").text  # 索引号
            link['gov_theme'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[4]").text  # 主题分类
            link['pub_dept'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]").text  # 发文机关
            link['orig_date'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td[4]").text  # 成文日期
            link['doc_title'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]").text  # 标题
            link['pub_id'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td[2]").text  # 发文字号
            link['pub_date'] = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td[4]").text  # 发布日期
            link['doc_content'] = self.driver.find_element_by_xpath("//*[@id='UCAP-CONTENT']").text  # 内容
        except Exception as e:
            print(f"An error occurred: {e}")
        return link

    def get_info2(self):
        link = {}
        try:
            link['seq_id'] = self.num  # 序列ID，从0—现有的文件数
            link['pub_url'] = self.url  # 原文链接
            link['doc_title'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[2]").text  # 标题
            link['pub_dept'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[4]").text  # 发文机关
            link['pub_id'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[2]").text  # 发文字号
            link['source'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[4]").text  # 来源
            link['gov_theme'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[3]/td[2]").text  # 主题分类
            link['duc_types'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[3]/td[4]").text  # 公文种类
            link['orig_date'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[2]").text  # 成文日期
            link['doc_content'] = self.driver.find_element_by_xpath("//*[@id='UCAP-CONTENT']").text  # 内容
        except Exception as e:
            print(f"An error occurred: {e}")
        return link

    def get_info3(self):
        link = {}
        try:
            link['seq_id'] = self.num  # 序列ID，从0—现有的文件数
            link['pub_url'] = self.url  # 原文链接
            link['doc_title'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/h1").text  # 标题
            link['pub_date'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[1]").text  # 发布日期
            link['source'] = self.driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[1]/span").text  # 来源
            link['doc_content'] = self.driver.find_element_by_xpath("//*[@id='UCAP-CONTENT']").text  # 内容
        except Exception as e:
            print(f"An error occurred: {e}")
        return link
