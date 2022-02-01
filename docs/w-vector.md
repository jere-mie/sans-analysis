# w~ vector

This encodes the angular variation in phase state of a spherical vesicle.  
Essentially, each element of w~ (w~ is of length L) is the "lth" grand sum of each Clij matrix. The grand sum of a matrix is simply the sum of all its elements. We can use [numpy](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html) to do this automatically:

```py
import numpy as np
x = np.matrix([[1, 2], [4, 3]])
print("x.sum") # prints 10
```

![w vector calculations](https://media.discordapp.net/attachments/937419611622752277/937897088841285662/unknown.png)

## Note: W~ matrix

![W matrix](https://media.discordapp.net/attachments/937419611622752277/937899089822109716/unknown.png)
