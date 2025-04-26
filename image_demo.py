# wweek 1 practical task:
# by Tahir Ali Bughio DIT/2k22/54 
# I have commented these all steps, so when you checked it you need to uncomment one by one and show the result.thanks 

# ***-Step 1: Load and Display Image-***
# it is not commented 

# import cv2
# image = cv2.imread('tahirjan.jpeg')
# cv2.imshow('Original Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ***-Step 2: Convert to Grayscale-***
# ***commented*** 

# import cv2
# image = cv2.imread('tahirjan.jpeg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale Image', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ***-Step 3: Resize Image-***
# ***commented*** 

# import cv2
# image = cv2.imread('tahirjan.jpeg')
# resized = cv2.resize(image, (300, 300))
# cv2.imshow('Resized Image', resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ***-Step 4: Edge Detection-***
# ***commented*** 

import cv2
image = cv2.imread('tahirjan.jpeg')
edges = cv2.Canny(image, 100, 200)
cv2.imshow('Edge Detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()




