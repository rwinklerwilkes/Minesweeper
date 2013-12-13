__author__ = 'Rich'
#set mouse button values, according to pygame
LEFT = 1
RIGHT = 3
#match difficulty to size, in rows
diff = {'easy':5,'medium':8,'hard':12}
#match difficulty to total number of mines
mine = {'easy':3,'medium':10,'hard':30}
#grey, in RGB
grey = (211,211,211)
#match number of neighbors to images
digit_img= {i:'Images/' + str(i) + '.png' for i in range(1,9)}
#set number 3 from top and left, in pixels
sq_num_offset = 3
img = ['Images/square.png','Images/flag.png','Images/mine.png','Images/down.png']
img_square = 0
img_flag = 1
img_mine = 2
img_down = 3