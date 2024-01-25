import random

def allocate_resources(resources, elements):

  

  # Iterate over the elements.
  for element in elements:
    # Choose a random resource.
    resource = random.choice(resources)

    # Add the resource to the allocation.
    allocation[element] = resource

  # Return the allocation.
  return allocation


# Create a list of resources.
resources = ["CPU", "Memory", "Disk"]

# Create a list of elements.
elements = ["Process 1", "Process 2", "Process 3"]

# Allocate the resources.
allocation = allocate_resources(resources, elements)

# Print the allocation.
print(allocation)


