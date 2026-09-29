import main
message = '...'
expected_rusults = { "xv": 15  }

if main.summation() == expected_rusults['xv']:
  message = 'passes running test'
else:
  message = 'fails the run test'

print(message)

