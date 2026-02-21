from ursina import *
from ursina import Ursina, window
from ursina.prefabs.first_person_controller import FirstPersonController
# for health bar
from ursina.prefabs.health_bar import HealthBar
# calculate player damage and make player dead
from player_dead import Dead
# manage night and day time
# from player_time import Time
# game map
from map import Map
# have inventory and pickup/drop function
from player_inventory import Inventory
from  player_guns import Gun
from player_enemy import Enemy




app = Ursina()

#intilize the gun system
gun_system = Gun()
gun_system.shoot()

# player properties
player = FirstPersonController(2)
player.position = (10, 0, 10)
player.height = 2
player.speed = 5
player.gravity = 1
player.cursor.visible = True
player.camera_pivot.y = 1.8
player.max_distance = 1.8

# game properties
window.fps_counter.enabled = True
sun = DirectionalLight()
sun.shadow = False
sun.enabled = False
Texture.default_filtering = None
window.vsync = False
mouse.sensitivity = Vec2(40, 40)
application.target_fps = 120
camera.clip_plane_far = 20

# health bar
hb1 = HealthBar(bar_color=color.lime, roundness=0.5, scale=(0.5, 0.025))

# death UI
death_ui = Entity(parent=camera.ui, enabled=False)

# spawn point
spawn_point = (10, 0, 10)

# textures and block
current_texture = "grass.png"
boxes = []

# initializing the modules
dead_system = Dead(player, hb1, death_ui, spawn_point)
map_system = Map()
inventory_system = Inventory(player=player, boxes = boxes, current_texture=current_texture)
map_system.generate()
enemy_system = Enemy(position=(15, 0, 15),player = player,dead_system=dead_system)

def input(key):
    inventory_system.input(key)
    gun_system.input(key)
    enemy_system.input(key)

def update():
    dead_system.update()
    enemy_system.update()

# death ui
Text(
    parent=death_ui,
    text='YOU DIED',
    scale=2,
    origin=(0, 0),
    y=0.1,
    color=color.red
)

Button(
    parent=death_ui,
    text='Respawn',
    scale=(0.2, 0.07),
    y=-0.1,
    collider='box',
    on_click=dead_system.respawn
)

# load the map 
inventory_system.load_map()

app.run()
