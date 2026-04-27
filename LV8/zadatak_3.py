import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import matplotlib.image as Image


model = keras.models.load_model('FCN.keras')

y_true=[7,2,0,0,1]

for i in range(1,6):
    idx = i-1
    img = Image.imread(f'test_{i}.png')


    if i not in [4,5]:
        img = img[:, :, 0]

    img_s = np.array(img).astype('float32')
    if img_s.max() > 1.0:
        img_s = img_s / 255
    img_s = np.expand_dims(img_s, -1)
    img_s = np.expand_dims(img_s, 0) # batch dimenzija

    print(img_s.shape)

    prediction = model.predict(img_s)
    y_pred = np.argmax(prediction, axis=1)

    plt.imshow(img, cmap='gray')
    print(y_pred[0])
    plt.title(f'True: {y_true[idx]}, Pred: {y_pred[0]}')
    plt.show()
