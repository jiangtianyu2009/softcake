import re

str = '[abc-123]kajjgkkrk'
print(re.split('[\[\]]', str)[1])