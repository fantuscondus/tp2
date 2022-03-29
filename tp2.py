a = "fanta conde"
basic.show_string(a)
led.plot(2, 3)

def on_forever():
    if input.button_is_pressed(Button.A):
        images.icon_image(IconNames.HAPPY).show_image(0)
    else:
        images.icon_image(IconNames.HAPPY).show_image(0)
basic.forever(on_forever)
