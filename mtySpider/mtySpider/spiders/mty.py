# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class MtySpider(scrapy.Spider):
    name = 'mty'
    allowed_domains = ['www.tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/Tourism-g294211-China-Vacations.html']
    def parse(self, response):
        file = open('urls.txt', 'w', encoding='utf-8')
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(
            executable_path='D:/pycharm_wordspaces/recommender_systems/spiders/mtySpider/chromedriver.exe',
            chrome_options=options)
        driver.get('https://www.tripadvisor.cn/Tourism-g294211-China-Vacations.html')
        moreCities = driver.find_element_by_xpath('//*[@id="BODYCON"]/div[2]/div/div/div[4]/div')
        if(not  moreCities):
            print("空！")
        while(moreCities):
            cities = driver.find_elements_by_xpath(
                '//*[@id="BODYCON"]/div[2]/div/div/div[2]/a')
            # for city in cities:
            #     url = city.get_attribute('href')
            #     print(url)
            #     file.write(url + '\n')
            # file.close()
            # break
            try:
                moreCities.click()
            except:
                cities = driver.find_elements_by_xpath(
                    '//*[@id="BODYCON"]/div[2]/div/div/div[2]/a')
                print(str(len(cities))+'******************')
                for city in cities:
                    # file = open('urls.txt', 'w', encoding='utf-8')
                    url = city.get_attribute('href')
                    print(url)
                    file.write(url + '\n')
                file.close()
            # cities = response.xpath('//*[@id="BODYCON"]/div[2]/div/div/div[2]/a/div[2]/div/span[2]/text()').extract()
            print(len(cities))
            moreCities = driver.find_element_by_xpath('//*[@id="BODYCON"]/div[2]/div/div/div[4]/div')

        for city in cities:
            # file = open('urls.txt', 'w', encoding='utf-8')
            url = city.get_attribute('href')
            file.write(url + '\n')
        file.close()
        pass
