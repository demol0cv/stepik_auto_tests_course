import math
from abc import abstractmethod

from selenium import webdriver

browser = webdriver.Firefox()

@abstractmethod
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

