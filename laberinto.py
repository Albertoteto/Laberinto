class Game:
    def __init__(self):
        self.maze = None

    def createDoor(self, side1,side2):
        door=Door()
        door.side1=side1
        door.side2=side2
        return Door()

    def createRoom(self, id):
        return Room(id)
    
    def createMaze(self):
        return Maze()

    def make2RommsMaze(self):
        self.maze = Maze()
        room1=Room(1)
        room2=Room(2)
        self.maze.add_room(room1)   
        self.maze.add_room(room2)   

        door=Door(room1,room2)  
        room1.sur=door
        room2.norte=door
        return self.maze    
    
    def make2RommsMazeFM(self):
        maze = self.createMazemaze()
        room1=Room(1)
        room2=Room(2)
        self.maze.add_room(room1)   
        self.maze.add_room(room2)   

        door=Door(room1,room2)  
        room1.sur=door
        room2.norte=door
        return self.maze    

class ElementoMapa:
    def __init__(self, nombre):
        self.nombre = nombre

class Maze(ElementoMapa):
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_door(self, door):
        self.doors[0].append(door)

class Room(ElementoMapa):
   def __init__(self, id):
        
        self.id=id
        self.norte= Wall()
        self.sur= Wall()
        self.este= Wall()
        self.oeste= Wall()
        


       
class Door(ElementoMapa):
    def __init__(self, side1, side2):
        self.side1 = side1 
        self.side2 = side2
        self.opened = False
    
    def entrar(self):
        if self.opened:
            print("Pasaste por la puerta")
        else:
            print("La puerta está cerrada")
    
class Wall(ElementoMapa):
    def __init__(self):
        pass
    def entrar(self):
        print("No puedes pasar")



game=Game()
game.make2RommsMaze()
game.maze.entrar()