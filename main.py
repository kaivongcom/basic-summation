S_LIST, S_LIST2, s_obj = [int(4),int(5),int(6)], [str(), str(), str()], {}
MAX_LENGTH = 3

for item in S_LIST: item_keyname = S_LIST[S_LIST.index(item)]; s_obj[item_keyname] = item
SUMMATION_OBJ = s_obj

def summation():
  s_list = list(SUMMATION_OBJ.values())
  if (type(s_list) == list) and len(s_list) == MAX_LENGTH:
    a, b, c = s_list
    return (a + b + c) 
  else:
    print("Please make function arguments there. List of {0} ints".format(MAX_LENGTH))
