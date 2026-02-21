from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Dead():
    def __init__(self,player,hb1,death_ui,spawn_point):
        self.player = player
        self.hb1 = hb1
        self.death_ui = death_ui
        self.spawn_point = spawn_point
        self.dead = False
        self.fall_s_y = None

    # this function is common function for any demage 
    def demage(self,power):
        if self.dead:
            return
        self.hb1.value -= power
        
        if self.hb1.value <= 0:
            self.dead = True
            self.death()
    
    def update(self):

        if self.dead:
            return 

        if self.player.y < -30 and not self.dead:
            self.demage(100)

        if not self.player.grounded:
            if self.fall_s_y is None:
                self.fall_s_y = self.player.y
        else:
            if self.fall_s_y is not None:
                self.fall_demage()
                self.fall_s_y = None
        
    def fall_demage(self):
       
        safe_fall = 5
        lands_y = 2

        total_distance = self.fall_s_y - self.player.y

        if total_distance <= safe_fall:
            self.demage(0)
        
        elif total_distance >= safe_fall:
            self.demage(int(total_distance * lands_y))
            
    #control the death ui 
    def show_death_ui(self):
        self.death_ui.enabled = True
        mouse.locked = False

    def hide_death_ui(self):
        self.death_ui.enabled = False
        mouse.locked = True
        
    def death(self):
        if self.hb1.value <= 0:
            self.show_death_ui()
    
    # respawn function for player
    def respawn(self):
        self.hide_death_ui()
        self.player.position = self.spawn_point
        self.player.velocity = Vec3(0,0,0)
        self.player.rotation = (0,0,0)
        self.hb1.value = 100
        self.dead = False
 