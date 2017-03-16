def _impl(ctx):
  print("This rule does nothing")


empty = rule(implementation=_impl)  
