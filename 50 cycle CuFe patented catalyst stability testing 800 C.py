import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
TGA_CLC = pd.read_csv(r'C:/Users/htian/Desktop/book in reading/50 cycle.csv')

###### to read full table information
print(TGA_CLC)
print(TGA_CLC.info(),'n')

########  read full list of first few lines#####
##### to identify the data your collected######
print(TGA_CLC.loc[0])
print(TGA_CLC.loc[1])
#print(TGA_CLC.loc[0:1])   ## see the unit corresponding relationship

### Identify key parmeters

sample_name = "patented Cu Fe oxygen carrier"
ramping_rate = "Ramp 10 °C/min to 800.00 °C"
Time_unit = "mins"
Temperature_Unit = "C"
Weight_unit = "mg"

# drop the unit line , which is the secon line##
#TGA_CLC2 = TGA_CLC.drop([0,1])
#print(TGA_CLC2)

### reindix from beginning###

#TGA_CLC3 = TGA_CLC2.reset_index(drop = True)

#print(TGA_CLC3)

### rename the columns###

TGA_CLC.columns= ['Time','Temperature','Weight']

print(TGA_CLC)

plt.figure(figsize=(20,8),dpi=400)
#### assign x, y1 and y2 axis#####
x= TGA_CLC['Time']
y1 = TGA_CLC['Temperature']
y2 = TGA_CLC['Weight']

#print(x)

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()           # twinx for mirror
ax1.plot(x,y1,'r-')
ax2.plot(x,y2,'b', linewidth=0.5)
 
ax1.set_xlabel('Time (min)')    #x-label
ax1.set_ylabel('Temperature C', color = 'b')   #y1-label
ax2.set_ylabel('Weight %',color = 'r')   #y2 label
plt.title(" 50-cycle CLC stability performance of " + sample_name)

plt.legend(labels= [ramping_rate], loc='upper center',fontsize=8)

plt.show()
