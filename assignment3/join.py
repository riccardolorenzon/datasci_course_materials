import MapReduce
import sys

"""
Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: table identifier
    # value: attributes
    key = record[0]
    order_id = record[1]
    attributes = record[2:]
    mr.emit_intermediate(order_id, [key, attributes])

def reducer(key, list_of_values):
    # key: word
    # list_of_values: list of attributes lists
    orders = [t[1] for t in list_of_values if t[0] == 'order']
    line_items = [t[1] for t in list_of_values if t[0] == 'line_item']

    for order in orders:
        for line_item in line_items:
            res = []
            res.append('order')
            res.append(key)
            res.extend(orders)
            res.append('line_item')
            res.append(key)
            res.extend(line_items)
            mr.emit(res)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
