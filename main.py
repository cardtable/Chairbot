class MovingMachine:
    def __init__(self):
        self.direction = 0 
        self.speed = 0  
        self.moving = False  

    def set_speed(self, speed):
        "Set the speed"
        if speed < 0:
            print("invalid speed")
        else:
            self.speed = speed
            if self.speed > 0:
                self.start_moving()
            else:
                self.stop_moving()
            print(self.speed)

    def change_direction(self, angle):
        "chaning direction"
        self.direction = (self.direction + angle) % 360
        print(self.direction)

    def start_moving(self):
        "start"
        if not self.moving:
            self.moving = True

    def stop_moving(self):
        "Stop the machine"
        if self.moving:
            self.moving = False
            print("Machine halted")

    def status(self):
        if self.moving:
            movement = "moving"
        else:
            movement = "halted"
        print(f"Current direction: {self.direction} degrees, Speed: {self.speed} m/s, Status: {movement}.")

