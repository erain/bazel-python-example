py_library(
    name = "lib",
    srcs = ["lib.py"],
    srcs_version = "PY2AND3",
)

py_binary(
    name = "bin",
    srcs = ["bin.py"],
    srcs_version = "PY2AND3",
    deps = [":lib"],
)

py_runtime(
    name = "python-2",
    files = [],
    interpreter_path = "/usr/local/google/home/yiyu/.pyenv/versions/2.7.11/bin/python",
)

py_runtime(
    name = "python-3",
    files = glob(["python-3/**"]),
    interpreter = "python-3/bin/python",
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)
