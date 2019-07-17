def count_instances(str_input):
    if not str_input:
        raise Exception('str_input cannot be of NoneType')

    tracker = {}

    for x in str_input:
        if x in tracker:
            tracker[x]+=1
        else:
            tracker[x]=1
    return tracker

def an_edit_away(str1, str2):
    if None in (str1, str2):
        raise Exception('st1 and str2 cannot be of NoneType')

    #get rid of strings that are more than 1 edit away, meaning they the size can eiher be the same size, or 1 apart
    str1_size = len(str1)
    str2_size = len(str2)

    if abs(str1_size - str2_size)>1:
        return False

    #track of unique letters and count_instances
    letters1 = count_instances(str1)
    letters2 = count_instances(str2)

    #get longest str, use str1 if equal len or if str1 is larger
    longest = letters1
    shortest = letters2

    if str2_size>str1_size:
        longest = letters2
        shortest = letters1

    #differences tracker
    differences = 0

    #compare dictionary instances
    for x in longest.keys():
        if x in shortest:#if both dic have the letter
            differences+=abs(longest[x]-shortest[x])
        else:
            differences+=abs(longest[x])
        if differences > 1:
            return False
    return True


s1a = 'hello'
s1b = 'hello'

s2a = 'hello'
s2b = 'helo'

s3a = 'hello'
s3b = 'heo'

s4a = 'wut'
s4b = 'what'

s5a = 'wzdt'
s5b = 'abcd'

s6a = 'hello'
s6b = 'hellx'


print(an_edit_away(s1a, s1b))
print(an_edit_away(s2a, s2b))
print(an_edit_away(s3a, s3b))
print(an_edit_away(s4a, s4b))
print(an_edit_away(s5a, s5b))
print(an_edit_away(s6a, s6b))
