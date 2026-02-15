l = []
for i in range(1,11):
    l.append(i)
print(f"Original list: {l}")
ff = l[:5]
print(f"Extracted first five elements: {ff}")
ff.reverse()
print(f"Reversed extracted elements: {ff}")