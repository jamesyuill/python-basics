import converters # getas entire doc, access through dot

from converters import lbs_to_kg # more specific import of function

# import utils
from utils import find_max

numbers = [3,4,6,7,8]
maximum = find_max(numbers)
print(maximum)

print(converters.kg_to_lbs(70))

lbs_to_kg(30)