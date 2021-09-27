#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import urllib.request
import json
API_KEY = 'HP68RMSSEI5OE1E4' 
def getStockData(symbol):
    global y
    global responseString
    global d
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
    ending = '&apikey=' + API_KEY
    fullURL = baseURL + symbol + ending
    print()
    print('Just a min, waiting for the data.....')
    connection = urllib.request.urlopen(fullURL)
    responseString = connection.read().decode()
    d='\n Response in JSON format is:{} \n'.format(responseString)
    prefixString = '"05. price": "'
    prefixStringPosition = responseString.index(prefixString)
    prefixStringLength = len(prefixString)
    start = prefixStringPosition + prefixStringLength
    end = responseString.index('"', start)
    prefixStringLength = len(prefixString)
    start = prefixStringPosition + prefixStringLength
    end = responseString.index('"', start)
    price = responseString[start:end]
    return price
    
def main():
    
    while True:
        f = open('japi.out', 'a')
        print()
        symbol = input('\n Enter your stock symbol (or press ENTER to quit): ')
        y=json.loads(responseString)
        # print('Response in Dictionary format is: ', y)
        if symbol == 'exit':
            break
        SPrice = getStockData(symbol)
        print()
        c='Response in Dictionary format is:\n {} \n'.format(y)
        f.write(d)
        f.write(c)
        b='\n The current price of {} is {} \n'.format(symbol, SPrice)
        f.write(b)
        e='--------------------------------------------------------------------------------------------------'
        f.write(e)
        print(d)
        print(c)
        print(b)
        print(e)
main()






# In[ ]:




