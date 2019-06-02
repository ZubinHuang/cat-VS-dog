import math
import os
import re
import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
from mpl_toolkits.axes_grid1 import host_subplot
from pylab import figure, show, legend

# read the log file
fp = open('/home/hzb/PycharmProjects/cat_dog/train.log', 'r')

train_iterations = []
train_loss = []
test_iterations = []
test_accuracy = []

for ln in fp:
    # get train_iterations and train_loss
    if '] Iteration ' in ln and 'loss = ' in ln:
        arr = re.findall(r'ion \d+.*?', ln)
        train_iterations.append(int(arr[0][4:]))
        train_loss.append(float(ln.strip().split(' = ')[-1]))

    # get test_iteraitions
    if '] Iteration' in ln and 'Testing net (#0)' in ln:
        arr = re.findall(r'ion \b\d+\b,', ln)
        test_iterations.append(int(arr[0].strip(',')[4:]))
    # get test_accuracy
    if '#0:' in ln and 'accuracy =' in ln:
        test_accuracy.append(float(ln.strip().split(' = ')[-1]))
fp.close()

host = host_subplot(111)
plt.subplots_adjust(right=0.8)  # ajust the right boundary of the plot window
par1 = host.twinx()
# set labels
host.set_xlabel("iterations")
host.set_ylabel("log loss")
par1.set_ylabel("test accuracy")

# plot curves
p1, = host.plot(train_iterations, train_loss, 'ob-', label="training loss")
p2, = par1.plot(test_iterations, test_accuracy, 'xg-', label="test accuracy")
#p3, = par1.plot(test_iterations, test_accuracy, 'xg-', label="validation accuracy")

# set location of the legend,
# 1->rightup corner, 2->leftup corner, 3->leftdown corner
# 4->rightdown corner, 5->rightmid ...
host.legend(loc=5)

# set label color
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
# set the range of x axis of host and y axis of par1
host.set_xlim([0, 100000])
par1.set_ylim([0., 1.05])
plt.draw()
plt.show()