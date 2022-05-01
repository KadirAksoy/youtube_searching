import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
##webdriver'ı güncel tutmalısın.

def open_video(video_name):
    video_name = str(video_name)            #Video adını aldık ve stringe çevirdik.
    driver=webdriver.Chrome()               #Driver değişkenimizi oluşturduk.
    driver.get("https://www.youtube.com/")  #Değişkenimizi youtube'a yönlendirdik.

                                            #Arama motoruna erişim sağladık.
    search = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input") 
    time.sleep(10)

    search.send_keys(video_name)            #Video adını arama motoruna girdik.
    search.send_keys(Keys.ENTER)            #Enter tuşuna bastık
    time.sleep(10)

                                            #Videoyu başlattık.
    click = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string') 
    click.click()
    





