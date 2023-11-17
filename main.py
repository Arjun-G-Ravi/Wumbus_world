from classes import Wumbus_world, Room
print("This is a Wumbus game. Choose the player's move to navigate around the map. If you fall into a pit, or gets eaten by Wumbus, you die. If you find the gold, and return back to starting position, you win")

size = int(input("Enter the size of the Wumbus world you want."))
world = Wumbus_world(size)

while world.player_alive:
    move = input("Play a move [u, d, l, r]:")
    world.play_move(move)
    world.detect_room()