from tkinter import Frame,Label,CENTER
import LogicsFinal
import Constants as c
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:LogicsFinal.move_up,c.KEY_DOWN:LogicsFinal.move_down,c.KEY_LEFT:LogicsFinal.move_left,
                    c.KEY_RIGHT:LogicsFinal.move_right}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
    def init_grid(self):
        background=Frame(self,bg=c.backgroundcolorgame,width=c.size,height=c.size)
        background.grid()
        for i in range(c.gridlen):
            gridrow=[]
            for j in range(c.gridlen):
                cell=Frame(background,bg=c.backgroundcolorcellempty,width=c.size/c.gridlen,height=c.size/c.gridlen)
                cell.grid(row=i,column=j,padx=c.gridpadding,pady=c.gridpadding)
                t=Label(master=cell,text='',bg=c.backgroundcolorcellempty,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                gridrow.append(t)
            self.grid_cells.append(gridrow)
    def init_matrix(self):
        self.matrix=LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
    def update_grid_cells(self):
        for i in range(c.gridlen):
            for j in range(c.gridlen):
                newno=self.matrix[i][j]
                if newno==0:
                    self.grid_cells[i][j].configure(text='',bg=c.backgroundcolorcellempty)
                else:
                    self.grid_cells[i][j].configure(text=str(newno),bg=c.backgroundcolordict[newno],fg=c.cellcolordict[newno])
        self.update_idletasks()
    def key_down(self,event):
        key=repr(event.char) 
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if LogicsFinal.get_current_state(self.matrix)=='WON':
                    self.grid_cells[1][1].configure(text='You',bg=c.backgroundcolorcellempty)
                    self.grid_cells[1][2].configure(text='Win!',bg=c.backgroundcolorcellempty)
                if LogicsFinal.get_current_state(self.matrix)=='LOST':
                    self.grid_cells[1][1].configure(text='You',bg=c.backgroundcolorcellempty)
                    self.grid_cells[1][2].configure(text='Lose!',bg=c.backgroundcolorcellempty)
gamegrid=Game2048()