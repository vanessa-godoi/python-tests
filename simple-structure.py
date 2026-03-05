A = int (input("Write a value for variable A "))
B = int (input("Write a value for variable B "))

if (A>B):
    aux=A;
    A=B;
    B=aux;

print("The value of variable A is now: ",A);
print("The value of variable B is now: ",B);