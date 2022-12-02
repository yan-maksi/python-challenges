""" 
-- Task - Breaking prisoners out of a unique prison using lists, logic, and loops --
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. 
A 1 represents an unlocked cell and a 0 represents a locked cell.
[1, 1, 0, 0, 0, 1, 0]
Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free,
with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked 
cells become locked again. You can only move from left to right and not go back.
 
[1, 1, 0, 0, 0, 1, 0]
You free the prisoner in the 1st cell
The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

Examples:
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
freed_prisoners([0, 0, 0]) ➞ 0
freed_prisoners([1, 1, 1]) ➞ 1

Notes:
You must free a prisoner in order for the locks to switch. So in the second example where 
the input is [1, 1, 1] after you release the first prisoner, the locks change to [0, 0, 0]. 
Since all cells are locked, you can release no more prisoners.
You always start within the leftmost element in the list (the first prison cell). 
If all the prison cells to your right are zeroes, you cannot free any more prisoners.
"""

import itertools 

def freed_prisoners(prison):
    groups = [[k, list(v)] for k, v in itertools.groupby(prison)]
    freed = [k for k, v in groups]
    persons = len(freed) if freed[0] == 1 else 0 
    print(f"Freed {persons} persons")
  
if __name__ == "__main__":
    cells = [int(item) for item in input("Enter the items: ").split(",")]
    print(f'Your list of items is: {cells}')
    freed_prisoners(cells)
