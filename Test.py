import random
from datetime import datetime, timedelta

birth_date = datetime(1900, 1, 1) + timedelta(days=random.randint(0, 44197))

print(birth_date[])