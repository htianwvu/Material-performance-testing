import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
csv_file_path = 'C:/Users/htian/Desktop/book in reading/mass spectra of Fe bentonite.csv'

massspec = pd.read_csv(csv_file_path )

# or XPS = pd.read_csv(CSV_FILE_PATH, skiprows=1)
###### to understand the table very carefully and table information
print(massspec.head(10))
print(massspec)
print(massspec.info(),'n')

######## very carefully read full list of first few lines#####
##### to identify the data your collected######
print(massspec.loc[0])
print(massspec.loc[1])
#print(FTIR.loc[0:1])   ## see the unit corresponding relationship


### Identify key parmeters

sample_name = "60% CuO/bentonite"
ramping_rate = "900 C"
#wavenumber_label_unit = "cm-1"
#Absorbance_Unit = " a.u."
#Weigt_uni = 'mg'

# drop the first few lines , which is the 2 line##
#XPS2 = XPS.drop(index = [0,1,2])
#print(XPS2)
# can also write as this before by using skiprows
#df = pd.read_csv(CSV_FILE_PATH, skiprows=1)


### reindix from beginning###

massspec2 = massspec.reset_index(drop = True)

print(massspec2)

### rename the columns###

#XPS3.columns= [  'Binding Energy (ev)','Intensity (a.u.)']

#print(XPS3)

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

x= massspec2['Time&Date']
y1= massspec2['Ar']
y2= massspec2['CO2']
y3= massspec2['CO'] 
y4= massspec2['He']
y5= massspec2['CH4']
y6= massspec2['N2']
y7= massspec2['O2']
y8= massspec2['H2']
y9= massspec2['H2O%']

#plt.plot(x, y1, color='m', label='Ar')
plt.plot(x, y2, color='green', label='CO2')
#plt.plot(x, y3, color='red', label='CO')
plt.plot(x, y5, color='m', label='CH4')
plt.plot(x, y8*2, color='r', label='H2*2')

plt.title("Mass spec of " + sample_name)

plt.legend(labels= [sample_name], loc='best',fontsize=18)

plt.xlabel('Reaction time (unlabelled)', fontsize=10)
plt.ylabel('Outlet concentration (%)',fontsize=10)

plt.show()

#XPS3.plot(x = 'Binding Energy (ev)', y='Intensity (a.u.)', linestyle = "-",
      #         linewidth=1, alpha=0.8,color = 'r')       


#plt.legend(labels= [sample_name], loc='best',fontsize=8)
#plt.xlabel('Binding Energy (ev)', fontsize=10)
#plt.ylabel('Intensity (a.u.)',fontsize=10)


#plt.xlim((-1,2))
#plt.ylim((3,4))

plt.show()


