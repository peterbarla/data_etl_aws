import os
import psycopg2
import sys
import boto3
import datetime

# OPEN FILE WITH CREDENTIALS
lines = []
with open('credentials.txt', 'rt') as f:  
    lines = f.readlines()

RS_PORT = 5439
RS_USER = lines[0].strip()
DATABASE = lines[1].strip()
CLUSTER_ID = lines[2].strip()
RS_HOST = lines[3].strip()

client = boto3.client('redshift')
cluster_creds = client.get_cluster_credentials(DbUser=RS_USER,
                                           DbName=DATABASE,
                                      ClusterIdentifier=CLUSTER_ID,
                                           AutoCreate=False)
def build_and_send_query(category: str, filename: str, lwm: str, hwm: str, timestamp: str)-> str:

    # CREATING A CONENCTION TO THE REDSHIFT CLUSTER
    try:
        conn = psycopg2.connect(
        host=RS_HOST,
        port=RS_PORT,
        user=cluster_creds['DbUser'],
        password=cluster_creds['DbPassword'],
        database=DATABASE)
    except Exception as ERROR:
        print(ERROR)
        sys.exit(1)
    print('AFTER CONENCTION')
    # EXECUTING THE QUERY
    try:
        cursor = conn.cursor()
        print(cursor.execute('INSERT INTO peter_schema.staging_uploaded_files (category, filename, lwm, hwm, timestamp) VALUES (%s, %s, %s, %s, %s)', 
            (category, filename, datetime.datetime.strptime(lwm, '%d%m%Y'), 
            datetime.datetime.strptime(hwm, '%d%m%Y'), datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S') )))
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as ERROR:
        print(ERROR)
        sys.exit(1)

    print('DONE!')