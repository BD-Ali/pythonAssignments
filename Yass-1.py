
from sympy import symbols, sympify
from types import *
import numpy as np


def str_to_func(function_str: str):
  x = symbols('x')

  function = sympify(function_str)
  return lambda val: function.subs(x, val)


def Secant_method(function: str, x0: float, x1: float) -> float:
  f = str_to_func(function)
  epsilon = 0.001
  max_iter = 30

  for _ in range(max_iter):
    fx0 = f(x0)
    fx1 = f(x1)

    if abs(fx1) < epsilon:
      return x1

    if abs(fx1 - fx0) < 1e-10:
      return x1

    x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

    if abs(x_next - x1) < epsilon:
      return x_next

    temp = x1
    x1 = x_next
    x0 = temp

  return x1


def ge(matrix: list[list[float]]) -> list[list[float]]:
  r = len(matrix)
  if r == 0:
    return matrix

  c = len(matrix[0])
  mat = [row.copy() for row in matrix]

  for i in range(min(r, c - 1)):
    if mat[i][i] == 0:
      for j in range(i + 1, r):
        if mat[j][i] != 0:
          temp = mat[i]
          mat[i] = mat[j]
          mat[j] = temp
          break

    if mat[i][i] == 0:
      continue

    pivot = mat[i][i]
    for k in range(i, c):
      mat[i][k] /= pivot

    for j in range(i + 1, r):
      factor = mat[j][i]
      for k in range(i, c):
        mat[j][k] -= factor * mat[i][k]

  return mat

