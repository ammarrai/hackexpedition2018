import requests
import pandas as pd 
import sys
import string
reload(sys)
sys.setdefaultencoding('utf-8')


data = (pd.read_table('this.txt'))
data1 = data.to_string(index=False)
data1=data1.replace(' ','')


data1.encode("ascii", errors="ignore").decode()

# data1 = str(data1)
# printable = set(data1.printable)
# data1 = filter(lambda x: x in printable, s)


#data1 = data1.decode('ascii', 'ignore')

# from unidecode import unidecode
# def remove_non_ascii(text):
#     return unidecode(unicode(text, encoding = "utf-8"))

# data1 = remove_non_ascii(data1)


url='https://batch.geocoder.cit.api.here.com/6.2/jobs?action=run&mailto=rao.saurabh94@gmail.com&gen=8&header=true&indelim=%7C&outdelim=%7C&outcols=displayLatitude,displayLongitude,locationLabel,houseNumber,street,district,city,postalCode,county,state,country&outputCombined=false&app_code=ttXKgG3O7n54xM7mMpZb5w&app_id=kjBkmWknDVu0lS1jzF5f'
headers = {'Content-Type':'text/plain'}

r = requests.post(url,data=data1,headers=headers)
print(r.content)

