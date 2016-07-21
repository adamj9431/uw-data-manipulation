import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    o_rows = []
    li_rows = []
    for record in list_of_values:
        if record[0] == "order":
            o_rows.append(record)
        elif record[0] == "line_item":
            li_rows.append(record)
    for o_row in o_rows:
        for li_row in li_rows:
            mr.emit(o_row + li_row)    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
