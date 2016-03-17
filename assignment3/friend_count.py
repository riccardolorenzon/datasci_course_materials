import MapReduce
import sys

"""
Friends count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person_a = record[0]
    person_b = record[1]

    # assumption: person_a is friend of person_b doesn't imply the opposite
    mr.emit_intermediate(person_a, 1)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
