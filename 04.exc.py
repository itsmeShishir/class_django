# exception handling -> error handling
# try, except, else, finally
try:
    a = int(input("enter a number: "))
    print(a/10)
except (ZeroDivisionError,ValueError ) as e:
    print(e)
    print(f"integer cannot be divide by zero {e}")
finally:
    print("other error")
print("hello")