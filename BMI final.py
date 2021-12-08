class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 0):
            raise ValueError('BMIが正常値の範囲を超えています')

    def __str__(self):
        return f'{self.value:.2f}'


hibiki_bmi = BMI(height=1.80, weight=67.0)
print(hibiki_bmi)

ohira_bmi = BMI(height=1.78, weight=67000.0)
print(ohira_bmi)
