import tkinter
import random

# init tk
root = tkinter.Tk()
root.title('Maze Generator: Kruskal')

# initialize variables
grid_width = 5
x_n = 120
y_n = 80
x_side = 20
y_side = 20
count = 0
res_time = 1

# create canvas
width = 2 * x_side + (2 * x_n + 1) * grid_width
height = 2 * y_side + (2 * y_n + 1) * grid_width
canvas = tkinter.Canvas(root, bg="white", height=height, width=width)

# draw grid
for x in range(x_side, width - x_side, grid_width):
    for y in range(y_side, height - y_side, grid_width):
        if x == x_side and y == y_side + grid_width:
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='paleturquoise', outline='paleturquoise')
        elif x == width - x_side - grid_width and y == height - y_side - 2*grid_width:
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='salmon', outline='salmon')
        else:
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='black', outline='black')


# kruskal
class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data


num_walls = 0
node_list = [Node(i) for i in range(x_n*y_n)]


def kruskal():
    global num_walls
    if num_walls < x_n*y_n - 1:
        crt_pos = random.randint(0, x_n*y_n-1)
        x, y = get_xy(crt_pos)
        out = wall_neighbors(crt_pos)
        if len(out) > 0:
            neighbor = out[random.randint(0, len(out)-1)]
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
            get_root(neighbor[0]).parent = node_list[crt_pos]
            x, y = get_xy(neighbor[0])
            if neighbor[1] == "a":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x, y + grid_width, x + grid_width, y + 2 * grid_width, fill='white',
                                        outline='white')
            if neighbor[1] == "b":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x, y - grid_width, x + grid_width, y, fill='white', outline='white')
            if neighbor[1] == "l":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x + grid_width, y, x + 2 * grid_width, y + grid_width, fill='white',
                                        outline='white')
            if neighbor[1] == "r":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x - grid_width, y, x, y + grid_width, fill='white', outline='white')
            num_walls += 1

        root.after(res_time, kruskal)
    else:
        print("Done")
        return


def get_root(pos):
    node = node_list[pos]
    r = node
    while node.parent is not None:
        node = node.parent
        r = node
    return r


def wall_neighbors(pos):
    out = []
    row = pos // x_n
    a = row * x_n
    b = (row+1) * x_n - 1
    if 0 <= pos-x_n < x_n*y_n:
        if get_root(pos).data != get_root(pos-x_n).data:
            out.append([pos-x_n, 'a'])
    if 0 <= pos+x_n < x_n*y_n:
        if get_root(pos).data != get_root(pos+x_n).data:
            out.append([pos+x_n, 'b'])
    if a <= pos-1 <= b:
        if get_root(pos).data != get_root(pos-1).data:
            out.append([pos-1, 'l'])
    if a <= pos+1 <= b:
        if get_root(pos).data != get_root(pos+1).data:
            out.append([pos+1, 'r'])
    return out


def get_xy(pos):
    r = pos // x_n
    c = pos % x_n
    x = x_side + (2*c+1)*grid_width
    y = y_side + (2*r+1)*grid_width
    return x, y


# add to window and show
canvas.pack()
root.after(res_time, kruskal)
root.mainloop()
