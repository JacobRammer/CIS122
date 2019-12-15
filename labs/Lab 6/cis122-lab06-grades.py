grades = input("Enter score: ")

# Initialize variables
count = 0
average = 0
low_score = grades
high_score = grades
total_score = 0
input_grades = True

while input_grades:
    count += 1
    total_score = total_score + int(grades)
    grades = input("Enter score: ")
    average = total_score / count
    if len(grades) == 0:
        input_grades = False
        break
    elif int(grades) <= int(low_score):
        low_score = grades
    elif int(grades) > int(high_score):
        high_score = grades

print("*** Results *** ", "\nCount:\t\t", count, "\nAverage:\t", average, "\nLow Score:\t"
      , low_score, "\nHigh Score:\t", high_score)
