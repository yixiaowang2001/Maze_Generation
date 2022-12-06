import tkinter
import random

# init tk
root = tkinter.Tk()
root.title('Maze Generator: DFS')

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

# dfs
s = []
visited = [False] * (x_n*y_n)
visited_count = 0
crt_pos = 0
visited[0] = True
visited_count += 1


def dfs():
    global visited_count, crt_pos
    if visited_count < x_n*y_n:
        x, y = get_xy(crt_pos)
        canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
        out = unvisited_neighbors(crt_pos, visited)
        if len(out) > 0:
            new_pos = out[random.randint(0, len(out)-1)]
            x, y = get_xy(new_pos[0])
            if new_pos[1] == "a":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x, y + grid_width, x + grid_width, y + 2*grid_width, fill='white',
                                        outline='white')
            if new_pos[1] == "b":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x, y - grid_width, x + grid_width, y, fill='white', outline='white')
            if new_pos[1] == "l":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x + grid_width, y, x + 2*grid_width, y + grid_width, fill='white',
                                        outline='white')
            if new_pos[1] == "r":
                canvas.create_rectangle(x, y, x + grid_width, y + grid_width, fill='white', outline='white')
                canvas.create_rectangle(x - grid_width, y, x, y + grid_width, fill='white', outline='white')
            s.append(new_pos[0])
            crt_pos = new_pos[0]
            visited[new_pos[0]] = True
            visited_count += 1
        else:
            crt_pos = s.pop()
        root.after(res_time, dfs)
    else:
        print("Done")
        return


def unvisited_neighbors(pos, visit_list):
    out = []
    row = pos // x_n
    a = row * x_n
    b = (row+1) * x_n - 1
    if 0 <= pos-x_n < x_n*y_n:
        if not visit_list[pos-x_n]:
            out.append([pos-x_n, 'a'])
    if 0 <= pos+x_n < x_n*y_n:
        if not visit_list[pos+x_n]:
            out.append([pos+x_n, 'b'])
    if a <= pos-1 <= b:
        if not visit_list[pos-1]:
            out.append([pos-1, 'l'])
    if a <= pos+1 <= b:
        if not visit_list[pos+1]:
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
root.after(res_time, dfs)
root.mainloop()
