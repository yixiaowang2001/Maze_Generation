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


# prim
def get_xy(pos):
    r = pos // x_n
    c = pos % x_n
    x = x_side + (2*c+1)*grid_width
    y = y_side + (2*r+1)*grid_width
    return x, y


def unvisited_neighbors(pos):
    global pos_list
    row = pos // x_n
    a = row * x_n
    b = (row+1) * x_n - 1
    if 0 <= pos-x_n < x_n*y_n:
        if not visited[pos - x_n] and not inlist[pos - x_n]:
            pos_list.append([pos-x_n, 'a'])
            inlist[pos - x_n] = True
    if 0 <= pos+x_n < x_n*y_n:
        if not visited[pos + x_n] and not inlist[pos + x_n]:
            pos_list.append([pos+x_n, 'b'])
            inlist[pos + x_n] = True
    if a <= pos-1 <= b:
        if not visited[pos - 1] and not inlist[pos - 1]:
            pos_list.append([pos-1, 'l'])
            inlist[pos - 1] = True
    if a <= pos+1 <= b:
        if not visited[pos + 1] and not inlist[pos + 1]:
            pos_list.append([pos+1, 'r'])
            inlist[pos + 1] = True


visited = [False] * (x_n*y_n)
inlist = [False] * (x_n*y_n)
pos_list = []
crt_pos = random.randint(0, x_n*y_n-1)
x, y = get_xy(crt_pos)
canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
visited[crt_pos] = True
inlist[crt_pos] = True
unvisited_neighbors(crt_pos)


def prim():
    global pos_list, crt_pos
    if len(pos_list) > 0:
        crt_pos = pos_list.pop(random.randint(0, len(pos_list) - 1))
        x, y = get_xy(crt_pos[0])
        if crt_pos[1] == "a":
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
            canvas.create_rectangle(x, y + grid_width, x + grid_width, y + 2 * grid_width, fill='white',
                                    outline='white')
        if crt_pos[1] == "b":
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
            canvas.create_rectangle(x, y - grid_width, x + grid_width, y, fill='white', outline='white')
        if crt_pos[1] == "l":
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
            canvas.create_rectangle(x + grid_width, y, x + 2 * grid_width, y + grid_width, fill='white',
                                    outline='white')
        if crt_pos[1] == "r":
            canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
            canvas.create_rectangle(x - grid_width, y, x, y + grid_width, fill='white', outline='white')
        visited[crt_pos[0]] = True
        unvisited_neighbors(crt_pos[0])
        root.after(res_time, prim)
    else:
        print("Done")
        return


# add to window and show
canvas.pack()
root.after(res_time, prim)
root.mainloop()
