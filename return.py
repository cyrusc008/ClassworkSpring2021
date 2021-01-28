def my_function(x):
  a = x + 5
  if a < 0:
    answer = "negative number"
  else:
    answer = "positive number"
  return a, answer

y, z = my_function(-20)
print(y)
print(z)