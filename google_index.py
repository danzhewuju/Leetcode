import re
import urllib.request
import urllib.error
import urllib.parse
import json
class GoogleIndex: # 通过google来检索论文的引用次数
    def __init__(self):
        self.url = 'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={}&btnG='
    
    def pre_paper_name(self, name):# 论文名称的预处理
        words = name.split()
        self.paper_name = "+".join(words)

    def get_index(self, paper_name):
        self.pre_paper_name(paper_name)
        self.url = self.url.format(self.paper_name)
        header={'Host': 'scholar.google.com',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Referer': 'https://scholar.google.com/schhp?hl=zh-CN',
             'Connection': 'keep-alive'}
        req = urllib.request.Request(url=self.url, headers=header)
        html = urllib.request.urlopen(req).read().decode('utf8')  # 打开url
        html = str(html)
        print(html)

google = GoogleIndex()
print(google.get_index("Decoding EEG by Visual-guided Deep Neural Networks"))


    



        
