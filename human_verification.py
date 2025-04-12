import cv2
import numpy as np
from pathlib import Path

class HumanVerification:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def verify_human(self, image_path):
        """
        Verify if the image contains a human face.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            tuple: (bool, str) - (is_human, message)
        """
        try:
            # Read the image
            img = cv2.imread(str(image_path))
            if img is None:
                return False, "Could not read the image file"
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            if len(faces) > 0:
                return True, f"Human face detected. Found {len(faces)} face(s)."
            else:
                return False, "No human face detected in the image."
                
        except Exception as e:
            return False, f"Error processing image: {str(e)}"

def main():
    verifier = HumanVerification()
    
    image_path = input("Enter the path to the profile picture: ")
    
    is_human, message = verifier.verify_human(image_path)
    
    print("\nVerification Results:")
    print(f"Status: {'Approved' if is_human else 'Rejected'}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main() 