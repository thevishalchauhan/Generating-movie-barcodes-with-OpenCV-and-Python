# USAGE
# python visualize_barcode.py --avgs output/jurassic_park_trailer.json --barcode output/jurassic_park_trailer.png --barcode-width 5

# import the necessary packages
import numpy as np
import argparse
import json
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--avgs", required=True,
	help="path to averages JSON file")
ap.add_argument("-b", "--barcode", required=True,
	help="path to output barcode visualization image")
ap.add_argument("-t", "--height", type=int, default=250,
	help="height of output barcode image")
ap.add_argument("-w", "--barcode-width", type=int, default=1,
	help="width of each bar in output image")
args = vars(ap.parse_args())

# load the averages file and convert it to a NumPy array
avgs = json.loads(open(args["avgs"]).read())
avgs = np.array(avgs, dtype="int")

# grab the individual bar width and allocate memory for
# the barcode visualization
bw = args["barcode_width"]
barcode = np.zeros((args["height"], len(avgs) * bw, 3),
	dtype="uint8")

# loop over the averages and create a single 'bar' for
# each frame average in the list
for (i, avg) in enumerate(avgs):
	cv2.rectangle(barcode, (i * bw, 0), ((i + 1) * bw,
		args["height"]), avg, -1)

# write the video barcode visualization to file and then
# display it to our screen
cv2.imwrite(args["barcode"], barcode)
cv2.imshow("Barcode", barcode)
cv2.waitKey(0)