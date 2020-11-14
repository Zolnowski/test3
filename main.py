@namespace
class SpriteKind:
    asteroid = SpriteKind.create()

def on_a_pressed():
    for value in sprites.all_of_kind(SpriteKind.asteroid):
        value.set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
