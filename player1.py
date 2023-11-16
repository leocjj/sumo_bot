import sumo_utils as su

PRIMARY_COLOR = su.RED
SECUNDARY_COLOR = su.BLUE

def move_bot(x: int, y: int, rot: int, x_opp: int, y_opp: int, rot_opp: int) -> tuple[int, int]:
    """
    x: own x-coordinate. Increases from top to bottom.
    y: own y-coordinate. Increases from left to right.
    rot: angle starting from the 0 in the positive x-axis and increases CCW
    x_opp: opponent x-coordinate. Increases from top to bottom.
    y_opp: opponent y-coordinate. Increases from left to right.
    rot_opp: opponent angle starting from the 0 in the positive x-axis and increases CCW
    Return: exactly two integers (a tuple).
        The first value represents the movement: 1 (forward), 0 (stop), -1 (backward)
        The second value represents the rotation: 1 (CCW or left), 0 (stop), -1 (CW or right)
    """

    # Window size in pixels.
    # Top-left corner have coordinates (0,0)
    # Right-bottom corner have coordinates (su.HEIGHT, su.WIDTH)
    su.HEIGHT
    su.WIDTH
    su.DOJO_HIGHT
    su.DOJO_WIDTH
    su.DOJO_X  # Top-left corner coordinates
    su.DOJO_Y

    """
    tolerance = 75
    if x < su.DOJO_X + tolerance and 0 <= rot < 90 and  270 <= rot <= 360:
        return 1, 0
    if x < su.DOJO_X + tolerance and 90 <= rot <=180:
        return 1, -1
    if x < su.DOJO_X + tolerance and 180 < rot <= 270:
        return 1, 1
    """

    return 1, 0