x = int(input())
y = int(input())
z = int(input())
n = int(input())

L = [[i, j, k]
     for i in range(x+1)
     for j in range(y+1)
     for k in range(z+1) if (i+j+k) != n]
print(L)

# List comprehension
# Making coordiantes' list such that the sum of coordinates is not requal to a particular number.
# range(x) means range from 0 to x exculsive of x
# Hence we used a range upto (x+1)
