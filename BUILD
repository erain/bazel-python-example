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
    srcs = [],
    python_path = "/usr/local/google/home/yiyu/.pyenv/versions/2.7.11/",
)

py_runtime(
    name = "python-3",
    srcs = glob(["python-3/**"]),
    python_path = "python-3",
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)
