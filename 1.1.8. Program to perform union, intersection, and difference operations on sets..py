a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations

union = A|B
intersection = A&B
difference = A-B

print(f"Union:  {union}")
print(f"Intersection:  {intersection}")
print(f"Difference:  {difference}")
