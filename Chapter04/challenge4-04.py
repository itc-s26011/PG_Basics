# ① ひとつめの関数を定義
def divide_by_two(num):
    result = num // 2  # 2で割った整数の商
    return result

# 関数定義終了


# ③ ふたつめの関数を定義
def multiply_by_four(num):
    result = num * 4  # 4を掛けた積
    return result

# 関数定義終了


# ⑤ 変数に整数を代入
value = 10

# ⑥ ① の関数を呼び出し、戻り値を別の変数に代入
half_value = divide_by_two(value)

# ⑦ ③ の関数を呼び出し、戻り値をさらに別の変数に代入
final_value = multiply_by_four(half_value)

# ⑧ 結果を表示
print(final_value)
