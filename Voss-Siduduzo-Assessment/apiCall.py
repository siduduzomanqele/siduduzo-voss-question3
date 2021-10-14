import json
import requests
import os
import traceback
import sys
import urllib.request
import shutil

headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
currentDir = os.getcwd()
imageDir = os.path.join(currentDir, 'Images')



def ImageDl(url,foldername):
    attempts = 0
    while attempts < 2:#retry 2 times
        try:
            filename = url.split('/')[-1]
            r = requests.get(url,headers=headers,stream=True,timeout=5)
            if r.status_code == 200:
                path = os.path.join(imageDir, foldername)
                with open(os.path.join(path,filename),'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw,f)
            print(filename)
            break
        except Exception as e:
            attempts+=1
            print(e)


def createFolder(mydirectory):
    path = os.path.join(imageDir, mydirectory)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    print("Directory '% s' created" % mydirectory)


def saveimages(counter):
    urljoin = "https://reqres.in/api/users?page="+ str(counter)
    response = requests.get(urljoin)
    res = response.json()
    print(res["data"])
    for i in res["data"]:
        imageUrl = i['avatar']
        foldername = i['first_name'] + i['last_name'] + str(i['id'])
        print(foldername)
        print(imageUrl)
        createFolder(foldername)
        ImageDl(imageUrl,foldername)
        print()


for i in range(2):
    i+=1
    saveimages(i)

