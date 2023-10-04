from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.Image = load_image('grass.png')


    def draw(self):
        self.Image.draw(400,30)

    def update(self):
        pass



class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame= 0
        self.image = load_image ('run_animation.png')
    def update(self):
        self.frame = random.randint(0,7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame *100, 0, 100, 100, self.x , self.y)
















def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
def Reset_World():
    global running
    running = True
    global grass
    global team
    global world

    world = []


    team = [Boy() for i in range(10)]
    grass = Grass()
    world.append(grass)
    world += team

def Update_World():
    for o in world:
        o.update()
    pass

def Render_World():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()



open_canvas()
# game main loop code
Reset_World()

while running:
    handle_events()
    Update_World()
    Render_World()
    delay(0.05)



# finalization code

close_canvas()
