#!/usr/bin/env python3
"""
@Filename:    visualize.py
@Author:      dulanj
@Time:        02/04/2022 11:09
"""
import cv2
import numpy as np

image_path = "scrum_23_136850_jpg.rf.3ead069c92c50ef78cf9dc61f4cfdf84.jpg"
annotation_path = "scrum_23_136850_jpg.rf.3ead069c92c50ef78cf9dc61f4cfdf84.txt"

event_names = {
    '0': 'Scrum',
    '1': 'Lineout',
    '2': 'Ruck',
}


def main():
    data = np.loadtxt(annotation_path, dtype=str, delimiter=' ')
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    print("Data:", data)
    print("Image shape:", image.shape)

    xmid = int(float(data[1]) * w)
    ymid = int(float(data[2]) * h)
    width = int(float(data[3]) * w)
    height = int(float(data[4]) * h)

    xmin = int(xmid - width / 2)
    xmax = int(xmid + width / 2)
    ymin = int(ymid - height / 2)
    ymax = int(ymid + height / 2)

    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    cv2.putText(image, event_names[data[0]], (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("image", image)
    cv2.imwrite("image_output.jpg", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
