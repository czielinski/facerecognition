# Face Recognition Demo

This is a face recognition demo written in Python using [OpenCV](http://opencv.org/). It uses a cascade classifier for [local binary patterns](https://en.wikipedia.org/wiki/Local_binary_patterns). It can recognize human faces in real-time video streams, e.g. from a webcam.

### Installation

You can clone the git repository via `git clone https://github.com/czielinski/facerecognition.git`. To run the code you need the `numpy` and the `opencv` libraries. On a Debian based system you can install them via `apt-get install python-numpy python-opencv`.

### Run the program

To run the program change to the `facerecognition/` directory and start it with `python facerecognition.py`. It will then record a video stream from your webcam and do face recognition in real-time as shown here:

![Example screenshot](https://github.com/czielinski/facerecognition/raw/master/screenshot.png "Example screenshot")

### Cascade classifier

I trained the cascade classifier in this demo using the tools provided in [this repository](https://github.com/mrnugget/opencv-haar-classifier-training). A dataset of cropped faces which can be used for training can be found in the [LFWcrop Face Dataset](http://conradsanderson.id.au/lfwcrop/), which is a cropped version of the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) database.

