# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class cityItem(scrapy.Item):
    cityId = scrapy.Field()
    cityName = scrapy.Field()
    cityProvience = scrapy.Field()
    spotsCount = scrapy.Field()
    comentsCount = scrapy.Field()
class spotItem(scrapy.Item):
    spotId = scrapy.Field()
    spotName1 = scrapy.Field()
    spotName2 = scrapy.Field()
    spotType = scrapy.Field()
    isHot = scrapy.Field()
    spotRank = scrapy.Field()
    spotCommentsCount = scrapy.Field()
    spotScore = scrapy.Field()
    spotAddress = scrapy.Field()
    spotPhotosCount = scrapy.Field()
    spotAbstract = scrapy.Field()
    spotNeighborhood = scrapy.Field()
    spotWebsite = scrapy.Field()
    spotPhone = scrapy.Field()
    spotEmail = scrapy.Field()
#
class commentItem(scrapy.Item):
    commentId = scrapy.Field()
    spotId = scrapy.Field()
    # feelTime = scrapy.Field()
    commentTime = scrapy.Field()
    userId = scrapy.Field()
    commentScore = scrapy.Field()
    thanksTimes = scrapy.Field()
    commentTitle = scrapy.Field()
    commentContent = scrapy.Field()
#
class userItem(scrapy.Item):
    userId = scrapy.Field()
    userName = scrapy.Field()
    # userRank = scrapy.Field()
    userJoinTime = scrapy.Field()
    # userFromVIP = scrapy.Field()
    # userCity = scrapy.Field()
    userCommentCounts = scrapy.Field()
    cityVisitedCount = scrapy.Field()
    # userCommentCounts2 = scrapy.Field()
    #
    cityVisited = scrapy.Field()
    userPhotoCount = scrapy.Field()
    # userComment1 = scrapy.Field()
    # userComment2 = scrapy.Field()
    # userComment3 = scrapy.Field()
    # userComment4 = scrapy.Field()
    # userComment5 = scrapy.Field()

class hotelItem(scrapy.Item):
    hotelId = scrapy.Field()
    hotelName = scrapy.Field()
    hotelDistence = scrapy.Field()

class RestaurantItem(scrapy.Item):
    restaurantId = scrapy.Field()
    restaurantName = scrapy.Field()
    restaurantDistence = scrapy.Field()

class spotNearItem(scrapy.Item):
    spotIt = scrapy.Field()
    spotName = scrapy.Field()
    spotDistence = scrapy.Field()