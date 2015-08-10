#!/usr/bin/python

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

from __future__ import print_function

import numpy as np
import cv2
import os
import sys
import datetime
import config


def main():
    # Display splash screen
    print(config.splash_screen)

    # Set up the video capture
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("ERROR: Could not open video capture device")
        sys.exit(1)

    # Set up the cascade classifier
    if not os.path.isfile(config.CLASSIFIER_PATH):
        print("ERROR: Cannot open classifier file")
        sys.exit(2)

    classifier = cv2.CascadeClassifier(config.CLASSIFIER_PATH)
    
    # Create a resizable window
    cv2.namedWindow(config.MAIN_WINDOW, cv2.cv.CV_WINDOW_NORMAL)

    # Capture loop
    while video_capture.isOpened():
        success, image = video_capture.read()
        if not success:
            print("ERROR: Could not read from video capture device")
            break

        # Rescale to IMAGE_WIDTH
        aspect_ratio = image.shape[0] / float(image.shape[1])
        image_size = (config.IMAGE_WIDTH, int(aspect_ratio * config.IMAGE_WIDTH))
        image = cv2.resize(image, image_size)

        # Detect
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        objects = classifier.detectMultiScale(gray, **config.DETECT_ARGS)
        time_string = str(datetime.datetime.now())

        # Extract zoomed images
        zoom_images = []
        for x, y, w, h in objects[:config.NUM_ZOOMS]:
            zoom_image = image[y : y + h, x : x + w, :].copy()
            zoom_image = cv2.resize(zoom_image, (config.ZOOM_SIZE, config.ZOOM_SIZE))
            zoom_images.append(zoom_image)
        
        # Draw markers
        num_objects = len(objects)
        for num, box in enumerate(objects, start=1):
            x, y, w, h = box
            
            # Draw circle
            center = (int(x + w/2), int(y + h/2))
            scale = config.MARKER_SCALE
            radius = int(scale * min(w, h))

            cv2.circle(image, center, radius, config.MARKER_COLOR, config.MARKER_THICK)

            # Write text
            text_pos = (int(center[0] + scale * w), int(center[1] + scale * h))
            text_msg = "{}".format(num)

            cv2.putText(image, text_msg, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 1, config.MARKER_COLOR, 3)

            # Status message
            format_args = (time_string, num, num_objects, center[0], center[1])
            print("{}: Detected object {}/{} at (x, y) = ({}, {})".format(*format_args))

        if num_objects > 0:
            print()

        # Display zoom bar
        if len(zoom_images) > 0:
            zoom_bar = np.hstack(zoom_images)
            zoom_h, zoom_w = zoom_bar.shape[:2]
            image[:zoom_h, -zoom_w:] = zoom_bar

        # Display the resulting image
        cv2.imshow(config.MAIN_WINDOW, image)

        # Waiting for escape key
        if cv2.waitKey(1) == config.ESC_KEY:
            break

    # Clean up
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
