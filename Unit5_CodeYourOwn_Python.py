"""
Unit 5
Code Your Own: Unit 5
[Your Title Here]
"""

#Tuple of categories the user can pick
animals = ("Birds", "Marine Animals", "Big Cats", "Pets")


#dictionaries of facts
birds = {
    "The closets living relative of the Tyrannosaurus Rex is the chicken" : True,
    "Birds pair for life": False,
    "If humans touch a baby bird, it's mother will always abandon it": False,
    "The reason birds sing is because they are happy": False
}

marine = {
    "Octopuses can regrow their limbs if they are severed": False,
    "Whales can breathe underwater": False,
    "ClownFish are able to change their gender": True,
    "A shark's brain is the size of a walnut": False
}

big_cats = {
    "Male lions hunt with their pride": False,
    "Cheetahs don't roar": True,
    "Male Leopards help raise their young": False,
    "Lions have the most powerful bite in the world": False
}

pets = {
    "Dogs can only see in black and white": False,
    "Cats are nocturnal": False,
    "Hamsters are Herbivores": False,
    "The fastest breed of dog is the greyhound": True
    
}


### - - - Instructions for the program - - - ###
# - Ask the user which category they will pick using the animals tuple
print(animals)
user_category = input("Please pick a category you want to guess at ")
print()
print("Here are three myths and one fact.")
number = 1


### - - - Compare user input with dictionaries - - - ###

#If the user wants birds unpack birds.items into fact and answer
if user_category == "birds" or user_category == "Birds":
    for fact, answer in list(birds.items()):
        print(str(number) + ") " + fact)
        number += 1
        
#Make a list for the values of birds and compare it to the user's answers   
    bird_list = list(birds.values())
    print()
    user_answer = int(input("Which one is the fact (1, 2, 3, or 4): "))
    user_answer_value = bird_list[user_answer - 1]
    print("You chose choice number " + str(user_answer))
   
    if user_answer_value == True:
        answer_correct = True          
    else:
        answer_correct = False
        
    
    
#If the user wants marine animals unpack marine.items into fact and answer        
elif user_category == "marine animals" or user_category == "Marine Animals":
    for fact, answer in list(marine.items()):
        print(str(number) + ") " + fact)
        number += 1 

#Make a list for the values of marine animals and compare it to the user's answers         
    marine_list = list(marine.values())
    print()
    user_answer = int(input("Which one is the fact (1, 2, 3, or 4): "))
    user_answer_value = marine_list[user_answer - 1]
    print("You chose choice number " + str(user_answer))
    
    if user_answer_value == True:
        answer_correct = True          
    else:
        answer_correct = False
        
        
#If the user wants big cats unpack big_cats.items into fact and answer        
elif user_category == "big cats" or user_category == "Big Cats":
    for fact, answer in list(big_cats.items()):
        print(str(number) + ") " + fact)
        number += 1

#Make a list for the values of big cats and compare it to the user's answers        
    big_cats_list = list(big_cats.values())
    print()
    user_answer = int(input("Which one is the fact (1, 2, 3, or 4): "))
    user_answer_value = big_cats_list[user_answer - 1]
    print("You chose choice number " + str(user_answer))
    
    if user_answer_value == True:
        answer_correct = True          
    else:
        answer_correct = False
        
        
#If the user answers anything else unpack pets.items into fact and answer         
else:
    for fact, answer in list(pets.items()):
        print(str(number) + ") " + fact)
        number += 1  

#Make a list for the values of pets and compare it to the user's answers        
    pets_list = list(pets.values())
    print()
    user_answer = int(input("Which one is the fact (1, 2, 3, or 4): "))
    user_answer_value = pets_list[user_answer - 1]
    print("You chose choice number " + str(user_answer))
    
    if user_answer_value == True:
        answer_correct = True          
    else:
        answer_correct = False
        
        
# if the answer is correct, display congrats statement
# if the answer is incorrect, display sorry statement
print()

if answer_correct:
    print("Congrats!! You guessed correctly")

if not answer_correct:
   print("Sorry, that was the wrong answer. Run the program again to get a second chance") 



