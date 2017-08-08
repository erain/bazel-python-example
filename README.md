# Introduction

Following commands show how to use this repo with bazel's py_runtime rule.

Use the system-wide python interpreter.

``` shell
$ bazel run :bin
INFO: Analysed target //:bin (8 packages loaded).
INFO: Found 1 target...
Target //:bin up-to-date:
  bazel-bin/bin
INFO: Elapsed time: 3.168s, Critical Path: 0.02s
INFO: Build completed successfully, 4 total actions

INFO: Running command line: bazel-bin/bin
*****************************************
* The Python version running is : 2.7.6 *
*****************************************
```

Use a python interpreter in an absolute path:

``` shell
$ bazel run --python_path=/usr/local/google/home/yiyu/.pyenv/versions/2.7.12/bin/python :bin
INFO: Analysed target //:bin (0 packages loaded).
INFO: Found 1 target...
Target //:bin up-to-date:
  bazel-bin/bin
INFO: Elapsed time: 0.272s, Critical Path: 0.01s
INFO: Build completed successfully, 2 total actions

INFO: Running command line: bazel-bin/bin
*****************************************
* The Python version running is : 2.7.12 *
*****************************************
```

Use `py_runtime` with `interpreter_path` which points to an absolute path

``` shell
$ bazel run --python_top=//:python-2 :bin
INFO: Analysed target //:bin (0 packages loaded).
INFO: Found 1 target...
Target //:bin up-to-date:
  bazel-bin/bin
INFO: Elapsed time: 0.253s, Critical Path: 0.01s
INFO: Build completed successfully, 2 total actions

INFO: Running command line: bazel-bin/bin
*****************************************
* The Python version running is : 2.7.11 *
*****************************************
```

Use `py_runtime` with `interpreter` which is a checked-in python interpreter

``` shell
$ bazel run --python_top=//:python-3 :bin
INFO: Analysed target //:bin (0 packages loaded).
INFO: Found 1 target...
Target //:bin up-to-date:
  bazel-bin/bin
INFO: Elapsed time: 4.063s, Critical Path: 0.50s
INFO: Build completed successfully, 4 total actions

INFO: Running command line: bazel-bin/bin
*****************************************
* The Python version running is : 3.7.0a0 *
*****************************************
```
