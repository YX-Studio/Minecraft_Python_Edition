# Version 2.0.0.57
# By YXStudio 2023~2025.
# Jul.12th,2025


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import math
import json
import os
import random
import tkinter as tk
from tkinter import messagebox,simpledialog


app = Ursina()

grass_texture = load_texture('assets/textures/blocks/grass_block.png')
stone_texture = load_texture('assets/textures/blocks/stone_block.png')
brick_texture = load_texture('assets/textures/blocks/brick_block.png')
dirt_texture = load_texture('assets/textures/blocks/dirt_block.png')
wood_texture = load_texture('assets/textures/blocks/wood_block.png')
diamond_texture = load_texture('assets/textures/blocks/diamond_block.png')
bedrock_texture = load_texture('assets/textures/blocks/bedrock_block.png')
tree_texture = load_texture('assets/textures/blocks/tree_block.png')
leaves_texture = load_texture('assets/textures/blocks/leaves_block.png')
sand_texture = load_texture('assets/textures/blocks/sand_block.png')
glass_texture = load_texture('assets/textures/blocks/glass_block.png')

barrier_texture = load_texture('assets/textures/blocks/barrier_block.png')

inv1_texture = load_texture('assets/textures/inventorys/hotbar1.png')
inv2_texture = load_texture('assets/textures/inventorys/hotbar2.png')
inv3_texture = load_texture('assets/textures/inventorys/hotbar3.png')
inv4_texture = load_texture('assets/textures/inventorys/hotbar4.png')
inv5_texture = load_texture('assets/textures/inventorys/hotbar5.png')
inv6_texture = load_texture('assets/textures/inventorys/hotbar6.png')
inv7_texture = load_texture('assets/textures/inventorys/hotbar7.png')
inv8_texture = load_texture('assets/textures/inventorys/hotbar8.png')
inv9_texture = load_texture('assets/textures/inventorys/hotbar9.png')
inv11_texture = load_texture('assets/textures/inventorys/hotbar11.png')
inv12_texture = load_texture('assets/textures/inventorys/hotbar12.png')

arm_texture = load_texture('assets/textures/arm/arm_texture.png')

sky_noon_texture = load_texture('assets/textures/sky/skybox_noon.png')
sky_noon1_texture = load_texture('assets/textures/sky/skybox_noon1.png')
sky_night_texture = load_texture('assets/textures/sky/skybox_night.png')
sky_night1_texture = load_texture('assets/textures/sky/skybox_night1.png')
sky_night2_texture = load_texture('assets/textures/sky/skybox_night2.png')

sun_texture = load_texture('assets/textures/sun/sun.png')

sight_texture = load_texture('assets/textures/sight/sight.png')

punch_sound = Audio('assets/sounds/punch_sound.m4a', loop=False, autoplay=False)

window.fps_counter.enabled = True
window.exit_button.visible = False

block_pick = 1
sun_angle = 0
sun_move = 0


if not os.path.exists('saves'):
    os.makedirs('saves')


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
        self.block_type = self.get_block_type(texture)

    def get_block_type(self,texture):
        if texture == grass_texture: return 1
        elif texture == stone_texture: return 2
        elif texture == brick_texture: return 3
        elif texture == dirt_texture: return 4
        elif texture == wood_texture: return 5
        elif texture == diamond_texture: return 6
        elif texture == tree_texture: return 7
        elif texture == leaves_texture: return 8
        elif texture == bedrock_texture: return 9
        elif texture == sand_texture: return 11
        elif texture == glass_texture: return 12
        else: return 1

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                if block_pick == 1:
                    Block(position=self.position+mouse.normal,texture=grass_texture)
                elif block_pick == 2:
                    Block(position=self.position+mouse.normal,texture=stone_texture)
                elif block_pick == 3:
                    Block(position=self.position+mouse.normal,texture=brick_texture)
                elif block_pick == 4:
                    Block(position=self.position+mouse.normal,texture=dirt_texture)
                elif block_pick == 5:
                    Block(position=self.position+mouse.normal,texture=wood_texture)
                elif block_pick == 6:
                    Block(position=self.position+mouse.normal,texture=diamond_texture)
                elif block_pick == 7:
                    Block(position=self.position+mouse.normal,texture=tree_texture)
                elif block_pick == 8:
                    Block(position=self.position+mouse.normal,texture=leaves_texture)
                elif block_pick == 9:
                    Block(position=self.position+mouse.normal,texture=bedrock_texture)
                elif block_pick == 11:
                    Block(position=self.position+mouse.normal,texture=sand_texture)
                elif block_pick == 12:
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
            position = (0,-0.460),
            model = 'quad',
            texture = texture,
            scale = (0.658,0.08)
        )

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

class Sky(Entity):
    def __init__(self,texture=sky_noon_texture):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            rotation = (150,-10,0),
            position = (0.9,-0.7),
            model = 'assets/blends/arm/arm',
            texture = arm_texture,
            scale = 0.2
        )
                
    def active(self):
        self.position = (0.7,-0.6)
                
    def passive(self):
        self.position = (0.9,-0.7)

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


def save_game():
    root = tk.Tk()
    root.withdraw()
    save_name = simpledialog.askstring('Save The Game','Please enter a name for the archive :')
    root.destroy()
    
    if not save_name:
        return
    
    SAVE_FILE = f'saves/{save_name}_game_save.json'
    
    blocks_data = []
    for entity in scene.entities:
        if isinstance(entity,Block):
            blocks_data.append({
                'position': [entity.position.x,entity.position.y,entity.position.z],
                'type': entity.block_type
            })
    
    player_data = {
        'position': [player.position.x,player.position.y,player.position.z],
        'rotation': [player.rotation.x,player.rotation.y,player.rotation.z],
        'block_pick': block_pick
    }
    
    game_data = {
        'sun_angle': sun_angle,
        'sun_move': sun_move,
        'save_name': save_name
    }
    
    save_data = {
        'blocks': blocks_data,
        'player': player_data,
        'game': game_data
    }
    
    with open(SAVE_FILE,'w',encoding='utf-8') as f:
        json.dump(save_data,f,ensure_ascii=False,indent=4)


def create_world():
    noise = PerlinNoise(octaves=3,seed=random.randint(0,999999999))
    scale = 36

    rand_hole_z = random.randint(1,11)
    rand_hole_x = random.randint(1,11)

    rand_1tree_z = random.randint(3,9)
    rand_1tree_x = random.randint(3,9)

    rand_2tree_z = 1
    rand_2tree_x = 11

    rand_3tree_z = 11
    rand_3tree_x = 1
            
    for z in range(13):
        for x in range(13):
            y = floor(noise([x/scale,z/scale])*8)

            Block(position=(x,y,z),texture=grass_texture)
            Block(position=(x,y-1,z),texture=dirt_texture)
            Block(position=(x,y-2,z),texture=dirt_texture)

            if rand_hole_z==z and rand_hole_x==x:
                Block(position=(x,y-4,z),texture=stone_texture)
            elif rand_1tree_z==z and rand_1tree_x==x:
                Block(position=(x  ,y+1,z)  ,texture=tree_texture)
                Block(position=(x  ,y+2,z)  ,texture=tree_texture)
                Block(position=(x  ,y+3,z)  ,texture=tree_texture)
                Block(position=(x-1,y+3,z-1),texture=leaves_texture)
                Block(position=(x-1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+3,z+1),texture=leaves_texture)
                Block(position=(x  ,y+3,z-1),texture=leaves_texture)
                Block(position=(x  ,y+3,z+1),texture=leaves_texture)
                Block(position=(x+1,y+3,z-1),texture=leaves_texture)
                Block(position=(x+1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+3,z+1),texture=leaves_texture)
                Block(position=(x-1,y+4,z-1),texture=leaves_texture)
                Block(position=(x-1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+4,z-1),texture=leaves_texture)
                Block(position=(x  ,y+4,z)  ,texture=leaves_texture)
                Block(position=(x  ,y+4,z+1),texture=leaves_texture)
                Block(position=(x+1,y+4,z-1),texture=leaves_texture)
                Block(position=(x+1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+5,z)  ,texture=leaves_texture)

                Block(position=(x,y,z),texture=dirt_texture)
                Block(position=(x,y-1,z),texture=dirt_texture)
                Block(position=(x,y-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,100)
                if rand_dia <= 10:
                    Block(position=(x,y-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,y-3,z),texture=stone_texture)
                
                Block(position=(x,y-4,z),texture=stone_texture)
            elif rand_2tree_z==z and rand_2tree_x==x:
                Block(position=(x  ,y+1,z)  ,texture=tree_texture)
                Block(position=(x  ,y+2,z)  ,texture=tree_texture)
                Block(position=(x  ,y+3,z)  ,texture=tree_texture)
                Block(position=(x-1,y+3,z-1),texture=leaves_texture)
                Block(position=(x-1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+3,z+1),texture=leaves_texture)
                Block(position=(x  ,y+3,z-1),texture=leaves_texture)
                Block(position=(x  ,y+3,z+1),texture=leaves_texture)
                Block(position=(x+1,y+3,z-1),texture=leaves_texture)
                Block(position=(x+1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+3,z+1),texture=leaves_texture)
                Block(position=(x-1,y+4,z-1),texture=leaves_texture)
                Block(position=(x-1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+4,z-1),texture=leaves_texture)
                Block(position=(x  ,y+4,z)  ,texture=leaves_texture)
                Block(position=(x  ,y+4,z+1),texture=leaves_texture)
                Block(position=(x+1,y+4,z-1),texture=leaves_texture)
                Block(position=(x+1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+5,z)  ,texture=leaves_texture)

                Block(position=(x,y,z),texture=dirt_texture)
                Block(position=(x,y-1,z),texture=dirt_texture)
                Block(position=(x,y-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,100)
                if rand_dia <= 10:
                    Block(position=(x,y-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,y-3,z),texture=stone_texture)
                
                Block(position=(x,y-4,z),texture=stone_texture)
            elif rand_3tree_z==z and rand_3tree_x==x:
                Block(position=(x  ,y+1,z)  ,texture=tree_texture)
                Block(position=(x  ,y+2,z)  ,texture=tree_texture)
                Block(position=(x  ,y+3,z)  ,texture=tree_texture)
                Block(position=(x-1,y+3,z-1),texture=leaves_texture)
                Block(position=(x-1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+3,z+1),texture=leaves_texture)
                Block(position=(x  ,y+3,z-1),texture=leaves_texture)
                Block(position=(x  ,y+3,z+1),texture=leaves_texture)
                Block(position=(x+1,y+3,z-1),texture=leaves_texture)
                Block(position=(x+1,y+3,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+3,z+1),texture=leaves_texture)
                Block(position=(x-1,y+4,z-1),texture=leaves_texture)
                Block(position=(x-1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x-1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+4,z-1),texture=leaves_texture)
                Block(position=(x  ,y+4,z)  ,texture=leaves_texture)
                Block(position=(x  ,y+4,z+1),texture=leaves_texture)
                Block(position=(x+1,y+4,z-1),texture=leaves_texture)
                Block(position=(x+1,y+4,z)  ,texture=leaves_texture)
                Block(position=(x+1,y+4,z+1),texture=leaves_texture)
                Block(position=(x  ,y+5,z)  ,texture=leaves_texture)

                Block(position=(x,y,z),texture=dirt_texture)
                Block(position=(x,y-1,z),texture=dirt_texture)
                Block(position=(x,y-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,100)
                if rand_dia <= 10:
                    Block(position=(x,y-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,y-3,z),texture=stone_texture)
                
                Block(position=(x,y-4,z),texture=stone_texture)
            else:
                Block(position=(x,y,z),texture=grass_texture)
                Block(position=(x,y-1,z),texture=dirt_texture)
                Block(position=(x,y-2,z),texture=dirt_texture)

                rand_dia = random.randint(1,100)
                if rand_dia <= 10:
                    Block(position=(x,y-3,z),texture=diamond_texture)
                else:
                    Block(position=(x,y-3,z),texture=stone_texture)
                
                Block(position=(x,y-4,z),texture=stone_texture)
            Block(position=(x,y-5,z),texture=bedrock_texture)

    for i in range(13):
        for y in range(-3,4):
            Barrier(position=(i,y,-1))
            Barrier(position=(i,y,13))
            Barrier(position=(-1,y,i))
            Barrier(position=(13,y,i))


inventory = Inventory()
hand = Hand()
Sight()
sky = Sky()
sun = Sun()


create_world()


def input(key):
    global block_pick,inventory
    
    if key == 'escape':
        root = tk.Tk()
        root.withdraw()
        save = messagebox.askyesnocancel('Game Exit','Do you want to save the game?')
        if save is not None:
            if save:
                save_game()
            quit()
        root.destroy()
    elif key == 'q':
        window.exit_button.visible = not window.exit_button.visible
    elif key == 'e':
        window.fps_counter.enabled = not window.fps_counter.enabled
    
    hotkeys = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 11,
        '-': 12
    }
    
    if key in hotkeys:
        block_pick = hotkeys[key]
        destroy(inventory)
        inventory_textures = {
            1: inv1_texture,
            2: inv2_texture,
            3: inv3_texture,
            4: inv4_texture,
            5: inv5_texture,
            6: inv6_texture,
            7: inv7_texture,
            8: inv8_texture,
            9: inv9_texture,
            11: inv11_texture,
            12: inv12_texture
        }
        inventory = Inventory(inventory_textures.get(block_pick,inv1_texture))


def update():
    global sun_angle,sun_move,sun,sky
    
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    
    if sun_move % 2 == 0:
        destroy(sun)
        sun = Sun(
            weight = math.cos(math.radians(sun_angle)) * 50, 
            height = math.sin(math.radians(sun_angle)) * 50, 
            angle = sun_angle
        )
        sun_angle += 0.01
    sun_move += 1

    sun_height = math.sin(math.radians(sun_angle)) * 50
    sky_textures = [
        (1.5,sky_night_texture),
        (2.0,sky_night1_texture),
        (2.5,sky_night2_texture),
        (3.0,sky_noon1_texture)
    ]
    
    sky.texture = sky_noon_texture
    for height, tex in sky_textures:
        if sun_height <= height:
            sky.texture = tex
            break


player = FirstPersonController()


app.run()