import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    sequence_id, nucleotides = record
    #remove last 10 characters
    nucleotides = nucleotides[:-10]
    mr.emit_intermediate(nucleotides, None)

def reducer(key, list_of_values):
    mr.emit(key)    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
