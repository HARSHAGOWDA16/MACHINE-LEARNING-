import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
import tensorflow as tf


a = tf.keras.datasets.mnist
(X_train, y_train),(X_test, y_test) = a.load_data()

X_train = tf.keras.utils.normalize(X_train, axis=1)

X_test = tf.keras.utils.normalize(X_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train,epochs=3)

accuracy,loss=model.evaluate(X_test,y_test)
print(accuracy)
print(loss)

model.save('digits.model')


for x in range(1,5):
    img=cv.imread(f'{x}.png')[:,:,0]
    img=np.invert(np.array([img]))
    prediction=model.predict(img)
    print(f'the result is :{np.argmax(prediction)}')

    plt.imshow(img[0],cmap=plt.cm.binary)
    plt.show()
