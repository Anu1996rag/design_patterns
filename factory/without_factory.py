class A:
    ...


if __name__ == "__main__":
    a = A()
    b = A()
    print(id(a), id(b))
