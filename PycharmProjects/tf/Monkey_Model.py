from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import time
start = time.time()

# dimensions of our images
img_width, img_height = 299, 299

# load the model we saved
model = load_model('transfer_learning_model.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# predicting images
img = image.load_img('data/grab/patas-monkey-03.jpg.990x0_q80_crop-smart.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict(images, batch_size=10)

print (classes)
end = time.time()
print(end - start)