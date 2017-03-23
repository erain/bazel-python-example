load("//:extension.bzl", "macro")

macro(name = "myrule")

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
    name = "py3",
    interpreter = "/usr/local/google/home/yiyu/.pyenv/versions/3.6.0/bin/python",
)

py_runtime(
    name = "py2",
    interpreter = "/usr/local/google/home/yiyu/.pyenv/versions/2.7.11/bin/python",
)

py_runtime_suite(
    name = "py_runtime_suite",
    default = ":py2",
    runtimes = {
        "k8": ":py2",
        "armeabi-v7a": ":py3",
    },
)

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)
