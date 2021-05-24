import sys
import subprocess

def call_git_with_arguments(args):
    subprocess.run(args)

def create_list_of_arguments(arg_list, args):
    arg_list.append("git")
    for arg in args[1:]:
        arg_list.append(str(arg))


if __name__ == "__main__":
    sys.argv.append("status")
    arg_list = []
    create_list_of_arguments(arg_list, sys.argv)
    call_git_with_arguments(sys.argv)
