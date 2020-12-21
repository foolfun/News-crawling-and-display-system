# -*- coding: utf-8 -*-
import threading
import sys
import Service
import re
import time
import os
# 处理页面编码问题
reload(sys)
sys.setdefaultencoding('utf-8')

'''
1a: 复旦
2b: 上海交通大学
3c: 同济大学
4d: 华东师范大学
5e: 华东理工大学
6f: 上海大学
7g: 上海财经大学
8h: 上海理工大学
9i: 上海师范大学
10j: 华东政法大学
11k: 上海海洋大学
12l: 上海对外经贸大学
13m: 上海工程技术大学
14n: 上海电力学院
15o: 上海应用技术大学
16p: 上海立信会计金融学院
17q: 上海政法学院
18r: 上海商学院
19s: 上海海关学院
20t: 上海健康医学院
'''


def s1():
    url = 'http://news.fudan.edu.cn/news/xxyw/'
    rege = re.compile('\d{4}/\d{4}/\d{5}.html')
    list2 = {'class': 'mar_5'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'date'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://news.fudan.edu.cn/', 'div', {'id': 'endtext'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','').strip().lstrip().rstrip(',')
        print title, time
        nid = 'a'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s2():
    url = 'http://news.sjtu.edu.cn/jdyw.htm'
    rege = re.compile('info/\d{4}/\d{7}.htm')
    date = Service.getNewsDate(url, 'span', {'class': 'timestyle1335'})
    get_href = Service.getNewsUrl(url, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://news.sjtu.edu.cn/', 'div', {'style': 'word-break:break-all;overflow:auto;width:100%'})
        if content == 0:
            print "获取内容失败，跳过"
            continue
        print content
        title = Service.getNewTitle(get_href[i])
        print title
        nid = 'b'
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','').strip().lstrip().rstrip(',')
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s3():
    url = 'http://news.tongji.edu.cn/classid-15.html'
    list2 = {'class': 'li_black'}
    content_list = Service.getNewsDate(url, 'li', list2)
    for i in xrange(0, len(content_list)):
        date = content_list[i].span
        if date == None:
            continue
        print date
        url2 = 'http://news.tongji.edu.cn/'
        print content_list[i].a.attrs['href']
        content = Service.getNewsContent(content_list[i].a, url2, 'div', {'class': 'news_content'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(content_list[i].a)
        print title
        nid = 'c'
        time = re.sub(r'[\(,\)]', '', date.string)
        time = '2017-'+time.replace('年', '-').replace('月', '-').replace('日','')
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s4():
    url = 'http://news.ecnu.edu.cn/1833/list.htm'
    rege = re.compile('/\w+/\w+/c\d{4}a\d{6}/page.htm')
    list2 = {'id': 'wp_news_w1'}
    date = Service.getNewsDate_div(url, list2, 'div', {'style': "white-space:nowrap"})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://news.ecnu.edu.cn/', 'div', {'class': 'Article_Content'})
        if content == 0:
            print "获取内容失败，跳过"
            continue
        print content
        title = Service.getNewTitle(get_href[i])
        print title
        nid = 'd'
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print time
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s5():
    url = 'http://news.ecust.edu.cn/news?important=1'
    rege = re.compile('/news/\d{5}\?important=1&category_id=')
    list2 = {'class': 'content'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'time'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://news.ecust.edu.cn/', 'p', {'class': 'promt'})
        if content == 0:
            print "获取内容失败，跳过"
            continue
        print content
        title = Service.getNewTitle2(get_href[i], 'http://news.ecust.edu.cn/', 'div', {'class': 'content_title'})
        print title
        nid = 'e'
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','').strip().lstrip().rstrip(',')
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s6():
    url = 'http://www.shu.edu.cn/index/yw.htm'
    rege = re.compile('/info/\d{4}/\d{5}.htm')
    list2 = {'class': 'list-con'}
    date = Service.getNewsDate_div(url, list2, 'div', {'class': 'list-date'})
    title = Service.getNewsDate_div(url, list2, 'div', {'class': 'list-txt-1'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://www.shu.edu.cn/', 'div', {'id': 'vsb_content'})
        if content == 0:
            print "获取内容失败，跳过"
            continue
        print content
        nid = 'f'
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        res = Service.judgeInsert('news', nid, time, title[i].string, content)
        if res == 0:
            break


def s7():
    url = 'http://news.sufe.edu.cn/179/list.htm'
    rege = re.compile('/\w+/\w+/c\d{3}a\d{5}/page.htm')
    list2 = {'id': 'wp_news_w69'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'time_yy'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://news.sufe.edu.cn/', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title, time
        nid = 'g'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break



def s8():
    url = 'http://www.usst.edu.cn/s/1/t/517/p/4/list.htm'
    rege = re.compile('/s/1/t/517/7\w+/\w+/info\d{5}.htm')
    list2 = {'class': 'column_list_content'}
    date = Service.getNewsDate_div(url, list2, 'td', {'class': 'postTime'})
    title = Service.getNewsDate(url, 'font', {'color': ''})
    print title[1]
    get_href = Service.getNewsUrl(url, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://www.usst.edu.cn', 'td', {'class': 'content'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        print content
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title[i].string,time
        nid = 'h'
        res = Service.judgeInsert('news', nid, time, title[i].string, content)
        if res == 0:
            break


def s9():
    url = 'http://xw.shnu.edu.cn/16365/list.htm'
    rege = re.compile('/\w+/\w+/c\d{5}a\d{6}/page.htm')
    list2 = {'id': 'dnn_ctr3336_ModuleContent'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'PublishDate'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://xw.shnu.edu.cn', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        print content
        title = Service.getNewTitle2(get_href[i], 'http://xw.shnu.edu.cn', 'span', {'id': 'dnn_ctr3336_ArticleDetails_ctl00_lblTitle'})
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title, time
        nid = 'i'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s10():
    url = 'http://news.ecupl.edu.cn/672/list.htm'
    rege = re.compile('/\d{2}/\w+/c\d{3}a\d{5}/page.htm')
    list2 = {'id': 'wp_news_w42'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'Article_PublishDate'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://news.ecupl.edu.cn/', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title
        nid = 'j'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s11():
    url = 'http://www.shou.edu.cn/yw/list.htm'
    rege = re.compile('/\d{4}/\d{4}/c\d{3}a\d{6}/page.htm')
    list2 = {'id': 'wp_news_w8'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'col_news_date'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://www.shou.edu.cn', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle2(get_href[i], 'http://www.shou.edu.cn', 'h1', {'class': 'arti_title'})
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title
        nid = 'k'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s12():
    url = 'http://news.suibe.edu.cn/1415/list.htm'
    rege = re.compile('/\w+/\w+/c\d{4}a\d{5}/page.htm')
    list2 = {'id': 'wp_news_w66'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'Article_PublishDate'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()

    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://news.suibe.edu.cn/', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title
        nid = 'l'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s13():
    url = 'http://news.tongji.edu.cn/classid-15.html'
    rege = re.compile('classid-\d{2}-newsid-\d{5}-t-show.html')
    list2 = {'class': 'li_black'}
    content_list = Service.getNewsDate(url, 'li', list2)
    for i in xrange(0, len(content_list)):
        date = content_list[i].span
        if date == None:
            continue
        print date
        url2 = 'http://news.tongji.edu.cn/'
        print content_list[i].a.attrs['href']
        content = Service.getNewsContent(content_list[i].a, url2, 'div', {'class': 'news_content'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(content_list[i].a)
        print title
        nid = 'm'
        time = re.sub(r'[\(,\)]', '', date.string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print time
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s14():
    url = 'http://news.shiep.edu.cn/campus_news/list.htm'
    Service.getNewsSoup(url)
    rege = re.compile('/\d{2}/\w+/c\d{4}a\d{6}/page.htm')
    list2 = {'id': 'wp_news_w1205'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'Article_PublishDate'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://news.shiep.edu.cn/', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title,time
        nid = 'n'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s15():
    url = 'http://www.sit.edu.cn/s/97/t/314/p/16/list.htm'
    rege = re.compile('/\w+/\w+/\w+/\w+/\w+/\w+/info\d{5}.htm')
    list2 = {'id': 'newslist'}
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href']
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'http://www.sit.edu.cn/', 'td', {'class': 'content'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        date = Service.getNewTitle2(get_href[i], 'http://www.sit.edu.cn/', 'td', {'height': '28'})
        title = Service.getNewTitle2(get_href[i], 'http://www.sit.edu.cn/', 'td', {'class': 'biaoti3'})
        print title
        date = str(date)
        time = date.replace('发布时间：','').replace('浏览次数：','').strip().lstrip().rstrip(',')
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print time
        nid = 'o'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s16():
    url = 'http://xww.sfu.edu.cn/info/iList.jsp?cat_id=12740'
    rege = re.compile('/\w+/\w+/\d{5}.htm')
    list2 = {'class': 'xjr_list'}
    date = Service.getNewsDate_2(url, 'div', list2, 'span')
    get_href = Service.getNewsUrl_div(url, list2, rege)
    # print get_href[1].attrs['href'], date[1].get_text()
    for i in xrange(0, len(date)):
        content = Service.getNewsContent(get_href[i], 'http://xww.sfu.edu.cn/', 'div', {'class': 'content'})
        if content == 0:
            print "获取内容失败，跳过"
            continue
        print content
        title = Service.getNewTitle(get_href[i])
        print title
        nid = 'p'
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print time
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s17():
    url = 'http://www.shupl.edu.cn/html/sy/xykx/1.html'
    rege = re.compile('http://www.shupl.edu.cn:80/html/sy/xykx/\d{4}/\d{2}/\d{2}/\w+-\w+-\w+-\w+-\w+.html')
    list2 = {'class': 'list_main_content'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'list_time'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], '', 'div', {'class': 'detail_content_display'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle2(get_href[i], '', 'h3', '')
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print title, time
        nid = 'q'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


def s18():
    url = 'http://www.sbs.edu.cn/xwzx/xyxw/'
    rege = re.compile('/\d{6}/t\d{8}\w+.html')
    list2 = {'class': 'news'}
    title = Service.getNewsDate_div(url, list2, 'li', {'class': 'list_title'})
    date = Service.getNewsDate_div(url, list2, 'li', {'class': 'list_date'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent2(get_href[i], 'http://www.sbs.edu.cn/xwzx/xyxw', 'p', {'align': 'justify'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        contents = ""
        for j in xrange(0,len(content)):
            contents = content[j].get_text("", strip=True)+contents
        print contents
        # print content)
        time = re.sub(r'[\(,\)]', '', date[i].string)
        time = time.replace('年', '-').replace('月', '-').replace('日','')
        print time, title[i].string
        nid = 'r'
        res = Service.judgeInsert('news', nid, time, title[i].string, contents)
        if res == 0:
            break


def s19():
    url = 'http://shanghai_edu.customs.gov.cn/tabid/44870/Default.aspx'
    rege = re.compile('/publish/portal135/tab\d{5}/module\d{6}/info\d{6}.htm')
    list2 = {'id': 'ess_ctr188254_ModuleContent'}
    get_href = Service.getNewsUrl_div(url, list2, rege)
    date = Service.getNewsDate(url, 'font', {'size': '2'})
    print get_href[1].attrs['href']
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent2(get_href[i], "",  'p', {'class': 'MsoNormal'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        contents = ""
        for j in xrange(0, len(content)):
            contents = content[j].get_text("", strip=True)+contents
        # print contents
        # print content.string
        time = date[i].string
        title = Service.getNewTitle(get_href[i])
        print title, time
        nid = 's'
        res = Service.judgeInsert('news', nid, time, title, contents)
        if res == 0:
            break


def s20():
    url = 'https://www.sumhs.edu.cn/rdxw/list.htm'
    rege = re.compile('/\w+/\w+/c\d{4}a\d{6}/page.htm')
    list2 = {'id': 'wp_news_w66'}
    date = Service.getNewsDate_div(url, list2, 'span', {'class': 'Article_PublishDate'})
    get_href = Service.getNewsUrl_div(url, list2, rege)
    print get_href[1].attrs['href'], date[1].get_text()
    for i in xrange(0, len(get_href)):
        content = Service.getNewsContent(get_href[i], 'https://www.sumhs.edu.cn', 'div', {'class': 'wp_articlecontent'})
        if content == 0:
            print "获取链接失败，跳过"
            continue
        # print content
        title = Service.getNewTitle(get_href[i])
        print title
        time = date[i].string
        print time
        nid = 't'
        res = Service.judgeInsert('news', nid, time, title, content)
        if res == 0:
            break


while True:
    os.system('news')
    threads = []
    t1 = threading.Thread(target=s1())
    threads.append(t1)
    t2 = threading.Thread(target=s2())
    threads.append(t2)
    t3 = threading.Thread(target=s3())
    threads.append(t3)
    t4 = threading.Thread(target=s4())
    threads.append(t4)
    t5 = threading.Thread(target=s5())
    threads.append(t5)
    t6 = threading.Thread(target=s6())
    threads.append(t6)
    t7 = threading.Thread(target=s7())
    threads.append(t7)
    t8 = threading.Thread(target=s8())
    threads.append(t8)
    t9 = threading.Thread(target=s9())
    threads.append(t9)
    t10 = threading.Thread(target=s10())
    threads.append(t10)
    t11 = threading.Thread(target=s11())
    threads.append(t11)
    t12 = threading.Thread(target=s12())
    threads.append(t12)
    t13 = threading.Thread(target=s13())
    threads.append(t13)
    t14 = threading.Thread(target=s14())
    threads.append(t14)
    t15 = threading.Thread(target=s15())
    threads.append(t15)
    t16 = threading.Thread(target=s16())
    threads.append(t16)
    t17 = threading.Thread(target=s17())
    threads.append(t17)
    t18 = threading.Thread(target=s18())
    threads.append(t18)
    t19 = threading.Thread(target=s19())
    threads.append(t19)
    t20 = threading.Thread(target=s20())
    threads.append(t20)
    time.sleep(86400)  #每隔一天运行一次 24*60*60=86400s

