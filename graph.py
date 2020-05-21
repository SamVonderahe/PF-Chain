# libraries
'''import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns'''


f = open("final", "r")
num_albums = 0;
for x in f:
  num_albums += 1
num_albums = int(num_albums / 3)

albums = ["Album"] * num_albums
ratings = ["Rating"] * num_albums
#year = ["Year"] * num_albums


f.seek(0)
for i in range(num_albums):
  f.readline()
  line = f.readline()
  while line.find('|') == -1 and len(line) > 0:
    line = f.readline()
  if len(line) == 0:
    break
  line = line.rstrip()
  line = line.split("|")
  albums[i] = line[0][1:]
  ratings[i] = line[1][1:]
  line = f.readline()
  line = line.rstrip()
  line = '(' + line + ')'
  albums[i] = albums[i] + line

albums=albums[::-1]
ratings=ratings[::-1]

f.close()
i = 0
while i < int(num_albums):
  while albums[i] == "Album":
    i += 1
  print(albums[i] + ': ')
  if ( ratings[i] == '10' ):
    for l in range(100):
      print('|', end='')
    print('10')
    print()
  else:
      for k in range(int(ratings[i].replace('.',''))):
        print('|', end='')
      print(ratings[i])
      print()
  i += 1



 
# data
#df=pd.DataFrame({'x': range(0,11), 'y': range(0,11) })
 
# plot
#plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
'''plt.plot(albums, ratings)
plt.axis('on')
plt.axis([0, num_albums, 0, 10])
plt.axis('image')
plt.show()'''

