# coding=utf-8
import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, required=True)
    args = parser.parse_args()

    startupFilePath = Path(os.getenv("DJANGO_STARTUP_NAME", "manage.py")).absolute()
    if not startupFilePath.is_file():
        print(f"Invalid startup file: {startupFilePath}")
        return

    startupTestArgs = shlex.split(os.getenv("DJANGO_STARTUP_TEST_ARGS", ""))

    djangoStartupArgs = [str(startupFilePath), "test", "--testrunner", "teamcity.django.TeamcityDjangoRunner"]
    djangoStartupArgs.extend(startupTestArgs)
    djangoStartupArgs.append(args.target)

    additionalGlobalsStr = os.getenv("DJANGO_STARTUP_ADDITIONAL_GLOBALS")
    if additionalGlobalsStr is not None:
        import ast
        additionalGlobals = ast.literal_eval(additionalGlobalsStr)
    else:
        additionalGlobals = {}

    print(f"Launching Django tests: {subprocess.list2cmdline(djangoStartupArgs)}")
    runModAsMain(djangoStartupArgs, additionalGlobals)


def runModAsMain(argv, codeGlobals):
    with open(argv[0]) as file:
        codeStr = file.read()
    sys.argv = argv
    code = compile(codeStr, os.path.basename(argv[0]), "exec")
    codeGlobals.update({
      "__name__": "__main__",
      "__file__": argv[0]
    })
    exec(code, codeGlobals)


if __name__ == '__main__':
    main()
