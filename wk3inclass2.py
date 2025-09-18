class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):
    def hello(self):
        print("Hello from D")
        super().hello()


class E(C):
    def hello(self):
        print("Hello from E")
        super().hello()


class F(B, E):
    def hello(self):
        print("Hello from F")
        super().hello()


print("MRO of F:", F.mro())
print()

f = F()
f.hello()

print("\n--- MRO conflict example ---")

try:
    class G(C, E):
        pass
except TypeError as e:
    print("MRO conflict error:", e)