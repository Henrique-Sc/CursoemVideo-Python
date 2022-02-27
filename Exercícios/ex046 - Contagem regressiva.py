from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('')
print(emojize(':boom:', use_aliases=True) * 11)

print('\033[31mBOM! BOOOMM!! POOOWW!!\033[m')
print('\n\033[34mFogos estourados!!\033[m')
