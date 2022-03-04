Country:
- each country need to have a list of adjacent countries
- countries must contain armies at all times
    - armies need to designate the player and the amount

Continent:
- continents have countries
- if a play has all countries, they get bonus armies

Map:
- composed of countries
- keep track of how many card "turn-ins" and increment each time

Player:
- has "countries" that they possess
- has cards, if they have 3 of the same, or all different, they can turn in the cards for extra armies
- can possess continents

Card:
- card has a country (for initial country selection)
- also has a symbol (3 total), for gaining additional armies

Dice:
- attacking dice (3)
- defending dice (2)
    
Init:
- attacking player adds armies
- redeems cards if they choose to
Attack:
- chooses a country to attack with, and a country to attack
    - attacking country must have 2 armies
- roll dice, match highest with highest, middle with lowest
    - attacking: roll 1 fewer than armies with max 3 dice
    - defending: roll equal to armies with max 2 dice
- subtract an army from defender for each > than defending dice
- subtract an army from attacker for each <= defending dice
- attacker can stop the attack at any time
Success:
- if first success, win a card
- choose to move amount of armies to the new country
    - need to leave one army and have at least one army in new country
