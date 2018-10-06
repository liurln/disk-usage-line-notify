#!/usr/bin/python3
import subprocess


def du(path):
    # This code from https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du', '-sh', path]).split()[0].decode('utf-8')


def main():
    print(du('.'))


if __name__ == '__main__':
    main()
