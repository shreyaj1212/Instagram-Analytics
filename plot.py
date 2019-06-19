import matplotlib as mpl
import matplotlib.pyplot as plt
#import numpy as np
import csv
#from datetime import date

def plot_all():
    followers =[]
    time_labels =[]
    followees =[] 

    with open('index.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            followers.append(row[1])
            time_labels.append(row[0])
            followees.append(row[2])

    sorted_y = sorted(followers+followees)
    
    plt.plot(time_labels+time_labels, sorted_y, " ")

    plt.plot(time_labels, followees,"-o", label='number of people @shreyyajaiin follows')
    plt.plot(time_labels, followers,"-o", label ='number of people who follow @shreyyajaiin')
    plt.title("Data for @shreyyajaiin")
    plt.xlabel("Number of Days After January 1, 2019")
    #plt.ylabel("Number")
    plt.legend()
    #plt.xlim(168, 365)
    #plt.ylim(200, 300)
    plt.show()

plot_all()
