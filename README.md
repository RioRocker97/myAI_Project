# myAI_Project
My AI project . Don't know where we heading.

# Progrssion
  - Get to know Image pre-processing step (skimage,matplotlib)
  - Try to implement Deep learning Algorithms (InceptionV3, ResNet50)
  - Clean image(Crop size to 224x224,change to grayscale)
  - Explore how to make "Model"
  - split data into 2 side => 80% for train , 20% for test
  - first configuration for InceptionV3
  - first training session (AUC around 0.4 || pretty low !! need to improve)
  - first predict (AUC > 0.5 have 600+ from 1022, Not bad !)
  - secound training session (BAD AUC , Inaccuracy)
  - second predict (AUC < 0.1 , Terrible)
  - thrid train and run (Good configuration but Does it suitable for the job ?)
  - 4th training and predict is just a minor setback
  - 5th training (accuracy is low,Model not ok enough,BUT!!! we're on the right track)
  - 5th predict (Terrible prediction , Overfitting ? ,too many layers ??)
  - 6th training and predict is ok (Muti-class)
  - 7th training and predict is weird (Muti-class and 1 class is lost ??)
  - Run Fun VGG's Model
  - /////////////////////////// PHASE 1 /////////////////////////////
  - A new start
  - Quick setting up (No finding only for now!)
  - first train (InceptionV3 + ResNet50)
  - we try to use pre-trained tensorflow Hub model (ResNet50)
  - first run Hub Resnet50 model is going great ! Begin full training (100 epoch)
  - run Hub resnet50 success ! (Good result)
  - run Hub InceptionV3 success ! (Good result)
  - train 7 classes on InceptionV3 success ! (Ok?)
# Things that ignored
  - data Folder
  - Model file (Will be available on Google drive)