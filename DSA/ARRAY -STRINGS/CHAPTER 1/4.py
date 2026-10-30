row,cols=3,4
matrix=[[int(input(f"value [{i}[{j}]: ")) for j in range(cols)] for i in range(row)]
for row in matrix:
    print(row) 
    

#     rows, cols = 3, 4
# # Har row ke andar columns ke liye loop chalega
# matrix = [[int(input(f"Val [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
