from bs4 import BeautifulSoup
import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search = input("enter your search: ")
r = requests.get("https://www.youtube.com/results?search_query=" + search)

path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
soup = BeautifulSoup(r.content, "html.parser")

results = soup.find_all("h3", {"class": "yt-lockup-title"})

videos = []
list = []
for items in results:
    list.append(items.a.text)
    videos.append(items.a["href"])

print("List Of Videos Found")
print("--------------------------------")
ct = 1
for i in list:
    print(str(ct) + ')' + i)
    ct += 1

print("================================")
choice = int(input("Enter Your Choice: "))

output = "https://youtube.com" + videos[choice-1]

driver = webdriver.Chrome()

driver.get("http://en.savefrom.net/")

link = driver.find_element_by_xpath('//*[@id="sf_url"]')
link.send_keys(output)

submit = driver.find_element_by_xpath('//*[@id="sf_submit"]')
submit.click()
try:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    quality = soup.find("div", {"class":"drop-down-box"})
    itms = quality.find_all("a")
    lst = []
    vid = []
    for it in itms:
        lst.append(it.text)
        vid.append(it["href"])

    ct = 1
    for i in lst:
        print(str(ct)+")"+i)
        ct += 1

    print("===============================")
    choice = int(input("Enter your choice: "))
    print("===============================")
    print("Your video is being downloaded...............")
#webbrowser.get(path).open(vid[choice-1])
    driver.get(vid[choice-1])
except:
    print("Sorry!!Video not found")
