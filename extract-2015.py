#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import fileinput
import sys

display = Display(visible=0, size=(800, 600))
display.start()

def grab(name_url):
    name, url = name_url.split(',')
    browser = webdriver.Chrome()
    browser.get(url)

    TIMEOUT = 30
    WebDriverWait(browser, TIMEOUT).until(
        lambda session: len(session.find_elements_by_tag_name('source')) > 1)

    # from ipdb import set_trace; set_trace(context=20)
    # with open('2.html', 'w') as file_object:
    #     file_object.write(browser.page_source)

    sources = browser.find_elements_by_tag_name('source')
    for source in sources:
        src = source.get_attribute('src')
        src = src[:src.find('?')]
        if 'presenter' in src:
            suffix = '-presenter'
        elif 'presentation' in src:
            suffix = '-presentation'
        else:
            suffix = '-unknown'
        print('%s,%s' % (name + suffix, src))
    browser.quit()

for line in fileinput.input():
   sys.stdout.flush()
   try:
       grab(line)
   except Exception as e:
       print(line, e)

display.stop()
