import main
message = '...'
summation_of_4_5_6 = 15
the_summation_of_3_ints_within_main = summation_of_4_5_6
expected_rusults = { "i": the_summation_of_3_ints_within_main }

message = 'passes running test' if (main.summation() == expected_rusults['i']) else 'fails the run test'
print(message)
