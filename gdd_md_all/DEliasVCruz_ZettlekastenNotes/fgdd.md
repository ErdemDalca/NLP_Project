# lang.py.module.numpy.array

Basic numpy unit for creating multidimensional data

## Synopsis

```py
  import numpy as np

  vector = np.array(<data>)
```

## Overview

The basic unit in `NumPy` is an array and it can have an arbitrary number of
dimension

### Attributes

All **arrays** share this **attributes**:

- `.shape`: **Check the dimensionality** of your array as a [tuple](./hsr4.md)
- `.size`: Check the **total number of values** in your array
- `.dimension`

## Cookbook

### Create a basic numpy array

When done **manually** they are usually **created from** a [list](./7cxo.md)

```py
  import numpy as np

  vector = np.array([[1, 2, 3], [4, 5, 6]])
  vector.shape

# Out: (2, 3)
"""
  An array of two dimentions
    - Two rows
    - Three columns
"""
```

### Create an array from a range

You can use the `arange` method to create an array from
a range similar to using the `range` method

```py
import numpy as np

arr = np.arange(5)
print(arr)

# Out: array([0, 1, 2, 3, 4])
```

### Get the dimensions and shape of an array

An array can have multiple dimension, for example a 1 dimensional
array will be a normal single `list` like `[0, 1, 2]` but a
two dimensional array will be a `list` of `lists` like `[[1, 2], [3, 4]]`

- You can inspect the dimensions of an array with the `dimension`
  attribute

- You can inspect the shape of an array with the `shape` attribute

```py
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])

print(arr1.dimension, arr1.shape, sep=" ")

# Out: 1 (1, 3)

print(arr2.dimension, arr2.shape, sep=" ")

# Out: 2 (3, 2)
```
