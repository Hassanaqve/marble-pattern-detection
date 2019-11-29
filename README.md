# marble-pattern-detection
You can detect marbles along via machine learning and IBM cloud.

We have the dataset of marble and we have to make a model to predict the marble. Unfortunately we only got one sample of each marble so we have to make things accourding to it. 

For this we have used Keras Data Augmentation library. We made 37 variations of each marble so we can train model over it.
Normally Data Augmentation is used when we have to remove bais from our data or in otherwords when we want to diverse our dataset but as we got only one sample for each marble we gotta do it. 

Then for model training we use Ibm clouds visual recognition service. i.e we train it on custom model and we were getting about 94% accuracy after model fitting.
