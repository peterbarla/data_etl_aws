from zipfile import ZipFile 
import os

# CREATE zipfiles FOLDER IF IT DOESN`T EXIST
if not os.path.exists('./zipfiles'):
    os.makedirs('./zipfiles')

# STORES ALL THE ZIPPED FILES FROM filenames
zipped_files = []

# ZIPS EACH FILE FROM filenames AND SAVES THE ZIPS IN THE zipfiles DIRECTORY AND ADDS THEM TO THE zipped_files LIST
def zipp(filenames: list)-> list:
    for f in filenames:
        with ZipFile(f'zipfiles/{f[:-4]}.zip', 'w') as zip:
            zip.write(f'files/{f}', f)
            zipped_files.append(zip)

    return zipped_files