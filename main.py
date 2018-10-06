#!/usr/bin/python3
# -*- coding: utf-8

import settings
import src.disk_usage as disk_usage
import src.line_api as line_api
import sys


def main():
    disk_usage_amount = disk_usage.du(sys.argv[2])
    message = f'Disk usage notify\nStation: {sys.argv[1]}\nDisk usage: {disk_usage_amount}'
    line_api.send_message(message, settings.LINE_MESSAGE_TOKEN)


if __name__ == '__main__':
    main()
