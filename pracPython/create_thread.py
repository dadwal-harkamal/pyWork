import threading

def square(n):
    print("square = {} ".format(n*n))

def cube(n):
    print("cube = {}".format(n*n*n))


if __name__ == "__main__":
        

    t1 = threading.Thread(target=square, args=(10,))
    t2 = threading.Thread(target=cube, args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
