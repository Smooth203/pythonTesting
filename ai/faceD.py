#package import
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

#construct arg parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--dataset', required = True, help = 'path to imput dir of faces')
ap.add_argument('-e', '--embeddings', required = True, help = 'path to output serialised db of facial embeddings')
ap.add_argument('-d', '--detector', required = True, help = 'paths to opencvs Deep learning detectof')
ap.add_argument('-m', '--embedding-model', required = True, help = 'paths to opencvs model')
ap.add_argument('-c', '--confidence', type = float, default = 0.5, help = 'minimum prob to filter weak detections')
args = vars(ap.parse_args())


print(os.path.sep.join([args['detector'], 'deploy.prototxt']))
#load our serialised face detector from disk
print("[INFO] loading face detector...")
protoPath = os.path.sep.join([args['detector'], 'deploy.prototxt'])
modelPath = os.path.sep.join([args['detector'], 'res10_300x300_ssd_iter_140000.caffemodel'])
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

#load our serialised face embedding model from disk
print("[INFO] loading face recogniser...")
embedder = cv2.dnn.readNetFromTorch(args['embedding_model'])

#grap the paths to the input image in our dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args['dataset']))

#initialise our lists of extracted fac embeddings & corresp. people names
knownEmbeddings = []
knownNames = []

#initialse the total number of faces processed
total = 0

#loop ocver image paths
for (i, imagePaths) in enumerate(imagePaths):
	#extractr name from path
	print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	#load the img, resize to 600px wide (maintaining aspect ratio), grab the img dimensions
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=600)
	(h, w) = image.shape[:2]

	#construct blob from img
	imageBlob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB = False, crop = False)

	#apply opencvs deep learning based face detector to localise face in input img
	detect.setInput(imageBlob)
	detections = detector.forward()

	#ensure at least 1 face is found
	if len(detections) > 0:
		#assuming each image only has 1 face in so bounding box found with the greates poss
		i = np.argmax(detections[0, 0, :, 2])
		confidence = detections[0, 0, i, 2]

		#ensure this detection fits with minimum prob, to filter weak detections
		if confidence > args['confidence']:
			#con[ute the x&y for bounding box 
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype('int')

			#extract face ROI and grab the dimensions
			face = image[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]

			#ensure the face width and heigh are sufficiently large
			if fW < 20 or fH < 20:
				continue

			#construct blob for the face ROI and pass blob through embedding model to get 128-d quant
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB = True, crop = False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			#add the name and face embedding to list
			knownNames.append(name)
			knownEmbeddings.append(vec.flatten(total = total + 1))

			#dump the fac embeddings + names to disk
			print("[INFO] serialising {} encodings...".format(total))
			data = {'embeddings': knownEmbeddings, 'names': knownNames}
			f = open(args['embeddings'], 'wb')
			f.write(pickle.dumps(data))
			f.close()