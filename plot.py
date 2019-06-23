import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

def plot_posts(): # plots the number of posts on @shreyyajaiin
    posts = []
    time_labels =[]
    with open('index.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            posts.append(row[3])
            time_labels.append(row[0])
    plt.plot(time_labels, posts,"-o", label='number of posts on @shreyyajaiin')

def plot_rest():    # plots the number of followers @shreyyajaiin has and the number of accounts that 
    time_labels =[] # follow @shreyyajaiin
    followers =[]
    followees =[] 
    posts = []
    sorted_y = []

    with open('index.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            followers.append(row[1])
            time_labels.append(row[0])
            followees.append(row[2])
            posts.append(row[3])


    sorted_y = sorted(followers+followees)
    
    plt.plot(time_labels+time_labels, sorted_y, " ")
    plt.plot(time_labels, followees,"-o", label='number of people @shreyyajaiin follows')
    plt.plot(time_labels, followers,"-o", label ='number of people who follow @shreyyajaiin')
    
    plt.title("Data for @shreyyajaiin")
    plt.xlabel("Number of Days After January 1, 2019")
    plt.legend()
    plt.show()

plot_posts() # these are separate methods because there is always an error when plotting the number
plot_rest()  # of posts on a scale with sorted_y

