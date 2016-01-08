#!/usr/bin/python3

import sys
import datetime

from utils_net import get, send_me_sms


def log(txt):
    with open("log_weather.txt", "a") as f_out:
        f_out.write(txt + "\n")


def get_meteo(city="nice,fr"):
    # key_API = "87f65bc51daf00643b6cf11ac138cd0a"
    url = "http://api.previmeteo.com/" + \
          "87f65bc51daf00643b6cf11ac138cd0a/ig/api"
    post = {"weather": city,
            "hl": "fr"}
    xml = get(url, params=post, verify=False).text
    token1 = """<day_of_week data="Auj"/>"""
    token_final_start = "<condition data="
    token_final_end = "/>"

    i_token1 = xml.find(token1)
    i_token_final_start = xml.find(token_final_start, i_token1 + 1)
    i_token_final_end = xml.find(token_final_end, i_token_final_start + 1)

    i_begin = i_token_final_start + len(token_final_start)
    i_end = i_token_final_end
    weather = xml[i_begin:i_end][1:-1]

    msg = "-".join(datetime.date.today().isoformat().split("-")[::-1]) + \
          " : " + weather

    send_me_sms(msg)
    print(msg, file=sys.stderr)
    log("[" + msg + "]\n" + xml)

get_meteo()
