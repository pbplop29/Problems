n = int(input())
if (n % 2 == 1 and n >= 1):
    print("Weird")
elif (n % 2 == 0 and 2 <= n <= 5):
    print("Not Weird")
elif (n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
elif (n % 2 == 0 and 6 <= n <= 100):
    print("Not Weird")
else:
    pass

# Easy probelm to print for different if cases
