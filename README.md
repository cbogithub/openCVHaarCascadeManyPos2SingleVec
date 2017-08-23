# openCVHaarCascadeManyPos2SingleVec
### This tutorial assumes you took the same steps in [sentdex's tutorial](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
 have already created your negative images, and named all directories and files the same as in the tutorial.

If you were following sentDex's tutorial on training your own Haar cascade you may have noticed that he uses only one
positive image and created a bunch of samples with that one image.  If you want to use more than one positive
image in your haar cascade then follow this.

Step 1
=======
Place all your positives images into one folder

Step 2
======
Open python console and import sampleCreator
Run sampleCreator.createInfoDirs(*pathToPositiveImagesFolder*)
This creates a bunch of folders that will hold your newly created samples

Step 3
======
Run sampleCreator.createSamples(*pathToPositiveImagesFolder*, *numberOfSamplesToBeCreatedPerImage*)
This will loop through all your images in your positives folders, creating however many samples you specify and place
them in the corresponding info folder. In sentdex's tutorial he made about 2000 images so I usually take
2000 and divide by the number the number of positive images I have. Next it will create a vec file for each info folder
and place them all in a directory called vecDirectory.

Step 4
======
Download this github Project [wulfebw/mergevec](https://github.com/wulfebw/mergevec)
Follow the directions on their readme running this command: "python mergevec.py -v vecDirectory -o your_output_filename.vec"
The resulting .vec file is then used in the "opencv_traincascade -data data -vec *newVecFileHere* -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20"
command



