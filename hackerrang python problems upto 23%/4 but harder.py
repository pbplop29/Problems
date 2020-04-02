n = int(input())
# taken the input for no of elements to be in the list
X = []
# Created an empty list for both the name and marks of students
Y = []
# Created an empty list for only thr marks of the students
for i in range(n):
    # declared a for loop that goes thorugh all its elements
    # This for loop is for taking the input and fillin in out X and Y
    name = str(input())
    # taken name as string
    marks = float(input())
    # Taken marks as floats
    student = (name, marks)
    # taken both name and marks to append to X
    student_marks = marks
    # Taken only marks to append to Y
    X.append(student)
    Y.append(student_marks)
    # Appended both of them
    i = i+1
    # Continued the for loop

   # code for finding second lowest mark begins
New_Y = sorted(set(list(Y)))
length = len(New_Y)
second_lowest = New_Y[1]
# code for finding second lowest ends
New_X = []
# An empty set called New_x that will contain only the names whose value corresponds to second lowest is created
for (j, p) in X:
    # (j,p) j is the name and p is the marks
    if p == second_lowest:
        #p is compared
        New_X.append(j)
        #j is appended
    else:
        pass
    i = i+1
    # for loop continued

for words in sorted(New_X):
    # gone through the New_X set to print them individually
    # used sorted to get them in alphabetic order
    print(words)
