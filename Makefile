verify:
	@test -f .env && echo "$FILE exists."

build: verify
	@docker build -t weather_checker .

start:
	@docker run --env-file .env weather_checker $(args)