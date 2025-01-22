# jsonファイルのクラス一覧を見る
import json
import urllib.request

# ImageNetのクラス名リストのURL
url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"

# URLからJSONファイルをダウンロードして読み込む
with urllib.request.urlopen(url) as f:
    class_idx = json.load(f)

# クラスIDとクラス名を表示
for class_id, (_, class_name) in class_idx.items():
    print(f"{class_name}")
