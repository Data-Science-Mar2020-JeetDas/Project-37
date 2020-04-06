# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/Project-37.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 36 : Ill-defined causes in cause-of-death registration (%)");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")



# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")



#******************* Question - : 0-3 :  ********************


df1 = df[df.Period == "1990-1994"]
print("\n\n--------------[ OUTPUT for 1990-1994 ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "1995-1999"]
print("\n\n--------------[ OUTPUT for 1995-1999 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2000-2004"]
print("\n\n--------------[ OUTPUT for 2000-2004 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == "2005"]
print("\n\n--------------[ OUTPUT for 2005 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot for slot-1 ----------------------

plt.title('Question - : slot-1')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 1990-1994")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 1995-1999")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2000-2004")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2005")


plt.legend()
plt.show()


#******************* Question - : 4-7 :  ********************


df1 = df[df.Period == "2006"]
print("\n\n--------------[ OUTPUT for 2006  ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "2006-2007"]
print("\n\n--------------[ OUTPUT for 2006-2007 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2006-2008"]
print("\n\n--------------[ OUTPUT for 2006-2008 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == "2007"]
print("\n\n--------------[ OUTPUT for 2007 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot for slot-2 ----------------------

plt.title('Question - : slot-2')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2006 ")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2006-2007")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2006-2008")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2007")


plt.legend()
plt.show()

#******************* Question - : 8-11 :  ********************


df1 = df[df.Period == "2007-2008"]
print("\n\n--------------[ OUTPUT for 2007-2008  ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "2007-2009"]
print("\n\n--------------[ OUTPUT for 2007-2009 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2008"]
print("\n\n--------------[ OUTPUT for 2008 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == "2008-2009"]
print("\n\n--------------[ OUTPUT for 2008-2009 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot for slot-3 ----------------------

plt.title('Question - : slot-3')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2007-2008 ")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2007-2009")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2008")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2008-2009")


plt.legend()
plt.show()

#******************* Question - : 12-15 :  ********************


df1 = df[df.Period == "2008-2010"]
print("\n\n--------------[ OUTPUT for 2008-2010  ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "2009"]
print("\n\n--------------[ OUTPUT for 2009 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2009-2010"]
print("\n\n--------------[ OUTPUT for 2009-2010 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == "2009-2011"]
print("\n\n--------------[ OUTPUT for 2009-2011 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot for slot-12-15 ----------------------

plt.title('Question - : slot-4')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2008-2010 ")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2009")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2009-2010")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2009-2011")


plt.legend()
plt.show()


#******************* Question - : 16-19 :  ********************


df1 = df[df.Period == "2010"]
print("\n\n--------------[ OUTPUT for 2010  ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "2010-2011"]
print("\n\n--------------[ OUTPUT for 2010-2011 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2010-2012"]
print("\n\n--------------[ OUTPUT for 2010-2012 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == "2011"]
print("\n\n--------------[ OUTPUT for 2011 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot for slot-16-19 ----------------------

plt.title('Question - : slot-5')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2010 ")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2010-2011")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2010-2012")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2011")


plt.legend()
plt.show()


#******************* Question - : 16-19 :  ********************


df1 = df[df.Period == "2011-2012"]
print("\n\n--------------[ OUTPUT for 2011-2012  ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == "2011-2013"]
print("\n\n--------------[ OUTPUT for 2011-2013 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == "2012"]
print("\n\n--------------[ OUTPUT for 2012 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])


i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)


#--------------- plot for slot-20-22 ----------------------

plt.title('Question - : slot-6')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2011-2012 ")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2011-2013")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2012")

plt.legend()
plt.show()
