import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
data_file_path = 'C:/Users/htian/Desktop/book in reading/WVU Share facility data/Bruker XRD data2.txt'

## read using ";" as seperator, and delete ","

Bruker_XRD = pd.read_table(data_file_path, sep = ',', na_values = ['missing'],encoding='utf-8')


# or XPS = pd.read_csv(CSV_FILE_PATH, skiprows=1)
###### to understand the table very carefully and table information
print(Bruker_XRD.head(10))
print(Bruker_XRD)
print(Bruker_XRD.info(),'n')

######## very carefully read full list of first few lines#####
##### to identify the data your collected######
#print(FTIR.loc[0])
#print(FTIR.loc[1])
#print(FTIR.loc[0:1])   ## see the unit corresponding relationship


### Identify key parmeters

sample_name = "Cu MOF"
ramping_rate = "RT"
#wavenumber_label_unit = "cm-1"
#Absorbance_Unit = " a.u."
#Weigt_uni = 'mg'

# drop the first few lines , which is the 2 line##
Bruker_XRD2= Bruker_XRD.drop(index = [0,1])
print(Bruker_XRD2)
# can also write as this before by using skiprows
#df = pd.read_csv(CSV_FILE_PATH, skiprows=1)


### reindix from beginning###

Bruker_XRD3 = Bruker_XRD2.reset_index(drop = True)

print(Bruker_XRD3)

### rename the columns###

Bruker_XRD3.columns= ['Angle','Intensity (a.u.)','nan']

print(Bruker_XRD3)

### change from "object" to "float" type, this is critical

Bruker_XRD3[['Angle','Intensity (a.u.)']] = Bruker_XRD3[['Angle','Intensity (a.u.)']].astype(float)

###

###### Plot the Spectra and add all labels###

#x= FTIR3['Wavenumbers']
#y= FTIR3['Absorbance']

#print(y)
####y2 = TGA_CLC3['Temperature']

##ax1.plot(x,y1,'b-')

#FTIR3.plot(x,y, color = 'b')

plt.figure(figsize=(20,8),dpi=400)
Bruker_XRD3.plot(x = 'Angle', y='Intensity (a.u.)', linestyle = "-",
               linewidth=1, alpha=0.8,color = 'r')       

plt.title("Bruker SAXS of " + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('Angle', fontsize=10)
plt.ylabel('Intensity (a.u.)',fontsize=10)


#plt.xlim((-1,2))
#plt.ylim((3,4))

plt.show()


