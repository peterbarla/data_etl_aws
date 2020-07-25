import zipfile
import os
from s3_pusher import upload

# CREATE zipfiles FOLDER IF IT DOESN`T EXIST
if not os.path.exists('./zipfiles'):
    os.makedirs('./zipfiles')

# STORES ALL THE ZIPPED FILES FROM filenames
zipped_files = []

# ZIPS EACH FILE FROM filenames AND SAVES THE ZIPS IN THE zipfiles DIRECTORY AND ADDS THEM TO THE zipped_files LIST
def zipp(filenames: list)-> list:
    for f in filenames:
        with zipfile.ZipFile(f'zipfiles/{f[:-4]}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
            zip.write(f'files/{f}', f)
            # UPLOAD ZIPPED FILE TO S3
            print(zip)
            upload(f'zipfiles/{f[:-4]}.zip')
