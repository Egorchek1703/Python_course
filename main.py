# Classes
from hero import *

first_hero = Heroes('Aracul', 1, 'witch', 125)
first_hero.increase_lvl()
first_hero.show_hero_desc() 
"""
Aracul is a witch and has:
        level: 1
        power: 125
"""

first_hero.health = 33      # Менее предпочтительный способ
first_hero.set_new_health(35)  # Более предпочтительный способ
print( "New health is " + str(first_hero.health) )

# ================= Orcs ===================
first_orc = Orcs("Orgun", 1, "Orc-warrior", 140, 5)
first_orc.show_hero_desc()
print( str(first_orc.armor_lvl) )

first_orc.show_hero_desc()