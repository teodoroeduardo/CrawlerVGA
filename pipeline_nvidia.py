from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import pandas as pd
import datetime as dt
import os
import time
from numpy import loadtxt
import numpy as np 
import re

df = pd.read_csv("./tables/KABUM - VGA_NVIDIA 20221205.csv")

class header:
    
    txt_manufacturers = open("./lists/list_manufacturers_vga.txt","r")
    txt_models = open("./lists/list_models_vga.txt","r")
    txt_lines = open("./lists/list_lines_vga.txt","r")
    
    list_manufacturers = txt_manufacturers.read().splitlines() 
    list_models = txt_models.read().splitlines()
    list_lines = txt_lines.read().splitlines()

    pattern_manufacturers = '|'.join(list_manufacturers)
    pattern_model = '|'.join(list_models)
    pattern_line = '|'.join(list_lines)

    df_nvidia = pd.read_csv('./tables/KABUM - VGA_NVIDIA 20221205.csv')

headers = header()
    
def model_searcher(search_str:str,search_list:str):
    search_obj = re.search(search_list,search_str,re.IGNORECASE)

    if search_obj:
        return_str = search_str[search_obj.start():search_obj.end()]
    else:
        return_str = 'NA'
    return return_str

df['Fabricante'] = df['Produto'].apply(lambda x:model_searcher(search_str=x,search_list=getattr(headers,'pattern_manufacturers')))
df['Modelo'] = df['Produto'].apply(lambda x:model_searcher(search_str=x,search_list=getattr(headers,'pattern_model')))
df['Linha'] = df['Produto'].apply(lambda x:model_searcher(search_str=x,search_list=getattr(headers,'pattern_line')))

df['Modelo'] = df['Modelo'].str.cat(df['Linha'],sep=' ')
df['Linha'].dropna()
print(df)