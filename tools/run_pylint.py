#!/usr/bin/env python3

import subprocess

import const


def main():
    subprocess.run(
        'pylint python --rcfile=tools/.pylintrc',
        cwd=const.REPO_PATH,
        shell=True,
    )


if __name__ == '__main__':
    main()
