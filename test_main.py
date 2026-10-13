#!/usr/bin/env python

import main
message = '...'
summation_of_numbers_1_to_100 = 5050
expected_rusults = { "i": summation_of_numbers_1_to_100 }

message = 'passes running test' if (main.summation() == expected_rusults['i']) else 'fails the run test'
print(message)
