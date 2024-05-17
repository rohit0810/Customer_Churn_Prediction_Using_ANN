

from tensorflow.keras.models import load_model
model1 = load_model('Your Path/model.h5')
def prediction(lst):
  pred=model1.predict(lst)
  pred=pred[0,0]
  if(pred>=0.5):
    return 1
  else:
    return 0
  return 0