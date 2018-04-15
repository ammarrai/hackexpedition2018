# get haversine distances from rachel's illegal data 
import pandas as pd
illegal = pd.read_csv('rachelillegal.csv')
ssc = pd.read_csv('VA_scc_locations.csv')
dba = pd.read_csv('4_1_filtered_rach.csv')

# illegal : lat , lon 
# ssc : displayLatitude , displayLongitude
# dba : organization.primaryAddress.latitude , organization.primaryAddress.longitude
from haversine import haversine
for i in range(1,len(illegal)):
    for j in range(1,len(ssc)):
		try:
		    val1 = (illegal['lat'][i], illegal['lon'][i])
		    val2 = (float(ssc['displayLatitude'][j]) , float(ssc['displayLongitude'][j]))
		    print((haversine(val1,val2)))
		except ValueError,e:
				print(e)