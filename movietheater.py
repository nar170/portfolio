# -*- coding: utf-8 -*-
"""MovieTheater.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kgzWgJzNPIyzydJPLQuMNxa0IWUvjCTx
"""

patrons = 20
adcost = 200
print("# Ads | Profits")

for i in range (0,201,25):
  ad = float(i)
  total = float(2*round(adcost**0.5) + patrons)
  profits = float((total * 10) - i - adcost)
  print(f"{int(ad)} | ${profits}")