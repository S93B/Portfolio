# Stellaris weapon simulator
The original idea of this project was to determine which weapons in the game stellaris were the 'best'.
I was specifically curious about the comparison between the XL size weapons. 
In the game the player has the choice between three types of these, each with their own unique stats and characteristics.
At first the project only had the weapon calculator and the weapon data. Target data such as hull, armor and shield points had to be input manually. 
Then I decided I would integrate ship and utility data. The data for this, however, is hidden in small .txt files, instead of a csv.
To compile the ship and utility component data I used the game's wiki page (which is constantly being updated) and ChatGPT to compile an initial excel file.
Small changes were made using excel. 
Since the game allows customization in terms of shield and armor components, I decided to divide the modules in equal parts. 
Most ships have even numbered utility component slots, a few small ships have uneven numbered slots. For those I choose for more shield components.
Something I would also do ingame.

Below I will show some of the output  

## Plots
This scatterplot shows the 'Time to kill' for all weapons that were able to destroy a battleship.
![Test](data_ttk/figure_all_ttk.png?raw=True "Time to kill")

![Test](data_ttk/figure_w_dps.png?raw=True "DPS")

sidenote voor torpedoes: damage multiplier is niet toegepast. Ingame output is daarom hoger afhankelijk van het doelwit. 

![Test](data_ttk/figure_XL_dps.png?raw=True "DPS XL weapons")
