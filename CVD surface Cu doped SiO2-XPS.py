import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
csv_file_path = 'C:/Users/htian/Desktop/book in reading/WVU Share facility data/Copy of XPS processed data21.csv'

XPS = pd.read_csv(csv_file_path, na_values = ['missing'])

# or XPS = pd.read_csv(CSV_FILE_PATH, skiprows=1)
###### to understand the table very carefully and table information
print(XPS.head(10))
print(XPS)
print(XPS.info(),'n')

######## very carefully read full list of first few lines#####
##### to identify the data your collected######
#print(FTIR.loc[0])
#print(FTIR.loc[1])
#print(FTIR.loc[0:1])   ## see the unit corresponding relationship


### Identify key parmeters

sample_name = "Surface Cu-doped SiO2"
ramping_rate = "RT"
#wavenumber_label_unit = "cm-1"
#Absorbance_Unit = " a.u."
#Weigt_uni = 'mg'

# drop the first few lines , which is the 2 line##
XPS2 = XPS.drop(index = [0,1,2])
print(XPS2)
# can also write as this before by using skiprows
#df = pd.read_csv(CSV_FILE_PATH, skiprows=1)


### reindix from beginning###

XPS3 = XPS2.reset_index(drop = True)

print(XPS3)

### rename the columns###

XPS3.columns= ['Binding Energy (ev)','Intensity (a.u.)']

print(XPS3)

### change from "object" to "float" type, this is critical

#FTIR3[['Wavenumbers','Absorbance']] = FTIR3[['Wavenumbers','Absorbance']].astype(float)

###

###### Plot the Spectra and add all labels###

#x= FTIR3['Wavenumbers']
#y= FTIR3['Absorbance']

#print(y)
####y2 = TGA_CLC3['Temperature']

##ax1.plot(x,y1,'b-')

#FTIR3.plot(x,y, color = 'b')

plt.figure(figsize=(20,8),dpi=400)
XPS3.plot(x = 'Binding Energy (ev)', y='Intensity (a.u.)', linestyle = "-",
               linewidth=1, alpha=0.8,color = 'r')       

plt.title("XPS of " + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('Binding Energy (ev)', fontsize=10)
plt.ylabel('Intensity (a.u.)',fontsize=10)


#plt.xlim((-1,2))
#plt.ylim((3,4))

plt.show()


