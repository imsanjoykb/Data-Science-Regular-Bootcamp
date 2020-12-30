#!/usr/bin/env python
# coding: utf-8

### Import Libraries
import pandas as pd
import sqlalchemy
import psycopg2
from elasticsearch import Elasticsearch
import csv
import json

### Connect to PostgreSQL Server
engine = sqlalchemy.create_engine('postgresql://postgres:uBlIJRA1hsc1@localhost:5432/jarvis')
df = pd.read_sql_table('aggregated',engine)


global c
c=0
def func(x):
    global c
    c= c+1
    return c

df['ID'] = df['id'].apply(func)
df2 = df.to_dict('records')


### Save as CSV File
df.to_csv('aggregated.csv',  index=False) 

### Data insert to Elasticsearch

def csv_reader(file_obj, delimiter=','):
    reader = csv.DictReader(file_obj)
    i = 1
    results = []
    for row in reader:
        print(row)
        es.index(index='jarvis', doc_type='test', id=i,body=json.dumps(row))
        i = i + 1

        results.append(row)
        print(row)




### Connect to Elasticsearch Server
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es)

### Bulk Data Generator
if __name__ == "__main__":
    with open("aggregated.csv") as f_obj:
        csv_reader(f_obj)







