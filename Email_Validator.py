import re

email_input = input("Enter your email :: ")

flag = re.match(r'^\w+@\D+.com', email_input)

if flag is not None:
  print('Your Email is valid::', flag.group())
else:
  print("Email is invalid")
