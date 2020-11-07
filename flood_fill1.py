def recurse(x,y,color,screen, prev_col):
    if x<0 or x>len(screen) or y<0 or y>len(screen[0]) or screen[x][y]!=prev_col or screen[x][y]==color:
        return 
    screen[x][y]=color
    recurse(x+1,y,color,screen, prev_col)
    recurse(x,y+1,color,screen,prev_col)
    recurse(x-1,y,color,screen, prev_col)
    recurse(x,y-1,color,screen, prev_col)

def main(screen,color,x,y):
    prev_col = screen[x][y]
    recurse(x,y,color, screen, prev_col)
    return screen
