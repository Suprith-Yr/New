import random

def allocate_resources(resources, elements):
 
  
  allocation = {}

  for element in elements:
    resource = random.choice(resources)
    while resource in allocation.values():
    
      resource = random.choice(resources)

    
    allocation[element] = resource
  return allocation


resources = ["CPU", "Memory", "Disk"]

elements = ["Process 1", "Process 2", "Process 3"]

allocation = allocate_resources(resources, elements)

print(allocation)