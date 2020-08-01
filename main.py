from recycler import empty
from file_generator import generate
from zipper import zipp
from s3_pusher import upload

# DELETING ALL CONTENT OF ./files BEFORE GENERATING THE NEW SET OF FILES
folder = './files'
empty(folder)

# DELETING ALL CONTENT OF ./zipfiles BEFORE ZIPPING THE NEWLY GENERATED FILESET
folder = './zipfiles'
empty(folder)

# STORES ALL THE GENERATED FILES
filenames = []

# GENERATE FILES
filenames = generate(1)

# ZIPP FILES IN filenames AND UPLOAD THEM
zipp(filenames)