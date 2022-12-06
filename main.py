from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import pandas as pd
import datetime as dt
import os


class SeleniumStartPage():
   
    def CrawlerNvidiaKabum():
        list_vga_tmp =[]

        driver = webdriver.Firefox()
        driver.get("https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia")
        driver.implicitly_wait(5)
        now = dt.datetime.now()
        now_str = now.strftime("%d/%m/%Y %H:%M:%S")
        now_save = now.strftime("%Y%m%d")
        
        for i in range(1,21):
            vgaTitle = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div/main/div[%i]/a/div/button/div/h2/span" %(i))
            vgaPrice = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div/main/div[%i]/a/div/div/span[2]" %(i))
            vgaLink = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div[1]/main/div[%i]/a" %(i))
            list_vga_tmp.append((vgaTitle.text,vgaPrice.text,vgaLink.get_attribute('href'),now_str))
        
        driver.find_element(By.XPATH,"//li[@class='next']").click()
       
        df_vga_nvidia_kabum = pd.DataFrame(list_vga_tmp,columns=["Produto","Preço","Link","Timestamp"])      
        
        
        #driver.quit()


SeleniumStartPage()
SeleniumStartPage.CrawlerNvidiaKabum()


"""        filename = 'KABUM - VGA_NVIDIA {}.csv'.format(now_save)
        outdir = './tables'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        savecrawler = os.path.join(outdir,filename)

        df_vga_nvidia_kabum.to_csv(savecrawler)"""

