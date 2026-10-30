<!-- 
### Git & GitHub Cheat Sheet

1. git --version
   - Role: Laptop par Git check karna ke installed hai ya nahi.

2. git init
   - Role: Current folder or directory ko Git repository banana aur local tracking shuru karna.
-->
<!-- 
3. git status
   - Role: Check karna ke project mein kaun si files untracked hain, modify hui hain konsi commit hain ya staging area mein hain(matlab tracked hn).

4. git add <file_name>.txt (you can just add another file or many files in a same line)
   - Role: Specific file ko staging area mein dalna taaki Git usko track karna shuru kar de commit ke liye.
-->
<!-- 
5. git commit -m "message"
   - Role: Staging area ki files ka permanent snapshot (save) le lena, sath mein ek message likhna zaroori hota hai ke kya change kiya hoya hai ya kiya banaya ha jo save kiya ha.

6. git log
   - Role: Project ki poori commit history check karna ke kab-kab kaunsa code save hua hai, kisne kiya hai aur kya message tha.
-->  
7.- **`git log --oneline`**: Shows the commit history in a compact, single-line format per commit, displaying only the short hash and the commit message for a quick overview. (Commits ki history ko chota aur clean single-line format mein dekhne ke liye.)
8.- **`git add .`**: Adds all new, modified,delete and current directory files to the staging area in one go. (Current folder ki saari files ko aik sath staging area mein laane ke liye sabse common tareeqa.)
- **`git add --all` (or `-A`)**: Adds all files across the entire repository (including deletions and modifications) to the staging area. (Poori repository ki saari changes ko staging area mein add karne ke liye.)
# Git Restore & Unstage Commands

- **`git restore --staged <file_name>`**: Used to unstage a file, moving it back from the staging area to the working directory without losing any code changes[cite: 5]. (Staging area se file ko nikal kar wapas un-staged state mein lane ke liye.)
- **`git restore <file_name>`**: Discards uncommitted changes made to a file in the working directory and reverts it back to the last committed state[cite: 5]. (Working directory ki uncommitted changes ko undo karke file ko pichli safe state par wapas laane ke liye.)
- **`.gitignore`**: Yeh ek special file hoti jo vs code mein banate hn  jo Git ko batati hai ke kaunsi files ya folders ko track nahi karna.
- **`.gitignore` Patterns**:
  - **`env`**: Kisi single file ko ignore karne ke liye (jaise private config files).
  - **`builds/`**: Kisi poore folder aur uske andar ki saari files ko ignore karne ke liye (slash `/` folder ko batata hai).
  - **`builds/build.txt`**: Kisi folder ke andar maujood sirf ek specific file ko ignore karne ke liye.
- **`.gitkeep`**: Yeh ek convention file hoti hai jo empty folders ko Git mein track karwane ke liye use hoti hai (kyunki Git by default khali folders ko ignore kar deta hai).
# Git Branching Commands

- **`git branch <branch_name>`**: Ek nayi branch banane ke liye use hota hai.
- **`git branch`**: Project mein maujood saari branches ki list dekhne aur current active branch ko check karne ke liye.
- **`git switch <branch_name>`**: Kisi doosri branch par switch (move) karne ke liye or ham osme jo marzi changes karle main branch ya baki branch vese hi rahe gi or bd osme switch hujaye gy
# Git Merge & Branch Deletion Commands

- **`git merge <branch_name>`**: Doosri branch ke changes ko apni current active branch mein milaane (merge karne) ke liye.
- **`:wq`**: Vim editor ke andar commit message save karke (`w`) editor se bahar aane (`q`) ke liye use hota hai (jab merge ke waqt default editor khul jaye or ese vs code me likhte or close kardete ose).
- **`git branch -d <branch_name>`**: Kaam khatam hone aur merge karne ke baad kisi branch ko delete karne ke liye.

- **`git switch -c <branch_name>`**: Ek hi command mein nayi branch banane aur us par foran switch (move) ho jaane ke liye use hoti hai.
# Git Stash Commands

- **`git stash`**: Uncommitted changes (changes jo abhi commit nahi ki gayen) ko temporary safe side par rakhne ke liye taake working directory clean ho jaye.
- **`git stash list`**: Saare saved stashes ki list dekhne ke liye.
- **`git stash pop`**: Stash ki hui latest changes ko wapas laane aur stash list se remove karne ke liye.
- **`git stash apply`**: Stash ki hui changes ko wapas laane ke liye, lekin isme changes stash list ke andar hi safe rehti hain (delete nahi hoti).
# Git Tag Commands

- **`git tag`**: Repository ke maujood saari tags ki list dekhne ke liye.
- **Annotated Tag (`git tag -a <tag_name> -m "<message>"`)**: Iske zariye tag ke sath ek proper message ya description bhi save hoti hai (jaise release version ke liye).
- **Lightweight Tag (`git tag <tag_name>`)**: Yeh ek simple tag hota hai jo baghair kisi message ke direct specific commit par lag jata hai.
- **`git rebase main`**: dosri branch ke commits ko `main` branch ke latest commit ke upar dobara play (replay) kar deta hai(ye dosri branch mein excute hota ha phir hm main mein switch karke merge kardete or merging commit nahi ata).
- Yeh messy merge commits se bachata hai aur project ki history ko ekdam clean aur linear rakhta hai.
- **`git clone <http_url>`**: Kisi bhi remote repository (jaise GitHub) ki public code ko apne local system par download karne ke liye use hoti hai OR PRIVATE mein karne ke liye tareeka change ha ya simple apka peronsal things mangta
## 6. Remote & Synchronization Commands
- **`git remote -v`**: Repository ke sath linked remote URLs (fetch aur push ke liye) ko check karne ke liye.(batata ha konsa fetch mein ha konsa main mein)
- **`git branch -M <branch_name>`**: Current branch ka naam change ya rename karne ke liye (jaise `main` ya `master` set karne ke liye).
- **`git push origin <branch_name>`**: Local changes ko remote repository(jaise ke github) par upload karne ke liye.
- **`git pull`**: Remote repository se latest changes ko apne local system par download aur merge karne ke liye.

