from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime as dt
import os
import time

class KabumCrawler():
    
    list_tmp = []

    driver = webdriver.Firefox()
    driver.get("https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia?page_number=1")
    driver.implicitly_wait(5)

    now = dt.datetime.now()
    now_str = now.strftime("%d/%m/%Y %H:%M:%S")
    now_save = now.strftime("%Y%m%d")

    list_kabum =[]
    qtd_produtos = int(driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div/div[1]/div/div[2]/b").text)

    try:
        count = 0
        while (count <= qtd_produtos):
            count = len(driver.find_elements(By.CSS_SELECTOR,"div.sc-ff8a9791-7")) + count

            for i in range(1,len(driver.find_elements(By.CSS_SELECTOR,"div.sc-ff8a9791-7"))+1):
                vgaTitle = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div/main/div[%i]/a/div/button/div/h2/span" %(i))
                vgaPrice = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div/main/div[%i]/a/div/div/span[2]" %(i))
                vgaLink = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[8]/div/div[2]/div[1]/main/div[%i]/a" %(i))
                list_kabum.append((vgaTitle.text,vgaPrice.text,vgaLink.get_attribute('href'),now_str))
                print(list_kabum)           
            
            try:
                driver.find_element(By.XPATH,"//li[@class='next']").is_displayed()
                driver.find_element(By.XPATH,"//li[@class='next']").click()
                time.sleep(2)
            except Exception as e:
                pass
        
        df_kabum = pd.DataFrame(list_kabum,columns=["Produto","Preço","Link","Data"])
        df_kabum_clean = df_kabum.drop_duplicates()
        filename = 'KABUM - VGA_NVIDIA {}.csv'.format(now_save)
        outdir = './tables'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        savecrawler = os.path.join(outdir,filename)

        df_kabum_clean.to_csv(savecrawler)
        
        driver.quit()
    except Exception as e:
        pass

KabumCrawler()