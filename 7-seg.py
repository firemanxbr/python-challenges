#!/usr/bin/python

import sys

"""
  dictionary codes source
  ------------> 6543210
  print 0, int('0111111', 2) #063       0
  print 1, int('0001010', 2) #010     +---+
  print 2, int('1011101', 2) #093    5|   |3
  print 3, int('1001111', 2) #079     +-6-+
  print 4, int('1101010', 2) #106    4|   |1
  print 5, int('1100111', 2) #103     +-2-+
  print 6, int('1110110', 2) #118
  print 7, int('0001011', 2) #011
  print 8, int('1111111', 2) #127
  print 9, int('1101011', 2) #107
"""

""" decimal to display number dictionary """
dec_to_display_dic = {
    0: '063',
    1: '010',
    2: '093',
    3: '079',
    4: '106',
    5: '103',
    6: '118',
    7: '011',
    8: '127',
    9: '107'}

""" display number to decimal dictionay """
display_to_dec_dic = {
    '063': 0,
    '010': 1,
    '093': 2,
    '079': 3,
    '106': 4,
    '103': 5,
    '118': 6,
    '011': 7,
    '127': 8,
    '107': 9}

""" my list for print result variable """
list_result = []


""" interactive read for user input decimal numbers
    recursive function """
def read_user_input():
    uinput = raw_input('---> ')

    if uinput.isdigit() or '+' in uinput or '=' in uinput:
        list_result.append(handle_codes(uinput))
        read_user_input()
    else:
        if uinput.upper() == "BYE":
            print '\n'.join(list_result)
            sys.exit(0)
        else:
            read_user_input()


""" function helper for decimal dictionary """
def get_decimal(s, dic):
    return dic[s]


""" function helper for display number dictionary """
def get_display(d, dic):
    return dic[d]


""" read last 3 characters of decimal to display str return
    recursive function """
def displaystr_to_decstr(dstr):
    ret = ''.join(str(get_decimal(dstr[:3], display_to_dec_dic)))

    if len(dstr)-3 > 0:
        return ret + displaystr_to_decstr(dstr[3:])
 
    return ret


""" read last 1 character of display to decimal str return
    recursive function """
def decstr_to_displaystr(dstr):
    ret = ''.join(str(get_display(int(dstr[:1]), dec_to_display_dic)))

    if len(dstr)-1 > 0:
        return ret + decstr_to_displaystr(dstr[1:])

    return ret


""" remove '+' and '=' and split first and second
    decimal setences. After sum to return uinput """
def handle_codes(uinput):
    uinput = uinput.strip('=')

    first, second = uinput.split('+')

    a = int(displaystr_to_decstr(first))
    b = int(displaystr_to_decstr(second))
    c = a + b

    result = decstr_to_displaystr(str(c))

    return "%s=%s" % (uinput, result)


""" Main """
read_user_input()
