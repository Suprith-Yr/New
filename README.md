import random

def allocate_resources(resources, elements):
  """Allocates resources to elements.

  Args:
    resources: A list of resources.
    elements: A list of elements.

  Returns:
    A dictionary mapping elements to resources.
  """

  # Create a dictionary to store the allocation.
  allocation = {}

  # Iterate over the elements.
  for element in elements:
    # Choose a random resource.
    resource = random.choice(resources)

    # Check if the resource is already allocated to another element.
    while resource in allocation.values():
      # If the resource is already allocated, choose another one.
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