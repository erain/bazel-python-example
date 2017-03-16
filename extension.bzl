load("//:empty.bzl", "empty")


def macro(name, visibility=None):
  # Create the rule.
  empty(name=name, visibility=visibility)
