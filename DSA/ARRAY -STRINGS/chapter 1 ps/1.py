matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
target = 8

# ==========================================
# 1. GALAT APPROACH (Jo aap test karna chah rahe thay):
# Agar aap seedha yeh likhte: if target in matrix:
# Toh Python yeh dekhega ke kya 8 poori row [1, 2, 3, 4] ke barabar hai.
# Result: Hamesha False aayega kyunki 8 koi poori row nahi hai.
# ==========================================


# ==========================================
# 2. SAHI APPROACH (Function ke sath):
# ==========================================

def searchMatrix(matrix, target):
    # Step 1: 'for row in matrix' matrix me se ek-ek poori row ko baahar nikalta hai.
    for row in matrix:
        
        # Step 2: 'if target in row' us choti row ke andar ja kar check karta hai 
        # ke kya target (jaise 8) us row ke andar mojood hai ya nahi.
        if target in row:
            return True  # Agar target mil gaya, toh yahin se True return kar do.
            
    # Step 3: Agar poori matrix check ho jaye aur target kahin na mile, toh False return karo.
    return False

# Function ko call kar ke terminal par print karana:
print(searchMatrix(matrix, target))