import random

def food_type(type_input):
    
    if type_input == 'snack':
        potential_list = ['Burger King', 'Jamba Juice', 'Starbucks', 'Sunshine Market', 'Su Pan Bakery',
                          'Tapioca Express', 'Yogurt World', 'Soda & Swine']
    elif type_input == 'drink':
        potential_list = ['Blue Pepper', 'The Loft', 'Jamba Juice', 'Lemongrass', 'Starbucks', 'Sunshine Market', 
                          'Tapioca Express', 'Soda & Swine']
    elif type_input == 'meal':
        potential_list = ['Blue Pepper', 'Bombay Coast', 'Burger King', 'The Loft', 'Lemongrass', 'Panda Express', 
                          'Seed + Sprout', 'Shogun', 'Soda & Swine', 'Subway', 'Taco Villa']
    return potential_list 

def dietary_restriction(type_input, type_of_food):
    
    ###The second question is if the person has any dietary restrictions. The ones that I settled for, vegetarian, gluten free, vegan and peanut allergy, were the ones that were some of the most common and restrictive on campus. To gather this data, I visited each vendor to ask about their capabilities around dietary restrictions as well as my friends who have these restrictions to get an idea of which places they avoid and which they frequent the most.###
    
    if type_input == 'vegetarian':
        return type_of_food
            
    elif type_input == 'gluten free':
        if 'Burger King' in type_of_food:
            type_of_food.remove('Burger King')
        if 'Panda Express' in type_of_food:
            type_of_food.remove('Panda Express')
        if 'Su Pan Bakery' in type_of_food:
            type_of_food.remove('Su Pan Bakery')
        if 'Subway' in type_of_food:
            type_of_food.remove('Subway')
        if 'Shogun' in type_of_food:
            type_of_food.remove('Shogun')
        
        return type_of_food
            
    elif type_input == 'vegan':
        if 'Shogun' in type_of_food:
            type_of_food.remove('Shogun')
        if 'Yogurt World' in type_of_food:
            type_of_food.remove('Yogurt World')
        if 'Tapioca Express' in type_of_food:
            type_of_food.remove('Tapioca Express')
        if 'Santorini' in type_of_food:
            type_of_food.remove('Santorini')
        if 'Panda Express' in type_of_food:
            type_of_food.remove('Panda Express')
        if 'Bombay Coast' in type_of_food:
            type_of_food.remove('Bombay Coast')   
        if 'Yogurt World' in type_of_food:
            type_of_food.remove('Yogurt World')
        if 'The Loft' in type_of_food:
            type_of_food.remove('The Loft')
            
        return type_of_food
            
    elif type_input == 'peanut allergy':
        if 'Lemongrass' in type_of_food:
            type_of_food.remove('Lemongrass')
        if 'Panda Express' in type_of_food:
            type_of_food.remove('Panda Express')
            
        return type_of_food
        
    elif type_input == 'none':
        return type_of_food
    
    return type_of_food        


def final_rec(food_restrictions):
    ###The final method will choose a vendor from the list of places left after the two previous questions and then give a bit of information about the place they choose.###
    
    final_choice = random.choice(food_restrictions)
    
    if final_choice == 'Bombay Coast':
        return 'Our recommendation is Bombay Coast. This restaurant offers Indian cuisine and' \
               'has a variety of vegetarian, gluten free and peanut free options. Similar to many ' \
               'restaurants with a shared kitchen, there is a chance of cross contamination of allergens.'
        
    
    
    elif final_choice == 'Burger King':
        return 'Our recommendation is Burger King. This restaurant offers affordable and quick food, ' \
               'accommodating many dietary restrictions. In particular, Burger King now has the Impossible ' \
               'Burger, which offers a vegetarian option as well as a vegan one if the mayonnaise is ' \
               'replaced with BBQ sauce and there is no cheese. Popular snacks include onion rings, french ' \
               'fries and chicken fries. Similar to many restaurants with a shared kitchen, there is a ' \
               'chance of cross contamination of allergens.'
        
        
    
    elif final_choice == 'The Loft':
        return 'Our recommendation is The Loft. This hole in the wall spot offers entertainment with ' \
               'frequent live performances and a variety of sandwiches, burgers, pizzas and more! They ' \
               'have many drinks varying from alcoholic beverages such as beer and mimosas to refreshing ' \
               'ones like lemonade. Similar to many restaurants with a shared kitchen, there is a chance ' \
               'of cross contamination of allergens.'
        
    
    elif final_choice == 'Jamba Juice':
        return 'Our recommendation is Jamba Juice. With a variety of different smoothies, ' \
               'acai bowls and snacks such as sweet waffles, Jamba Juice makes for a great pick-me-up ' \
               'during the day!\nThey have a variety of milk alternatives such as soy milk or oat milk and ' \
               'have many supplements you can add to their smoothies. Similar to many restaurants with a ' \
               'shared kitchen, there is a chance of cross contamination of allergens.'
    
    
    elif final_choice == 'Lemongrass':
        return 'Our recommendation is Lemongrass. This restaurant offers a taste of Thai cuisine, ' \
               'famous for their peanut sauce. Gluten free options include their salmon plate and a ' \
               'delicious vegan option is their Pad Thai with tofu. The Thai tea is one of the best on ' \
               'campus, making for a refreshing treat! Similar to many restaurants with a shared kitchen, ' \
               'there is a chance of cross contamination of allergens.'
        
        
    
    elif final_choice == 'Panda Express':
        return 'Our recommendation is Panda Express. This restaurant offers a variety of different sides, ' \
               'from beef and broccoli to honey walnut shrimp, to pair with their rice and/or chow mein. ' \
               'Healthier options are also available with their teryaki chicken and side of vegetables! ' \
               'Similar to many restaurants with a shared kitchen, there is a chance of cross contamination ' \
               'of allergens.'
      
    
    elif final_choice == 'Rubios':
        return 'Our recommendation is Rubios. This restaurant offers a variety of proteins from the land to ' \
               'the sea and any protein can be replaced with grilled vegetables to make it vegetarian or ' \
               'vegan. Several of the options, such as the bowls or tacos, are also gluten free. Similar to ' \
               'many restaurants with a shared kitchen, there is a chance of cross contamination of allergens.'
        
      
    elif final_choice == 'Santorini':
        return 'Our recommendation is Santorini. This restaurant offers a taste of the Mediterranean, with ' \
               'a variety of proteins from gyros to chorizo. They are quite famous for their Loaded Fries, ' \
               'which are gluten free, and many salad options. If on campus early in the morning, don\'t ' \
               'worry! They have a full breakfast menu from 7:30AM to 11:30AM. Similar to many restaurants ' \
               'with a shared kitchen, there is a chance of cross contamination of allergens.'
        
    
    elif final_choice == 'Seed + Sprout':
        return 'Our recommendation is Seed + Sprout. This newer restaurant offers fresh food with healthier ' \
               'options, loaded with vegetables and full of flavor. The \'Choose your own bowl\' style ' \
               'menu allows for flexible choices with most dietary restrictions. They also feature a great ' \
               'breakfast menu, with one of their most popular items the Loco Moco. Similar to many ' \
               'restaurants with a shared kitchen, there is a chance of cross contamination of allergens.'
        
       
    
    elif final_choice == 'Shogun':
        return 'Our recommendation is Shogun. This restaurant offers a variety of Asian cuisine, ' \
               'from chicken curry katsu to a full sushi menu with more than plenty of options to browse. ' \
               'Not only that, but it\'s a great place for entertainment with their pool tables open for ' \
               'students to use. Similar to many restaurants with a shared kitchen, there is a chance of ' \
               'cross contamination of allergens.'
        
    
    elif final_choice == 'Starbucks':
        return 'Our recommendation is Starbucks. Famous for their various drinks from coffee to tea to their ' \
               'very own Refreshers, Starbucks offers a variety of different choices. They also have a great ' \
               'bakery selection with breakfast sandwiches, cake pops, baked goods, paninis and more to ' \
               'choose from. Similar to many restaurants with a shared kitchen, there is a chance of cross ' \
               'contamination of allergens.'
        
    
    elif final_choice == 'Subway':
        return 'Our recommendation is Subway. Famous for allowing customers to customize their sandwiches, ' \
               'Subway offers several toppings, proteins, sauces and more to fit many dietary restrictions. ' \
               'They also offer sweet treats like freshly baked cookies and salty snacks such as chips to go ' \
               'with your sandwich.\nSimilar to many restaurants with a shared kitchen, there is a chance of ' \
               'cross contamination of allergens.'
        
      
    
    elif final_choice == 'Sunshine':
        return 'Our recommendation is Sunshine Market. This market is not only conveniently located in ' \
               'the center of campus but offers a variety of snacks and necessities, from chips to drinks to ' \
               'Brown Bag Sandwiches to fit everyone\'s needs.\nTheir office is also working with The Hub to ' \
               'get EBT accepted to become more accessible to the student population.'
        
       
    
    elif final_choice == 'Su Pan Bakery':
        return 'Our recommendation is Su Pan Bakery, hidden behind Burger King. This small and relatively ' \
               'new Mexican bakery offers sweet treats and filling desserts to snack on throughout the day, ' \
               'from pastries all the way to whole cakes and pies that can be purchased. With how hard you ' \
               'work, you deserve to treat yourself!'
        
    
    elif final_choice == 'Tapioca Express':
        return 'Our recommendation is Tapioca Express. Known for being the boba hotspot on campus, ' \
               'Tapioca Express, TapEx for short, offers refreshing beverages along with popular snacks ' \
               'such as popcorn chicken. Their vast drink menu offers many options to browse and even have ' \
               'specials on different days of the week! Similar to many restaurants with a shared kitchen, ' \
               'there is a chance of cross contamination of allergens.'
        
     
    
    elif final_choice == 'Croutons':
        return 'Our recommendation is Croutons. Famous for their salads, sandwiches and soups, Croutons is ' \
               'a great spot to grab lunch, especially their popular two item combo. Their hours are limited ' \
               'as they\'re open 10AM-3PM, but many options can be turned vegan or gluten free by asking to ' \
               'remove the cheese or croutons. Similar to many restaurants with a shared kitchen, there is a ' \
               'chance of cross contamination of allergens.'
        
        
    
    elif final_choice == 'Yogurt World':
        return 'Our recommendation is Yogurt World. As the on campus fro-yo spot, Yogurt World offers many ' \
               'flavors as well as topping to choose from. It makes for a great pick-me-up snack, and look out ' \
               'for their color changing spoons! Similar to many restaurants with a shared kitchen, there ' \
               'is a chance of cross contamination of allergens.'
        
        
    
    elif final_choice == 'Blue Pepper':
        return 'Our recommendation is Blue Pepper. This restaurant offers a taste of Thai food, serving many ' \
               'different foods from noodles to rice to several curries, allowing for customers to choose ' \
               'depending on what catches their eyes. They also offer many desserts, from boba to mango ' \
               'sticky rice! Similar to many restaurants with a shared kitchen, there is a chance of cross ' \
               'contamination of allergens.'
        
    
    elif final_choice == 'Soda & Swine':
        return 'Our recommendation is Soda & Swine. As the newest dining spot on campus with a beautiful ' \
               'aesthetic, it can be tricky finding seats at this packed place! Famous for their sliders, ' \
               'which have vegan options included, Soda & Swine offers a taste casual food that\'s been ' \
               'elevated. They also offer a variety of beers to choose from! Similar to many restaurants ' \
               'with a shared kitchen, there is a chance of cross contamination of allergens.'
        
    
    elif final_choice == 'Taco Villa':
        return 'Our recommendation is Taco Villa. This restaurant offers a variety of tacos, burritos and ' \
               'bowls, allowing for customers to choose flexibly. Their bowls are gluten free and the ' \
               'protein can be replaced with vegetables to make for vegetarian and vegan options and offer ' \
               'drinks such as horchata on their menu. Similar to many restaurants with a shared kitchen, ' \
               'there is a chance of cross contamination of allergens.'

