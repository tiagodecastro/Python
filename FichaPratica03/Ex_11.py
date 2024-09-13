n0025 = 0
n2650 = 0
n5175 = 0
n76100 = 0

while True:
    print("Introduza um número: ")
    n = int(input())

    if 0 <= n <= 25:
        n0025 += 1
    elif 26 <= n <= 50:
        n2650 += 1
    elif 51 <= n <= 75:
        n5175 += 1
    elif 76 <= n <= 100:
        n76100 += 1
    else:
        break

print (f"[00,25]: {n0025}")
print (f"[26,50]: {n2650}")
print (f"[51,75]: {n5175}")
print (f"[76,100]: {n76100}")