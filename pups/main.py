from pups.items import Item
from pups.character import CharacterWithItems
from pups.character import CharacterStats as stat

player1 = CharacterWithItems(name='Vasya')
player2 = CharacterWithItems(name='Petya')


sword1 = Item('Меч Васи', stats={stat.DAMAGE: 3}, durability=100)
sword2 = Item('Меч Пети', stats={stat.DAMAGE: 1}, durability=100)

player1.set_weapon(sword1)
player2.set_weapon(sword2)

print(player1.stats())
print(player2.stats())

while player1.hp > 0 and player2.hp > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1.stats())
    print(player2.stats())