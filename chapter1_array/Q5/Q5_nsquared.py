def count_instances(str1, letter):
    #counts instances of a letter across a string
    counter = 0
    for x in str1:
        if letter == x:
            counter+=1

    return counter

def an_edit_away(str1, str2):
    if None in (str1, str2):
        raise Exception('st1 and str2 cannot be of NoneType')

    #get rid of strings that are more than 1 edit away, meaning they the size can eiher be the same size, or 1 apart
    str1_size = len(str1)
    str2_size = len(str2)

    if abs(str1_size - str2_size)>1:
        return False

    #track unique letters
    unique_letters = []

    #get longest str, use str1 if equal len or if str1 is larger
    longest = str1
    shortest = str2

    if str2_size>str1_size:
        longest = str2
        shortest = str1

    #get unique characters
    for x in longest:
        if x in unique_letters:
            pass
        else:
            unique_letters.append(x)

    #loop through each unique_letters and, see differences between two strings, telling us how many edits they are from one another
    differences = 0

    for x in unique_letters:
        differences+= abs(count_instances(str1, x) - count_instances(str2, x))

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
print(an_edit_away(s5a, s5b))
print(an_edit_away(s6a, s6b))
