# python_game

The goal of this project is to make a working game using python code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Requirements

You only need one python programming software to start with this project.

```
Thonny or PyCharm
```

### Installing

To start with this project I would reccomend begin writing base game.

```
For example you could use def run_game(): anf afterwards start adding imports

import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from ship import Ship
import game_functions as gf

def run_game():

and so on...
```

If you have finished writing code for base game you should start with game functions.

```
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Check key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()
        
        and so on...
```

For next step it is important to start adding stats and a scoreboard to the game.

```
class GameStats():
    """game stats"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()
        
        and so on...
```

You also need settings for your game to define you bullet speed etc.

```
class Settings:
    """class to store all settings for example game"""

    def __init__(self):
        """initialize the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (20,20,69)
        # ship settings
        self.ship_limit = 3
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
        # aliens settings
        self.fleet_drop_speed = 5
        # speed up factor
        self.speedup_scale = 1.1
        self.init_dynamic_settings()
        
        and so on...
```
And for last the aliens and ship you will be playing with.

```
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for alien description"""
    def __init__(self, game_settings, screen):
        """Create alien object and define its start position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # load alien image and set rect atribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # set aliens position
        self.x = float(self.rect.x)
        
        and so on...
```

## Running the tests

To start the game you will need to press run code and if everything is done correctly the gamme should start

### Break down into end to end tests

If you have problem starting the code then everything must be checked again for the reason that it is really easy to not notice the mistakes you have done.

## Built With

* https://www.jetbrains.com/pycharm/

## Contributing

My code is found at https://github.com/BluBack/python_game.

## Versioning

I use PyCharm 2021.3 for this project.
## Authors

* **Kristo Kangro** - *Anna Karutina* - [AnnaKarutina](https://github.com/AnnaKarutina)

## License

This project is not licensed.

## Acknowledgments

* Hat tip to https://github.com/AnnaKarutina
