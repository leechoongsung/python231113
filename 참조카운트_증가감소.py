class MyClass:
    #초기화 메서드(초기화)
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)

    #소멸자 메서드(정리작업)    
    def __del__(self):
        print("Instance is deleted!")

#메모리관리 자동        

c = MyClass(10)
c_copy = c
del c 
del c_copy


print("전체 코드 실행 종료")