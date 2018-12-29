# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

pattern = re.compile(r'(<strong>(\d+?)</strong>)+')

def spider():
    url_head = 'http://jyc.kxue.com/list/'
    tag_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
              'p','q','r','s','t','u','v','w','x','y','z']
    print("start......")
    for tag in tag_list:
        page_num = 1
        page_count=0
        flag = True
        content = ''
        content = tag+'\n'
        while flag:
            if page_num == 1:
                url = url_head + tag +'.html'
            else:
                url = url_head + tag + '_' + str(page_num) + '.html'
            print("url",url)
            r = requests.get(url)
            r.encoding='gbk'
            doc_html = r.text
            doc_b = BeautifulSoup(doc_html, "lxml")
            if page_num == 1:
                pageinfo = doc_b.find('span', class_ = 'pageinfo')
                page_total = pageinfo.strong.get_text()
                # 正则方式取值
                # pageinfo = pageinfos[0]
                # m = pattern.findall(str(pageinfo))
                # page_total = m[0][1]
            page_num += 1
            if page_num > int(page_total):
                flag = False
            for item in doc_b.find_all('span', class_='hz'):
                if item.a == None or item.span == None:
                    continue
                content += str(item.a.get_text()) + '        ' + str(item.span.get_text()) +'\n'
        with open('synonyms.txt','a+', encoding='utf-8') as f:
            f.write(content)
    print("finish")

if __name__ == '__main__':
    spider()