from food_module.py import *

def test_food_input():
    
    #To see if what the user inputs as their food_type runs through the method.
    
    food_choice = food_type('snack')
    
    assert food_choice == user_input
    
def test_dietary_restriction():
    
    #To check if the user input of dietary_restriction works when run through the method.
    
    cannot_eat = dietary_restriction('peanut allergy')
    
    assert cannot_eat == user_input 
    