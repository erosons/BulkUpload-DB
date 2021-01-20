from timeit import timeit

code="""
class Human:
    def __init__(self,eye,hands,legs,ears):
        self.eye=eye
        self.hands=hands
        self.legs=legs
        self.ears=ears


    def Human_attributes(self):
        print(f"I am human with {self.eye} eyes,{self.hands} hands,{self.ears}")

    @classmethod
    def human_attributes_creator(cls):
        print(f"Iam human with 2 eyes,2 hands,2 ears")

    @staticmethod
    def Human_attrib():
        print(f"Iam human with 2 eyes,2 hands,2 ears")


samson=Human(2,2,2,2)
samson.Human_attributes()

"""
print(timeit(code,number=500000))