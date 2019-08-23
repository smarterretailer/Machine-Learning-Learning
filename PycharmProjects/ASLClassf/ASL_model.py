import time
start = time.time()

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# dimensions of our images
img_width, img_height = 299, 299

# load the model we saved
model = load_model('asl_transfer_learning_model.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# predicting images
img = image.load_img('data/training/n4/n4036.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict(images, batch_size=29)

print (classes)

end = time.time()
print(end - start)