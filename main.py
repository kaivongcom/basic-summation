SUMMATION_OBJ = { "four": 4, "five": 5, "six": 6 } 

def summation():
  s_list = list(SUMMATION_OBJ.values())
  if (type(s_list) == list) and len(s_list) == 3:
    a, b, c = s_list
    return (a + b + c) 
  else:
    print("Please make function arguments there, List of 3 ints")
