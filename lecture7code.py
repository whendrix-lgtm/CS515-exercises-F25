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
