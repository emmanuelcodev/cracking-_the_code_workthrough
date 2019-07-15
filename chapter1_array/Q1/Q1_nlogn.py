def unique_char(str_input):
    if not str_input:
        raise Exception('str_input cannot be of NoneType')
        #duplicate = False

    str_input = sorted(str_input)#sort in nlogn time

    previous = str_input[0]

    for x in range(len(str_input)-1):#if duplicates, then prev element and current element will be equal if sorted
        if previous == str_input[x+1]:
            return False

        previous = str_input[x+1]

    return True#since list is exhuasted





s1 = "hello"
s2 = "helo"
s3 = "numem"
s5 = []
s4 = None


print(unique_char(s1))
print(unique_char(s2))
print(unique_char(s3))
print(unique_char(s4))
print(unique_char(s5))
