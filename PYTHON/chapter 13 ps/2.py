# t
# Step 1: Generate the multiplication table of 7 into a list
l = [str(7 * i) for i in range(1, 11)]

# Step 2: Combine the list elements into a single string separated by newlines
vertical_string = "\n".join(l)

# Step 3: Print the result
print(vertical_string)