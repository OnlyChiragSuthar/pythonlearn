# with open("myline.txt","r") as f:
#     f.seek(3)
#     text = f.read(5)
#     print(text)

# with open('file.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(10)

#   # Read the next 5 bytes
#   data = f.read(5)

with open('myline.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  g = f.seek(current_position)
  print(g)

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)

# with open('sample.txt', 'r') as f:
#   print(f.read())