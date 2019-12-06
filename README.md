# Hot Air Adventure

Hot air balloon adventure game created with Python and Arcade.

About:

This game consists of three levels, and challenges users to navigate a hot air balloon over buildings and collect 25 coins within a time frame of 1 minute.
The user progresses to the next level if 25 coins are collected in less than a minute. 
The buildings slowly move upwards, and the coins rotate and fall from the sky at random intervals. The scope of the challenge increases as the user progresses through the levels.
Each level corresponds to a different time of day, and the background changes accordingly. For each coin that the user collects, the score increases by 1 point. 
For each building that the user collides with, the score decreases by 5 points. 


Demo video: 


https://www.youtube.com/watch?v=B1yPDLrryMc&feature=youtu.be



Installation:
```
> pip install -r requirements.txt
```
```
> python maingame.py
```
Instructions:

The user should use the arrow keys to move the balloon toward the coins while avoiding collision with surrounding buildings.
The objective of each level is to collect 25 coins in less than 1 minute. The screen scrolls to the right as the user progresses through the level.

Author:

Swetha Sankar: swetha@udel.edu

Acknowledgments:

Sounds: 
Background music and sound effects from freesounds.org. Level 1/2/3 themes from @mativve and "Level Up" sound effect from @dersuperanton. 

Images: 
Background images created with canva.com.

Coin image from https://dlpng.com/png/185509. 

Trophy image from https://www.hiclipart.com/search?clipart=prize. 

Balloon from https://www.clipartmax.com/middle/m2i8H7H7N4A0Z5A0_0-hot-air-balloon-png-rainbow-color/. 

Crown image from https://carlisletheacarlisletheatre.org/pin/crown-clip-art-golden/. 

References:

Used Dr.Bart's Arcade Activities as a point of reference: https://github.com/swetha-sankar/ArcadeActivities

Arcade Academy Tutorials:

Scrolling Screen: http://arcade.academy/examples/sprite_move_scrolling.html?highlight=scroll

On Screen Timer: http://arcade.academy/examples/timer.html?highlight=timer

Levels: http://arcade.academy/examples/sprite_collect_coins_diff_levels.html?highlight=level

Views: http://arcade.academy/examples/view_screens_minimal.html?highlight=views

Sprite Properties: http://arcade.academy/examples/sprite_collect_coins_move_down.html#sprite-collect-coins-move-down

Asteroid Smasher: http://arcade.academy/examples/asteroid_smasher.html#asteroid-smasher