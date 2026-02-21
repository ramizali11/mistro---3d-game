from ursina import *

class Map:
    def __init__(self):
        self.ground_blocks = []
    
    # generate the ground
    def generate(self):
        block = Entity(
            model='plane',
            collider = 'mesh',
            texture='grass.png',
            position=(10, 0, 10),
            origin_y=0.5,
            scale=(21, 0, 21)

        )

