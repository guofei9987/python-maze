## python-maze
Generate a maze using Python  

```py
import matplotlib.pyplot as plt
import numpy as np


from maze import Maze
maze=np.zeros(shape=(100,100))
start_point=np.array([0,0])
maze_generator=Maze(maze, start_point)
plt.imshow(maze_generator.maze)
```

![maze](http://www.guofei.site/pictures_for_blog/algorithm/maze/maze1_2.png)

## Generate a maze with a picture using Python
```py
import cv2
pic = cv2.imread('duck.jfif')
pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
pic = cv2.resize(pic, (100, 100))
pic = (pic > pic.mean()) * (-1)

from maze import Maze

start_point=np.array([50,50])
maze_generator=Maze(pic, start_point)
plt.imshow(maze_generator.maze)
```
![duck_maze](https://github.com/guofei9987/python-maze/blob/master/duck_maze.png?raw=true)

If you want to know why it works, see [here](http://www.guofei.site/2019/06/22/maze.html)

Go and try other pictures
![heart_maze](https://github.com/guofei9987/python-maze/blob/master/heart.png?raw=true)
