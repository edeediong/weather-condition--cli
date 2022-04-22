# weather-condition-cli

Remembering to bring an umbrella with me on rainy days and sunscreen on sunny days is difficult.
This script enables you check the weather and lets you know whether you need to pack an
umbrella or sunscreen.

## How to Use

To run the app, take the following steps:

* Signup at [WeatherApi](https://www.weatherapi.com/) and grab an API Key from them. It's free and does not need a credit card.

* Clone the repository into your local machine

* Rename `.env.example` to `.env` and paste your API key from the first step.

* Run `make start args=<args>`
  * Where `<args>` is either `shine` or `rain`.

### Legacy Way

You can run the commands without using make by following the instructions below:

* Build the Docker image with `docker build -t weather_checker .`

* Run the application with `docker run --env-file .env weather_checker <args>`
  * Where `<args>` is either `shine` or `rain`.

## Example Usage

[![asciicast](https://asciinema.org/a/xmr2jjECI1NZRe8yCFzdxweGy.svg)](https://asciinema.org/a/xmr2jjECI1NZRe8yCFzdxweGy)
