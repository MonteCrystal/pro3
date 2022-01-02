import cv2
import sys

indir = sys.argv[1]
outdir = sys.argv[2]
img = cv2.imread(indir)
img = cv2.bitwise_not(img)
cv2.imwrite(outdir, img)