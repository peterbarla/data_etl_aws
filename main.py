from recycler import empty
from file_generator import generate
from zipper import zipp

# DELETING ALL CONTENT OF ./files BEFORE GENERATING THE NEW SET OF FILES
folder = './files'
empty(folder)

# DELETING ALL CONTENT OF ./zipfiles BEFORE ZIPPING THE NEWLY GENERATED FILESET
folder = './zipfiles'
empty(folder)

# STORES ALL THE GENERATED FILES
filenames = []

# GENERATE FILES
filenames = generate(10)

# STORES ALL ZIPPED GENERATED FILES
zipfiles = []

# ZIPP FILES IN filenames
zipfiles = zipp(filenames)