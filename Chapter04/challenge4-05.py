# ① 引数が1つある関数を定義
def convert_float(value):
    try:
        return float(value)
    except ValueError:
        print("float型に変換できません")

# 関数定義終了


# ③ 文字列の小数を引数に指定して関数を呼び出す
result = convert_float("3.14")

# ④ 戻り値を表示
print(result)
