# =====================================================================================
#                      A to Z CONCEPT: OVERLAP LOGIC IN INTERVALS
# =====================================================================================
#
# 1. PEHLA QUESTION: START TIME KI BASE PAR SORTING KYUN ZAROORI HAI?
# -------------------------------------------------------------------------------------
# - Jab hum 'intervals.sort(key=lambda x: x[0])' karte hain, toh hum time ko ek
#   seedhi line (timeline) par set kar dete hain.
# - Is sorting ka sabse bada fayda yeh hai ke START TIMES hamesha order mein aa jaate hain.
#   Iska matlab hai ke jo interval baad mein aayega, uska START TIME pichle interval
#   ke START TIME se hamesha BADA ya BARABAR hoga.
# - Is wajah se humein start times ki tension khatam ho jaati hai—shuruwat hamesha 
#   pichle interval ki hi pehle hui thi.
#
# 2. DOOSRA QUESTION: HUM PICHLE KE END TIME KO NAYE KE START TIME SE KYUN COMPARE KARTE HAIN?
# -------------------------------------------------------------------------------------
# - Timeline par imagine karo: 
#   Pichla interval 'A' shuru hua aur kisi point (END TIME) par khatam hua.
#   Naya interval 'B' kisi point (START TIME) se shuru ho raha hai.
#
# - CASE A: NO OVERLAP (GAP HAIN)
#   Agar 'A ka END TIME < B ka START TIME' (e.g., A = [1, 3], B = [5, 8])
#   Matlab 'A' shaam 3 baje khatam ho gaya, aur 'B' shaam 5 baje shuru ho raha hai.
#   Bech mein 3 se 5 baje tak khali time hai. Zero takrao! Dono alag alag rahenge.
#
# - CASE B: OVERLAP (TAKRAO HAIN)
#   Agar 'A ka END TIME >= B ka START TIME' (e.g., A = [1, 6], B = [2, 8])
#   Matlab 'A' shaam 6 baje tak chal raha tha, lekin 'B' shaam 2 baje hi shuru ho gaya!
#   'B' pichle interval ke chalte hue time ke andar hi ghus gaya. Isi ko OVERLAP kehte hain.
#
# 3. TEESRA QUESTION: HUM SIRF AAKHRI INTERVAL KE END TIME KO HIN KYUN UPDATE KARTE HAIN?
# -------------------------------------------------------------------------------------
# - Kyunki Sorting ki wajah se START TIME pehle hi sabse chota wala set ho chuka hota hai
#   (jaise [1, 6] mein '1' fix hai).
# - Jab doosra interval [2, 8] overlap karta hai, toh humein bas yeh check karna hota hai
#   ke yeh naya interval kahin hamare boundary time ko aur aage toh nahi le kar ja raha.
#
# 4. CHOUTHA QUESTION: 'max(merged[-1][1], interval[1])' KA ASAL CHAKKAR KYA HAI?
# -------------------------------------------------------------------------------------
# - Misal 1 (Lamba Naya Interval):
#   Pichla group = [1, 6]  (End = 6)
#   Naya interval = [2, 8] (End = 8)
#   dono merge huye toh lamba boundary ban gaya 8. 'max(6, 8) = 8'. Naya interval ban gaya [1, 8].
#
# - Misal 2 (Chota Naya Interval / Completely Inside):
#   Pichla group = [1, 6]  (End = 6)
#   Naya interval = [2, 4] (End = 4)  --> Yeh toh 6 se pehle hi khatam ho gaya!
#   Agar hum bina max() dekhe 4 set kar dete, toh hamara interval [1, 4] chota ho jata!
#   Isi liye 'max(6, 4) = 6' lagate hain taake boundary wahi [1, 6] rahe aur choti na ho.
#
# SUMMARY:
# - Comparison: merged[-1][1] < interval[0]  ==> Checks if NO overlap
# - Merging   : merged[-1][1] = max(merged[-1][1], interval[1]) ==> Extends END time if OVERLAP
# =====================================================================================