def hue_to_rgb_led(h: float) -> tuple[int, int, int]:
    """
    This is a hue function that converts a float in the range of [0-1] to three r,g,b values
    If you give this function the input in 360 steps, you can move past all the colors (red, yellow, green, cyan, blue, purple, back to red, etc)
    You can just loop x in range(361) and run hue_to_rgb_led(x/360)
    """
    # clamp h between [0-1]
    h = max(h, 0)
    h = min(h, 1)

    r, g, b = 0, 0, 0
    if h < 1 / 3:
        r = 2 - h * 6
        g = h * 6
        b = 0
    elif h < 2 / 3:
        r = 0
        g = 4 - h * 6
        b = h * 6 - 2
    else:
        r = h * 6 - 4
        g = 0
        b = (1 - h) * 6
    # clamp values
    r = min(r, 1)
    g = min(g, 1)
    b = min(b, 1)
    r *= 100
    g *= 100
    b *= 100

    # Use these to set the RPi LED (or whatever light you're trying to light)
    return (r, g, b)