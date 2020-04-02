s = input()
ss= input()
s_new = ''.join(s.split(ss))
x = int((len(s)-len(s_new))/len(ss))
print(x)

#this function returns how many times the ss string appeared in s string