n = int(input())
# taken input of the range of dictionary we want
marks_library = {

}
# declared and emoty dictionary
for i in range(n):
    # run for loop for range n ; the value we took in beginning
    name = str(input())
    # taken name
    math = float(input())
    phy = float(input())
    chem = float(input())
    # taken marks
    marks = (math, phy, chem)
    # listed the marks
    marks_library.__setitem__(name, marks)
    # appended the marks and name to the dictionary such that name was the ky and marks was the keyvvalue
    # Or we can just have
    # marks.library[name]=marks
    i = i+1
    # continued the for loop
print(marks_library)
# the dictionary was printed to check if it was succesfully formed or not
# This was not required
name_taken = str(input())
# input of the name was taken for which the average marks was to be displayed
marks_only = marks_library[name_taken]
# a new set was formed for the marks of the selected names
print(marks_only)
# the set of marks_only was printed just to ensure if it was taken correctly
#not needed
summation = 0
# summation value was put to zero before starting a loop
for i in marks_only:
    # This for loop ran through the members of marks_only serially
    summation += i
    # sum was added
    i += 1
    # loop was continued till the last element
    avg = (summation/3)
    # average was calculated
print(round(avg, 2))
# Average for the inputted name was calcualted after accessing the marks from the dictionary
