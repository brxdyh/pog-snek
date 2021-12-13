#CISC108 Project 12 - Fall 2021
#Brady Hatch (brxdyh@udel.edu)
#Snake Game
from designer import *
import random

set_window_color('red')

"""
The world dictionary adds the different objects and parameters
the code needs to run
"""
World = {
    'snake': DesignerObject,
    'snake speed': int,
    'direction': str,
    'food': DesignerObject,
    'bodies': [DesignerObject],
    'tail': DesignerObject,
    'message': DesignerObject,
    'score': int,
    'deathscreen': DesignerObject
    }

def create_world() -> World:
    """
    This creates the world with all of the designer objects
    and their parameters.
    
    Args: None
    
    Returns:
        the game World
    """
    return {
        'snake': create_snake(),
        'snake speed': 10,
        'direction': 'right',
        'food': spawn_food(),
        'bodies': [],
        'message': text("black", "Score:", 30, 60, 30),
        'score': 0
        }

def create_snake() -> DesignerObject:
    """
    Creates the snake with a saved image, scales it to a proper size, then
    returns it as a DesignerObject.
    
    Args: None
    
    Returns:
        DesignerObject
    """
    snake = image("snake_head.png")
    snake['scale'] = 0.13
    return snake

def spawn_food() -> DesignerObject:
    """
    Defines the food to allow it the png image to be displayed in the
    world window, returned as a DesignerObject
    
    Args: None
    
    Returns:
        DesignerObject"""
    food = image("mango.png")
    food['scale'] = 0.09
    food['x'] = random.randint(0, 800)
    food['y'] = random.randint(0, 600)
    return food

def random_food(world: World):
    """
    This function assigns the current food x and y values
    to new random ones, with the x being random between 0-800 ('the
    window width') and y being random between 0-600 ('the window height')
    
    Args:
        World(dict)
        
    Returns: None
    """
    world['food']['x'] = random.randint(0, 800)
    world['food']['y'] = random.randint(0, 600)
    
def create_body() -> DesignerObject:
    """
    Creates the body segment DesignerObject, a green rectangle
    with a width of 35px and height of 30px
    
    Args: None
    
    Returns:
        DesignerObject
    """
    return rectangle('green', 35, 30)

def respawn_food_and_add_body(world: World):
    """
    This function checks that if the snake is colliding with food,
    then to run the random_food function, moving the food to a random location, and
    to add a ner body segment DesignerObject to the world
    
    Args:
        World(dict)
    
    Returns: None
    """
    if colliding(world['snake'], world['food']) == True:
        random_food(world)
        new_part = create_body()
        world['bodies'].append(new_part)
        world['score'] = world['score'] + 1
        
def move_snake(world: World):
    """
    Whatever direction the snake head is facing, controlled
    by the user, the snake will start moving towards
    
    Args:
        World(dict)
    
    Returns: None
    """
    if world['direction'] == 'left':
        head_left(world)
    elif world['direction'] == 'right':
        head_right(world)
    elif world['direction'] == 'up':
        head_up(world)
    elif world['direction'] == 'down':
        head_down(world)
        
def move_body(world: World, bodies: [DesignerObject]):
    """
    Stores the snake head x and y value in order to pass it onto every new body
    segment, and assign it's values to those stored values.
    
    Args:
        World(dict)
        bodies (a list of designer objects)
    
    Returns: None
    """
    old_x = world['snake']['x']
    old_y = world['snake']['y']
    for body in world['bodies']:
        current_x = body['x']
        current_y = body['y']
        body['x'] = old_x
        body['y'] = old_y
        old_x = current_x
        old_y = current_y
       
def head_left(world: World):
    """
    Allows the snake to move left, and flips the image
    to the proper direction
    
    Args:
        World (dict)
    
    Returns: None
    """
    world['snake']['x'] -= world['snake speed']
    world['snake']['angle'] = 180
    
def head_right(world: World):
    """
    Allows the snake to move right, and flips the image
    to the proper direction
    
    Args:
        World(dict)
        
    Returns: None
    """
    world['snake']['x'] += world['snake speed']
    world['snake']['angle'] = 0
    
def head_up(world: World):
    """
    Allows the snake to move up and flips the image to
    the proper direction
    
    Args: World(dict)
    
    Returns: None
    """
    world['snake']['y'] -= world['snake speed']
    world['snake']['angle'] = 90
    
def head_down(world: World):
    """
    Allows the snake to move down and flips the image to
    the proper direction
    
    Args:
        World (dict)
        
    Returns: None
    """
    world['snake']['y'] += world['snake speed']
    world['snake']['angle'] = 270

###ALL OF THESE BOUNCE FUNCTIONS MAKE THE SNAKE BOUNCE THE OPPOSITE WAY
###WHEN IT HITS ANY OF THE 4 SIDES OF THE WINDOW
def bounce_left(world: World):
    if world['snake']['x'] > get_width():
        world['direction'] = 'left'
        
def bounce_right(world: World):
    if world['snake']['x'] < 0:
        world['direction'] = 'right'
        
def bounce_up(world: World):
    if world['snake']['y'] > get_height():
        world['direction'] = 'up'
        
def bounce_down(world: World):
    if world['snake']['y'] < 0:
        world['direction'] = 'down'
    
def control_snake(world: World, key: str):
    """
    Whatever the user inputs, is what the direction of the snake
    head is schanged to, cuasing it to change direction
    
    Args:
        World (dict)
        key (str): the key the user presses as an input
        
    Returns: None
    """
    if key == 'left' or key == 'A':
        world['direction'] = 'left'
    elif key == 'right' or key == 'D':
        world['direction'] = 'right'
    elif key == 'up' or key =='W':
        world['direction'] = 'up'
    elif key == 'down' or key == 'S':
        world['direction'] = 'down'

def score_count(world: World):
    """
    The score count that is displayed in the game window, updating when
    a point is scored.
    
    Args:
        World (dict)
        
    Returns: None
    """
    score = world['score']
    world['message']['text'] = "Score: " + str(score)
    
def add_score(world: World):
    """
    Adds 1 point to the world 'score' when the snake collides with food.
    
    Args:
        World (dict)
        
    Returns: None
    """
    if colliding(world['snake'], world['food']) == True:
        world['score'] += 1
               
def create_deathscreen() -> DesignerObject:
    """
    An image to be shown on death in game.
    
    Args: None
    
    Returns:
        DesignerObject
    """
    screen = image("over.png")
    return screen
        
def game_over(world: World):
    """
    Ends the game when the snake collides with any 4 sides of the window, or
    runs into itself.
    
    Args:
        World(dict)
        
    Returns: None
    """ 
    if world['snake']['x'] > get_width():
        pause()
    elif world['snake']['y'] > get_height():
        pause()
    elif world['snake']['x'] < 0:
        pause()
    elif world['snake']['y'] < 0:
        pause()
    for body in world['bodies'][12:]:
        if colliding(world['snake'], body) == True:
            pause()

"""
All of the 'when' statements allow functions to run when certain
things are happening, including starting and updating.
"""
when('starting', create_world)
when('updating', move_snake)
when('updating', bounce_left)
when('updating', bounce_right)
when('updating', bounce_up)
when('updating', bounce_down)
when('updating', respawn_food_and_add_body)
when('updating', move_body)
when('updating', score_count)
when('updating', game_over)
when('typing', control_snake)
when('typing', add_score)

#start it up!
start()