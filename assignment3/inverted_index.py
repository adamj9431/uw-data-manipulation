import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = [docid, documentText]
    docid, text = record
    words = text.split()
    emittedWords = set()
    for word in words:
        if word not in emittedWords:
            mr.emit_intermediate(word, docid)
            emittedWords.add(word)

def reducer(key, list_of_values):
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
