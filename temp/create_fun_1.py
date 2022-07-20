#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 00:07:02 2022

@author: kamil
"""

import random
import math
import plotly.express as px
import pandas as pd
import pathlib

def divide(val, num=5, minSize=4):
     import random
     import math
     chunks = []
     for i in range(num-1):
         maxSize = math.ceil(val/(num-len(chunks)))
         newSize = random.randint(minSize, maxSize)
         val = val - newSize
         chunks.append(newSize)
     chunks.append(val)
     return chunks
def generate_function(trend, range_x):
    
    x = []
    y = []
    global_trend_plus = 0
    global_trend_minus = 0
    global_trend = 0
    x_coordinate = 0
    
    chunk_length = int(range_x/len(trend))
    ch = divide(range_x, len(trend), chunk_length)
    
    for i in range(len(trend)):
        
        for j in range(ch[i]):
            
            if x_coordinate % 10 == 0 and trend[i] == 'u':
                global_trend_plus += 10
            elif x_coordinate % 10 == 0 and trend[i] == 'd':
                global_trend_minus -= 10
            else:
                global_trend = 0
            x.append(x_coordinate)
            y.append(math.sin(x_coordinate * math.pi * random.random()) * 3.5
                     - math.cos(x_coordinate * math.pi * random.random()) * 3.5 + random.random() * 2
                     + global_trend_plus + global_trend_minus)
            
            x_coordinate += 1
            
    return x, y
def generate_trend(length = 5):
    result = []
    trends = ['u', 'c', 'd']
    for i in range(length):
        result.append(trends[random.randint(0,2)])
    
    return result

range_x = 1000
x, y = generate_function(generate_trend(12), range_x)
        
current_directory = str(pathlib.Path().resolve())

df = pd.DataFrame(dict(
    x = x,
    y = y
))

list_of_c = []
amp = 15
i  = 0
while i < (len(y)-1):
    print(i)
    temp = []
    y_first = y[i]
    temp.append(i)
    for j in range(i, len(y)-1):
        if abs(y[j+1]-y_first) < amp:
            temp.append(j+1)
        else:
            if len(temp) > 50:
                list_of_c.append(temp)
                i = j
            break
    i += 1


        
print('end loop')
print(len(list_of_c))

fig = px.line(df, x="x", y="y", title="Input") 

for i in list_of_c:
    fig.add_vrect(
        x0=i[0], x1=i[-1],
        fillcolor="LightSalmon", opacity=0.5,
        layer="below", line_width=0,
        )
    

file_name = 'figure'
file_name_temp = file_name
i = 1
path = pathlib.Path(current_directory + "/" + file_name + ".html")
while path.is_file():
    path = pathlib.Path(current_directory + "/" + file_name_temp + ".html")
    if path.is_file():
        print('file exists')
        file_name_temp = file_name + str(i)
    else:
        print('file does not exist')
    
    i += 1

file_name = file_name_temp
    
fig.write_html(current_directory + "/" + file_name + ".html")
    

print(current_directory + "/first_figure.html")
    
    