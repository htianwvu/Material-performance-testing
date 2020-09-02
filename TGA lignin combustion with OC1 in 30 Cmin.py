import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
TGA_CLC = pd.read_excel(r'C:/Users/htian/Desktop/book in reading/Biomass combustion-TGA/2) Biomass + OC in N2/Biomass(2).xls',
                        sheet_name = 'a Table 1 - Isothermal 15.0 min')

###### to read full table information
print(TGA_CLC)
print(TGA_CLC.info(),'n')

########  read full list of first few lines#####
##### to identify the data your collected######
print(TGA_CLC.loc[0])
print(TGA_CLC.loc[1])
#print(TGA_CLC.loc[0:1])   ## see the unit corresponding relationship

### Identify key parmeters

sample_name = "Lignin + OC in N2"
ramping_rate = "Ramp 10 °C/min to 900.00 °C"
Time_unit = "mins"
Temperature_Unit = "C"
Weight_unit = "mg"

# drop the unit line , which is the secon line##
TGA_CLC2 = TGA_CLC.drop([0,1])
print(TGA_CLC2)

### reindix from beginning###

TGA_CLC3 = TGA_CLC2.reset_index(drop = True)

print(TGA_CLC3)

### rename the columns###

TGA_CLC3.columns= ['Time','Weight %', 'Weight mg', 'Heat Flow (Normalized)',
                   'Heat Flow mW','Temperature']

print(TGA_CLC3)

#### assign x, y1 and y2 axis#####
x= TGA_CLC3['Time']
y1 = TGA_CLC3['Weight %']
y2 = TGA_CLC3['Temperature']

#print(x)

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()           # twinx for mirror
ax1.plot(x,y1,'b-')
ax2.plot(x,y2,'r--')
 
ax1.set_xlabel('Time (min)')    #x-label
ax1.set_ylabel('Weight %',color = 'b')   #y1-label
ax2.set_ylabel('Temperature C',color = 'r')   #y2 label
plt.title("CLC performance of " + sample_name + ' in TGA')

plt.legend(labels= [ramping_rate], loc='upper right',fontsize=8)

plt.show()
