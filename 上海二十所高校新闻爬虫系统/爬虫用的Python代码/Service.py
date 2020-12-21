# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib2
from bs4 import BeautifulSoup
import re


# 插入到mongo里
def insertNews(school, nid, date, title, content):
    conn = MongoClient('localhost', 27017)
    db = conn.schoolNews
    my_set = db[school]
    if my_set.find_one({"nid": nid, "title": title, "date": date}):
        return 0
    else:
        my_set.save({"nid": nid, "date": date, "title": title, "content": content})
        print 'please wait a moment'


def judgeInsert(school, nid, date, title, content):
    s = insertNews(school, nid, date, title, content)
    if s == 0:
        print '该数据已有---》跳过存储'
        return 0


# 获取一个页面的代码并用BeautifulSoup渲染
def getNewsSoup(url):
    try:
        urlcontent = urllib2.urlopen(url).read()
        soup = BeautifulSoup(urlcontent, "html.parser")
    except urllib2.URLError:
        print ">>>>>>》》》打不开网页(最有可能的原因是：校园网又挂了)《《《<<<<<<<"
        return 0
    return soup


# 从全篇获取时间list
def getNewsDate(url,_list1,_list2):
    soup = getNewsSoup(url)
    if soup == 0:
        return 0
    else:
        content_list = soup.find_all(_list1, _list2)
        return content_list

# 从全篇获取后半链接
def getNewsUrl(url, rege):
    soup = getNewsSoup(url)
    get_href = soup.find_all('a', href=rege)
    return get_href


# div缩小范围来获取时间
def getNewsDate_div(url,_list2, _date1, _date2):
    soup = getNewsSoup(url)
    content_list = soup.find('div', _list2)
    date = content_list.find_all(_date1, _date2)
    return date


# 缩小范围来获取时间，时间只有标签条件，没有属性条件
def getNewsDate_2(url,_list1,_list2, _date1):
    soup = getNewsSoup(url)
    content_list = soup.find(_list1, _list2)
    date = content_list.find_all(_date1)
    return date


# div缩小范围来获取后边的链接
def getNewsUrl_div(url,_list2, rege):
    soup = getNewsSoup(url)
    content_list = soup.find('div', _list2)
    get_href = content_list.find_all('a', href=rege)
    return get_href



#新闻标题title
def getNewTitle(get_href):
    title = get_href.attrs['title']
    return title


#新闻标题title
def getNewTitle2(get_href,url,_t1,_t2):
    soup = getNews(get_href, url)
    if soup == 0:
        return 0
    else:
        title = soup.find(_t1, _t2).get_text("", strip=True)
        return title


# 获取新闻内容页面的代码并做soup
def getNews(get_href, url):
    _href = get_href.attrs['href'].replace('../info', '/info').replace('./', '/')
    _href= url + _href
    # news = urllib2.urlopen(get_href).read()
    # soup = BeautifulSoup(news, "html.parser")
    try:
        news = urllib2.urlopen(_href).read()
    except urllib2.URLError:
        print "=================获取链接失败->跳过================="
        return 0
    # print _href
    soup = BeautifulSoup(news, "html.parser")
    return soup


# 获取新闻内容
def getNewsContent(get_href, url, _c1, _c2):
    soup = getNews(get_href, url)
    if soup == 0:
        return 0
    else:
        get_content = soup.find(_c1, _c2).get_text("", strip=True)
        return get_content

# 获取新闻内容，通过找到全部的匹配项然后连接起来
def getNewsContent2(get_href, url, _c1, _c2):
    soup = getNews(get_href, url)
    if soup == 0:
        return 0
    else:
        get_content = soup.find_all(_c1, _c2)
        return get_content

# 从全篇获取content
def getNewsContent3(url,_list1,_list2):
    soup = getNewsSoup(url)
    if soup == 0:
        return 0
    else:
        content_list = soup.find(_list1, _list2)
        return content_list

# def news_1(url,rg,list2,a1,a2,b1,b2,b3,c1,c2,c3,d):
#     rege = re.compile(rg,)
#     date = getNewsDate_div(url, list2, a1, a2)
#     get_href = getNewsUrl_div(url, list2, rege)
#     # print get_href[1].attrs['href'], date[1].get_text()
#     for i in xrange(0, len(get_href)):
#         content = getNewsContent(get_href[i], b1, b2, b3)
#         if content == 0:
#             print "获取链接失败，跳过"
#             continue
#         # print content
#         title = getNewTitle2(get_href[i], c1, c2, c3)
#         print title
#         nid = d+str(i)
#         insertNews('news', nid, date[i].string, title, content)

