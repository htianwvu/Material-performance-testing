import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
csv_file_path = 'C:/Users/htian/Desktop/book in reading/WVU Share facility data/PXRD data2.csv'

PXRD = pd.read_csv(csv_file_path, na_values = ['missing'], sep = ',', skiprows = 26)

# or XPS = pd.read_csv(CSV_FILE_PATH, skiprows=1)
###### to understand the table very carefully and table information
print(PXRD.head(10))
print(PXRD)
print(PXRD.info(),'n')

#########################################
##########process data##########

# dropna all unnecessary data in columns######
##Raman2 = Raman.dropna(axis =1)
##print(Raman2)
sample_name = 'standard high-entropy alloy'
plt.figure(figsize=(20,8),dpi=400)

################################
##########Change the name of first line #########
PXRD.columns= ['2 Delta','Relative Intensity (a.u)']

# check the first and last five lines###
print(PXRD)

## Plot the Spectra and add all labels###

PXRD.plot(kind = "line", x = '2 Delta', y='Relative Intensity (a.u)',
                 linewidth=1, alpha=0.8,color = 'b')

plt.title("Power X-Ray Diffraction of " + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('2 Delta', fontsize=10)
plt.ylabel('Relative Intensity (a.u.)',fontsize=10)


plt.show()
