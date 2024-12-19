import random
import q5

total = 20
random_counts = [0 for _ in range(total)]

def setup():
    s.createCanvas(640, 240)

def draw():
    s.background(255)

    index = random.randrange(0, total)
    random_counts[index] += 1

    s.stroke(0)
    s.fill(127)

    w = s.width / total
    for i in range(total):
        h = random_counts[i]
        s.rect(i * w, s.height - h, w - 1, h)

s = q5.init('sketch')
