def chec(add):
    def inside(a, b):
        if b == 0:
            print("Cant bitch")
            return
        add(a, b)
    return inside


@chec
def div(a, b):
    print(a/b)


div(4, 2)
div(1, 0)
