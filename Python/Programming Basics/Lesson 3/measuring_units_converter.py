size = float (input())
source_metric = input()
dest_metric = input()

if source_metric == 'mm':
     size = size/ 1000
if source_metric == 'cm':
     size = size / 100
if source_metric == 'mi':
     size = size / 0.000621371192
if source_metric == 'in':
     size = size / 39.3700787
if source_metric == 'km':
     size = size / 0.001
if source_metric == 'ft':
     size = size / 3.2808399
if source_metric == 'yd':
     size = size / 1.0936133
if dest_metric == 'km':
     size = size * 0.001
if dest_metric == 'mm':
     size = size * 1000
if dest_metric == 'cm':
     size = size * 100
if dest_metric == 'mi':
     size = size * 0.000621371192
if dest_metric == 'in':
     size = size * 39.3700787
if dest_metric == 'ft':
     size = size * 3.2808399
if dest_metric == 'yd':
     size = size * 1.0936133

print((F'{size}'))
