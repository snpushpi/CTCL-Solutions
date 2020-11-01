def flood_fill(screen,x,y,prevc,newc):
    if x<0 or x>len(screen[0]) or y<0 or y>len(screen) or screen[x][y]!=prevc or screen[x][y]==newc:
        return 
    screen[x][y]=newc
    flood_fill(screen,x+1,y,prevc,newc)
    flood_fill(screen,x-1,y,prevc,newc)
    flood_fill(screen,x,y+1,prevc,newc)
    flood_fill(screen,x,y-1,prevc,newc)

def main(screen,x,y,newc):
    prevc = screen[x][y]
    flood_fill(screen,x,y,prevc,newc)
    return screen