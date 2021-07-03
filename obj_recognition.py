from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16



def get_objects_from_photo(img_path):
    model = VGG16()
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    top_labels = list()
    for i in range(7):
        try:
            l = label[0][i]
            top_labels.append(l)
            print('%s (%.2f%%)' % (l[1], l[2]*100))
        except: break ;
    return top_labels
