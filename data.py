#data mapping(i dont actually now how this should be made)
#also unfinished!! just ignore this file

from main import MovingMachine

class mapped_data:
    def __init__(self, initial_speed=0):
        self.speed = initial_speed 
    


def dchange():
    
    mapped_

def manualchange():
    machine = MovingMachine()  # Create an instance of MovingMachine
    while True:
        command = input("status/speed/direction/stop/quit")
        if command == "speed":
            speed = float(input("Enter new speed: "))
            machine.set_speed(speed)
        elif command == "direction":
            direction = float(input("Enter new direction: "))
            machine.change_direction(direction)
        elif command == "stop":
            machine.stop_moving()
        elif command == "status":
            machine.status()
        elif command == "quit":
            break
        else:
            print("Invalid command")
        machine.status()
