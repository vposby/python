"""
Sudoku
v 0.1 - create working solution generator
"""

import sys,random,pprint,pdb #pygame

def randomize(): #rearranges nums
    nums=[]
    for i in range(9):
        nums.append(str(i+1))
    iters=random.randrange(25,51)
    for i in range(iters):
        index=random.randrange(0,9)
        nums.append(nums[index])
        nums.pop(index)
    return(nums)

def gridPop():
    for i in range(9):
        row.update({i+1:[]})
        box.update({i+1:[]})
        grid['row'][i+1]=randomize()
        for j in range(9):
            if len(col)<9: col.update({j+1:[]})
            grid['col'][j+1].append(grid['row'][i+1][j])
        """
        if i<3:
            for k in range(9):
                if len(grid['box'][i+1][k+1])<3:
        """

def verify(grid):
    print('not defined yet')

row={}
col={}
box={}
grid={'row':row,'col':col,'box':box}

gridPop()
pprint.pprint(grid)
sys.exit()
