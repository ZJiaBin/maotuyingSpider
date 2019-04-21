# -*- coding: utf-8 -*-
import scrapy
from items import cityItem ,spotItem,commentItem,userItem
import pymysql
class Mtyspider1Spider(scrapy.Spider):
    name = 'mtySpider1'
    allowed_domains = ['www.tripadvisor.cn']
    # file = open('urls.txt','r',encoding='utf-8')
    # urls = file.readlines()
    start_urls = []
    spotUrl = open('commentsUrl.txt', 'r', encoding='utf-8')
    urls = spotUrl.readlines()
    for url in urls:
        start_urls.append(url)
    # for url in urls:
    #     url = url.replace('\n','')
    #     start_urls.append(url)

    # def parse(self, response):

        # cityId = scrapy.Field()
        # cityName = scrapy.Field()
        # cityProvience = scrapy.Field()
        # spotsCount = scrapy.Field()
        # comentsCount = scrapy.Field()
        # spotUrlFile = open('spotListUrl.txt','a+',encoding='utf-8')
        # cItem = cityItem()
        # url = response.url
        # id = url.split('-')[1]
        # cItem['cityId']=id
        # locationInof = response.xpath('//*[@id="taplc_trip_planner_breadcrumbs_0"]/ul//li//text()').extract()
        # locationList = []
        # for l in locationInof:
        #     if(len(l.strip())>1):
        #         locationList.append(l)
        # cityName = locationList[-1].replace('旅游','')
        # cItem['cityName'] = cityName
        # # print("城市名称："+cityName)
        # if(len(locationList)==4):
        #     cItem['cityProvience'] = locationList[-2]
        # else:
        #     cItem['cityProvience'] = cityName
        # spotInfo = response.xpath('//*[@class="attractions twoLines"]/a//text()').extract()
        # spotList = []
        # for s in spotInfo:
        #     if (len(s.strip()) > 1):
        #         spotList.append(s)
        # cItem['spotsCount'] = spotList[1].replace(')','').replace('(','')#此处有bug，有的景点没有评论，为空，list这里会越界
        # comentsCount = spotList[-1].replace('条点评','')
        # # comentsCount = comentsCountInfo[0]+comentsCountInfo[1].replace('条点评','')
        # cItem['comentsCount'] = comentsCount
        # nextUrl = response.xpath('//*[@class="attractions twoLines"]/a/@href').extract()
        # nextUrl = response.urljoin(nextUrl[0])
        # spotUrlFile.write(nextUrl+'\n')


        # cityId = cItem['cityId']
        # cityName = cItem['cityName']
        # cityProvience = cItem['cityProvience']
        # spotsCount = cItem['spotsCount']
        # comentsCount = cItem['comentsCount']
        # attribute = [cityId,cityName,cityProvience,spotsCount,comentsCount]
        # temp = ''
        # for att in attribute:
        #     temp = temp + '"'+att+'"'+","
        # temp = temp[:-1]
        # sql = 'INSERT INTO city  VALUES( '+temp+')'
        #
        # connect = pymysql.Connect(
        #     host='localhost',
        #     user='root',
        #     passwd='123456',
        #     db='maotuying',
        #     charset='utf8'
        # )
        # cursor = connect.cursor()
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # print('插入了一条城市数据')
        #     # 提交到数据库执行
        #     connect.commit()
        # except:
        #     # 如果发生错误则回滚
        #     connect.rollback()
        #     print("error!")
        # return cItem
        # spotUrl = open('spotListUrl.txt', 'r', encoding='utf-8')
        # urls = spotUrl.readlines()
        # for url in urls:
        #     yield scrapy.Request(url, callback=self.second_parse)  # 进入景点玩乐子页
    #
    # def parse(self,response):
    #
    #
    #     print('解析第yi层')
    #     pages = response.xpath('//*[@class="pageNumbers"]/a[last()]/text()').extract()
    #     pagesList = []
    #     for page in pages:
    #         if (len(page.replace('\n','').strip()) > 0):
    #             pagesList.append(page.replace('\n',''))
    #     if(len(pagesList)==0):pageCount = 1
    #     else:pageCount = int(pagesList[0])
    #     # print(response.url)
    #     for page in range(pageCount):
    #         url = response.url
    #         index = str(30*page)
    #         #这里每个url得到每一页的景点信息，进行下一层嵌套
    #         url = url.replace('Activities-','Activities-oa'+index+'-')
    #         # print(url)
    #
    #         yield scrapy.Request(url, callback=self.third_parse)  # 进入景点玩乐子页
    # #
    # def third_parse(self,response):
    #     print('解析第er层')
    #     spotUrlFile = open('commentsUrl.txt', 'a+', encoding='utf-8')
    #     #//*[@id="ATTR_ENTRY_2228870"]/div/div/div/div[1]/div[2]
    #     spotUrls = response.xpath('//*[@class="listing_title "]//a/@href').extract()
    #     for spot in spotUrls:
    #         url = response.urljoin(spot)
    #         spotUrlFile.write(url + '\n')
    #         yield scrapy.Request(url, callback=self.fourth_parse)  # 进入单个景点页

    # def fourth_parse(self,response):
    #     print('解析第san层')
    #     # spotType = scrapy.Field()
    #     # spotScore = scrapy.Field()
    #
    #     # spotAddress = scrapy.Field()
    #     # spotNeighborhood = scrapy.Field()
    #     # spotWebsite = scrapy.Field()
    #     # spotPhone = scrapy.Field()
    #     # spotEmail = scrapy.Field()
    #     sItem = spotItem()
    #     url = response.url
    #     spotId = url.split('-')[2]
    #     sItem['spotId']=spotId
    #     spotNames = response.xpath('//*[@id = "HEADING"]//text()').extract()
    #     spotName1 = spotNames[0]
    #     sItem['spotName1'] = spotName1
    #     print('景点名称：'+spotName1)
    #     if(len(spotNames)==2):
    #         spotName2 = spotNames[1]
    #         sItem['spotName2'] = spotName2
    #     else:
    #         sItem['spotName2'] = spotName1
    #     # //*[@data-prwidget-name = "common_header_pop_index"]//span/text()
    #     rank = response.xpath('//*[@class = "popIndexContainer"]//span/text()').extract()[1].replace(',','')
    #     sItem['spotRank'] = rank
    #     total = response.xpath('//*[@class = "popIndexContainer"]//span/text()').extract()[3].split(' ')[1].replace(',','')
    #     total = int(total)  # 用于计算是否热门
    #     if (int(rank) <= total / 10):
    #         hot = 'yes'
    #     else:
    #         hot = 'no'
    #     sItem['isHot']=hot
    #     commentCount = response.xpath('//*[@class = "ratingContainer"]//span/text()').extract()
    #     if(len(commentCount)==0):sItem['spotCommentsCount'] = 'none'
    #     else:
    #         sItem['spotCommentsCount'] = commentCount[0].split()[0]
    #     locality = response.xpath('//*[@class="locality"]/text()').extract()[0]
    #
    #     # streetAddress = response.xpath('//*[@class="street-address"]/text()').extract()[0]
    #     streetAddress = response.xpath('//*[@class="street-address"]/text()').extract()
    #     if(len(streetAddress)==0):streetAddress=''
    #     else:streetAddress = streetAddress[0]
    #     address = locality + streetAddress
    #     sItem['spotAddress'] = address
    #     # photoCount = response.xpath('//*[@class = "see_all_count"]/span[2]/text()').extract()[0].split()[1]
    #     photoCount = response.xpath('//*[@class = "see_all_count"]/span[2]/text()').extract()
    #     if(len(photoCount)==0):sItem['spotPhotosCount'] = 'none'
    #     else:
    #         sItem['spotPhotosCount'] = photoCount[0].split()[1]
    #     abstract = response.xpath('//*[@id="component_5"]//text()').extract()
    #     if(len(abstract)==0):sItem['spotAbstract'] = 'none'
    #     else:
    #         abstract = ' '.join(abstract)
    #         sItem['spotAbstract'] = abstract
    #
    #     neighborhood = response.xpath('//*[@class="detail_section neighborhood"]//text()').extract()
    #     if(len(neighborhood)==0):sItem['spotNeighborhood']='none'
    #     else:
    #         sItem['spotNeighborhood'] = neighborhood[0]
    #
    #     email = response.xpath('//*[@class = "contactType email"]/div/span[2]/text()').extract()
    #     if (len(email) > 0):
    #         email = 'yes'
    #     else:
    #         email = 'no'
    #     sItem['spotEmail'] = email
    #     phone = response.xpath('//*[@class = "detail_section phone"]/text()').extract()
    #     if (len(phone) > 0):
    #         phone = phone[0]
    #     else:
    #         phone = 'no'
    #     sItem['spotPhone'] = phone
    #     website = response.xpath('//*[@class = "detail_section website"]//text()').extract()
    #     if (len(website) > 0):
    #         website = 'yes'
    #     else:
    #         website = 'no'
    #     sItem['spotWebsite'] = website
    #     spotStyle = response.xpath(
    #         '//*[@class = "is-hidden-mobile header_detail attractionCategories"]/div/a/text()').extract()
    #     spotStyle = ','.join(spotStyle)  # 景点类型
    #     sItem['spotType'] = spotStyle
    #     # point = response.xpath('//*[@class = "headerInfoWrapper"]//@alt').extract()[0].split('，')[0].replace('分','')  # 得分
    #     point = response.xpath('//*[@class = "headerInfoWrapper"]//@alt').extract()
    #     if(len(point)==0):sItem['spotScore'] = '没有评分'
    #     else:
    #         sItem['spotScore'] = point[0].split('，')[0].replace('分','')
    #
    #     spotId = sItem['spotId']
    #     spotName1 = sItem['spotName1']
    #     spotName2 = sItem['spotName2']
    #     spotType = sItem['spotType']
    #     isHot = sItem['isHot']
    #     spotRank = sItem['spotRank']
    #     spotCommentsCount = sItem['spotCommentsCount']
    #     spotScore = sItem['spotScore']
    #     spotAddress = sItem['spotAddress']
    #     spotPhotosCount = sItem['spotPhotosCount']
    #     spotAbstract = sItem['spotAbstract']
    #     spotNeighborhood = sItem['spotNeighborhood']
    #     spotWebsite = sItem['spotWebsite']
    #     spotPhone = sItem['spotPhone']
    #     spotEmail = sItem['spotEmail']
    #     attribute = [spotId,spotName1,spotName2,spotType,isHot,spotRank,spotCommentsCount,spotScore,
    #                  spotAddress,spotPhotosCount,spotAbstract,spotNeighborhood,spotWebsite,spotPhone,spotEmail]
    #     temp = ''
    #     for att in attribute:
    #         temp = temp + '"'+att+'"'+","
    #     temp = temp[:-1]
    #     sql = 'INSERT INTO spot  VALUES( '+temp+')'
    #
    #     connect = pymysql.Connect(
    #         host='localhost',
    #         user='root',
    #         passwd='123456',
    #         db='maotuying',
    #         charset='utf8'
    #     )
    #     cursor = connect.cursor()
    #     try:
    #         # 执行sql语句
    #         cursor.execute(sql)
    #         # print('插入了一条城市数据')
    #         # 提交到数据库执行
    #         connect.commit()
    #     except:
    #         # 如果发生错误则回滚
    #         connect.rollback()
    #         print("error!")
    #     # pageCount = int(response.xpath('//*[@class = "pageNumbers"]/a/@data-page-number').extract()[-1])  # 评论一共有多少页
    #     pageCount = response.xpath('//*[@class = "pageNumbers"]/a/@data-page-number').extract()
    #     if(len(pageCount)==0):
    #         pageCount = 1
    #     else:
    #         pageCount = int(pageCount[-1])
    #     # https://www.tripadvisor.cn/Attraction_Review-g294217-d311573-Reviews-or10-Victoria_Peak_The_Peak-Hong_Kong.html
    #     # https://www.tripadvisor.cn/Attraction_Review-g294217-d311573-Reviews-Victoria_Peak_The_Peak-Hong_Kong.html
    #     urls = open('spotUrls.txt','a+',encoding='utf-8')
    #     for i in range(pageCount):
    #         url = response.url.replace('Reviews-', 'Reviews-or' + str(10 * i) + '-')
    #         urls.write(url+'\n')
            # yield scrapy.Request(url, callback=self.fifth_parse)

        # return sItem
    #
    # def fifth_parse(self, response):
    def parse(self, response):
        urls = response.xpath('//*[@class="title "]/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.sixth_parse)  # 进入单个评论页

    def sixth_parse(self,response):
        # commentTitle = scrapy.Field()
        # commentCount = scrapy.Field()

        cItem = commentItem()
        url = response.url
        commentId = url.split('-')[3]
        cItem['commentId'] = commentId
        spotId = url.split('-')[2]
        cItem['spotId'] = spotId
        # //*[@id="review_604217943"]/div/div[2]/div[4]
        # data = response.xpath('//*[@class = "prw_rup prw_reviews_stay_date_hsx"]/text()').extract()[0]  # 体验日期
        # cItem['feelTime'] = data
        commentTime = response.xpath('//*[@class = "ratingDate"]/@title').extract()[0]  # 评论日期
        # print('评论时间：' + commentTime)
        cItem['commentTime'] = commentTime
        userId = response.xpath('//*[@class="member_info"]//*[@class="info_text"]/div/text()').extract()[0]  # 评论人id
        cItem['userId'] = userId
        score = float(response.xpath('//*[@class="reviewSelector"]/div/div[2]/span[1]/@class').extract()[0].split('_')[
                          -1]) / 10  # 评论分数
        cItem['commentScore'] = score
        gratefulTime = response.xpath('//*[@class = "numHelp emphasizeWithColor"]/text()').extract()
        if (len(gratefulTime) == 0):
            grateful = 0
        else:
            grateful = gratefulTime[0].split(' ')[0]  # 评论感谢次数
        cItem['thanksTimes'] = grateful
        content = response.xpath('//*[contains(@class,"fullText")]/text()').extract()[0]  # 评论内容
        title = response.xpath('//*[@class = "title"]/text()').extract()[0]  # 评论标题
        # memberName = response.xpath('//*[contains(@class,"social-member-common-MemberName__display_name_container")]'
        #                             '/h1[1]/span[1]/text()').extract()[0]  # 评论人昵称
        cItem['commentTitle'] = title
        cItem['commentContent'] = content
        memberId = response.xpath('//*[@class = "member_info"]//*[@class = "info_text"]/div/text()').extract()[0]
        memberUrl = 'https://www.tripadvisor.com/Profile/' + memberId
        memberUrlFile = open('memberUrl.txt','a+',encoding='utf-8')
        memberUrlFile.write(memberUrl+'\n')
        commentId = cItem['commentId']
        spotId = cItem['spotId']
        commentTime = cItem['commentTime']
        userId = cItem['userId']
        commentScore = cItem['commentScore']
        thanksTimes = cItem['thanksTimes']
        commentTitle = cItem['commentTitle']
        commentContent = cItem['commentContent']
        attribute = [commentId, spotId, commentTime, userId, commentScore, thanksTimes, commentTitle, commentContent]
        temp = ''
        for att in attribute:
            temp = temp + '"' + str(att) + '"' + ","
        temp = temp[:-1]
        sql = 'INSERT INTO comment  VALUES( ' + temp + ')'
        connect = pymysql.Connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='maotuying',
            charset='utf8'
        )
        cursor = connect.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            print('插入了一条评论数据')
            # 提交到数据库执行
            connect.commit()
        except:
            # 如果发生错误则回滚
            print('error')
            connect.rollback()
        # yield scrapy.Request(memberUrl, callback=self.seventh_parse)  # 进入用户页面
        # return cItem
    #
    # def seventh_parse(self, response):
    #     uItem = userItem()
    #     url = response.url
    #     memberId = url.split('/')[-1]  # 评论人id
    #     uItem['userId'] = memberId
    #     memberName = response.xpath('//*[contains(@class,"social-member-common-MemberName__display_name_container")]'
    #                                 '/h1[1]/span[1]/text()').extract()[0]  # 评论人昵称
    #     print("昵称:"+memberName)
    #     uItem['userName'] = memberName
    #     joinTime = response.xpath('//*[contains(@class,"social-member-MemberCreated")]/'
    #                               'text()').extract()[0]  # 加入时间
    #     uItem['joinTime'] = joinTime
    #     travelMapUrl = 'https://www.tripadvisor.com/' + \
    #                    response.xpath('//*[@data-tab-name="Travel map"]/@href').extract()[0]
    #
    #     yield scrapy.Request(travelMapUrl, callback=self.eighth_parse,item = uItem)
    #
    # def eighth_parse(self, response,uItem):
    #
    #
    #     visitCount = response.xpath('//*[@class = "pin_counts pc_all"]/text()').extract()[0].replace(')', '').replace(
    #         '(', '')  # 去过的城市的数量
    #     uItem['cityVisitedCount'] = visitCount
    #     photoCount = \
    #     response.xpath('//*[@class = "contributionCounts"]/ul[@class="counts"]/li[2]/text()').extract()[0].split(' ')[
    #         0]  # 照片的数量
    #     uItem['userPhotoCount'] = photoCount
    #     contributions = \
    #     response.xpath('//*[@class = "contributionCounts"]/div/span[@class = "totalCount"]/text()').extract()[0]  # 评论数量
    #     uItem['userCommentCounts'] = contributions
    #     citiesId = response.xpath('//ul[@class = "cityGrid"]/li/a/@href').extract()  # 评论过的城市id
    #     citiesId = [id.split('/')[-1] for id in citiesId]  # 去过城市的id
    #     uItem['cityVisited']=citiesId
    #     userId = uItem['userId']
    #     userName = uItem['userName']
    #     userJoinTime = uItem['userJoinTime']
    #     userCommentCounts = uItem['userCommentCounts']
    #     cityVisitedCount = uItem['cityVisitedCount']
    #     cityVisited = uItem['cityVisited']
    #     userPhotoCount = uItem['userPhotoCount']
    #     sql = """
    #                                INSERT INTO commentor
    #                                    VALUES(userId,userName,userJoinTime,userCommentCounts,cityVisitedCount,cityVisited,userPhotoCount);
    #                            """
    #     connect = pymysql.Connect(
    #         host='localhost',
    #         user='root',
    #         passwd='123456',
    #         db='maotuying',
    #         charset='utf8'
    #     )
    #     cursor = connect.cursor()
    #     try:
    #         # 执行sql语句
    #         cursor.execute(sql)
    #         print('插入了一条评论人数据')
    #         # 提交到数据库执行
    #         connect.commit()
    #     except:
    #         # 如果发生错误则回滚
    #         connect.rollback()
    #     # return uItem