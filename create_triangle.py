from numpy import tan as tan

def create_triangle(screen_w, screen_h, percent):
    center_x, center_y = screen_w//2, screen_h//2
    width = int(center_x * percent)
    height = int(width//2 * tan(60*pi/180))
    return ( (center_x, center_y), (center_x+width, center_y), (center_x+width//2, center_y-height) )
