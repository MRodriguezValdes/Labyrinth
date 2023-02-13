import os 
import colorama as cl


def print_maze_way (solution,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]==0:
                print (cl.Fore.RED + "▅" ,end=" ")
                continue
            if solution[i][j] ==1:
                print (cl.Fore.GREEN + "▅" ,end=" ")
                continue
            print (cl.Fore.WHITE + "▅" ,end=" ")
        print()


def generate_maze(blocks,rows,columns):
    maze = [[0]*columns for i in range(rows)]
    for i in range ( rows):
        for j in range(columns):
            if (i,j) in blocks:
                maze[i][j]=0
                continue
            maze[i][j]=1
    return maze


def print_maze(maze:list[list[int]]):
    for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j]==0:
                    print (cl.Fore.RED + "▅" ,end=" ")
                    continue
                print (cl.Fore.WHITE + "▅" ,end=" ")
            print()

            
def is_valid (maze,x,y):
    return x>=0 and y>=0 and x<len(maze) and y<len(maze[x]) and maze[x][y]==1


def generate_desition_key(current_cell,desitions:dict):
    desitions.setdefault(current_cell,[])
    return desitions


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
    solution[0][0]=1
    visited =[]
    desitions={}
    i_can_move =True
    current_cell=(0,0)
    
    while current_cell!=(len(maze)-1,len(maze[0])-1) and i_can_move:
        desitions  = generate_desition_key(current_cell,desitions)
        directions = posibilities(current_cell,maze,desitions)   
       
        change=False      
        for index,next_cell in enumerate (directions):
            x,y=current_cell
            i,j=next_cell
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
                    change=True
            elif index == len(directions)-1 and not change:
                i_can_move=False
                print("I don't have any solution")
    return solution


if __name__ == "__main__":
    print("------------------Creating Maze------------------")
    columns= int(input("How many columns do you want: "))
    rows = int(input("How many rows do you want: "))
    print("*******************************************")
    blocks=[(0,1),(2,1),(2,2),(2,3),(1,3),(0,5),(4,0),(4,1),(4,2),(4,3),(5,0),(5,1),(5,2),(3,3)]
    maze = generate_maze(blocks,rows,columns)
    print("------------------Maze------------------")
    print_maze(maze)
    print("----------------Solution----------------")
    solution=solve(maze)
    print_maze_way(solution,maze)