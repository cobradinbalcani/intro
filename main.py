from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Override the settings of the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',  # First red, then changed later to black
    width=utils.width_prct(100),  # or  width=settings.WIDTH
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)

)

game_title.place(
    x=utils.width_prct(25), y=0
)

left_frame = Frame(
    root,
    bg='black',  # First blue, then changed later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,
                 y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',  # First yellow, then changed later to black
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),
                   y=utils.height_prct(25))


#  Creation of the cells
# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0, row=0
# )
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column=1, row=0
# )

#  for loop cell's creation

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
#  print(len(Cell.all))  #  how many cells there are
#  print(Cell.all)       #  coordinates of the cells

#  Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)


Cell.randomize_mines()
# for c in Cell.all:     #  chosen mines = True or False
#     print(c.is_mine)



if __name__ == '__main__':
    root.mainloop()

# Run the window
# root.mainloop()