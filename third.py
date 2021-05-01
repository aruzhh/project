from tkinter import *
import csv

filename = 'weather.csv'
f_open = open(filename)
read = csv.reader(f_open, delimiter=',')
data = list(read)
del(data[0])
city = []
date = []
var = []
tem = []
step = 0
for x in range(0, len(data)):
    date.append(data[x][1])
    city.append(data[x][0])