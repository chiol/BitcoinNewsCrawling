import csv
from datetime import date,timedelta
import pysentiment as ps
import json

f = open("bitcoinnews.csv",'r',encoding='utf-8')
wf = open("count.csv",'w',encoding='utf-8',newline='')

rd_f = csv.reader(f)
wd_f = csv.writer(wf)

original_data = {}

d = date.today() - timedelta(days=732)
td = timedelta(days=1)

hiv4 = ps.HIV4()

for line in rd_f:
    if line == []:
        continue
    date = line[0]
    title = line[1]

    tokens = hiv4.tokenize(title)
    score = hiv4.get_score(tokens)

    if date in original_data:
        original_data[date]["count"] += 1
        original_data[date]["pos"] += score['Positive']
        original_data[date]["neg"] += score['Negative']
    else:
        original_data[date] = {}
        original_data[date]["count"] = 1
        original_data[date]["pos"] = score['Positive']
        original_data[date]["neg"] = score['Negative']

wd_f.writerow(['date','count', 'pos', 'neg'])

for i in range(733):
    dd = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
    if dd in original_data:
        wd_f.writerow([dd, original_data[dd]["count"],original_data[dd]["pos"],original_data[dd]["neg"]])
    else:
        wd_f.writerow([dd,0,0,0])
    d = d + td