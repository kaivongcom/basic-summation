import main
message, test_pass = '...', bool(False)
summation_of_4_5_6 = 15
the_summation_of_3_ints_within_main = summation_of_4_5_6
expected_rusults = { "i": the_summation_of_3_ints_within_main }

def test_expectations():
    test_pass = (main.summation() == expected_rusults['i'])
    return test_pass

message = 'passes running test' if test_expectations() else 'fails the run test'
print(message)
