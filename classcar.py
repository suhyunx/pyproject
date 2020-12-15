class Car :
    seat = 5
	
    def __init__(self, company, model) :
        self.company = company
        self.model = model
    
    def showCompany(self) :
        return self.company

    def showModel(self) :
        return self.model

k5 = Car('기아', 'K5')

print('제조회사 : %s' % k5.showCompany())
print('모델 : %s' % k5.showModel())
print('탑승인원 : %d' % k5.seat)
