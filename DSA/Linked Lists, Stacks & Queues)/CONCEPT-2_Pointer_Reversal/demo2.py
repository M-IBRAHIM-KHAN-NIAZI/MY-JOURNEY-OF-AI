# =====================================================================
# CONCEPT-2: POINTER REVERSAL (PURE CONCEPTUAL EXPLANATION)
# =====================================================================
# 
# 1. BASICS & PURPOSE:
#    - Linked List mein pointer reversal ka asal maqsad hota hai dabbon ke 
#      arrows (connections) ko seedhe se ulta karna. 
#    - Jaise list pehle aage ki taraf ja rahi thi (1 -> 2 -> 3 -> None), 
#      usko palat kar ulta karna (None <- 1 <- 2 <- 3).
#
# 2. INITIAL SETUP (STARTING STATE):
#    - `prev = None` (Peeche wala rasta): Isko shuru mein None rakhte hain 
#      kyunki jab pehla dabba ulta hoga, toh usne aakhir mein jaakar list ka 
#      tail (end) banna hai, aur aakhri dabbe ke baad hamesha None hota hai.
#    - `current` (Current dabba): Yeh woh dabba hota hai jahan hum is waqt 
#      khade hote hain (shuruwat hamesha head se hoti hai).
#
# 3. THE CORE LOOP & MOVEMENT LOGIC (while loop):
#    - Jab tak hum aakhri dabbe tak nahi pahunch jaate, yeh 3 kaam bar bar 
#      repeat hote hain:
#
#    --- STEP 1: BACKUP / SAVING THE NEXT ADDRESS ---
#    - Kyunki aage jaakar hum current node ka arrow palatne wale hain, isliye 
#      agar hum agle node ka pata pehle se save nahi karenge toh wo hamesha 
#      ke liye kho jayega. 
#    - Isliye sabse pehle aage wale dabbe ka pata ek safe jagah save kar lete hain.
#
#    --- STEP 2: REVERSING THE ARROW (FLIPPING) ---
#    - Yahi asal reversal hai! 
#    - `current.next` ka matlab hai "current node ke aage wala arrow". 
#      Jab hum usko `prev` ke barabar kar dete hain, toh wo aage jane ke 
#      bajaye pichhe ki taraf jud jata hai.
#
#    --- STEP 3: SHIFTING THE POINTERS FORWARD ---
#    - Ek dabba ulta ho chuka, ab aage barhna hai.
#    - `prev` uth kar current dabbe par aa jata hai (ke ab tu pichhla hissa ban gaya hai).
#    - `current` uth kar us safe kiye hue agle dabbe par chala jata hai taake 
#      wahan bhi yhi process chal sake.
#
# 4. FINAL RESULT:
#    - Jab `current` chalte-chalte aakhri dabbe se bhi aage nikal kar `None` 
#      par pahunch jata hai, toh loop khud-b-khud ruk jata hai.
#    - Is point par, hamara `prev` pointer aakhri valid dabbe par baitha hota hai, 
#      jo ke ab ulta hokar nayi list ka HEAD (shuruwat) ban chuka hota hai. 
#    - Hum bas us `prev` ko wapas return kar dete hain, aur hamari poori list 
#      seedhi se ekdum ulti milti hai!
# =====================================================================