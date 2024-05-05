grade = int(input("Enter your grade: "))

if grade >= 91:
    print('You recieved', str(grade)+'%'+',', 'which is an Outstanding')
elif grade < 91 and grade >= 82:
    print('You recieved', str(grade)+'%'+',', ' which is an Excellent')
elif grade < 82 and grade >= 73:
    print('You recieved', str(grade)+'%'+',', ' which is a Very Good')
elif grade < 73 and grade >= 64:
    print('You recieved', str(grade)+'%'+',', ' which is a Good')
elif grade < 64 and grade >= 55:
    print('You recieved', str(grade)+'%'+',', ' which is a Competent')
elif grade < 55 and grade >= 46:
    print('You recieved', str(grade)+'%'+',', ' which is a Satisfactory')
elif grade < 46 and grade >= 35:
    print('You recieved', str(grade)+'%'+',', ' which is a Below Standard')
else:
    print('You recieved', str(grade)+'%'+',', ' which is a Not Demonstrated')