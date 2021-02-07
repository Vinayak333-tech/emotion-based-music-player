# Project title : Emotion based music recommendations<h1>


#### The human face plays an important role in knowing an individual's emotion. The required inputs are extracted from the human face directly using a webcam or a static image uploaded by the user. We use these features for  deducing the emotion of an individual.We train a sequential CNN model, consisting of an input layer,three (Convolution+pooling) layers,two fully connected layers and an output layer, on the training images. The prediction of the model helps us  fetch a list of songs that match with the “emotion” derived from the input image provided earlier. This helps the user to listen to songs related to his/her current mood and eliminates the time-consuming task of searching songs related to his/her emotion. Emotion Based Song Player provides four playlists to the users as it captures four emotions namely “Happy”, “Angry”, “Sad” , “Neutral” which can be customised by the user as per his/her taste of music.
# Machine Learning Algorithms tried and used: 


### 1.Bag Of Visual Words
#### Bag Of Visual Words(also known as Bag Of Features) is a technique to compactly describe images and compute similarities between images.
#### It is used for image classification. The approach has its origin in text retrieval(information retrieval) and is an extension to the NLP algorithm Bag of Words. In Bag Of Words, we scan through the entire document and keep a count of each word appearing in the document. Then, we create a histogram of frequencies of words and use this histogram to describe the text document. In Bag Of Visual Words, our input is an image instead of a text document and we use visual words to describe an image.BoVW approach works well with large microscope images that capture many details.Approximately 80% of the images in our dataset are around 210*210 pixels.Features extractors like SIFT,BRISK,ORB didn’t work well with our images and gave 80% validation accuracy.
#### If you want to read more on Bag of Visual words please check this medium post on BoVW [https://medium.com/analytics-vidhya/bag-of-visual-words-bag-of-features-9a2f7aec7866]

### 2.Facial Landmarks technique
#### In this technique, we extract the 68 facial landmarks and the centre of gravity.We then calculate the distance of each of these 68 landmarks from the centre of gravity and the angle made by this line with the horizontal.We can also calculate the euclidean distance between each pair of landmarks.We use these distances and angles as our input vector.Next,we train a classifying model like SVM,random forest,etc on the input data.
#### The problem with this approach is in the first step i.e the technique we use to extract the facial landmarks as it has to be perfect for higher accuracy of our model.The most widely known model for this task is Dlib’s 68 key points landmark predictor which gives very good results in real-time. But the problem starts when the face is occluded or at an angle to the camera which is very important for our task.

### 3.CNN
#### This is the algorithm that we implemented in our project and the training dataset comprises the JAFFE dataset,KDEF dataset and a few images captured by the team.A sequential CNN model is trained on these images.The dataset consists of 4789 training images and 1198 validation images.
#### The input image is of shape (250,250,1) as we are dealing with grayscale images.For images greater than 250 pixels we use INTER_AREA interpolation technique to shrink the images and For images smaller than 250 pixels we use INTER_CUBIC technique to zoom the images.
#### Dropouts and l2 regularization have been used to avoid overfitting.The model is compiled with Adam optimizer(lr=0.001).The model is trained for 50 epochs.
#### Final Results:The model achieves training accuracy of 0.98 and validation accuracy of 0.92 after 50 epochs.The model can be trained for a few more epochs to achieve better performance. :Our sequential CNN model gives satisfactory results.The model was validated on five different test sets and gives ~90% accuracy.We need to keep in mind that humans express the same emotion in different ways and hence the model may fail sometimes.The models can be extended to capture additional emotions such as ‘Disgust’,’Surprise’,etc. We can try transfer learning and fine tuning i.e training the last few layers of the model.If working with facial landmark detection method,we can try training a CNN model for predicting the 68 facial landmarks.The app can be integrated with music-streaming API to fetch the songs.


# Tech/Frameworks/Libraries Used:
#### JQuery, Django, Keras, Pandas, cv2.



Screenshots:

![Screenshot](/images/screenshot1.png)

![Screenshot](/images/screenshot4.png)

![Screenshot](/images/screenshot5.png)

![Screenshot](/images/screenshot2.png)

![Screenshot](/images/screenshot3.png)




## Contributors:
#### Vinayak Mishra
[https://github.com/Vinayak333-tech/]

