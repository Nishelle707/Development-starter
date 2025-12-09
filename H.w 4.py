weather = input("What's the weather like today?: ")

if weather in ("Rainy", "Rain"):
    print(" RAINY: Make sure to have an umbrella or raincoat with you")

elif weather in ("Sunny", "hot", "warm"):
    print(" SUNNY: Wear sunscreen or use an umbrella when going out")

else:
    print(" SNOWY: Wear a jacket or pullover so you won't get cold")
