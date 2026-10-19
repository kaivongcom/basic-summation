S_LIST, S_LIST2, s_obj = set({int(4),int(5),int(6)}), [str('four'), str('five'), str('six')], {}
MAX_LENGTH = 3

for item in S_LIST2: s_obj[item] = S_LIST.pop()
SUMMATION_OBJ = s_obj

def summation():
  s_list = list(SUMMATION_OBJ.values())
  if (type(s_list) == list) and len(s_list) == MAX_LENGTH:
    a, b, c = s_list
    return (a + b + c) 
  else:
    print("Please make function arguments there. List of {0} ints".format(MAX_LENGTH))
