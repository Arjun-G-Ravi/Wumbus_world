from random import choice
class Room:
    def __init__(self, idx, idy):
        self.idx = idx
        self.idy = idy
        self.stench = False
        self.breeze = False
        self.pit = False
        self.Wumbus = False
        self.id = self.idx + 4 * self.idy 

    def __repr__(self):
        return f'Room No:{self.id}'

        
        
class Wumbus_world:
    def __init__(self, size):
        self.size = size
        self.create_world()   
        self.player_index_x = 0
        self.player_index_y = 0
        self.player_pos = (self.player_index_x, self.player_index_y)
        self.player_alive = True 
    
    def create_world(self):
        self.board = [[Room(i,j) for i in range(self.size)] for j in range(self.size)]
        all_rooms = [element for sublist in self.board for element in sublist]
        print(all_rooms)
        self.num_Wumbus = 1
        self.num_pits = self.size//2
        self.num_gold = 1
        self.gold_room = choice(all_rooms) 
        all_rooms.remove(self.gold_room) 
        self.Wumbus_room = choice(all_rooms)
        # This wont work. Have to do some logic to actually define how to put the pits and the Wumbus. Will come back after I get the logic
         
    def play_move(self,move):
        if move == 'u':
            new_player_index = (self.player_index_x, self.player_index_y+1)
        elif move == 'd':
            new_player_index = (self.player_index_x, self.player_index_y-1)
        elif move == 'l':
            new_player_index = (self.player_index_x-1, self.player_index_y)
        elif move == 'r':
            print('Moved Right')
            new_player_index = (self.player_index_x+1, self.player_index_y)    
        else:
            raise Exception("ILLEGAL MOVE")
        
        if self.size in new_player_index:
            print("Wall there")
            return False
        else:
            self.player_index_x, self.player_index_y = new_player_index
            self.player_pos = new_player_index
            print('Updated player pos')
            return True
    
    def detect_room(self):
        room = self.board[self.player_index_x][self.player_index_y]
        if room.stench:
            print("This room has a stench")
        if room.breeze:
            print("This room has a breeze.")
        if room.pit:
            print("This room has a pit. You fall into the pit. You die.")
            self.player_alive = False
        if room.Wumbus:
            print("This room has a Wumbus. You are eaten alive by the Wumbus.")
            self.player_alive = False

    def display(self):
        for i in range(self.size):
             print(self.board[i])
        
        
        
        
if __name__ == '__main__':
    w = Wumbus_world(3)

    w.display()