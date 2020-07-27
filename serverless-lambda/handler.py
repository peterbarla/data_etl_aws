import json
from datetime import time, datetime

def handler(event, context):

    # GET THE UPLAODED FILES NAME
    uploaded_filename = event['Records'][0]['s3']['object']['key']

    # GET THE UPLOADED FILES CATEGORY TYPE
    file_category = uploaded_filename.split('_')[0][:-1]

    # GET THE FILES LWM
    lwm = uploaded_filename.split('_')[1][:8]

    # GET THE FILES HWM
    hwm = uploaded_filename.split('_')[2][:8]

    # ARRIVAL TIME
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(uploaded_filename, file_category, lwm, hwm, timestamp)

    
