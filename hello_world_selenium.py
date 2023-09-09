#sudo apt-get install chromium-chromedriver in case of ubuntu
import unittest
from  pyunitreport import HTMLTestRunner#helps orchestrate the thingy
from selenium import webdriver

class HelloWorld(unittest.TestCase):#all of our test cases
    @classmethod
    def set_UpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedrivee')
        driver=cls.driver
        driver.implicitly_wait(10) 
        
    def test_search_text_field(self):
        
        
    def tests_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')
    def test_visit_wikipedia(self):
        self.driver.get('')
    @classmethod    
    def tear_downClass(cls):
        cls.driver.quit()
        return super().tearDown()
    
    if __name__ =='__main__':
        unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello-world-report'))
    
        