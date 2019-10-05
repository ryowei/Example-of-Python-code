#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:10:03 2019

@author: chibaryowei
"""

import Module_cale

print("Product:", Module_cale.product(5))
print("add:"    , Module_cale.add(5))


# 讓Python知道，這邊就是程式的進入點
if __name__ == "__main__":
    import sys
    import cale
    print("argv[0]:", sys.argv[0] )
    print("Product:", cale.product(int(sys.argv[1])))
    print("Add:", cale.add(int(sys.argv[1])))