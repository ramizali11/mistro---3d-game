from ursina import *
class Gun:
    # this function control the gun animation, model, and texture
    def shoot(self):
        global gun
        gun = Entity(
            parent=camera,
            model='assets\\pubg-mobile-ak47\\source\\Akm.fbx',
            texture= "assets\\pubg-mobile-ak47\\textures\\body.png",
            position=(0.5, -1.5, 0.5),
            scale=(0.04, 0.04, 0.04),
            rotation=(0, 90, 0),
        )

        gun.rotation = (90, 90, 0)

        gun.animate_rotation(
            Vec3(0, 0, 0),  
            duration=0.1,   
            curve=curve.linear 
        )

    def input(self, key):
        global gun
        if key == 'left mouse down':    
            gun.position = (0.5, -1.6, 0.6)
        else:
            gun.position = (0.5, -1.5, 0.5) 


