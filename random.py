# Dominic Casamatta : 22 Noc 2019
# Random generator to select a random order from Starubucks
# Goals:
#   create list: done
#   generate random outcomes: done
#   

import random
from tkinter import *
root = Tk()

root.title("Starbucks Order Generator")
root.geometry("400x200")

root.mainloop()
#lists
size = ["Tall",
        "Grande",
        "Venti",
        "Trenta"
        ]

drink = ["Strawberry Acai Refresher",
        "Pink Drink",
        "Strawberry Frappuccino",
        "Salted Carmel Mocha",
        "Mango Dragonfruit Refresher",
        "Iced Guava White Tea",
        "Starbucks Cold Brew",
        "Nitro Cold Brew",
        "White Chocolate Mocha",
        "Mocha Cookie Crumble Frappuccino",
        "Eggnog Latte",
        "Carmel Frappuccino",
        "Cold Brew with Salted Cream Cold Foam",
        "Carmel Macchiato",
        "Cappuccino",
        "Vanilla Bean Creme Frappuccino",
        "Royal English Breakfast Black Tea",
        "Dark Roast",
        "Blonde Roast",
        "Medium Roast",
        "Peppermint Mocha Frappuccino",
        "Peppermint Hot Chocolate",
        "Caffe Americano",
        "Flat White",
        "Mint Majesty Tea",
        "Chai Tea Latte",
        "Matcha Green Tea Latte",
        "Iced Green Tea",
        "Emperor's Clouds and Mist Green Tea",
        "Iced Peachc Green Tea Lemonade",
        "Toasted White Chocolate Mocha Frappuccino",
        "Iced Cocoa Cloud Macchiato",
        "Chestnut Praline Latte",
        "Caffe Latte",
        "Caffe Mocha",
        "Nitro Cold Brew with Sweet Cream",
        "Signature Hot Choloate",
        "Toasted White Chocolate Mocha",
        "Pumpkin Spice Latte",
        "Iced Caramel Cloud Macchiato",
        "Peppermint Mocha",
        "Nitro Cold Brew with Cascara Cold Foam"
        ]

food = ["Double Smoked Bacon Cheddar and Egg Sandwhich",
        "Lemon Loaf",
        "Chicken Artichoke on Ancient Grain Flatbread",
        "Protein Bistro Box",
        "Peanut Butter Cup Cookie",
        "Hearty Veggie and Brown Rice Salad Bowl",
        "Double Chocolate Brownie",
        "Spinach and Feta Wrap with Cage-free Egg White",
        "Greek and Honey Yogurt Parfait",
        "Organic Avocado Spread"
        ]
#inputs
drink_choice = input("Do you want a drink?\n")
food_choice = input("Do you want food?\n")
size = random.choice(size)
food = random.choice(food)
drink = random.choice(drink)

#process to select random
if drink_choice == 'yes':
    print("Size: ", size)
    print("Drink: ", drink)
          
elif drink_choice == 'no':
    print("Size and Drink: N/A")

else:
    print("Error")

if food_choice == 'yes':
    print("Food: ", food)

elif food_choice == 'no':
    print("Food: N/A")

else:
    print("Error")



        
