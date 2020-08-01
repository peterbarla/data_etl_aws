import os
import psycopg2
import sys
import boto3
import datetime

'''REDSHIFT_DATABASE = 'peterdb'
REDSHIFT_USER = 'peter.barla'
REDSHIFT_PASSWD = 'Pepecsek1'
REDSHIFT_PORT = '5439'
REDSHIFT_ENDPOINT = 'redshift-peter-1.cncdopxmun4t.us-east-2.redshift.amazonaws.com'''

RS_PORT = 5439
RS_USER = 'peter.barla'
DATABASE = 'peterdb'
CLUSTER_ID = 'redshift-peter-1'
RS_HOST = 'redshift-peter-1.cncdopxmun4t.us-east-2.redshift.amazonaws.com'
client = boto3.client('redshift')
cluster_creds = client.get_cluster_credentials(DbUser=RS_USER,
                                           DbName=DATABASE,
                                      ClusterIdentifier=CLUSTER_ID,
                                           AutoCreate=False)
def build_and_send_query(category: str, filename: str, lwm: str, hwm: str, timestamp: str)-> str:

    # CREATING INSERT QUERY
    #REDSHIFT_QUERY = f"INSERT INTO peter_schema.staging_uploaded_files(category, filename, lwm, hwm, timestamp) VALUES({category}, {filename}, {lwm}, {hwm}, {timestamp})"


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
    #print(type(REDSHIFT_QUERY))
    # EXECUTING THE QUERY
    try:
        cursor = conn.cursor()
        print(cursor.execute('INSERT INTO peter_schema.staging_uploaded_files (category, filename, lwm, hwm, timestamp) VALUES (%s, %s, %s, %s, %s)', 
            (category, filename, datetime.datetime.strptime(lwm, '%d%m%Y'), 
            datetime.datetime.strptime(hwm, '%d%m%Y'), datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S') )))
        #print(cursor.execute(REDSHIFT_QUERY))
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as ERROR:
        print(ERROR)
        sys.exit(1)

    print('DONE!')