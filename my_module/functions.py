"""A collection of function for doing my project."""
import requests
import time 
from datetime import date
import numpy as np
import math

from my_module.classes import *

def start():
    """ Prompts to learn or convert
        -----------
        name = string
            name of participant
        user_decision = string
            User input to make decision and call other functions
        return
        -----------
        new function named called
        """
    today = get_weekday()
    print("Happy " + today + "! Let's get into it I heard you'd like to convert some currency !")
    
    time.sleep(2) 
    print("I'm currently able to convert USD into different currencies!")
    time.sleep(1)
    print ( 'such as AUD, EUR, JPY, GBP, CHF, CAD, ZAR, MXN, CNY, and more!')
    time.sleep(2)
    print("So let's get converting!")
    time.sleep(1) 
    start_options()

def start_options():
    """ Prompts to learn or convert
        -----------
        name = string
            name of participant
        user_decision = string
            User input to make decision and call other functions
        return
        -----------
        new function named called
        """
    
    print("Who am I speaking with today?")
    time.sleep(1) 
    user_name = input("Type name: ")
    time.sleep(2)
    print(user_name + " are you interested in learning the current exchange rate or would you like to convert some currency?")
    time.sleep(1)
    user_decision = input("Type 'learn' or 'convert' or 'quit' to end session: ")
    time.sleep(2) 
    if user_decision.lower() == 'learn' or 'convert':
        decisionbool = False
    else:
        decisionbool = True
    
    while decisionbool == False:    
        if user_decision.lower() == 'learn':
            fetchrate(user_name)
        elif user_decision.lower() == 'convert':
            convert_curr(user_name)
    
        
def start_options2(name):
    
    """ Prompts to learn or convert
        -----------
        name = string
            name of participant
        user_decision = string
            User input to make decision and call other functions
        return
        -----------
        new function named called
        """
    name = name 
    print("Welcome back " + name + " are you interested in learning the current exchange rate or would you like to convert some currency?")
    time.sleep(2)
    user_decision = input("Type 'learn' or 'convert' or 'quit' to end session: ")
    
    time.sleep(2) 
    if user_decision == 'learn' or 'convert':
        decisionbool = False
    else:
        decisionbool = True
        
    while decisionbool == False:    
        if user_decision == 'learn':
            fetchrate(name)
        elif user_decision == 'convert':
            convert_curr(name)
        
        
def fetchrate(name):
    """ Prompts to retrieve exchange rate of currency
        -----------
        name = string
            name of participant
        curr_type = string
            User input what is desired currency type
        return
        -----------
        new function named called
        """
    name = name
    print (name + ' what currency would you like to know the exchange rate for?')
    curr_type = input("currency type: ")
    rate_fetch = BigConverter(name , 0, curr_type)
    rate_fetch.rate_fetcher()
    time.sleep(4) 
    print ("Let's go back to the original options!")
    time.sleep(2)
    start_options2(name)
    

def convert_curr(name):
    """ Prompts to convert currency
        -----------
        name = string
            name of participant
        curr_want = string
            User input what is desired currency type
        curr_fetch = string
            User input of starting amount of USD
        return
        -----------
        new function named called
        """
    print("How many USD are you starting with today?")
    start_amount = input("starting USD: ")
    curr_want = input("What currency are you converting to?: ")
    curr_fetch = BigConverter(name, start_amount, curr_want)
    curr_fetch.converter()
    time.sleep(4) 
    print ("Let's go back to the original options!")
    time.sleep(2)
    start_options2(name)
     
    return none

def get_weekday():
    """ Retrieves the day of use
        -----------
        today = int
            from 0 (Monday) to 6 (Sunday) value of days
        dayoweek = string
            the day of the week
        -----------
        dayoweek
        """
    today = date.today().weekday()
    if today == 0:
        dayoweek = 'Monday'
    elif today == 1:
        dayoweek = 'Tuesday'
    elif today == 2:
        dayoweek = 'Wednesday'
    elif today == 3:
        dayoweek = 'Thursday'
    elif today == 4:
        dayoweek = 'Friday'
    elif today == 5:
        dayoweek = 'Saturday'
    else:
        dayoweek = 'Sunday'
    return dayoweek
   