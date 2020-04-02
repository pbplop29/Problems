n = int(input())
# takes in the length of the list you want it to be
B = input().split()[:n]
# froms a list of length n such that elements are to be inputted with a space between them,
# unlike usual for loop for appending, split() with inpurt helps to input members with spaces
# [:n] is the part that limits the number of elements taken
a = b = B[0]
# we put two var both to be the 1st element of the list

for i in range(n):
    if B[i] > a:
        b = a
        a = B[i]
        # This loop helps us to give max value to a and th eprevious value of a to b, which is the min value
    else:
        b = B[i]
        # This loop helps to ignore the value lesser than a and put it to b
print(b)
