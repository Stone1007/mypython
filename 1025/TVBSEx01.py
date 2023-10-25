# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:16:27 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://supertaste.tvbs.com.tw/food'


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')

#food = soup.find('div',class_ = 'article__content')

food = soup.find('div',{'class' : 'article__content'})

a = food.find_all('a')

for row in a:
    img = row.find('img').get('data-original')
    title = row.find('h3').text.strip()
    postdata = row.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw/' + row.get('href')
    print('圖片 :',img)
    print('標題 :',title)
    print('日期 :',postdata)
    print('連結 :',link)
    print()
    print()
    
    
    
    
    
    
    
    
    