# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import  cityItem ,spotItem,commentItem,userItem
import pymysql
class MtyspiderPipeline(object):



    def process_item(self, item, spider):
        connect = pymysql.Connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='maotuying',
            charset='utf8'
        )
        cursor = connect.cursor()
        if isinstance(item, cityItem):
            cityId = item['cityId']
            cityName = item['cityName']
            cityProvience = item['cityProvience']
            spotsCount = item['spotsCount']
            comentsCount = item['comentsCount']
            sql = """
                INSERT INTO city 
                    VALUES(cityId,cityName,cityProvience,spotsCount,comentsCount);
            """

        elif isinstance(item, spotItem):
            spotId = item['spotId']
            spotName1 = item['spotName1']
            spotName2 = item['spotName2']
            spotType = item['spotType']
            isHot = item['isHot']
            spotRank = item['spotRank']
            spotCommentsCount = item['spotCommentsCount']
            spotScore = item['spotScore']
            spotAddress = item['spotAddress']
            spotPhotosCount = item['spotPhotosCount']
            spotAbstract = item['spotAbstract']
            spotNeighborhood = item['spotNeighborhood']
            spotWebsite = item['spotWebsite']
            spotPhone = item['spotPhone']
            spotEmail = item['spotEmail']
            sql = """
                    INSERT INTO spot 
                    VALUES(spotId,spotName1,spotName2,spotType,isHot,spotRank,spotCommentsCount,spotScore,spotAddress,spotPhotosCount,spotAbstract,spotNeighborhood,spotWebsite,spotPhone,spotEmail,);
                """

        elif isinstance(item, commentItem):
            commentId = item['commentId']
            spotId = item['spotId']
            commentTime = item['commentTime']
            userId = item['userId']
            commentScore = item['commentScore']
            thanksTimes = item['thanksTimes']
            commentTitle = item['commentTitle']
            commentContent = item['commentContent']
            sql = """
                            INSERT INTO comment 
                                VALUES(commentId,spotId,commentTime,userId,commentScore,thanksTimes,commentTitle,commentContent);
                        """

        elif isinstance(item, userItem):
            userId = item['userId']
            userName = item['userName']
            userJoinTime = item['userJoinTime']
            userCommentCounts = item['userCommentCounts']
            cityVisitedCount = item['cityVisitedCount']
            cityVisited = item['cityVisited']
            userPhotoCount = item['userPhotoCount']
            sql = """
                           INSERT INTO commentor 
                               VALUES(userId,userName,userJoinTime,userCommentCounts,cityVisitedCount,cityVisited,userPhotoCount);
                       """
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            connect.commit()
        except:
            # 如果发生错误则回滚
            connect.rollback()
        return item
