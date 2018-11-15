#下载个性网上主栏目下的图片

import os

import requests
#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

from bs4 import BeautifulSoup

savePath = "F:\七牛云测试上传图片\mycomic_picture"

comicmainUrl ="https://www.woyaogexing.com/tupian/dongman/"
mainurl = "https://www.woyaogexing.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}




def createFilePath(save_Path):

    if os.path.exists(save_Path) is False:
        os.makedirs(save_Path)

    #保持在当前目录下
    os.chdir(save_Path)



def downloadPicture(title_url):

    lanmu_response = requests.get(title_url,headers= headers)

    #使用response.content 替换response.text 解决中文乱码的问题
    soup = BeautifulSoup(lanmu_response.content,"html.parser")

    # 找到主标签栏目
    lanmu_index = soup.find("div",id="main")

    lanmu_pic_index = lanmu_index.find("div",class_="pMain pMain_1") #获取包含图片div列表

    #print(lanmu_pic_index)

    # 获得当前栏目下所有包含img(包含图片)的列表
    lanmu_pic_my_lindex = lanmu_pic_index.findAll("a",class_="img")


    # [< img class ="lazy" src="//img2.woyaogexing.com/2018/11/15/2b350b8d057b62c9!380x240.jpg" / >,......]

    #print(lanmu_pic_my_lindex)

    for pic_item in lanmu_pic_my_lindex:

        #print(pic_item)

        #得到图片的地址
        pic_url = pic_item.find("img").get('src')

        href = mainurl + pic_item.get("href")

        #print(href)
        file_name = pic_url
        try:

            abslute_url = "https:"+pic_url

            print(abslute_url)

            # 获取图片title作为文件名称
            file_name = pic_item.get('title')+".jpg"

            myheaders = {'Referer': href}

            img = requests.get(abslute_url,headers = myheaders)

            f = open(file_name, 'ab')

            f.write(img.content)

            print(file_name,'图片保存成功!')

            f.close()

        except Exception as e:

            print(e)





def main():
    print("执行main方法----")
    createFilePath(savePath)

    response = requests.get(comicmainUrl,headers= headers)

    #使用response.content 替换response.text 解决中文乱码的问题
    soup = BeautifulSoup(response.content,"html.parser")
    #soup = BeautifulSoup(response.text,"html.parser",content.decode('gb2312', 'ignore'))
    # 找到主标签栏目
    lanmu_index = soup.find("div",id="main")

    lanmu_all = lanmu_index.find("div",class_="subnav-l z").find_all("a")

    #print("lanmu_all"+lanmu_all.tostring())


    for lanmu_title in lanmu_all:
        print(lanmu_title.text)   #打印出标签栏目名称

        createFilePath(lanmu_title.text)

        lanmuurl = mainurl + lanmu_title.get("href")
        #print(lanmuurl)

        downloadPicture(lanmuurl)

        #执行完一组照片下载后，切换到上级目录执行
        os.chdir(os.path.pardir)




if __name__ == '__main__':
    main()

