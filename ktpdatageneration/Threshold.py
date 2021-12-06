from glob import glob
import os
import cv2

# read your one blurred image and convert to gray
# im_gray = cv2.imread('ktp_tif/ktp_1_1.tif', 0)


# define the paths to your input images and to where you want to put the output images    
in_dir = 'ktp_fake_tif'
out_dir = 'ktp_fake_tif_thresh'

# read the input image file names with paths into a list
infiles = in_dir + '/*.tif'
img_names = glob(infiles)
print(img_names)

# loop over each input image in a for loop
for fn in img_names:
    print('processing %s...' % fn)

    # read an input image as gray
    im_gray = cv2.imread(fn, 0)
    
    # threshold it with OTSU thresholding and get the threshold value
    thresh, im_bw = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(thresh)

    # threshold it with your saved threshold
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

    # write the result to disk in the previously created output directory
    name = os.path.basename(fn)
    outfile = out_dir + '\\' + name
    cv2.imwrite(outfile, im_bw)
    print('saved %s' % outfile)