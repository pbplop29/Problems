x = []
for i in range(4):
    A = str(input())
    B = A.split(' ')
    x.append(B)
    i += 1

t1 = x[0]
t2 = x[1]
t3 = x[2]
t4 = x[3]

day1 = int(t1[1])
day2 = int(t2[1])
day3 = int(t3[1])
day4 = int(t4[1])

day_diff_a = abs(int(day1)-int(day2))
day_diff_b = abs(int(day3)-int(day4))

time1 = t1[4].split(':')
time2 = t2[4].split(":")
sec_diff_a = abs(int(time1[2])-int(time2[2]))
min_diff_a = abs(int(time1[1])-int(time2[1]))
hrs_diff_a = abs(int(time1[0])-int(time2[0]))
time_difference_a = hrs_diff_a*60*60 + min_diff_a*60 + sec_diff_a

time3 = t3[4].split(":")
time4 = t4[4].split(":")
sec_diff_b = abs(int(time3[2])-int(time4[2]))
min_diff_b = abs(int(time3[1])-int(time4[1]))
hrs_diff_b = abs(int(time3[0])-int(time4[0]))
time_difference_b = hrs_diff_b*60*60 + min_diff_b*60 + sec_diff_b
x1A = t1[5]
x2A = t2[5]
x3A = t3[5]
x4A = t4[5]

xDA = int(x1A) - int(x2A)
xDB = int(x3A) - int(x4A)

xDA_min = int((str(xDA))[-2:])
xDA_hrs = int((str(xDA))[:-2])
xDB_min = int((str(xDB))[-2:])
xDB_hrs = int((str(xDB))[:-2])

xDA_time = abs(xDA_hrs*60*60) + abs(xDA_min*60)
xDB_time = abs(xDB_hrs*60*60) + abs(xDB_min*60)

if '-' in str(xDA_hrs):
    xDA_time_final = int('-'+str(xDA_time))

if '-' in str(xDB_hrs):
    xDB_time_final = int('-'+str(xDB_time))
else:
    xDB_time_final = xDB_time

time_difference_aX = time_difference_a - xDA_time_final
time_difference_bX = time_difference_b - xDB_time_final

time_diff_without_time_change_a = day_diff_a*24*3600 + time_difference_a
time_diff_without_time_change_b = day_diff_b*24*3600 + time_difference_b

time_diff_with_time_change_a = day_diff_a*24*3600 + time_difference_aX
time_diff_with_time_change_b = day_diff_b*24*3600 + time_difference_bX
print(time_diff_with_time_change_a)
print(time_diff_with_time_change_b)


