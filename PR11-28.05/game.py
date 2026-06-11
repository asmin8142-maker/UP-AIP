from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()

window.title = '3D Labyrinth'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = True

# ------------------- НЕБО И СВЕТ -------------------

Sky()

DirectionalLight(
    y=10,
    z=10,
    shadows=True,
    rotation=(45, -45, 45)
)

AmbientLight(color=color.rgba(100, 100, 100, 0.5))

# ------------------- ПОЛ -------------------

ground = Entity(
    model='plane',
    scale=(50, 1, 50),
    texture='white_cube',
    texture_scale=(50, 50),
    color=color.light_gray,
    collider='box'
)

# ------------------- СТЕНЫ ЛАБИРИНТА -------------------

walls = []

maze = [
    "####################",
    "#     #       #    #",
    "# ### # ##### # ## #",
    "# #   #     # #    #",
    "# # ##### # # ######",
    "# #     # # #      #",
    "# ##### # # ###### #",
    "#     # # #      # #",
    "##### # # ###### # #",
    "#   # #        # # #",
    "# # # ######## # # #",
    "# # #        # #   #",
    "# # ######## # #####",
    "# #          #     #",
    "#################  #"
]

for z in range(len(maze)):
    for x in range(len(maze[z])):
        if maze[z][x] == "#":
            wall = Entity(
                model='cube',
                color=color.azure,
                position=(x, 1, z),
                texture='white_cube',
                collider='box'
            )
            walls.append(wall)

# ------------------- ИГРОК -------------------

player = FirstPersonController(
    position=(1, 2, 1),
    speed=5,
    jump_height=2,
    gravity=1
)

# ------------------- КЛЮЧ -------------------

has_key = False

key = Entity(
    model='cube',
    color=color.yellow,
    scale=0.5,
    position=(3, 1, 3),
    collider='box'
)

# ------------------- ДВЕРИ -------------------

doors = []

door_positions = [
    (8, 1, 2),
    (12, 1, 7),
    (16, 1, 12)
]

for pos in door_positions:
    door = Entity(
        model='cube',
        color=color.brown,
        scale=(1, 2, 0.3),
        position=pos,
        collider='box'
    )
    doors.append(door)

# ------------------- ЛОВУШКИ -------------------

traps = []

# Тип 1 — красные ямы
trap_positions_red = [
    (5, 0.1, 5),
    (10, 0.1, 8)
]

for pos in trap_positions_red:
    trap = Entity(
        model='cube',
        color=color.red,
        scale=(1, 0.1, 1),
        position=pos,
        collider='box'
    )
    traps.append(trap)

# Тип 2 — зеленые ловушки
trap_positions_green = [
    (7, 0.1, 12),
    (14, 0.1, 4)
]

for pos in trap_positions_green:
    trap = Entity(
        model='cube',
        color=color.green,
        scale=(1, 0.1, 1),
        position=pos,
        collider='box'
    )
    traps.append(trap)

# Тип 3 — черная ловушка
black_trap = Entity(
    model='cube',
    color=color.black,
    scale=(2, 0.1, 2),
    position=(17, 0.1, 10),
    collider='box'
)

traps.append(black_trap)

# ------------------- ВЫХОД -------------------

exit_zone = Entity(
    model='cube',
    color=color.gold,
    scale=(2, 2, 2),
    position=(18, 1, 14),
    collider='box'
)

# ------------------- ТЕКСТ -------------------

info_text = Text(
    text='Find the key!',
    position=(-0.85, 0.45),
    scale=2
)

win_text = Text(
    text='',
    origin=(0, 0),
    scale=3,
    color=color.yellow
)

# ------------------- ЗВУКИ -------------------

pickup_sound = Audio(
    'coin',
    autoplay=False
)

door_sound = Audio(
    'door_open',
    autoplay=False
)

win_sound = Audio(
    'powerup',
    autoplay=False
)

# ------------------- ЛОГИКА -------------------

def update():
    global has_key

    # Подбор ключа
    if key.enabled and distance(player.position, key.position) < 1.5:
        has_key = True
        key.enabled = False
        info_text.text = 'Key collected!'
        pickup_sound.play()

    # Двери
    for door in doors:
        if distance(player.position, door.position) < 2:
            if has_key:
                door.disable()
                door_sound.play()

    # Ловушки
    for trap in traps:
        if distance(player.position, trap.position) < 1:
            player.position = (1, 2, 1)
            info_text.text = 'You fell into a trap!'

    # Победа
    if distance(player.position, exit_zone.position) < 2:
        win_text.text = 'YOU WIN!'
        info_text.text = ''
        win_sound.play()

app.run()