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

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)
