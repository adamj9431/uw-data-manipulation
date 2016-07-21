import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

DIR_FRIEND = 0
DIR_FOLLOWER = 1

def mapper(record):
    person, friend = record
    mr.emit_intermediate(person, (DIR_FRIEND, friend))
    mr.emit_intermediate(friend, (DIR_FOLLOWER, person))

def reducer(key, list_of_values):
    person = key
    friends = set()
    followers = set()
    for tup in list_of_values:
        if tup[0] == DIR_FRIEND:
            friends.add(tup[1])
        elif tup[0] == DIR_FOLLOWER:
            followers.add(tup[1])
    for follower in followers:
        if follower not in friends:
            mr.emit((person, follower))
            mr.emit((follower, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
