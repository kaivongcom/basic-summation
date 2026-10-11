S_LIST, s_obj = (list(range(1,100))+[100]), {}
MAX_LENGTH = 100
SUMMATION_OBJ = S_LIST

def summation():
  s_list = list(SUMMATION_OBJ)
  if (type(s_list) == list) and len(s_list) <= MAX_LENGTH:
    int_counter = 0
    for item in s_list:
        int_counter += item
    return int_counter 
  else:
    print("Please make function arguments there, List of {0} ints".format(MAX_LENGTH))
