def solve():
    # Read the length of array a
    n = int(input())

    # Read the elements of array b
    v = list(map(int, input().split()))

    # Print the first element of b
    print(v[0], end=" ")

    # Iterate from the first element to the (n-2)-th element of b
    for i in range(n - 2):
        # Print the minimum value between the current element and the next element of b
        print(min(v[i], v[i + 1]), end=" ")

    # Print the (n-2)-th element of b
    print(v[n - 2])

if __name__ == "__main__":
    # Read the number of test cases
    t = int(input())

    # Iterate for each test case
    for _ in range(t):
        solve()
