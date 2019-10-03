# my chinese girlfriend has infulenced this code
# apparently chinese bing has "better" images
import re
import os
import requests
from time import sleep

headers = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
                   "Gecko/20100101 Firefox/64.0")
}

def get_index(resolution, index=1):
    url = f"https://bing.ioliu.cn/ranking?p={index}"
    res = requests.get(url, headers=headers)
    urls = re.findall('pic=(.*?)\\.jpg', res.text)
    _old_resolution = urls[1].split("_")[-1]
    return {url.split("/")[-1].replace(_old_resolution, resolution): url.replace(_old_resolution, resolution) + ".jpg"
            for url in urls}

def download_pic(pics):
    if os.path.exists('Bing wallpaper'):
        pass
    else:
        os.mkdir('Bing wallpaper')
        print('Directory created successfully')
    try:
        for pic_name, pic_url in pics.items():
            res = requests.get(pic_url, headers=headers)
            with open(f"ing wallpaper\\{pic_name}.jpg", mode="wb") as f:
                f.write(res.content)
            print(f"{pic_name} Download completed")
    except Exception as e:
        print("Download completed", e)

def input_index():
    print("Bing Wallpaper Download Tool, this tool is not authorized by the resource station.")
    print("For learning and communication purposes only, it is possible to stop maintenance at any time..")
    print("At present, the resource station has 87 pages, and currently only provides 1920x1080 resolution download")
    while True:
        sleep(0.1)
        index = input("Please enter the number of pages to download(Max=87):")
        try:
            if index == "Q":
                exit()
            index = 87 if int(index) > 87 else int(index)
            return index
        except ValueError:
            print("Please enter a number, or enter Q to quit!")

def main():
    index = input_index()
    i = 1
    while i <= index:
        print(f"Currently on page {i}, a total of {index} pages need to be downloaded")
        pics = get_index("1920x1080", i)
        download_pic(pics)
        i += 1
    print("The download is complete and will close after 3 seconds...")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("0")

if __name__ == '__main__':
    main()
