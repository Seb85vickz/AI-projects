import os
import cv2

# 1. Get the folder and image path safely
current_folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_folder, "novitech.png")

print(f"Looking for image at: {image_path}")

# 2. Read the image into the variable 'img'
img = cv2.imread(image_path)

# 3. Check if the image loaded and process it
if img is None:
    print("\n[ERROR] Could not open or find the image!")
else:
    print("\n[SUCCESS] Image loaded successfully! Processing...")
    
    # Convert the 'img' to grayscale
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Save the new grayscale image to your folder
    cv2.imwrite('photo.jpg', grayImage)
    
    # Show both the original and the grayscale versions
    cv2.imshow('Original', img)
    cv2.imshow('Grayscale', grayImage)
    
    # Wait for you to press a key, then close
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(img.shape)
print(img.size)