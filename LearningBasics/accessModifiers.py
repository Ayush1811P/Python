class test:
    __name="Ayush"
    __rollNo=18

    def __showDetails(self):
        name=self._test__name
        rollno=self._test__rollNo
        return f"{name},{rollno}"
    
class test2(test):
    ...
t1=test()
t1=test2()
# t1._name="AAAYUSH"
# print(t1.__name)        
T1=test()
print(T1._test__showDetails())


