
fp = open("log.txt", "a")

def log(func):
    def wrapper(*args, **kwargs):
        fp.write(f"Volám funkci {func.__name__} s argumenty {args} a {kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

@log
def ahoj(jmeno):
    print(f"Ahoj {jmeno}!")

@log
def cau():
    print("Cau, jak to de?")


if __name__ == "__main__":
    ahoj("Metre")
    cau()



