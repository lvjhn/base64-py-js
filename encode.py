import base64 
import array 

items      = [1, 2, 3, 4, 5]
items_b    = array.array("f", items).tobytes() 
base64_str = base64.b64encode(items_b).decode("utf-8") 

print(base64_str)