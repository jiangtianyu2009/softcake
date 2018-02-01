import re

strss = '[abc-123]kajjgkkrk'
print(re.split('[\[\]]', strss)[1])
