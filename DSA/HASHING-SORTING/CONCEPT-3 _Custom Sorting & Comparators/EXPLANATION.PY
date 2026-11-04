def merge(intervals):
    # Step 1: Intervals ko starting time (x[0]) ke mutabiq ascending order mein sort karo
    intervals.sort(key=lambda x: x[0])
    
    merged = [] # Yahan hum apne final merged intervals store karenge
    
    for interval in intervals:
        # =========================================================================
        # LINE 1 EXPLANATION: Overlap check karne ki condition
        # =========================================================================
        # - 'not merged': Check karta hai kya 'merged' list abhi khaali hai? 
        #   Agar khaali hai (jaise bilkul shuru mein loop start hota hai), toh yeh True 
        #   ho jayega aur pehla interval bina kisi check ke add ho jayega.
        # - 'or': Ya phir agar list khaali nahi hai, toh agli condition check hogi.
        # - 'merged[-1]': Python mein negative index '-1' ka matlab hota hai 'aakhri element (last interval)' 
        #   jo abhi tak 'merged' list ke andar add hua hai.
        # - 'merged[-1][1]': Yahan '-1' aakhri interval ko batata hai, aur aage wala '[1]' us interval ka 
        #   doosra element yaani uska 'End Time' nikal kar deta hai (kyunki [0] start time hota hai aur [1] end time).
        # - '< interval[0]': Kya aakhri interval ka end time, naye aane wale interval ke start time 
        #   ('interval[0]') se chota hai? 
        #   Matlab agar pichla interval pehle hi khatam ho chuka hai aur naya baad mein shuru ho raha hai, 
        #   toh iska matlab hai ke **dono ke beech mein koi overlap (takrao) nahi hai**!
        if not merged or merged[-1][1] < interval[0]:
            # Agar list khaali ho ya koi overlap na ho, toh naye interval ko seedha list mein add kar do
            merged.append(interval)
            
        else:
            # =========================================================================
            # LINE 2 EXPLANATION: Overlap hone par intervals ko merge/extend karne ki logic
            # =========================================================================
            # Jab overlap ho jaye (yaani upar wali condition false ho jaye), toh humein pichle interval 
            # ke end time ko extend karna padता hai taake naya interval uske andar merge ho jaye.
            # - 'merged[-1][1]': Merged list ke aakhri interval ka purana 'End Time'.
            # - 'interval[1]': Naye wale interval ka 'End Time'.
            # - 'max(...)': Yeh function dono end times ko aapas mein compare karta hai aur jo 
            #   sabse bada (maximum) number hota hai, usko chun leta hai taake merged interval poori tarah stretch ho jaye.
            # - '=': Yeh naya bada end time wapas aakhri interval ke end time par assign (update) ho jata hai.
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

# Test the function
input_intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
print("Merged Intervals:", merge(input_intervals))
# Output: [[1, 6], [8, 10], [15, 18]]