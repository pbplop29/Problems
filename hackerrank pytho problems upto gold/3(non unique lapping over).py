def count_substring(s, ss):
    n=0
    #gave n=0 so we can add onto it later
    for i in range(0,len(s)):
        #declared a fucniton from 0 yo yhe length of the main string
        if s[i:i+len(ss)] == ss:
            #if the portion of main string from i to length of ss was equal to ss.
            s = s[:i:]+s[i+1::]
            #that portion was removed
            n += 1
            #and 1 was added to n and the code was rerun
    return(n)




#calling the function
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)