from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - dt.strptime(input(), fmt)).total_seconds())))

# datetime as dt
# understanding strptime
# .total_seconds() --> is a module that returns total seconds in a given strptime thing
# fmt -> format --> %a = day %d = date %b =Month %Y =year %H:%M:%S = hour:minute:second   %z = time-zone-diff
# dt.strptime(date,fmt) --> arranges in the format and then . total_seconds()calculates total seconds invlolved
