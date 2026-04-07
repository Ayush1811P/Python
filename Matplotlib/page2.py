# import matplotlib.pyplot as plt

# x=["Monday","Tuesday","Wednesday","Thursday","Friday"]
# y=[10,15,7,25,12]
# plt.plot(x,y)#plotting axis
# plt.title("BAKERY SALES THIS WEEK")
# plt.xlabel("Days of the week")
# plt.ylabel("Sales per day")

# plt.show()



import matplotlib.pyplot as plt
#SYNTAX FOR PYPLOT
#plt.plot(x,y color="color_name", linestyle="line-style",linewidth=1,marker="market-type",label='label_name')

months=[1,2,3,4]
sales=[1000,1500,1200,1800]

plt.plot(months,sales, color="blue",linestyle='--',linewidth=2,marker='o',label='Sales_data')
plt.xlabel("Months")
plt.ylabel("Sales/months")
plt.title("MONTLY SALES DATA REPORT")
plt.legend(loc='lower right')#upper left
plt.grid(color='red',linestyle=':',linewidth=1)
#plt.grid()#makes background verticle and horizontal lines
plt.xlim(1,4)#about our x axis range 1-4
plt.ylim(0,1800)#about our y axis range 0-1800
plt.xticks([1,2,3,4],["M1",'M2','M3','M4'])

plt.show()