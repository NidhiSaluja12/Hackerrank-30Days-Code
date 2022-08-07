import math
import os
import random
import re
import sys



def solve(meal_cost, tip_percent, tax_percent):
    
    tip = (tip_percent*meal_cost)/100
    tax = (tax_percent*meal_cost)/100
    total = meal_cost+tip+tax
    return int(round(total))

if __name__ == '__main__':
    meal_cost = float(raw_input().strip())

    tip_percent = int(raw_input().strip())

    tax_percent = int(raw_input().strip())

    res = solve(meal_cost, tip_percent, tax_percent)
    print(res)

