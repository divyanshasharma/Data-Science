import matplotlib.pyplot as plt

x=['NB CV','NB tfidf','LogRegression Regularized','ANN']

y1=[0.851,0.858,0.894,0.896]
y2=[0.864,0.872,0.902,0.908]
y3=[0.841,0.852,0.898,0.900]
y4=[0.855,0.862,0.897,0.898]
y5=[0.836,0.847,0.892,0.897]
y6=[0.853,0.867,0.895,0.902]

plt.style.use('seaborn')
line1 = plt.plot(x,y1,label='X1',marker='*',markersize=10) #Plotting data1
line2 = plt.plot(x,y2,label='X2',marker='*',markersize=10) #Plotting data2
line3 = plt.plot(x,y3,label='X3',marker='*',markersize=10) #Plotting data3
line4 = plt.plot(x,y4,label='X4',marker='*',markersize=10) #Plotting data4
line5 = plt.plot(x,y5,label='X5',marker='*',markersize=10) #Plotting data5
line6 = plt.plot(x,y6,label='X6',marker='*',markersize=10) #Plotting data6
plt.title('Comparison of F1 Scores')
plt.legend()
plt.show()

y11=[0.855,0.860,0.893,0.896]
y22=[0.866,0.874,0.901,0.907]
y33=[0.844,0.856,0.896,0.899]
y44=[0.858,0.864,0.896,0.897]
y55=[0.841,0.851,0.891,0.896]
y66=[0.858,0.864,0.894,0.902]

plt.style.use('seaborn')
line1 = plt.plot(x,y11,label='X1',marker='*',markersize=10) #Plotting data1
line2 = plt.plot(x,y22,label='X2',marker='*',markersize=10) #Plotting data2
line3 = plt.plot(x,y33,label='X3',marker='*',markersize=10) #Plotting data3
line4 = plt.plot(x,y44,label='X4',marker='*',markersize=10) #Plotting data4
line5 = plt.plot(x,y55,label='X5',marker='*',markersize=10) #Plotting data5
line6 = plt.plot(x,y66,label='X6',marker='*',markersize=10) #Plotting data6
plt.title('Comparison of Accuracies')
plt.legend()
plt.show()