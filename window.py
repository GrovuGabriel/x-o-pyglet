import pyglet
from pyglet.window import key

class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(resizable=True)
        self.player1_score = 0
        self.player2_score = 0
        self.won=False
        self.set_minimum_size(400, 400)
        self.black=(0,0,0,255)
        self.white=(255,255,255,255)
        self.grey=(15,15,15,255)
        self.red=(255,0,0,255)
        self.blue=(0,0,255,255)
        self.player1 = pyglet.text.Label('Player1: '+str(self.player1_score), x=15, y=self.height-15,font_name='Times New Roman', font_size=30, bold=True, anchor_x='left', anchor_y='top')
        self.player2 = pyglet.text.Label('Player2: '+str(self.player2_score), x=self.width-15, y=self.height-15,font_name='Times New Roman', font_size=30, bold=True, anchor_x='right', anchor_y='top')
        self.line_size = self.height/1.5
        self.cells=[]
        self.play_area_calculate()
        self.x_o=pyglet.shapes.Batch()
        self.play_matrix = [[0,0,0],[0,0,0],[0,0,0]]
        self.player=1
        self.x_o_labels=[None,None,None,None,None,None,None,None,None]

    def play_area_calculate(self):
        x1=self.width/2-self.line_size/2
        y1=self.height/2-self.line_size/2
        x2=self.width/2+self.line_size/2
        y2=self.height/2+self.line_size/2

        l1_x1=x1+(x2-x1)/3
        l1_y1=y1
        l1_x2=x1+(x2-x1)/3
        l1_y2=y2
        l2_x1=x1+(x2-x1)/3*2
        l2_y1=y1
        l2_x2=x1+(x2-x1)/3*2
        l2_y2=y2
        l3_x1=x1
        l3_y1=y1+(y2-y1)/3
        l3_x2=x2
        l3_y2=y1+(y2-y1)/3
        l4_x1=x1
        l4_y1=y1+(y2-y1)/3*2
        l4_x2=x2
        l4_y2=y1+(y2-y1)/3*2

        self.cell_size = (l2_x1-l1_x1)
        self.cells_batch=pyglet.shapes.Batch()
        if self.cells == []:
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1-self.cell_size, y=l1_y2-self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1, y=l1_y2-self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1+self.cell_size, y=l1_y2-self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1-self.cell_size, y=l1_y2-2*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1, y=l1_y2-2*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1+self.cell_size, y=l1_y2-2*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1-self.cell_size, y=l1_y2-3*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1, y=l1_y2-3*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
            self.cells.append(pyglet.shapes.Rectangle(x=l1_x1+self.cell_size, y=l1_y2-3*self.cell_size, width=self.cell_size, height=self.cell_size, color=self.black, batch=self.cells_batch))
        else:
            self.cells[0].x=l1_x1-self.cell_size
            self.cells[0].y=l1_y2-self.cell_size
            self.cells[0].width=self.cell_size
            self.cells[0].height=self.cell_size
            self.cells[1].x=l1_x1
            self.cells[1].y=l1_y2-self.cell_size
            self.cells[1].width=self.cell_size
            self.cells[1].height=self.cell_size
            self.cells[2].x=l1_x1+self.cell_size
            self.cells[2].y=l1_y2-self.cell_size
            self.cells[2].width=self.cell_size
            self.cells[2].height=self.cell_size
            self.cells[3].x=l1_x1-self.cell_size
            self.cells[3].y=l1_y2-2*self.cell_size
            self.cells[3].width=self.cell_size
            self.cells[3].height=self.cell_size
            self.cells[4].x=l1_x1
            self.cells[4].y=l1_y2-2*self.cell_size
            self.cells[4].width=self.cell_size
            self.cells[4].height=self.cell_size
            self.cells[5].x=l1_x1+self.cell_size
            self.cells[5].y=l1_y2-2*self.cell_size
            self.cells[5].width=self.cell_size
            self.cells[5].height=self.cell_size
            self.cells[6].x=l1_x1-self.cell_size
            self.cells[6].y=l1_y2-3*self.cell_size
            self.cells[6].width=self.cell_size
            self.cells[6].height=self.cell_size
            self.cells[7].x=l1_x1
            self.cells[7].y=l1_y2-3*self.cell_size
            self.cells[7].width=self.cell_size
            self.cells[7].height=self.cell_size
            self.cells[8].x=l1_x1+self.cell_size
            self.cells[8].y=l1_y2-3*self.cell_size
            self.cells[8].width=self.cell_size
            self.cells[8].height=self.cell_size

        self.play_area = pyglet.shapes.Batch()
        self.line1 = pyglet.shapes.Line(l1_x1, l1_y1, l1_x2, l1_y2, width=5, color=(255,255,255,255), batch=self.play_area)
        self.line2 = pyglet.shapes.Line(l2_x1, l2_y1, l2_x2, l2_y2, width=5, color=(255,255,255,255), batch=self.play_area)
        self.line3 = pyglet.shapes.Line(l3_x1, l3_y1, l3_x2, l3_y2, width=5, color=(255,255,255,255), batch=self.play_area)
        self.line4 = pyglet.shapes.Line(l4_x1, l4_y1, l4_x2, l4_y2, width=5, color=(255,255,255,255), batch=self.play_area)

    def labels_calculate(self):
        for i in range(9):
            if self.x_o_labels[i]!=None:
                self.x_o_labels[i].x=self.cells[i].x+self.cell_size/2
                if self.x_o_labels[i].text=="X":
                    self.x_o_labels[i].font_size=self.cell_size/2
                    self.x_o_labels[i].y=self.cells[i].y+self.cell_size/1.7
                else:
                    self.x_o_labels[i].font_size=self.cell_size/1.3
                    self.x_o_labels[i].y=self.cells[i].y+self.cell_size/1.4
                    


    def on_resize(self, width, height):
        self.line_size = self.height/1.5
        self.player1.x=15
        self.player1.y=self.height-15
        self.player2.x=self.width-15
        self.player2.y=self.height-15
        self.player1.font_size=self.line_size/10
        self.player2.font_size=self.line_size/10
        self.play_area_calculate()
        self.labels_calculate()
        return super().on_resize(width, height)
    
    def on_draw(self):
        self.clear()
        self.cells_batch.draw()
        self.play_area.draw()
        self.player1.draw()
        self.player2.draw()
        self.x_o.draw()
    
    def change_player(self):
        if(self.player == 1):
            self.player = 2
            self.player1.font_size=self.line_size/10-5
            self.player2.font_size=self.line_size/10+5
        else:
            self.player = 1
            self.player1.font_size=self.line_size/10+5
            self.player2.font_size=self.line_size/10-5

    def draw_on_cell(self, cell,index):
        if(self.player == 1):
            self.x_o_labels[index]=pyglet.text.Label('X', x=cell.x+self.cell_size/2, y=cell.y+self.cell_size/1.7,font_name='Comic Sans MS', font_size=self.cell_size/2, bold=True, anchor_x='center', anchor_y='center', batch=self.x_o)
            self.change_player()
        else:
            self.x_o_labels[index]=pyglet.text.Label('o', x=cell.x+self.cell_size/2, y=cell.y+self.cell_size/1.4,font_name='Comic Sans MS', font_size=self.cell_size/1.3, bold=True, anchor_x='center', anchor_y='center', batch=self.x_o)
            self.change_player()

    def on_mouse_release(self, x, y, button, modifiers):
        for i in range(0,9):
            if self.intersects(x, y, self.cells[i]) and self.play_matrix[i//3][i%3] == 0:
                self.play_matrix[i//3][i%3] = self.player
                self.draw_on_cell(self.cells[i],i)
        if self.check_win()!=0:
            if not self.won:
                self.award_win(self.check_win())
                pyglet.clock.schedule_once(self.reset_game, 1)
        if self.check_draw():
            pyglet.clock.schedule_once(self.reset_game, 1)
            

    def award_win(self, player):
        if player == 1:
            self.player1_score+=1
        else:
            self.player2_score+=1
        self.update_score()
        self.won = True

    def update_score(self):
        self.player1.text = "Player 1: "+str(self.player1_score)
        self.player2.text = "Player 2: "+str(self.player2_score)

    def on_mouse_motion(self, x, y, dx, dy):
        for cell in self.cells:
            if(self.intersects(x, y, cell)):
                cell.color = self.grey
            elif cell.color == self.grey:
                cell.color = self.black


    def intersects(self, x, y, cell):
        if cell.x < x < cell.x+cell.width and cell.y < y < cell.y+cell.height:
            return True
        else:
            return False
        
    
    def on_key_release(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pyglet.app.exit()
        if symbol == key.R:
            self.play_matrix = [[0,0,0],[0,0,0],[0,0,0]]
            self.x_o_labels=[None,None,None,None,None,None,None,None,None]
            self.x_o.delete()
            self.x_o=pyglet.graphics.Batch()
        if symbol == key.F:
            self.set_fullscreen(not self.fullscreen)
            
    def check_win(self):
        for i in range(3):
            if self.play_matrix[i][0] == self.play_matrix[i][1] == self.play_matrix[i][2] != 0:
                return self.play_matrix[i][0]
            if self.play_matrix[0][i] == self.play_matrix[1][i] == self.play_matrix[2][i] != 0:
                return self.play_matrix[0][i]
        if self.play_matrix[0][0] == self.play_matrix[1][1] == self.play_matrix[2][2] != 0:
            return self.play_matrix[0][0]
        if self.play_matrix[0][2] == self.play_matrix[1][1] == self.play_matrix[2][0] != 0:
            return self.play_matrix[0][2]
        return 0
    
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.play_matrix[i][j] == 0:
                    return False
        return True

    def reset_game(self,dt):
        # count the 0s in the matrix
        count=0
        for i in range(0,3):
            for j in range(0,3):
                if self.play_matrix[i][j] == 0:
                    count+=1
        if count%2 != 0:
            if self.player == 1:
                self.player = 2
                self.player1.font_size=self.line_size/10-5
                self.player2.font_size=self.line_size/10+5
            else:
                self.player = 1
                self.player1.font_size=self.line_size/10+5
                self.player2.font_size=self.line_size/10-5

        self.play_matrix = [[0,0,0],[0,0,0],[0,0,0]]
        self.x_o_labels=[None,None,None,None,None,None,None,None,None]
        self.x_o=pyglet.graphics.Batch()
        self.won = False

         
        
        
        
