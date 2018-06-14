# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time


class StockSpider(object):
    def __init__(self):
        # URL
        self.url = 'http://stockapp.finance.qq.com/mstats/#mod=list&id=sha&module=SS&type=rankash&sort=32&page=1&max=40'
        # 设置浏览器无界面
        # op = Options()
        # op.set_headless()
        self.driver = webdriver.Chrome()

    def __del__(self):
        '当本对象销毁的时候退出浏览器'
        print("执行了")
        self.driver.quit()

    def get_data_list(self):
        '''获取租房信息列表'''
        # 获取本页所有股票信息列表
        li_s = self.driver.find_elements_by_xpath('//ul[@id="list-body"]/li')
        # 遍历列表
        data_list = []
        for li in li_s:
            try:
                item = {}
                item['stock_code'] = li.find_element_by_xpath('./div[1]/a').text
                item['stock_name'] = li.find_element_by_xpath('./div[2]/a').text
                item['new_price'] = li.find_element_by_xpath('./div[3]//span').text
                item['price_limit'] = li.find_element_by_xpath('./div[4]//span').text
                item['turnover'] = li.find_element_by_xpath('./div[5]//span').text
                # print(item)
                data_list.append(item)
            except Exception as e:
                print("解析数据出错!")
                # print(li.get_attribute('class'))
                # 5. 下一页
        next_page = self.driver.find_element_by_link_text("下一页")
        return next_page, data_list

    def save_data_list(self, data_list):
        print("type(data_list)：", type(data_list))
        print("data_list：", data_list)

        with open('stock.txt', 'a', encoding='utf8') as f:
            for data in data_list:
                print(data)
                print(type(data))
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 1. 准备URL
        # 2. 发送请求获取页面内容
        self.driver.get(self.url)
        # 3. 使用driver的by_xpath方法提取内容
        while True:
            next_page, data_list = self.get_data_list()
            # 4. 把提取到内容写到文件中
            self.save_data_list(data_list)
            # 如果有下一页就点击下一页,否则就退出
            if next_page is not None:
                next_page.click()
                time.sleep(2)
            else:
                break


# 测试
if __name__ == '__main__':
    StockSpider().run()
