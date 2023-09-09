from unittest import TestLoader,TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from  hello_world_seleniuum import SearchTests

assertions_test=TestLoader().loadTestsFromTestCase(AssertionsTest)
smoketest=TestSuite([assertions_test,search_test])

kwargs={'output':'smoke-report'}


runner=HTMLTestRunner(**kwargs)
runner.run(smoketest)