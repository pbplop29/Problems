n = int(input())
# basically taken input for how many times we want to put in commands
group = []
# declared an epmty list
for i in range(n):
    # run through a for loop for n number of times
    take = input().split()
    # taken input in a single line, no mapping done,
    # just a lis was formed like
    # ['command'.'placeholder_command1','placeholder_command2'] and so on
    command = take[0]
    # command was input at first
    placeholder_command = take[1:]
    # everything except the first was arguement
    if command != "print":
        # when command was print, it was printed but when it wasnt, the following was done
        command += "(" + ",".join(placeholder_command) + ")"
        # An example will show this
        # ['insert', '0','5']
        #command = insert
        #placeholder_command = ['0','5']
        # ','.join(placeholder command) = 0,5
        # "("+ ",".join(placeholder_command) +")" =(0,5)
        # command += "("+ ",".join(placeholder_command) +")" = insert(0.5)
        eval("group." + command)
        # group.insert(0,5)
        # --> Note everything up above were strings hence, eval was used to convert the strings to an expression and then process it.
    else:
        print(group)
