from datetime import date, timedelta, datetime
import os
import random

# POSSIBLE CATEGORY TYPES
category_types = ['sum', 'hist', 'prob', 'glow']

# GET CURRENT DATE IN %D/%M/%Y format
todays_date = datetime.now()
formatted_today = todays_date.strftime('%d%m%Y%H:%M:%S')

# GET TOMORROW`S DATE IN %D/%M/%Y format
tomorrows_date = date.today() + timedelta(days=1)
formatted_tomorrow = tomorrows_date.strftime('%d%m%Y')


# CREATE 10 FILES WITH A RANDOM CATEGORY AND A STARTING AND ENDING AVAILABILITY BOUND LIKE CATEGORY_LWM_HMW IN A FOLDER
if not os.path.exists('./files'):
    os.makedirs('./files')

filenames = []

# GENERATE COUNT NUMBER OF FILES
def generate(count: int)-> list:
    for count in range(count):
        # PICK A RANDOMLY SELECTED CATEGORY TYPE WITH A RANDOMLY GENERATED INDEX
        random_category_index = random.randint(0, 3)
        random_category = category_types[random_category_index]
        open(f'files/{random_category}{count}_{formatted_today}_{formatted_tomorrow}.txt', 'w+')
        filenames.append(f'{random_category}{count}_{formatted_today}_{formatted_tomorrow}.txt')
    return filenames
