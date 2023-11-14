class Person:
    """
    Person 클래스는 ID와 직함(Title)을 가지는 기본적인 인물 정보를 표현합니다.
    """

    def __init__(self, person_id, title):
        """
        Person 클래스의 초기화 메서드입니다.

        Parameters:
            person_id (int): 개인 식별자(ID)입니다.
            title (str): 직함(Title)입니다.
        """
        self.person_id = person_id
        self.title = title

    def printInfo(self):
        """
        현재 Person 객체의 정보를 출력하는 메서드입니다. ID와 Title을 출력합니다.
        """
        print(f"Person: ID={self.person_id}, Title={self.title}")


class Manager(Person):
    """
    Manager 클래스는 Person 클래스를 상속받아 Manager 특유의 스킬을 추가로 가지는 클래스입니다.
    """

    def __init__(self, person_id, title, skill):
        """
        Manager 클래스의 초기화 메서드입니다. Person 클래스의 초기화 메서드를 호출하면서 스킬을 추가로 설정합니다.

        Parameters:
            person_id (int): 개인 식별자(ID)입니다.
            title (str): 직함(Title)입니다.
            skill (str): 관리자 특유의 스킬입니다.
        """
        super().__init__(person_id, title)
        self.skill = skill

    def printInfo(self):
        """
        현재 Manager 객체의 정보를 출력하는 메서드입니다. Person의 printInfo를 호출한 후 Manager 특유의 스킬을 출력합니다.
        """
        super().printInfo()
        print(f"Manager Skill: {self.skill}")


class Employee(Person):
    """
    Employee 클래스는 Person 클래스를 상속받아 Employee 특유의 역할(Role)을 추가로 가지는 클래스입니다.
    """

    def __init__(self, person_id, title, role):
        """
        Employee 클래스의 초기화 메서드입니다. Person 클래스의 초기화 메서드를 호출하면서 역할을 추가로 설정합니다.

        Parameters:
            person_id (int): 개인 식별자(ID)입니다.
            title (str): 직함(Title)입니다.
            role (str): 직원 특유의 역할(Role)입니다.
        """
        super().__init__(person_id, title)
        self.role = role

    def printInfo(self):
        """
        현재 Employee 객체의 정보를 출력하는 메서드입니다. Person의 printInfo를 호출한 후 Employee 특유의 역할을 출력합니다.
        """
        super().printInfo()
        print(f"Employee Role: {self.role}")


# Sample test codes

# 1.
person1 = Person(1, "Mr.")
person1.printInfo()

# 2.
manager1 = Manager(2, "Ms.", "리더십")
manager1.printInfo()

# 3.
employee1 = Employee(3, "Dr.", "개발자")
employee1.printInfo()

# 4.
person2 = Person(4, "Mrs.")
person2.printInfo()

# 5.
manager2 = Manager(5, "Mr.", "커뮤니케이션")
manager2.printInfo()

# 6.
employee2 = Employee(6, "Miss", "디자이너")
employee2.printInfo()

# 7.
person3 = Person(7, "Dr.")
person3.printInfo()

# 8.
manager3 = Manager(8, "Ms.", "문제 해결")
manager3.printInfo()

# 9.
employee3 = Employee(9, "Mr.", "테스터")
employee3.printInfo()

# 10.
person4 = Person(10, "Mrs.")
person4.printInfo()


#...(나머지 샘플 테스트 케이스들도 이어집니다)
p1 = Person(100, "개발자")
p1.printInfo()
