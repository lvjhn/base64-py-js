import base64
import array 

string      = "AQAAAAIAAAADAAAABAAAAAUAAAA="
string_b    = base64.b64decode(string)

items       = array.array('i')
items.frombytes(string_b)
items       = items.tolist()

print(items)


