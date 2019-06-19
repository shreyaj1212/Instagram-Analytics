#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:56:43 2019

@author: Shreya Jain
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression as lr
from threading import Timer
from datetime import date
#from apscheduler.schedulers.blocking import BlockingScheduler

def get_num_followers():
	now = datetime.datetime.now()
	#print(now)
	url = "https://inkphy.com/user/shreyyajaiin"
	html = urlopen(url)
	soup = BeautifulSoup(html, 'lxml')
	type(soup)

	text = soup.get_text()
	#print(text)

	i=0

	all_span = soup.find_all('span')
	#print(all_span)
	for span in all_span:
		i=i+1
		if i==6:
			numFollows = span.text
			print("@shreyyajaiin has " + numFollows +  " followers.")
	return numFollows
	"""with open('index.csv', 'a') as csv_file:
					writer = csv.writer(csv_file)
					print("writing [" + str(numFollows) + ", "+str(to_int(now))+"]...")
					writer.writerow([numFollows, to_int(now)])
				df = pd.read_csv('index.csv')"""

def get_num_follows():
	now = datetime.datetime.now()
	#print(now)
	url = "https://inkphy.com/user/shreyyajaiin"
	html = urlopen(url)
	soup = BeautifulSoup(html, 'lxml')
	type(soup)

	text = soup.get_text()
	#print(text)

	i=0

	all_span = soup.find_all('span')
	for span in all_span:
		i=i+1
		if i==7:
			numFollows = span.text
			print("@shreyyajaiin follows " + numFollows +  " other accounts.")
	return numFollows
	"""with open('follows.csv', 'a') as csv_file:
					writer = csv.writer(csv_file)
					print("writing [" + str(numFollows) + ", "+str(to_int(now))+"]...")
					writer.writerow([numFollows, to_int(now)])
				df = pd.read_csv('follows.csv')"""

def to_int(date):
	mon = date.month
	return 365*(date.year-2019) + get_days(mon, date.year) + date.day

def determine_num_days_per_month(mon, year):
	num_days_per_month = 0
	if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon==8 or mon == 10 or mon ==12:
		num_days_per_month=31
	elif mon==2:
		is_div_by_4 = year%4
		if is_div_by_4==0:
			num_days_per_month=29
		else:
			num_days_per_month=28
	else:
		num_days_per_month=30 
	return num_days_per_month

def get_days(month, year):
	sum = 0
	for i in range(month-1):
		sum = sum + determine_num_days_per_month(i, year)
	return sum

def write_to_index():
	numFollowers = get_num_followers()
	numFollowees = get_num_follows()
	now = to_int(datetime.datetime.now())
	with open('index.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([now, numFollowers, numFollowees])

write_to_index()

