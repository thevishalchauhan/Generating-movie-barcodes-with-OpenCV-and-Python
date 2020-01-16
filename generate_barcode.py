# USAGE
# python generate_barcode.py --video videos/jurassic_park_trailer.mp4 --output output/jurassic_park_trailer.json --skip 25

# import the necessary packages
import argparse
import json
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video")
ap.add_argument("-o", "--output", required=True,
	help="path to output JSON file containing frame averages")
ap.add_argument("-s", "--skip", type=int, default=0,
	help="# of frames to skip (to create shorter barcodes)")
args = vars(ap.parse_args())

# initialize the list of frame averages along with the total
# number of frames read
avgs = []
total = 0

# grab a pointer to the video file
print("[INFO] looping over frames in video (this will take awhile)...")
video = cv2.VideoCapture(args["video"])

# loop over the frames of the video
while True:
	# grab the current frame
	(grabbed, frame) = video.read()
 
	# check to see if we have reached the end of the
	# video
	if not grabbed:
		break

	# increment the total number of frames read
	total += 1

	# check to see if we should compute the average RGB value
	# of the current frame
	if args["skip"] == 0 or total % args["skip"] == 0:
		avg = cv2.mean(frame)[:3]
		avgs.append(avg)

# release the video pointer
video.release()

# dump the frame averages to file
print("[INFO] saving frame averages...")
f = open(args["output"], "w")
f.write(json.dumps(avgs))
f.close()
print("[INFO] {:,} total frame averages saved".format(len(avgs)))