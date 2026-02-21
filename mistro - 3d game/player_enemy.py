from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# this class amange the enemy 
class Enemy(Entity):
    def __init__(self, position,player, dead_system):
        self.player = player
        super().__init__(
            parent = scene,
            model = 'zombie.glb',
            scale  = 0.02,
            collider='box',
            position = position,
            rotation_y = 180 
        )
        self.hp = 100
        self.maxhp = 100
        self.bar = Entity(parent=self, model='quad', color=color.lime, scale=(0.5, 0.05,1), position=(0, 2, 0.01))
        self.dead_system = dead_system
        self.attack_cooldown = 1.5
        self.last_attack_time = 0


    # this functuion is for enemy demage from the gun and to repawn after died
    def demage(self, amount):
        self.hp -= amount
        print(f"Enemy HP: {self.hp}")
        if self.hp <= 0:
            print("Enemy died!")
            self.position = (random.randint(0, 20), 1, random.randint(0, 20))
            self.hp = 100
        else:
            self.bar.scale_x = 0.5 * (self.hp / self.maxhp)
            if self.hp / self.maxhp < 0.3:
                self.bar.color = color.red

    # this function is for enemy behavior, movement and attack
    def update(self):
        self.speed = 0.5
       
        direction = self.player.position - self.position
        direction.y = 0
    
        if distance(self.position, self.player.position) < 2:
            if time.time() - self.last_attack_time > self.attack_cooldown:
                self.last_attack_time = time.time()
                self.dead_system.demage(10)

        self.position += direction.normalized() * self.speed * time.dt

        ground_hit = raycast(self.position + Vec3(0, 5, 0), Vec3(0, -1, 0), distance=10, ignore=[self])
        if ground_hit.hit:
            self.y = ground_hit.world_point.y

        target = Vec3(self.player.x, self.y, self.player.z)
        self.look_at(target)
        self.rotation_y += 180  
        self.rotation_x = 0
        self.rotation_z = 0

        if direction.length() > 0.5:
            self.y = sin(time.time() * 5) * 0.02

     

    def input(self, key):
        if key == 'left mouse down':
            hit_info = raycast(camera.world_position,camera.forward)
            if hit_info.hit:
                    self.demage(15)