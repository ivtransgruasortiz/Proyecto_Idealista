#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 20:38:13 2018

@author: iv
"""

###############################
## SELECT PLATFORM: ##########
#############################    
###-- WINDOWS OR LINUX --###
###########################
import sys
if sys.platform == 'win32':
    path = 'C:\\Users\\ivan.ortiz\\Documents\\MisProgramas_Iv_PYTHON\\CRIPTOMONEDAS\\'
    print ('\n#### Windows System ####')
    system = sys.platform
else:
    path = '/home/iv/Desktop/MasterBIGDATA/'
    print ('\n#### Linux System ####')
    system = sys.platform

#print ('\n')
print ('#####################################')
print ('#####################################')
print ('\n### Importing Libraries... ###')
import time
import datetime
import pandas as pd
import numpy as np
import pylab as pl
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import csv
import json
import lxml
import urllib
import statsmodels
import pylab
import requests as rq
import sklearn
import nltk
import scipy
import tables
import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import datetime as dt
import timeit
import math
from scipy import stats
from pandas_datareader import wb, DataReader
import wget
import tqdm #from tqdm import trange # Barra de progreso en bucles ## for i in trange(<number>) ##
import base64

def get_oauth_token():
    url = "https://api.idealista.com/oauth/token"
    
    apikey= ''
    secret= ''
    auth = base64.b64encode(apikey + ':' + secret)
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' ,'Authorization' : 'Basic ' + auth}
    params = urllib.urlencode({'grant_type':'client_credentials'})
    content = rq.post(url,headers = headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    return bearer_token

def search_api(token, url):
    """
    token: oauthtoken
    country: es, it, pt
    max_items: num max of item listed
    operation: sale or rent
    propertyType: homes, offices, premises, garages, bedrooms   
    """    
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
    content = rq.post(url, headers = headers)
    result = json.loads(content.text)#['access_token']
    return result

country = 'es' #values: es, it, pt
locale = 'es' #values: es, it, pt, en, ca
language = 'es' #
max_items = '50'
operation = 'sale' #values: sale, rent
property_type = 'homes' #values: homes, offices, premises, garages, bedrooms
order = 'priceDown' 
'''
homes : distance, price, street, photos, publicationDate,
modificationDate, size, floor, rooms, ratioeurm2 (sólo alquiler),
weigh, priceDown
'''
center = '40.4167,-3.70325' 
distance = '60000'
sort = 'desc'
bankOffer = 'false'
numPage = '1'
#minSize =  #minsize (from 60 m2 to 1000m2)
#maxSize =  #maxSize (from 60 m2 to 1000m2)
#virtualTour = #boolean 
#flat = #boolean 
#penthouse = #boolean 
#duplex = #boolean 
#studio = #boolean 
#chalet = #boolean 
#countryHouse = #boolean
# chalet subtypology (for propertyType = homes and chalet = true)
#subTypology =  #values: [independantHouse, semidetachedHouse,terracedHouse]
df_tot = pd.DataFrame()
limit = 10
for i in range(1,limit):
    url = ('https://api.idealista.com/3.5/'+country+'/search?operation='+operation+#"&locale="+locale+
           '&maxItems='+max_items+
           '&order='+order+
           '&center='+center+
           '&distance='+distance+
           '&propertyType='+property_type+
           '&sort='+sort+ 
           '&numPage=%s'+
#           '&t=%s'+
#           '&apikey={api_key}'+
#           '&bankOffer='+bankOffer
           '&language='+language) %(i)

          
    a = search_api(get_oauth_token(), url)
    df = pd.DataFrame.from_dict(a['elementList'])
    df_tot = pd.concat([df_tot,df])
df_tot = df_tot.reset_index()





