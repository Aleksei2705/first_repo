# Import the module.
import python_weather

import asyncio
import os


async def main() -> None:

  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:

    # Fetch a weather forecast from a city.

    current_city = input("Введи город и узнай в нем погоду: " )

    weather = await client.get(current_city)

    celsius = (weather.temperature - 32) / 1.8

    # Fetch the temperature for today.
    print(" В городе " + current_city + " " + str(round(celsius)) + "°")
    print("")
    print("")
    print("")
    print("* Камиль - зловещий весельчак! *")
    print("")
    print("")
    input('Покинь дебри нажав "Enter"')

    # Fetch weather forecast for upcoming days.
    #for daily in weather:
    #  print(daily)

    # Each daily forecast has their own hourly forecasts.
    #  for hourly in daily:
    #    print(f' --> {hourly!r}')*//

if __name__ == '__main__':

  # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details.
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(main())