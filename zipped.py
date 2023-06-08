# Step 1
N, X = map(int, input().split())

# Step 2
marks = []
for _ in range(X):
    marks.append(list(map(float, input().split())))

# Step 3
for student_marks in zip(*marks):
    average = sum(student_marks) / X
    print("{:.1f}".format(average))
