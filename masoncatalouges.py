# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:50:17 2017

@author: emadezzeldin
"""

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html
import time
import sqlite3

#courses = [str (link.text) for link in browser.find_elements_by_tag_name ('a') if str (link.text) [-1:] in map (str,range (10))]
#courses.remove ('University Catalog\n2017-2018')
#courseslinks= [str (link.get_attribute('href')) for link in browser.find_elements_by_tag_name ('a') if str (link.text) [-1:] in map (str,range (10))]
#courseslinks.remove ('http://catalog.gmu.edu/') 
#courses_formatter = [course.replace(' ','+') for course in courses]
#baseurl = 'http://catalog.gmu.edu/search/?scontext=courses&search='
#urls    = [baseurl + course for course in courses_formatter]



def openbrowser():
    global browser
    current_directory = os.getcwd()
    path_to_chromedriver = current_directory + '/chromedriver'
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
def update_root ():
    global root
    root = lxml.html.fromstring(browser.page_source)


#http://catalog.gmu.edu/colleges-schools/engineering/data-analytics-engineering-ms/#requirementstext

#http://catalog.gmu.edu/search/?scontext=courses&search=
#

#coursedesc = []
def run_gmu ():
    for url in urls[128:]: 
        try:
            browser.get (url)
            coursedesc.append (str (browser.find_element_by_class_name ('courseblockdesc').text))
            time.sleep (5)
        except:
            continue
        
        
def store ():
    conn = sqlite3.connect ('DEAN.sqlite')
    cur  = conn.cursor ()
    cur.execute (''' DROP TABLE IF EXISTS Courses''')
    cur.execute ('''CREATE TABLE IF NOT EXISTS Courses  (CourseTitle VARCHAR , CourseURL VARCHAR , Coursedesc VARCHAR)''')
    for i in range (133):
        Title = courses [i]
        url   = urls [i]
        Desc  = coursedesc [i]
        cur.execute (''' INSERT INTO Courses (CourseTitle,CourseURL,Coursedesc) VALUES (?,?,?)''', (Title,url,Desc))
    conn.commit()
    cur.close ()