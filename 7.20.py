#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:48:51 2021

@author: nurguliminova
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:43:09 2021

@author: nurguliminova
"""
import random
import numpy

counts = [10**x for x in range(0,7)];
def generate_list(size):
   l = []
   for i in range(size):
       l.append(random.randint(0,7))

def generate_array(size):
   l = numpy.random.rand(size)

# You generated functions, but never ran them. -10