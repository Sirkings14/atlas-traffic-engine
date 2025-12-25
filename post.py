import random

with open("posts.txt", "r", encoding="utf-8") as f:
    posts = f.read().strip().split("\n\n")

print(random.choice(posts))
