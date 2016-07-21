import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# assuming 5x5 matrices
A_COLS = 5

def mapper(record):
    matrix, i, j, value = record
    
    for k in range(A_COLS):
        if matrix=="a":
            mr.emit_intermediate((i,k), (j, value))
        elif matrix=="b":
            mr.emit_intermediate((k,j), (i, value))

def reducer(key, list_of_values):
    i, j = key
    cells = {}
    for tup in list_of_values:
        k, value = tup
        if k not in cells:
            cells[k] = [value, 0]
        else:
            cells[k][1] = value
    dotProduct = 0
    for cell in cells.values():
        dotProduct += cell[0]*cell[1]
    
    mr.emit((i, j, dotProduct))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
