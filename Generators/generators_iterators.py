class FirstHundredGenerator:
    def __init__(self):
        self.number=0

    def __next__(self):
        if self.number<100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration()

    # def __iter__(self):
    #     return self


gen=FirstHundredGenerator()
print(next(gen))
print(next(gen))
print(gen.number)
gen.__next__()
print(gen.number)

#making it iterable
class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

print(sum(FirstHundredIterable()))
for i in FirstHundredIterable():
    print(i)

# print(sum(FirstHundredGenerator()))
# for i in FirstHundredGenerator():
#     print(i)

