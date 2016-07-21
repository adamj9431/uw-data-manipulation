import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)

def reducer(key, list_of_values):
    person = key
    friendCount = sum(list_of_values)
    mr.emit((person, friendCount))    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
