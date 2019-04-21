import random
def getRandomIp():
    ip = open('ip.txt', 'r', encoding='utf-8')
    ips = ip.readlines()
    ips = [ip.replace('\n', '') for ip in ips]
    return ips[-1]
