# The MIT License (MIT)
#
# Copyright (c) 2015 Christian Zielinski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULtAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Splash screen
splash_screen = """
  _____                ____                            _ _   _             
 |  ___|_ _  ___ ___  |  _ \ ___  ___ ___   __ _ _ __ (_) |_(_) ___  _ __  
 | |_ / _` |/ __/ _ \ | |_) / _ \/ __/ _ \ / _` | '_ \| | __| |/ _ \| '_ \ 
 |  _| (_| | (_|  __/ |  _ <  __/ (_| (_) | (_| | | | | | |_| | (_) | | | |
 |_|  \__,_|\___\___| |_| \_\___|\___\___/ \__, |_| |_|_|\__|_|\___/|_| |_|
                                           |___/                           
"""

# Path to classifier
CLASSIFIER_PATH = "classifier/face-lbp.xml"

# Main program
MAIN_WINDOW = "Face Recognition Demo"
IMAGE_WIDTH = 640
ESC_KEY = 27

# Detector
DETECT_ARGS = dict(scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))

# Graphical marker
MARKER_SCALE = 0.9
MARKER_COLOR = (0, 0, 255)
MARKER_THICK = 2

# Zoom
NUM_ZOOMS = 5
ZOOM_SIZE = int(IMAGE_WIDTH / NUM_ZOOMS)
