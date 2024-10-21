# my Mad Libs Game


# Collecting user inputs
name = input("Enter your name: ")
game = input("Enter your favorite game: ")
favorite_bike = input("Enter your favorite bike name: ")
dream = input("Enter your dream: ")
best_friend = input("Enter your best friend's name: ")
favorite_country = input("Enter your favorite country: ")
favorite_cricketer = input("Enter your favorite cricketer: ")
where_you_live = input("Where do you live? ")

# Creating the story
story = f"""Once upon a time, {name} was playing {game} with their best friend, {best_friend}. 
            During the game, {name} dreamed of riding their favorite bike, the {favorite_bike}, 
            across the beautiful landscapes of {favorite_country}. 
            Suddenly, they spotted their favorite cricketer, {favorite_cricketer}, nearby! 
            Excited, {name} ran to meet {favorite_cricketer} and share their dream of becoming a great player. 
            They talked about cricket and the amazing places to ride bikes, like {where_you_live}. 
            It was a day full of adventure and inspiration!"""


# Running the Mad Libs game

print("\nHere's your Mad Libs story:")
print(story)
