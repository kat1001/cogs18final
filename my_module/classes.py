"""Classes used throughout project"""
import requests
import time 
from datetime import date
import numpy as np
import math
from IPython.display import Image
from my_module.functions import *



class BigConverter(): 
        
    def __init__(self,name, cur_start, cur_want, url = 'https://api.exchangerate-api.com/v4/latest/USD' ):
        """ Describes a BigConverter set
        
        Parameters
        -----------
        self.name : string
            Name of participant
        self.cur_start : int or float
            Starting amount of currency for converting
        self.cur_want : string
            Name of currency wanted
        self.api : dictionary
            Collection of exchange rate data as whole
        self.possi_rate : dictionary key
            Collection of exchange rate values       
        Return 
        ------------
        none
        
        """
        
        
        self.api = requests.get(url).json()
        self.possi_rate = self.api['rates']
        self.name = name
        self.cur_start = cur_start
        self.cur_want = cur_want.upper()
        
    def rate_fetcher(self):
        """ Gets the currency exchange rate for wanted value
        Parameters
        -----------
        want_today = string
            What value has the user selceted as wanted
        rate_today = list?
            exchange rate of the chosen value for the day
        name_today = string
            Name of user
        check = float or int
            Value of exchange rate to get rid of error?     
        stri_value = string
            String value of the rounded exchange rate
        Return 
        ------------
        Print statement giving the exchange rate for the desired currency per 1 USD.
        
        """
        want_today = self.cur_want
        rate_today = self.possi_rate[want_today]
        name_today = self.name
        check = rate_today
        stri_value = str(round(check,3))
        print(name_today + ' the exchange rate from usd to ' + self.cur_want + " is: " + stri_value + ' per each 1 USD')
     
    def converter(self):
        """ Gets the currency exchange rate for wanted value
        Parameters
        -----------
        want_today = string
            What value has the user selceted as wanted
        rate_today = float or int
            exchange rate of the chosen value for the day
        name_today = string
            Name of user
        stri_value = string
            String value of the exchange rate
        multiplier_key = list?
            amount of USD are started with
        strin_mult_key = string
            value of multiplier_key as a string
        exchanged = float
            value of the starting usd amount times the exchanged rate for desired currency
        stringyexchan = string
            value of the rounded exchange rate as a string
       
        Return 
        ------------
        Print statement providing the exchange currency value.
        """
        name_today = self.name
        want_today = self.cur_want
        rate_today = self.possi_rate[want_today]
        multiplier_key = self.cur_start 
        strin_mult_key = str(multiplier_key)
        exchanged = float(rate_today) * float(multiplier_key)
        stringyexchan = str(round(exchanged,3))
        print(name_today + ' I have exchanged your ' + strin_mult_key +' USD to ' + stringyexchan + ' ' + want_today)      


   

