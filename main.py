import datetime
import pyinputplus as pyip

your_name = pyip.inputStr('What is your name? ')
your_dob = pyip.inputDate('What is your Date of Birth? ', formats=['%d/%m/%Y'])

print(f'Hi {your_name}\n'
      f'You are {datetime.date.today() - your_dob} old!'
      )
