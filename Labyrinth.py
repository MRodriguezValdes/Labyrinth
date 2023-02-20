import colorama as cl


#Print the way to the exit ...
def print_maze_way (solution:list[tuple[int,int]],maze:list[list[int]],start:tuple,end:tuple)->None:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i,j) == start:
                print (cl.Fore.BLUE + "▅" ,end=" ")
                continue
            if (i,j) ==end:
                print (cl.Fore.BLUE + "▅" ,end=" ")
                continue
            if maze[i][j]==0:
                print (cl.Fore.RED + "▅" ,end=" ")
                continue
            if  (i,j) in solution:
                print (cl.Fore.GREEN + "▅" ,end=" ")
                continue
            print (cl.Fore.WHITE + "▅" ,end=" ")
        print()


#Print the labyrinth we want to solve ...
def print_maze(maze:list[list[int]],start:tuple,end:tuple) ->None:
    for i in range(len(maze)):
            for j in range(len(maze[i])):
                if (i,j) == start:
                    print (cl.Fore.BLUE + "▅" ,end=" ")
                    continue
                if maze[i][j]==0:
                    print (cl.Fore.RED + "▅" ,end=" ")
                    continue
                if (i,j) ==end : 
                    print (cl.Fore.BLUE + "▅" ,end=" ")
                    continue
                print (cl.Fore.WHITE + "▅" ,end=" ")
            print()


def generate_maze(blocks:list[tuple[int,int]],rows:int,columns:int)->list[list[int]]:
    maze:list[list[int]] = [[0]*columns for i in range(rows)]
    for i in range ( rows):
        for j in range(columns):
            if (i,j) in blocks:
                maze[i][j]=0
                continue
            
            maze[i][j]=1
    return maze


def is_valid (maze:list[list[int]],next_cell:tuple[int,int])->bool:
    x,y=next_cell
    return x>=0 and y>=0 and x<len(maze) and y<len(maze[x]) and maze[x][y]==1


def generate_next_movement(current_cell:tuple[int,int] , maze:list[list[int]] ,desitions:dict)->tuple[int,int]:
   
    x,y=current_cell
    
    desitions.setdefault(current_cell,[])

    if x!=len(maze)-1 and  not (x+1,y) in desitions[current_cell]  and not (x+1,y) in desitions['wait-desitions']:
        desitions['indications_of_movements'].append('Abajo')
        return (x+1,y)
    if y!=len(maze[x])-1 and  not (x,y+1) in desitions[current_cell] and not (x,y+1) in desitions['wait-desitions']:
        desitions['indications_of_movements'].append('Derecha')
        return (x,y+1)
    if y>0 and  not (x,y-1) in desitions[current_cell] and not (x,y-1) in desitions['wait-desitions']:
        desitions['indications_of_movements'].append('Izquierda')
        return (x,y-1)
    if x>0 and  not (x-1,y) in desitions[current_cell] and not (x-1,y) in desitions['wait-desitions']:
        desitions['indications_of_movements'].append('Arriba')
        return (x-1,y)
    return (-1,-1)


def solve(maze:list[list[int]] ,x:int,y:int ,endX:int,endY:int) -> tuple[list[int],list[str]]:
    
    desitions:dict={'indications_of_movements':['Salida'],'way':[(x,y)],'wait-desitions':[]}
    i_can_move:bool =True
    current_cell:tuple=(x,y)

   #We want to generate movements until  we're  on the exit or we haven't more movements
    while  current_cell != (endX,endY) and i_can_move:
        
        #If you want to see all the steps to solve our maze, please uncomment this 
        # print_maze_way(desitions["way"],maze,(x,y),(endX,endY))
        # print("\n\n")
        
        next_cell:tuple = generate_next_movement(current_cell,maze,desitions)
        desitions[current_cell].append(next_cell)
        
        if is_valid(maze,next_cell): 
            if not next_cell in desitions: 
                current_cell=next_cell
                desitions['way'].append(current_cell)
                continue
            
            # We always want our last decision to be to go back, we need to implement any move first.
            else:
                desitions[current_cell].pop()
                desitions['wait-desitions'].append(next_cell)
                desitions['indications_of_movements'].pop()
                continue
        
        # If we do not have any movement, we check if our waiting list is empty and our first position on the road where it is the beginning is not eliminated. 
        elif next_cell == (-1,-1) and len(desitions['wait-desitions'])!=0 and len(desitions['way']) > 1:
            current_cell=desitions['wait-desitions'].pop()
            desitions['way'].pop()

        # In this case we can't move      
        elif next_cell == (-1,-1):
            i_can_move=False
            print("I haven't any solution")

        #If the movement  not is valid we remove it of our indications list
        if (len(desitions['indications_of_movements'])>1):
            desitions['indications_of_movements'].pop()
        
    return  desitions['way'],desitions['indications_of_movements']



if __name__ == "__main__":
    print("------------------Creating Maze------------------")
    columns:int= int(input("How many columns do you want: "))
    rows:int = int(input("How many rows do you want: "))
    x_Start :int= int(input("X coordinate to the start: "))
    y_Start:int = int(input("Y coordinate to the start: "))
    x_End:int=int(input("X coordinate to the end: "))
    y_End:int=int(input("Y coordinate to the end: "))
    print("*******************************************")
    blocks:list[tuple]=[(0,1),(2,1),(2,2),(2,3),(1,3),(0,5),(4,0),(4,2),(4,3),(5,0),(5,3),(3,3)]
    maze:list[list[int]] = generate_maze(blocks,rows,columns)
    print("------------------Maze------------------")
    print_maze(maze,(x_Start,y_Start),(x_End,y_End))
    print("----------------Solution----------------")
    solution,indications=solve(maze,x_Start,y_Start,x_End,y_End)
    print_maze_way(solution,maze,(x_Start,y_Start),(x_End,y_End))
    print("*******************************************")
    print("----------------Coordenates-----------------")
    print (solution)
    print("\n----------------------Indications-----------------------")
    print (indications)
