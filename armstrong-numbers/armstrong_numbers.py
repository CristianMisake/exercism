def is_armstrong_number(number):
    number = str(number)
    cantidad = len(number)
    armstrong = 0
    for i in number:
        armstrong += pow(int(i), cantidad)
    return (armstrong == int(number))
