#!/usr/bin/env python3
import sys
import subprocess


def call_git_with_arguments(args):
    succesfull = subprocess.run(args).returncode
    if succesfull != 0:
        sys.stdout.write("\u001b[31mGit not Installed.")
        exit()
def create_list_of_arguments(arg_list, args):
    arg_list.append("git")
    for arg in args[1:]:
        arg_list.append(str(arg))


if __name__ == "__main__":
    arg_list = []
    create_list_of_arguments(arg_list, sys.argv)
    call_git_with_arguments(arg_list)