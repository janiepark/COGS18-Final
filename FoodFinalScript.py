

#First importing all the necessary methods and modules.
import random
from food_module import food_type
from food_module import dietary_restriction
from food_module import final_rec


#Asks the user a question in a friendly interactive manner.
user_input = input('Let\'s find something for you to eat today!\nPlease enter what type of food you ' \
                    'would like to eat from the three options of "snack", "meal" or "drink": \n')

#To check that the user put one of the possible categories. If they did not, it will loop back with the options.
while True:
    if str.lower(user_input) in ('snack','meal','drink'):
        break
    else:
        user_input = input("\nSorry, we don't have that option. Please start over and choose one of the " \
                           "available options. \n")
    
        
#A call on the method asking what category of food they would like.  
type_of_food = food_type(str.lower(user_input))

#Asks the user in an interactive way about their dietary restrictions.
user_input = input("\nThank you for choosing a type of food!\nOur next question is, do you happen to be " \
                   "vegetarian, vegan, gluten free or have a peanut allergy?\nIf so, please type 'vegetarian'," \
                   " 'vegan', 'gluten free' or 'peanut allergy'. If not, please type 'none': \n")

#Double checks to make sure the user entered a possible option. If they did not, it asks them again.
while True:
    if str.lower(user_input) in ('vegetarian','vegan','gluten free', 'peanut allergy', 'none'):
        
        break
        
    else:
        user_input = input("\nSorry, we could not recognize what you said or currently do not have a " \
                           "comprehensive list for that dietary restriction. Please select one of the " \
                           "available options previously mentioned. \n")
        
#Call on the method dietary_restriction that stores it in a variable.
restrictions = dietary_restriction(user_input, type_of_food)

#A dicitonary of all the different food places that gives a short description as the value.
food_descriptions = {'Bombay Coast' : 'Our recommendation is Bombay Coast. This restaurant offers Indian cuisine and' \
                'has a variety of vegetarian, gluten free and peanut free options. Similar to many ' \
                'restaurants with a shared kitchen, there is a chance of cross contamination of allergens.' ,
                'Burger King' : 'Our recommendation is Burger King. This restaurant offers affordable and quick food, ' \
                'accommodating many dietary restrictions. In particular, Burger King now has the Impossible ' \
                'Burger, which offers a vegetarian option as well as a vegan one if the mayonnaise is ' \
                'replaced with BBQ sauce and there is no cheese. Popular snacks include onion rings, french ' \
                'fries and chicken fries. Similar to many restaurants with a shared kitchen, there is a ' \
                'chance of cross contamination of allergens.', 
                'The Loft' : 'Our recommendation is The Loft. This hole in the wall spot offers entertainment with ' \
                'frequent live performances and a variety of sandwiches, burgers, pizzas and more! They ' \
                'have many drinks varying from alcoholic beverages such as beer and mimosas to refreshing ' \
                'ones like lemonade. Similar to many restaurants with a shared kitchen, there is a chance ' \
                'of cross contamination of allergens.' ,
                'Jamba Juice' : 'Our recommendation is Jamba Juice. With a variety of different smoothies, ' \
                'acai bowls and snacks such as sweet waffles, Jamba Juice makes for a great pick-me-up ' \
                'during the day! They have a variety of milk alternatives such as soy milk or oat milk and ' \
                'have many supplements you can add to their smoothies. Similar to many restaurants with a ' \
                'shared kitchen, there is a chance of cross contamination of allergens.',
                'Lemongrass' : 'Our recommendation is Lemongrass. This restaurant offers a taste of Thai cuisine, ' \
                'famous for their peanut sauce. Gluten free options include their salmon plate and a ' \
                'delicious vegan option is their Pad Thai with tofu. The Thai tea is one of the best on ' \
                'campus, making for a refreshing treat! Similar to many restaurants with a shared kitchen, ' \
                'there is a chance of cross contamination of allergens.', 
                'Panda Express' : 'Our recommendation is Panda Express. This restaurant offers a variety of ' \
                'different sides, from beef and broccoli to honey walnut shrimp, to pair with their rice and/or ' \
                'chow mein. Healthier options are also available with their teryaki chicken and side of vegetables! ' \
                'Similar to many restaurants with a shared kitchen, there is a chance of cross contamination ' \
                'of allergens.', 
                'Rubios' : 'Our recommendation is Rubios. This restaurant offers a variety of proteins from the ' \
                'land to the sea and any protein can be replaced with grilled vegetables to make it vegetarian or ' \
                'vegan. Several of the options, such as the bowls or tacos, are also gluten free. Similar to ' \
                'many restaurants with a shared kitchen, there is a chance of cross contamination of allergens.', 
                'Santorini' : 'Our recommendation is Santorini. This restaurant offers a taste of the ' \
                'Mediterranean, with a variety of proteins from gyros to chorizo. They are quite famous for ' \
                'their Loaded Fries,which are gluten free, and many salad options. If on campus early in the ' \
                'morning, don\'t worry! They have a full breakfast menu from 7:30AM to 11:30AM. Similar to many ' \
                'restaurants with a shared kitchen, there is a chance of cross contamination of allergens.', 
                'Seed + Sprout' : 'Our recommendation is Seed + Sprout. This newer restaurant offers fresh ' \
                'food with healthier options, loaded with vegetables and full of flavor. ' \
                'The \'Choose your own bowl\' style menu allows for flexible choices with most dietary ' \
                'restrictions. They also feature a great breakfast menu, with one of their most popular ' \
                'items the Loco Moco. Similar to many restaurants with a shared kitchen, there is a ' \
                'chance of cross contamination of allergens.',
                'Shogun' : 'Our recommendation is Shogun. This restaurant offers a variety of Asian cuisine, ' \
                'from chicken curry katsu to a full sushi menu with more than plenty of options to browse. ' \
                'Not only that, but it\'s a great place for entertainment with their pool tables open for ' \
                'students to use. Similar to many restaurants with a shared kitchen, there is a chance of ' \
                'cross contamination of allergens.', 
                'Starbucks' : 'Our recommendation is Starbucks. Famous for their various drinks from coffee to ' \
                'tea to their very own Refreshers, Starbucks offers a variety of different choices. They also ' \
                'have a great bakery selection with breakfast sandwiches, cake pops, baked goods, paninis ' \
                'and more to choose from. Similar to many restaurants with a shared kitchen, there is a ' \
                'chance of cross contamination of allergens.',
                'Subway' : 'Our recommendation is Subway. Famous for allowing customers to customize their ' \
                'sandwiches, Subway offers several toppings, proteins, sauces and more to fit many dietary ' \
                'restrictions. They also offer sweet treats like freshly baked cookies and salty snacks such ' \
                'as chips to go with your sandwich.\nSimilar to many restaurants with a shared kitchen, ' \
                'there is a chance of cross contamination of allergens.',
                'Sunshine' : 'Our recommendation is Sunshine Market. This market is not only conveniently ' \
                'located in the center of campus but offers a variety of snacks and necessities, from chips ' \
                'to drinks to Brown Bag Sandwiches to fit everyone\'s needs.\nTheir office is also working ' \
                'with The Hub to get EBT accepted to become more accessible to the student population.',
                'Su Pan Bakery' : 'Our recommendation is Su Pan Bakery, hidden behind Burger King. This ' \
                'small and relatively new Mexican bakery offers sweet treats and filling desserts to snack ' \
                'on throughout the day, from pastries all the way to whole cakes and pies that can be purchased. ' \
                'With how hard you work, you deserve to treat yourself!',
                'Tapioca Express' : 'Our recommendation is Tapioca Express. Known for being the boba hotspot ' \
                'on campus, Tapioca Express, TapEx for short, offers refreshing beverages along with popular snacks ' \
                'such as popcorn chicken. Their vast drink menu offers many options to browse and even have ' \
                'specials on different days of the week! Similar to many restaurants with a shared kitchen, ' \
                'there is a chance of cross contamination of allergens.', 
                'Croutons' : 'Our recommendation is Croutons. Famous for their salads, sandwiches and soups, ' \
                'Croutons is a great spot to grab lunch, especially their popular two item combo. Their hours ' \
                'are limited as they\'re open 10AM-3PM, but many options can be turned vegan or gluten free ' \
                'by asking to remove the cheese or croutons. Similar to many restaurants with a shared kitchen, ' \
                'there is a chance of cross contamination of allergens.',
                'Yogurt World' : 'Our recommendation is Yogurt World. As the on campus fro-yo spot, ' \
                'Yogurt World offers many flavors as well as topping to choose from. It makes for a great ' \
                'pick-me-up snack, and look out for their color changing spoons! Similar to many restaurants ' \
                'with a shared kitchen, there is a chance of cross contamination of allergens.',
                'Blue Pepper' : 'Our recommendation is Blue Pepper. This restaurant offers a taste of ' \
                'Thai food, serving many different foods from noodles to rice to several curries, allowing ' \
                'for customers to choose depending on what catches their eyes. They also offer many desserts, ' \
                'from boba to mango sticky rice! Similar to many restaurants with a shared kitchen, there is a ' \
                'chance of cross contamination of allergens.',
                'Soda & Swine' : 'Our recommendation is Soda & Swine. As the newest dining spot on campus ' \
                'with a beautiful aesthetic, it can be tricky finding seats at this packed place! Famous ' \
                'for their sliders, which have vegan options included, Soda & Swine offers a taste casual ' \
                'food that\'s been elevated. They also offer a variety of beers to choose from! Similar to ' \
                'many restaurants with a shared kitchen, there is a chance of cross contamination of allergens.',
                'Taco Villa' : 'Our recommendation is Taco Villa. This restaurant offers a variety of tacos, ' \
                'burritos and bowls, allowing for customers to choose flexibly. Their bowls are gluten free and ' \
                'the protein can be replaced with vegetables to make for vegetarian and vegan options and offer ' \
                'drinks such as horchata on their menu. Similar to many restaurants with a shared kitchen, ' \
                'there is a chance of cross contamination of allergens.'}


#Chooses a final vendor after the two inputs and gives information about it.
print("\n" + final_rec(restrictions))

#Checks the satisfaction of the user. If they like the choice, it stops, but if not, loops through again.
user_input = input("\nThank you for using our service! If you're not satisfied with your choice, " \
               "would you like to choose a new one? If so, type 'yes'. If no, type 'no': \n")
while True:

    if str.lower(user_input) == ('no'):
        print('\nHope you enjoy!')
        
        break
        
    elif str.lower(user_input) == ('yes'):
        
        print(final_rec(restrictions))
        
        user_input = input("\nThank you for using our service! If you're not satisfied with your choice, " \
                       "would you like to choose a new one? If so, type 'yes'. If no, type 'no': \n")
        
    else:
        user_input = input("\nSorry, could not recognize what you typed. Based upon the previous " \
                           "question, please answer 'yes' or 'no': \n")






