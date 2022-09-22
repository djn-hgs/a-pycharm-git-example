import datetime as dt
import pyinputplus as pyip

your_name = pyip.inputStr('What is your name? ')
your_dob = pyip.inputDate('What is your Date of Birth? ', formats=['%d/%m/%Y'])

print(f'Hello {your_name}\n'
      f'You are {dt.date.today() - your_dob} old!'
      )
