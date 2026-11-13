# LeetCode 1472: Design Browser History
# Step 1: Node Setup (Har page ek dabba hai)
class Node:

  def __init__(self, url):
    self.url = url  # Page ka naam/url
    self.prev = None  # Peeche wale page ka rasta
    self.next = None  # Aage wale page ka rasta


# Step 2: Browser History Class & Driver Setup
class BrowserHistory:

  def __init__(self, homepage: str):
    # Driver Setup: Constructor mein hum homepage se pehla node banate hain
    self.head = Node(homepage)
    self.current = self.head  # Shuru mein current pointer homepage par khada hai

  def visit(self, url: str) -> None:
    # Naya page/dabba banaya
    new_node = Node(url)

    # Wiring: Naye node ka prev current par joda, aur current ka next naye node par
    new_node.prev = self.current
    self.current.next = new_node

    # Current pointer ko aage shift karke naye page par le aaye
    self.current = new_node

  def back(self, steps: int) -> str:
    # Back Function: Jab tak steps bache hain aur peeche node mojood hai (`self.current.prev`)
    while steps > 0 and self.current.prev:
      self.current = self.current.prev  # Current ko peeche khiska do
      steps -= 1  # Step kam kar do
    return self.current.url  # Jis page par ruke, uska url return karo

  def forward(self, steps: int) -> str:
    # Forward Function: Jab tak steps bache hain aur aage node mojood hai (`self.current.next`)
    while steps > 0 and self.current.next:
      self.current = self.current.next  # Current ko aage khiska do
      steps -= 1  # Step kam kar do
    return self.current.url  # Jis page par ruke, uska url return karo

browserHistory = BrowserHistory("google.com")
print("Initialized with: google.com")

  # Naye pages visit kiye
browserHistory.visit("leetcode.com")
print("Visited: leetcode.com")

browserHistory.visit("youtube.com")
print("Visited: youtube.com")

  # Back aur Forward testing
print("\n--- Testing Back & Forward ---")
print("Back 1 step:", browserHistory.back(1))  # Expected: "leetcode.com"
print("Back 1 step:", browserHistory.back(1))  # Expected: "google.com"
print("Forward 1 step:", browserHistory.forward(1))  # Expected: "leetcode.com"
  