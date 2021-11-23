import requests as req
import bs4 as bs
import re 

url = 'https://janelwashere.com/files/bible_daily.txt'
file = req.get(url)

my_dict = {}
total_file = file.text
total_file = re.sub('[^A-Za-z0-9]+ ', ' ', total_file)
print(total_file[0:5000])
# for i in file.text.split(' '):
#     print(i)


for i in total_file.split(' '):
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1

# for key, value in my_dict.items():
#     #print(key, value)


# value = my_dict['Chapter']
# print(value)