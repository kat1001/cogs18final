"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import my_func, my_other_func
from my_module.functions import *
from my_module.classes import *
##
##
### tests if fetchrate function returns valid results
def test_fetchrate():
    curr_fetch = BigConverter('tay', 15.06, 'aud')
    assert curr_fetch.rate_fetcher() is not None
    assert test_fetchrate() == None
### tests if converter function returns valid results
def test_converter():
    curr_fetch = BigConverter('tay', 15.06, 'aud')
    assert curr_fetch.converter() is not None
    assert test_converter() == None
### tests if convert_curr is callable   
def test1():
    assert callable(convert_curr)
### tests if get_weekday is callable    
def test2():
    assert callable(get_weekday)
def test3():
    assert get_weekday == type(string)
def test4():
    assert callable(fetchrate)
  




                 
    