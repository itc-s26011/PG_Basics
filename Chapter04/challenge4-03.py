# 関数定義
def sample(a, b, c, d="Dの初期値", e="Eの初期値"):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("e =", e)

# 関数定義終了


# 引数を3つ指定して呼び出し
print("【引数を3つ指定した場合】")
sample("りんご", "みかん", "ぶどう")

print()

# 引数を5つ指定して呼び出し
print("【引数を5つ指定した場合】")
sample("りんご", "みかん", "ぶどう", "もも", "なし")
