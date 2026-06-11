my_profile = {
    "身長": "140cm",
    "好きな色": "水色",
    "好きな作家": ["新海誠", "凪良ゆう"],
    "好きなミュージシャン": "Snow Man",
    "好きなグループ": "原因は自分にある。"
}

key = input("キーを入力してください: ")

if key in my_profile:
    print(my_profile[key])
