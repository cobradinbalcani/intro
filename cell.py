import random
from tkinter import Button, Label
import ctypes
import settings
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #  Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            #  text=f'{self.x}, {self.y}'  text on the cell
        )
        btn.bind('<Button-1>', self.left_click_actions)  # Left click
        btn.bind('<Button-3>', self.right_click_actions)  # Right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f'Cells left:{Cell.cell_count}',
            #  width=12,
            #  height=4,      if there is font, you don't need anymore this attributes
            bg='black',
            fg='white',
            font=('', 30)

        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        #  print(event)
        #  print('left clicked')
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
            #  If mines count is equal to the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game over', 0)
                sys.exit()

        #  Cancel Left and Right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property  # read-only attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),  # cell[0,0]
            self.get_cell_by_axis(self.x - 1, self.y),      # cell[0,1]
            self.get_cell_by_axis(self.x - 1, self.y + 1),  # cell[0,2]
            self.get_cell_by_axis(self.x, self.y + 1),      # cell[1,2]
            self.get_cell_by_axis(self.x + 1, self.y),      # cell[2,1]
            self.get_cell_by_axis(self.x, self.y - 1),      # cell[1,0]
            self.get_cell_by_axis(self.x + 1, self.y - 1),  # cell[2,0]
            self.get_cell_by_axis(self.x + 1, self.y + 1),  # cell[2,2]
        ]
        #  comprehension list to eliminate the None elements
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:

            Cell.cell_count -= 1
        #  print(self.get_cell_by_axis(0, 0))          example of printing if not mine
        #  print(self.surrounded_cells)                if not mine, print the surrounded cells
        #  print(self.surrounded_cells_mines_length)   if not mine, print how many mines are surrounding
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length
        )
        #  Replace the text off cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells left:{Cell.cell_count}'
                )
            #  If this was a mine candidate, then for safety, we should
            #  configure the background color to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        #  Mark the cell as opened (Use is as the last line of the method)
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        # A logic do interrupt the game and display a message that player lost!
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game over', 0)
        sys.exit()

    def right_click_actions(self, event):
        # print(event)
        # print('right clicked')
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        #  my_list = ['Leo', 'Theo', 'Keo']  #  picked names from example list
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
