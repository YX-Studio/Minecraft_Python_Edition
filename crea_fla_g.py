# Version 1.0.0.50
# By YXStudio 2023~2025.
# Feb.22nd,2025


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import math


app = Ursina()


grass_texture      = load_texture('assets/textures/blocks/grass_block.png')
stone_texture      = load_texture('assets/textures/blocks/stone_block.png')
brick_texture      = load_texture('assets/textures/blocks/brick_block.png')
dirt_texture       = load_texture('assets/textures/blocks/dirt_block.png')
wood_texture       = load_texture('assets/textures/blocks/wood_block.png')
diamond_texture    = load_texture('assets/textures/blocks/diamond_block.png')
bedrock_texture    = load_texture('assets/textures/blocks/bedrock_block.png')
tree_texture       = load_texture('assets/textures/blocks/tree_block.png')
leaves_texture     = load_texture('assets/textures/blocks/leaves_block.png')
sand_texture       = load_texture('assets/textures/blocks/sand_block.png')
glass_texture      = load_texture('assets/textures/blocks/glass_block.png')

barrier_texture    = load_texture('assets/textures/blocks/barrier_block.png')

inv_texture        = load_texture('assets/textures/inventorys/inventory.png')
inv1_texture       = load_texture('assets/textures/inventorys/inventory1.png')
inv2_texture       = load_texture('assets/textures/inventorys/inventory2.png')
inv3_texture       = load_texture('assets/textures/inventorys/inventory3.png')
inv4_texture       = load_texture('assets/textures/inventorys/inventory4.png')
inv5_texture       = load_texture('assets/textures/inventorys/inventory5.png')
inv6_texture       = load_texture('assets/textures/inventorys/inventory6.png')
inv7_texture       = load_texture('assets/textures/inventorys/inventory7.png')
inv8_texture       = load_texture('assets/textures/inventorys/inventory8.png')
inv9_texture       = load_texture('assets/textures/inventorys/inventory9.png')
inv11_texture      = load_texture('assets/textures/inventorys/inventory11.png')
inv12_texture      = load_texture('assets/textures/inventorys/inventory12.png')

arm_texture        = load_texture('assets/textures/arm/arm_texture.png')

sky_noon_texture   = load_texture('assets/textures/sky/skybox_noon.png')
sky_noon1_texture  = load_texture('assets/textures/sky/skybox_noon1.png')
sky_night_texture  = load_texture('assets/textures/sky/skybox_night.png')
sky_night1_texture = load_texture('assets/textures/sky/skybox_night1.png')
sky_night2_texture = load_texture('assets/textures/sky/skybox_night2.png')

sun_texture        = load_texture('assets/textures/sun/sun.png')

sight_texture      = load_texture('assets/textures/sight/sight.png')

punch_sound        = Audio('assets/sounds/punch_sound.m4a',loop=False,autoplay=False)

window.fps_counter.enabled = True
window.exit_button.visible = False

block_pick = 1
sun_angle = 0
sun_move = 0


def input(key):
    global player, scene
    if key == 'escape':
        quit()


class Block(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/blends/block/block',
            texture = texture,
            color = color.rgb(1,1,1),
            highlight_color = color.rgb(1.1,1.1,1.1),
            origin_y = 0.5,
            scale = 0.5
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                if block_pick == 1:
                    Block(position = self.position+mouse.normal,texture=grass_texture)
                if block_pick == 2:
                    Block(position = self.position+mouse.normal,texture=stone_texture)
                if block_pick == 3:
                    Block(position = self.position+mouse.normal,texture=brick_texture)
                if block_pick == 4:
                    Block(position = self.position+mouse.normal,texture=dirt_texture)
                if block_pick == 5:
                    Block(position = self.position+mouse.normal,texture=wood_texture)
                if block_pick == 6:
                    Block(position = self.position+mouse.normal,texture=diamond_texture)
                if block_pick == 7:
                    Block(position = self.position+mouse.normal,texture=tree_texture)
                if block_pick == 8:
                    Block(position = self.position+mouse.normal,texture=leaves_texture)
                if block_pick == 9:
                    Block(position = self.position+mouse.normal,texture=bedrock_texture)
                if block_pick == 11:
                    Block(position=self.position+mouse.normal,texture=sand_texture)
                if block_pick == 12:
                    Block(position=self.position+mouse.normal,texture=glass_texture)
                
            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)

class Barrier(Entity):
    def __init__(self,position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/blends/block/block',
            texture = barrier_texture,
            color = color.rgb(1,1,1),
            origin_y = 0.5,
            scale = 0.5,
            collider = 'box'
        )

class Inventory(Entity):
    def __init__(self,texture=inv1_texture):
        super().__init__(
            parent = camera.ui,
            position = Vec2(0,-0.425),
            model = 'quad',
            texture = texture,
            scale = (0.654,0.08)
            
        )
inventory = Inventory()

class Sun(Entity):
    def __init__(self,height=0,weight=50,angle=0):
        super().__init__(
            parent = scene,
            rotation = (-angle,0,0),
            position = (6,height+6,weight+6),
            model = 'quad',
            texture = sun_texture,
            scale = 7
        )
sun = Sun()
                
class Sky(Entity):
    def __init__(self,texture=sky_noon_texture):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = texture,
            scale = 150,
            double_sided = True
        )
sky = Sky()

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.9,-0.7),
            model = 'assets/blends/arm/arm',
            texture = arm_texture,
            scale = 0.2,
        )
                
    def active(self):
        self.position = Vec2(0.7,-0.6)
                
    def passive(self):
        self.position = Vec2(0.9,-0.7)
hand = Hand()

class Sight(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            position = Vec2(0,0),
            model = 'quad',
            texture = sight_texture,
            color = color.color(0,1,0,0.5),
            scale = (0.035,0.035)
        )
Sight()


def creat_world():
    rand_1tree_z = random.randint(3,9)
    rand_1tree_x = random.randint(3,9)

    rand_2tree_z = 1
    rand_2tree_x = 11

    rand_3tree_z = 11
    rand_3tree_x = 1

    for z in range(13):
        for x in range(13):
            if rand_1tree_z == z and rand_1tree_x == x:
                Block(position=(x  ,1,z)  ,texture=tree_texture)
                Block(position=(x  ,2,z)  ,texture=tree_texture)
                Block(position=(x  ,3,z)  ,texture=tree_texture)
                Block(position=(x-1,3,z-1),texture=leaves_texture)
                Block(position=(x-1,3,z)  ,texture=leaves_texture)
                Block(position=(x-1,3,z+1),texture=leaves_texture)
                Block(position=(x  ,3,z-1),texture=leaves_texture)
                Block(position=(x  ,3,z+1),texture=leaves_texture)
                Block(position=(x+1,3,z-1),texture=leaves_texture)
                Block(position=(x+1,3,z)  ,texture=leaves_texture)
                Block(position=(x+1,3,z+1),texture=leaves_texture)
                Block(position=(x-1,4,z-1),texture=leaves_texture)
                Block(position=(x-1,4,z)  ,texture=leaves_texture)
                Block(position=(x-1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,4,z-1),texture=leaves_texture)
                Block(position=(x  ,4,z)  ,texture=leaves_texture)
                Block(position=(x  ,4,z+1),texture=leaves_texture)
                Block(position=(x+1,4,z-1),texture=leaves_texture)
                Block(position=(x+1,4,z)  ,texture=leaves_texture)
                Block(position=(x+1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,5,z)  ,texture=leaves_texture)

                Block(position=(x,0,z),texture=dirt_texture)
                Block(position=(x,-1,z),texture=dirt_texture)
                Block(position=(x,-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,-3,z),texture=stone_texture)
                
                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-4,z),texture=diamond_texture)
                else:
                    Block(position=(x,-4,z),texture=stone_texture)
                
                Block(position=(x,-5,z),texture=bedrock_texture)
            elif rand_2tree_z == z and rand_2tree_x == x:
                Block(position=(x  ,1,z)  ,texture=tree_texture)
                Block(position=(x  ,2,z)  ,texture=tree_texture)
                Block(position=(x  ,3,z)  ,texture=tree_texture)
                Block(position=(x-1,3,z-1),texture=leaves_texture)
                Block(position=(x-1,3,z)  ,texture=leaves_texture)
                Block(position=(x-1,3,z+1),texture=leaves_texture)
                Block(position=(x  ,3,z-1),texture=leaves_texture)
                Block(position=(x  ,3,z+1),texture=leaves_texture)
                Block(position=(x+1,3,z-1),texture=leaves_texture)
                Block(position=(x+1,3,z)  ,texture=leaves_texture)
                Block(position=(x+1,3,z+1),texture=leaves_texture)
                Block(position=(x-1,4,z-1),texture=leaves_texture)
                Block(position=(x-1,4,z)  ,texture=leaves_texture)
                Block(position=(x-1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,4,z-1),texture=leaves_texture)
                Block(position=(x  ,4,z)  ,texture=leaves_texture)
                Block(position=(x  ,4,z+1),texture=leaves_texture)
                Block(position=(x+1,4,z-1),texture=leaves_texture)
                Block(position=(x+1,4,z)  ,texture=leaves_texture)
                Block(position=(x+1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,5,z)  ,texture=leaves_texture)

                Block(position=(x,0,z),texture=dirt_texture)
                Block(position=(x,-1,z),texture=dirt_texture)
                Block(position=(x,-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,-3,z),texture=stone_texture)
                
                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-4,z),texture=diamond_texture)
                else:
                    Block(position=(x,-4,z),texture=stone_texture)
                
                Block(position=(x,-5,z),texture=bedrock_texture)
            elif rand_3tree_z == z and rand_3tree_x == x:
                Block(position=(x  ,1,z)  ,texture=tree_texture)
                Block(position=(x  ,2,z)  ,texture=tree_texture)
                Block(position=(x  ,3,z)  ,texture=tree_texture)
                Block(position=(x-1,3,z-1),texture=leaves_texture)
                Block(position=(x-1,3,z)  ,texture=leaves_texture)
                Block(position=(x-1,3,z+1),texture=leaves_texture)
                Block(position=(x  ,3,z-1),texture=leaves_texture)
                Block(position=(x  ,3,z+1),texture=leaves_texture)
                Block(position=(x+1,3,z-1),texture=leaves_texture)
                Block(position=(x+1,3,z)  ,texture=leaves_texture)
                Block(position=(x+1,3,z+1),texture=leaves_texture)
                Block(position=(x-1,4,z-1),texture=leaves_texture)
                Block(position=(x-1,4,z)  ,texture=leaves_texture)
                Block(position=(x-1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,4,z-1),texture=leaves_texture)
                Block(position=(x  ,4,z)  ,texture=leaves_texture)
                Block(position=(x  ,4,z+1),texture=leaves_texture)
                Block(position=(x+1,4,z-1),texture=leaves_texture)
                Block(position=(x+1,4,z)  ,texture=leaves_texture)
                Block(position=(x+1,4,z+1),texture=leaves_texture)
                Block(position=(x  ,5,z)  ,texture=leaves_texture)

                Block(position=(x,0,z),texture=dirt_texture)
                Block(position=(x,-1,z),texture=dirt_texture)
                Block(position=(x,-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,-3,z),texture=stone_texture)
                
                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-4,z),texture=diamond_texture)
                else:
                    Block(position=(x,-4,z),texture=stone_texture)
                
                Block(position=(x,-5,z),texture=bedrock_texture)
            else:
                Block(position=(x,0,z),texture=grass_texture)
                Block(position=(x,-1,z),texture=dirt_texture)
                Block(position=(x,-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,-3,z),texture=stone_texture)
                
                rand_dia = random.randint(1,10)
                if rand_dia == 1:
                    Block(position=(x,-4,z),texture=diamond_texture)
                else:
                    Block(position=(x,-4,z),texture=stone_texture)
                
                Block(position=(x,-5,z),texture=bedrock_texture)
    
    for br1 in range(13):
        Barrier(position=(br1,-3,-1))
        Barrier(position=(br1,-2,-1))
        Barrier(position=(br1,-1,-1))
        Barrier(position=(br1,0 ,-1))
        Barrier(position=(br1,1 ,-1))
        Barrier(position=(br1,2 ,-1))
        Barrier(position=(br1,3 ,-1))
    for br2 in range(13):
        Barrier(position=(br2,-3,13))
        Barrier(position=(br2,-2,13))
        Barrier(position=(br2,-1,13))
        Barrier(position=(br2,0 ,13))
        Barrier(position=(br2,1 ,13))
        Barrier(position=(br2,2 ,13))
        Barrier(position=(br2,3 ,13))
    for br3 in range(13):
        Barrier(position=(-1,-3,br3))
        Barrier(position=(-1,-2,br3))
        Barrier(position=(-1,-1,br3))
        Barrier(position=(-1,0 ,br3))
        Barrier(position=(-1,1 ,br3))
        Barrier(position=(-1,2 ,br3))
        Barrier(position=(-1,3 ,br3))
    for br4 in range(13):
        Barrier(position=(13,-3,br4))
        Barrier(position=(13,-2,br4))
        Barrier(position=(13,-1,br4))
        Barrier(position=(13,0 ,br4))
        Barrier(position=(13,1 ,br4))
        Barrier(position=(13,2 ,br4))
        Barrier(position=(13,3 ,br4))
creat_world()


def update():
    global block_pick
    global inventory
    global sun_angle
    global sun_move    
    global sun
    global sky

    if held_keys['1'] and block_pick < 10:
        block_pick = 1
        destroy(inventory)
        inventory = Inventory(inv1_texture)
    if held_keys['2'] and block_pick < 10:
        block_pick = 2
        destroy(inventory)
        inventory = Inventory(inv2_texture)
    if held_keys['3'] and block_pick < 10:
        block_pick = 3
        destroy(inventory)
        inventory = Inventory(inv3_texture)
    if held_keys['4'] and block_pick < 10:
        block_pick = 4
        destroy(inventory)
        inventory = Inventory(inv4_texture)
    if held_keys['5'] and block_pick < 10:
        block_pick = 5
        destroy(inventory)
        inventory = Inventory(inv5_texture)
    if held_keys['6'] and block_pick < 10:
        block_pick = 6
        destroy(inventory)
        inventory = Inventory(inv6_texture)
    if held_keys['7'] and block_pick < 10:
        block_pick = 7
        destroy(inventory)
        inventory = Inventory(inv7_texture)
    if held_keys['8'] and block_pick < 10:
        block_pick = 8
        destroy(inventory)
        inventory = Inventory(inv8_texture)
    if held_keys['9'] and block_pick < 10:
        block_pick = 9
        destroy(inventory)
        inventory = Inventory(inv9_texture)
    if held_keys['z']:
        block_pick = 1
        destroy(inventory)
        inventory = Inventory(inv1_texture)

    if held_keys['1'] and block_pick > 10:
        block_pick = 11
        destroy(inventory)
        inventory = Inventory(inv11_texture)
    if held_keys['2'] and block_pick > 10:
        block_pick = 12
        destroy(inventory)
        inventory = Inventory(inv12_texture)
    if held_keys['x']:
        block_pick = 11
        destroy(inventory)
        inventory = Inventory(inv11_texture)
                    
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    
    if sun_move % 2 == 0:
        destroy(sun)
        sun = Sun(weight=math.cos(math.radians(sun_angle))*50,height=math.sin(math.radians(sun_angle))*50,angle=sun_angle)
        sun_angle += 0.01
    sun_move += 1

    if math.sin(math.radians(sun_angle)) * 50 <= 1.5:
        destroy(sky)
        sky = Sky(texture=sky_night_texture)
    elif math.sin(math.radians(sun_angle)) * 50 <= 2:
        destroy(sky)
        sky = Sky(texture=sky_night1_texture)
    elif math.sin(math.radians(sun_angle)) * 50 <= 2.5:
        destroy(sky)
        sky = Sky(texture=sky_night2_texture)
    elif math.sin(math.radians(sun_angle)) * 50 <= 3:
        destroy(sky)
        sky = Sky(texture=sky_noon1_texture)
    else:
        destroy(sky)
        sky = Sky(texture=sky_noon_texture)


player = FirstPersonController()


app.run() 