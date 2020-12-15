class Person :
	
    def __init__(self, name, address, email) :
        self.name = name
        self.address = address
        self.email = email
    
    def getName(self) :
        return self.name

    def getAddress(self) :
        return self.address

    def getEmail(self) :
        return self.email

person = Person('박수현', '대전시 동구', 'ktu9988@naver.com')

print('성명 : %s' % person.getName())
print('주소 : %s' % person.getAddress())
print('이메일 : %s' % person.getEmail())
