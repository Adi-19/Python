def outer_func():
    outer_var = 10
    def inner_func():
        inner_var = 20
        print("Outer variable var", outer_var)
        print("Inner variable ", inner_var)

    inner_func()
    print("Outer variable", outer_var)
    print("Inner variable", inner_var)

outer_func()
