SUMMATION_LIST = [4,5,6]

def summation():
  s_list = SUMMATION_LIST
  if (type(s_list) == list) and len(s_list) == 3:
    a, b, c = s_list
    return (a + b + c) 
  else:
    print("Your arguments should be a List of 3 ints, sorry") 



