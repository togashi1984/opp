'''
class （成人の）BMI:
    関連しそうな属性：
　　　　-身長
　　　　-体重
　　　　-BMIという値そのもの
　　　　ルール：
　　　　　　-10以上40以下＜--常識的な範囲
　　　　　　-表示する時は少数第2位まで

　　　　　　-ex23.678->23.67
        -できること
　　　　　　-？？？
'''
# クラス名はUpperCamelCaseが普通,変数、メソッド、関数名はSnakeCaseが普通(BMIはいきなり例外だが（笑）)
# UpperCamel:SpartaCmapDay
# lowerCamel:spartaCampDay
# SnakeCase:sparta_camp_day

# クラスは抽象の世界
#プログラミングでは抽象化に強くなるのは重要な観点
class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
#8:32==>bmi.calculate_bmiって何か変…これにすればまとまるじゃん！ていう違和感が大事
# self.value = self.weight / (self.height ** 2)
#もっと言うとself.height = height,self.weight = weightもいらなくなる

#heightやweightをインスタンス変数と呼ぶ
#[self.〇〇]は属性と呼ぶ,クラスの中で呼びだす時は[self.〇〇]
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
#クラス内における関数=>インスタンスメソッド

# BMIクラスのインスタンス化
# #Instance:実体（具体・具象）の世界
hibiki_bmi = BMI(height=1.80, weight=67.0)

print(hibiki_bmi.height, hibiki_bmi.weight)
print(hibiki_bmi.calculate_bmi())

ohira_bmi = BMI(height=1.78, weight=75.0)
print(ohira_bmi.height, ohira_bmi.weight)
print(ohira_bmi.calculate_bmi())

 #augment:プログラミングでは引数の意味














