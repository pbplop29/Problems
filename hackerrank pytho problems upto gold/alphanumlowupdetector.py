l = input()
alphanum=False
alpha = False
num = False
lower = False
upper = False


for a in l:
    if a.isalnum():
        alphanum = True
    if a.isalpha():
        alpha = True
    if a.isdigit():
        num = True
    if a.isupper():
        upper = True
    if a.islower():
        lower = True
print(alphanum)
print(alpha)
print(num)
print(lower)
print(upper)




