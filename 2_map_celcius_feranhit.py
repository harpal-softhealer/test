celsius_temperatures = [25,30,22,26,29,28]

feranhit = lambda celc : celc * (9/5) + 32

feranhit_temperatures = list(map(feranhit,celsius_temperatures))


print(feranhit_temperatures)