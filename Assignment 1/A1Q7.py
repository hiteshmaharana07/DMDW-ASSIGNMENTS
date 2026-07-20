# WAP to display Fibonacci series of N numbers using UDF
def fibbo(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
n = int(input("Enter the count: "))
fibbo(n)
