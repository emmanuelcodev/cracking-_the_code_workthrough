def is_a_rotation(s1, s2):
    if None in (s1, s2):
        raise Exception('s1 and s2 cannot be of NoneType')

    s1_size = len(s1)
    s2_size = len(s2)

    if s1_size!=s2_size:#rotations mean its the same string, so it str lenght must match
        print('not same size')
        return False

    counter_s1 = 0
    counter_s2 = 0
    for x in range(s1_size):
        if s1[counter_s1] == s2[counter_s2]:#idea is to know how many letters match, to see how many letters in the array
            print('\n')
            print(s1[counter_s1])
            print(s2[counter_s2])
            print('same')
            counter_s1+=1
            counter_s2+=1
        else:
            counter_s2 = 0# because they are equal length, if the letters do not match we don't count them and if they stop matching we reset it, because it's not the same word
            counter_s1 += 1

    if counter_s2:
        print('counter_s2 ', counter_s2)
        return s2[counter_s2:] in s1 #isSubstring equivalent
    else:
        print('counter_s2 ', counter_s2)
        return False

s1 = 'hello'
s2 = 'hello'
print(is_a_rotation(s1, s2))

s1 = 'wat'
s2 = 'twa'
print(is_a_rotation(s1, s2))


s1 = 'waterbottle'
s2 = 'erbottlewat'
print(is_a_rotation(s1, s2))

print('\n')
s1 = 'waterbottle'
s2 = 'erboxtlewat'
print(is_a_rotation(s1, s2))
