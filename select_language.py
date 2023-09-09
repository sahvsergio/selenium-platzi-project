import  unittest
from selenium  import webdriver
from selenium.webdriver.support.ui import Select

from  ddt import ddt ,data, unpack

@ddt
#before  the class



@data(('dress',6),('music',5))
@unpack