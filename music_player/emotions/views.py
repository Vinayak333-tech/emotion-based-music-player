from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
# Create your views here.
import numpy as np
from keras.models import model_from_json
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
import cv2
from .forms import *
from django.contrib import messages

# json_file = open('/Users/mayuragarwal/Downloads/model786.json', 'r')  # /Users/mayuragarwal/Downloads/model786.json
json_file = open('/Users/mayuragarwal/Downloads/model786.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('/Users/mayuragarwal/Downloads/model786.h5')
loaded_model.compile(loss=categorical_crossentropy,
                     optimizer=Adam(lr=0.001),
                     metrics=['accuracy'])
face_classifier = cv2.CascadeClassifier('/Users/mayuragarwal/Desktop/sample_project/haarcascade_frontalface_alt.xml')

# face_classifier = cv2.CascadeClassifier('/Users/mayuragarwal/Desktop/sample_project/haarcascade_frontalface_alt.xml')


@require_POST
@login_required(login_url='accounts:login')
def predict(request):
    form = PredictionForm(request.POST, request.FILES)
    if form.is_valid():
        ins = form.save(commit=False)
        ins.user=request.user
        ins.save()
        
        image = cv2.imread(ins.image.path, 0)
        faces = face_classifier.detectMultiScale(image, 1.3, 5)
        if len(faces) == 0:
            ins.delete()
            messages.info(request, f"Sorry no face detected.Please try again")
            return redirect("startpage")
        for (x, y, w, h) in faces:
            roi_gray = image[y:y + h, x:x + w]
            if roi_gray.shape[0] > 250 or roi_gray.shape[1] > 250:
                roi_gray = cv2.resize(roi_gray, (250, 250), interpolation=cv2.INTER_AREA)
            else:
                roi_gray = cv2.resize(roi_gray, (250, 250), interpolation=cv2.INTER_CUBIC)
            roi_gray = np.array(roi_gray, 'float32')
            roi_gray /= 255
            label = loaded_model.predict(roi_gray.reshape(-1, 250, 250, 1))
            emotion = np.argmax(label[0])
            dic = {0: 'Happy',
                   1: 'Angry',
                   2: 'Sad',
                   3: 'Neutral'}
            ins.emotion = dic[emotion]
            ins.user=request.user
            ins.save()
            return redirect('playlist:emotion', type=emotion)
    else:
        return redirect('startpage')
