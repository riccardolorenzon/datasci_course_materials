import MapReduce
import sys

"""
Asymmetric friendship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person_a = record[0]
    person_b = record[1]
    s = sorted([person_a, person_b])
    key = ' '.join(s)
    # assumption: person_a is friend of person_b doesn't imply the opposite
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    friends = key.split(' ')

    if len(list_of_values) == 1:
        mr.emit((friends[0], friends[1]))
        mr.emit((friends[1], friends[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
