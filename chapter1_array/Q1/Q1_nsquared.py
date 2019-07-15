def unique_char(str_input):
    if not str_input:
        raise Exception('str_input cannot be of NoneType')
    #duplicate = False

    for x in str_input:
        duplicate = False

        for y in str_input:
            if x == y:
                if duplicate:
                    return False
                #print('y is ', y, 'x is ', x)
                duplicate = True

    return True





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
