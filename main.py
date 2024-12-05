#!/usr/bin/env python3

import sys
sys.path.append('./modules')

import typer
app = typer.Typer()

import weather_m


@app.command()
def weather():
    weather_status=weather_m.fetch_weather()
    print(f'The current weather in HCM city is {weather_status}!')
    

@app.command()
def blaa():
    print('bla')

if __name__ == '__main__':
    app()