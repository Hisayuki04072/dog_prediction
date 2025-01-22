# VGG16模倣モデル
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.layers import (
    Input,
    Dense,
    Conv2D,
    MaxPooling2D,
    Flatten,
    GlobalAveragePooling2D,
)
from tensorflow.keras import Model
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions


def predict(input_image_path):
    input_image = Input(shape=(224, 224, 3), name="image")

    x = Conv2D(64, (3, 3), padding="same", activation="relu", name="conv1-1")(
        input_image
    )
    x = Conv2D(64, (3, 3), padding="same", activation="relu", name="conv1-2")(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name="pool1")(x)
    print(f"1ブロック目の概形:{x.shape}")  # 112×112

    x = Conv2D(128, (3, 3), padding="same", activation="relu", name="conv2-1")(x)
    x = Conv2D(128, (3, 3), padding="same", activation="relu", name="conv2-2")(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name="pool2")(x)
    print(f"2ブロック目の概形:{x.shape}")

    x = Conv2D(256, (3, 3), padding="same", activation="relu", name="conv3-1")(x)
    x = Conv2D(256, (3, 3), padding="same", activation="relu", name="conv3-2")(x)
    x = Conv2D(256, (3, 3), padding="same", activation="relu", name="conv3-3")(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name="pool3")(x)
    print(f"3ブロック目の概形:{x.shape}")

    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv4-1")(x)
    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv4-2")(x)
    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv4-3")(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name="pool4")(x)

    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv5-1")(x)
    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv5-2")(x)
    x = Conv2D(512, (3, 3), padding="same", activation="relu", name="conv5-3")(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name="pool5")(x)

    classes = 1000
    x = Flatten(name="flatten")(x)

    x = Dense(4096, activation="relu", name="dense1")(x)
    x = Dense(4096, activation="relu", name="dense2")(x)
    x = Dense(classes, activation="softmax", name="pred_pro")(x)

    model = Model(inputs=input_image, outputs=x)  # モデル作成
    model.summary()
    model.load_weights("vgg16_weights_tf_dim_ordering_tf_kernels.h5")

    img = image.load_img(input_image_path, target_size=(224, 224))

    x = image.img_to_array(img)
    x = x[np.newaxis, ...]
    x = preprocess_input(x)

    preds = model.predict(x)

    predict = decode_predictions(preds)[0]
    pred_ans = predict[0][1]
    pred_score = predict[0][2]
    pre_all = predict

    # 一番予測結果の高い犬種と確率をreturn
    return pred_ans, pred_score


if __name__ == "__main__":  # デバック用
    img_path = "static/dog_image/OIP (2).jpg"
    y = predict(img_path)
    print(y[0])
    print(y[1])
