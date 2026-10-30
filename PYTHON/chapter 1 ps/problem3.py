import os

# Specify the directory path you want to list (use '.' for the current directory)
directory_path = "."

# Get the list of all files and directories in the specified path
contents = os.listdir("/")

print(f"Contents of '{directory_path}':")
for item in contents:
  print(item)