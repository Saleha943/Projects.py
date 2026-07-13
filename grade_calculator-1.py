marks=[]
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))
avg=sum(marks)/5
print("Average:",avg)
if avg>=90:
    print("Grade: A")
elif avg>=80:
    print("Grade: B")
elif avg>=70:
    print("Grade: C")
elif avg>=60:
    print("Grade: D")
else:
    print("Grade: F")