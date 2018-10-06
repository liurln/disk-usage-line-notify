#!/usr/bin/python3
# -*- coding: utf-8

import requests

line_api_notify_url = 'https://notify-api.line.me/api/notify'


def send_message(message, token):
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Authorization': 'Bearer ' + token}
    res = requests.post(line_api_notify_url, headers=headers,
                        data={'message': message})
