from ursina import *
# the main reason of this class is to create the world and load it 
class Inventory:
    def __init__(self, player, boxes, current_texture):
        self.player = player
        self.boxes = boxes
        self.current_texture = current_texture

    def input(self, key):
        # Quit application
        if key == 'escape':
            application.quit()

        # this all code for development

    #     if key == '1':
    #         self.current_texture = "grass.png"
    #     elif key == '2':
    #         self.current_texture = "stone.png"
    #     elif key == '3':
    #         self.current_texture = "brick.png"
    #     elif key == '4':
    #         self.current_texture = "simplebrick.png"
    #     elif key == '5':
    #         self.current_texture = "wood.png"


    #     # Raycast for placing/removing blocks
    #     hit = raycast(
    #         camera.world_position,
    #         camera.forward,
    #         distance=8,
    #         ignore=[self.player]
    #     )

    #     # Place block
    #     if hit.hit and key == 'left mouse down' and hit.entity:
    #         pos = hit.entity.position + hit.normal
    #         new_block = Entity(
    #             model='cube',
    #             texture=self.current_texture,
    #             position=pos,
    #             origin_y=0.5,
    #             collider='box'
    #         )
    #         new_block.texture_name = self.current_texture
    #         self.boxes.append(new_block)

    #     # Remove block
    #     elif hit.hit and key == 'right mouse down' and hit.entity in self.boxes:
    #         self.boxes.remove(hit.entity)
    #         destroy(hit.entity)

    #     # Save map
    #     if key == 's':
    #         self.save_map()

    # def save_map(self):
    #     with open('map.txt', 'w') as f:
    #         for box in self.boxes:
    #             x, y, z = box.position
    #             texture = getattr(box, "texture_name", "grass.png")
    #             f.write(f"{x},{y},{z},{texture}\n")
    #     print("Map saved.")


    # Load map from file
    def load_map(self):
        for box in self.boxes:
            destroy(box)
        self.boxes.clear()

        try:
            with open('map.txt', 'r') as f:
                for line in f:
                    x, y, z, tex = line.strip().split(',')
                    pos = Vec3(float(x), float(y), float(z))
                    block = Entity(
                        model='cube',
                        texture=tex,
                        position=pos,
                        collider='box' if distance(self.player.position,pos) < 15 else None,
                        origin_y=0.5,
                        static = True
                    )
                    block.texture_name = tex
                    self.boxes.append(block)
            print("Map loaded.")
        except FileNotFoundError:
            print("No saved map found.")
