#オブジェクト指向：誰にでもわかる名前や文章にしよう！
'''
ユーザーネーム:自分独自のデータ型を作る
データ型宣言：UserName
　　　　属性：実際のユーザー名
　　　ルール：ユーザー名は4文字以上20文字以下である
　できること：ユーザー名を大文字に変換する=>メソッド
'''


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数ルール違反やで！')
        self.name = name

    def screen_name(self):
        return self.name.upper()
# raise:は意図的に間違いを起こす（こっちから怒ってやるぜ）為に使う

# UserNameクラスのインスタンス化
hibiki = UserName(name='hibiki')
print(hibiki.screen_name())
# print(hibiki)
# print(type(hibiki)):typeで型がわかる
# print(hibiki.name)#.を入れる事でその値にアクセスできる

# sho = UserName('sho')
# print(sho.name)

# string型で大文字にするには.upper()を使う
