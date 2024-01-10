from PyQt5.QtCore import QDateTime
from datetime import datetime

# Assume dt is a QDateTime object
qdt = QDateTime.currentDateTime()

# Convert QDateTime to Python's datetime
pydt = qdt.toPyDateTime()
pydt = pydt.replace(second=0,microsecond=0)
print(type(pydt))  # <class 'datetime.datetime'>
print(pydt)        # Current date and time in Python's datetime format
