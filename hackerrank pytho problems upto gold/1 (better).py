
n = int(input())
marks_library = {

}
for i in range(n):
    name, *line = input().split()
    # *line is taken here which can be mapped later on,
    # i dont know the use yet but i guess it takes all the inputs after the first input to be a member of the list callled line.
    marks = list(map(float, line))
    # basically maps everythin except the first input to be a float
    marks_library[name] = marks
    # this is same as .__setitem__
name_taken = input()
# name is taken as input
marks_only = marks_library[name_taken]
# set of only marks is formed
summation = 0
# sum is put 0
for i in marks_only:
    summation += i
    i += 1
    avg = (summation / 3)
    #average is found
print("{:.2f}".format(avg))
# "{:<no.>f}" --> this makes the number into a float with <no.> numbers of decimal places.
