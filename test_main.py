#!/usr/bin/env python

import main
message = '...'
summation_of_numbers_1_to_100 = 5050
expected_rusults = { "xv": summation_of_numbers_1_to_100 }

message = 'passes running test' if (main.summation() == expected_rusults['xv']) else 'fails the run test'
print(message)
