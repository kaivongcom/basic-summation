import main
message = '...'
expected_rusults = { "xv": 15  }

message = 'passes running test' if (main.summation() == expected_rusults['xv']) else 'fails the run test'
print(message)

