import lib


def main():
  """
  Check and show the Python runtime we claim is actual Python runtime
  """
  python_version = lib.python_version()
  print("*****************************************")
  print("* The Python version running is : %s *" % python_version)
  print("*****************************************")


if __name__ == "__main__":
  # we will only care about the first command line args,
  # which is the python version we will passin
  main()
