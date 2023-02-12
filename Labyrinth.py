import os 
import colorama as cl

def print_maze (solution,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]==0:
                print (cl.Fore.RED + "▅" ,end=" ")
                continue
            if solution[i][j] ==1:
                print (cl.Fore.GREEN + "▅" ,end=" ")
                continue
            print (cl.Fore.WHITE + "▅" ,end=" ")
        print("")
            
def is_valid (maze,x,y):
    return x>=0 and y>=0 and x<len(maze) and y<len(maze[x]) and maze[x][y]==1

def posibilities(current_cell:tuple , maze,desitions):
    x,y=current_cell
    posibilities = []
    if x!=len(maze)-1 and  not (x+1,y) in desitions[current_cell] :
       posibilities.append((x+1,y))
    if y!=len(maze[x])-1 and  not (x,y+1) in desitions[current_cell]:
       posibilities.append((x,y+1))
    if y>0 and  not (x,y-1) in desitions[current_cell]:
       posibilities.append((x,y-1))
    if x>0 and  not (x-1,y) in desitions[current_cell]:
       posibilities.append((x-1,y))

    return posibilities

def solve(maze):
    solution =[[0]*len(maze[i]) for i in range(len(maze))];
    visited =[]
    desitions={}
    i_can_move =True
    current_cell=(0,0)
    solution[0][0]=1

    while current_cell!=(len(maze)-1,len(maze[0])-1) and i_can_move:
        if current_cell in desitions:
            directions = posibilities(current_cell,maze,desitions)
        else:
            desitions[current_cell]=[]
            directions = posibilities(current_cell,maze,desitions)          
        for index,tuple_dir in enumerate(directions):
            x,y=current_cell
            i,j=tuple_dir
            desitions[current_cell].append((i,j))
            if is_valid(maze,i,j) and not (i,j) in visited:
                    solution[i][j]=1
                    visited.append(current_cell) 
                    current_cell=(i,j)
                    break
            elif is_valid(maze,i,j) :
                if index == len(directions)-1:
                    visited.append(current_cell)
                    solution[x][y]=0
                    current_cell=(i,j)
                    break
                else:
                    desitions[current_cell].pop()
            elif index == len(directions)-1:
                i_can_move=False
    return solution


if __name__ == "__main__":
    maze = [[1,0,1,1,1,0],
            [1,0,1,0,1,1],
            [1,0,1,1,1,1],
            [1,0,1,1,0,1],
            [1,1,1,0,0,1],
            [1,1,0,1,1,1]]
    solution=solve(maze)
    print_maze(solution,maze)