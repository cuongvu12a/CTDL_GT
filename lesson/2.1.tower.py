
# Tower of Hanoi 
# Move n disks from pole A to pole C using pole B as a temporary pole
def tower(n, a, b, c):
    if n == 1:
        print(f"Move disk 1 from {a} to {c}")
    else:
        tower(n-1, a, c, b)
        print(f"Move disk {n} from {a} to {c}")
        tower(n-1, b, a, c)


tower(3, 'A', 'B', 'C')