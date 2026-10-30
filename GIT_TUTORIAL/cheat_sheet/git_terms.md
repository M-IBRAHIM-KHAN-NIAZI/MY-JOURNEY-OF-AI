# Git Core Definitions & Terms

- **Directory** (Working Directory): The folder on your computer where your actual project files and folders are located. (Yeh computer par aapke project ka asal folder hota hai jahan saari files padi hoti hain.)

- **Repository** (Repo): A project directory that has Git tracking enabled, containing a hidden .git folder that saves the complete history of your project. (Yeh ek aisa folder hota hai jিসের andar Git ki tracking on hoti hai aur poori history save rehti hai.)


- **Staging Area** (Index / Waiting Room): A temporary holding area where you prep and line up your simple new files or modified files before saving them permanently. (Yeh ek tarah ka waiting room hota hai jahan files commit hone se pehle line-up hoti hain.)

- **Commit**: A permanent snapshot or save point of the files in the staging area, saved with a unique ID and a custom message. (Yeh staging area wali files ka ek permanent save point hota hai jiske sath message attached hota hai.)
# Git Branching Best Practices

- **One feature = One branch**: Har naye feature, bug fix, ya improvement ke liye ek alag dedicated branch banayein[cite: 15].
- **Never develop directly on main**: `main` branch ko hamesha stable rakhein aur us par direct code na karein[cite: 15].
- **Delete merged branches**: Jo branch merge ho chuki ho, usay foran delete kar dein taake repository clean rahe[cite: 15].
- **Use meaningful branch names**: Branch ka naam hamesha saaf aur samajh anay wala rakhein jo uske maqsad ko zahir kare (jaise `feature/user-login`)[cite: 15].
- **Keep branches short-lived**: Branches ko zyada lamba na chalayein; risks aur conflicts se bachne ke liye unhein jald az jald merge kar dein[cite: 15].

- **`git fetch`**: Remote repository se sirf latest changes ko download karta hai, lekin unhein aapki current working branch mein merge **nahi** karta.
- **`git pull`**: Remote repository se changes download karta hai aur foran aapki current branch ke sath **merge** bhi kar deta hai (`git fetch` + `git merge`).