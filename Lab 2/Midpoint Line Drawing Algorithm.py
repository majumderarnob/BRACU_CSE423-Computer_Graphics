from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

id = input('Please Enter your ID: ')


def draw_points(x, y):
    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(1.5, 0.5, 1.0)
    glVertex2f(x, y)
    glEnd()


def Find_zone(x_1, y_1, x_2, y_2):
    dx = x_2 - x_1
    dy = y_2 - y_1

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx >= 0 and dy <= 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx >= 0 and dy <= 0:
            zone = 6
        elif dx <= 0 and dy <= 0:
            zone = 5
    # print(f'Zone: {zone}')
    return zone
2

def convert_to_zone0(x, y, zone):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def convert_to_Origin(x, y, zone):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def midpoint_line(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    d_E = 2 * dy
    d_NE = 2 * dy - dx
    x = x1
    y = y1
    while (x < x2):
        x_p, y_p = convert_to_Origin(x, y, zone)
        draw_points(x_p, y_p)
        if d < 0:
            x += 1
            d += d_E
            # print(f'dE')
        else:
            x += 1
            y += 1
            d += d_NE
            # print(f'dNE')


def Draw_Line(x1, y1, x2, y2):
    curr_z = Find_zone(x1, y1, x2, y2)
    x1_prime, y1_prime = convert_to_zone0(x1, y1, curr_z)
    x2_prime, y2_prime = convert_to_zone0(x2, y2, curr_z)
    midpoint_line(x1_prime, y1_prime, x2_prime, y2_prime, curr_z)


def id_drawing_1(a):
    if a == '0':
        Draw_Line(250, 450, 100, 450)
        Draw_Line(100, 450, 100, 150)
        Draw_Line(250, 150, 100, 150)
        Draw_Line(250, 150, 250, 450)
        # Draw_Line(100, 150, 175, 450)

    elif a == "1":
        Draw_Line(250, 150, 250, 450)

    elif a == "2":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(250, 450, 250, 300)
        Draw_Line(100, 300, 250, 300)
        Draw_Line(100, 150, 100, 300)
        Draw_Line(100, 150, 250, 150)

    elif a == "3":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(250, 450, 250, 300)
        Draw_Line(100, 300, 250, 300)
        Draw_Line(250, 300, 250, 150)
        Draw_Line(250, 150, 100, 150)

    elif a == "4":
        Draw_Line(100, 450, 100, 300)
        Draw_Line(100, 300, 250, 300)
        Draw_Line(250, 450, 250, 300)
        Draw_Line(250, 300, 250, 150)

    elif a == "5":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(100, 450, 100, 300)
        Draw_Line(100, 300, 250, 300)
        Draw_Line(250, 300, 250, 150)
        Draw_Line(250, 150, 100, 150)

    elif a == "6":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(100, 450, 100, 150)
        Draw_Line(250, 150, 100, 150)
        Draw_Line(250, 150, 250, 300)
        Draw_Line(250, 300, 100, 300)

    elif a == "7":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(250, 450, 250, 150)

    elif a == "8":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(100, 450, 100, 150)
        Draw_Line(250, 300, 100, 300)
        Draw_Line(250, 150, 100, 150)
        Draw_Line(250, 150, 250, 450)

    elif a == "9":
        Draw_Line(250, 450, 100, 450)
        Draw_Line(100, 450, 100, 300)
        Draw_Line(250, 150, 250, 450)
        Draw_Line(250, 150, 100, 150)
        Draw_Line(250, 300, 100, 300)


def id_drawing_2(b):
    if b == "0":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 150, 450, 450)
        Draw_Line(300, 150, 300, 450)
        Draw_Line(300, 150, 450, 150)

    elif b == "1":
        Draw_Line(300, 150, 300, 450)

    elif b == "2":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 300, 450, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(300, 300, 300, 150)
        Draw_Line(300, 150, 450, 150)

    elif b == "3":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 150, 450, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(300, 150, 450, 150)

    elif b == "4":
        Draw_Line(300, 450, 300, 300)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(450, 450, 450, 150)

    elif b == "5":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(300, 300, 300, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(450, 300, 450, 150)
        Draw_Line(300, 150, 450, 150)

    elif b == "6":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(300, 150, 300, 450)
        Draw_Line(450, 300, 450, 150)
        Draw_Line(300, 150, 450, 150)

    elif b == "7":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 150, 450, 450)

    elif b == "8":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 150, 450, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(300, 150, 300, 450)
        Draw_Line(300, 150, 450, 150)

    elif b == "9":
        Draw_Line(300, 450, 450, 450)
        Draw_Line(450, 150, 450, 450)
        Draw_Line(450, 300, 300, 300)
        Draw_Line(300, 300, 300, 450)
        Draw_Line(300, 150, 450, 150)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    id_drawing_1(id[-2])
    id_drawing_2(id[-1])
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"20301089")
glutDisplayFunc(showScreen)

glutMainLoop()
