l=[]
for i in range(1,11):
    l.append(i)
print(f"Original list: {l}")
l=l[:5]
print(f"Extracted first five elements: {l}")
l=l[::-1]
print(f"Reversed extracted elements: {l}")
