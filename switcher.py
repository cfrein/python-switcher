#!/usr/bin/env python
"""Website with flask
"""
from flask import Flask, render_template, request, jsonify

import wifileds
MILIGHT = "192.168.0.11"
DIM_VALUE = 10

app = Flask(__name__)

led_connection = wifileds.limitlessled.connect(MILIGHT)


def pink_lamp():
    """set deko-lamp to pink
    """
    led_connection.rgbw.set_color("pink", 3)
    print "Pink now"


def bright_floor():
    """
    """
    led_connection.rgbw.white(1)
    print "Floor is shining bright"


def dim_floor():
    """
    """
    led_connection.rgbw.set_brightness(DIM_VALUE)
    print "Floor dimmed down"


@app.route('/')
def main():
    title = "Switch some Things"
    scenarios = {
        "1": "Flur hell",
        "2": "Morning scene",
        "3": "TV",
        "4": "Pink Deko"
    }
    return render_template('selector.html', title=title, scenarios=scenarios)


@app.route('/_button')
def _button():
    print "button"
    return ""


# @app.route('/hello/')
@app.route('/_led')
def _led():
    state = request.args.get('state')
    print (state)
    if state == "1":
        bright_floor()
    if state == "2":
        dim_floor()
    if state == "4":
        pink_lamp()
#    if state=="on":
#        print "on"
#    else:
#        print "off"
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0')
