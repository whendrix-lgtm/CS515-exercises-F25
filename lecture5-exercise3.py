# arg_max:  takes an arbitrary number of arguments
# and returns the largest (using >)
def arg_max(*args):
  if not args:
    raise ValueError('Must specify at least one value')
  max_arg = args[0]
  for arg in args[1:]:
    if arg > max_arg:
      max_arg = arg
  return max_arg

print(f'arg_max(1,6,3,4,2,7,1,4,2,-1) = {arg_max(1,6,3,4,2,7,1,4,2,-1)}')
print(f"arg_max('apple','belt','aardvark','xavier') = {arg_max('apple','belt','aardvark','xavier')}")

# Lambda function delta that calculates the differences
# between consecutive elements of a list

test = [0, 1, 3, 6]
delta = lambda list : [list[i] - list[i-1] for i in range(1,len(list))]
print(f'delta({test}) = {delta(test)}')
print("Should be [1, 2, 3]")

# Lambda function smoothness that outputs the result of
# applying delta until 1 element is left and return that element

smoothness = lambda list : list[0] if len(list) == 1 else smoothness(delta(list))

def smoothness2(list):
  if len(list) == 1:
    return list[0]
  else:
    return smoothness2(delta(list))

print(f'smoothness({test}) = {smoothness(test)}')
print('Manual calculation:')
print(test)
while len(test) > 1:
  test = delta(test)
  print(test)
print(test[0])
