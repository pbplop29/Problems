n = int(input())
B = map(int, input().split()[:n])
# Maps every input to int value.
print(B)
B_new = sorted(set((list(B))))
# Sorts the array by removing redundancy and putting in order
print(sorted(set((list(B)))))

L = len(B_new)
# Takes the length of sorted B

print(B_new[L-2])
# Prints the second largest element.
