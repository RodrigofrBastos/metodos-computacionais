import numpy as np
import cv2


# while True:

#     img = np.zeros((1080,1920), np.uint8)
#     cv2.imshow('frame', img)
#     key = cv2.waitKey(1)

    
#     if key == ord("q"):
#         break

# cv2.destroyAllWindows()

frame = np.ones((16,9), dtype=complex)
print(frame)

frame1 = np.diag(range(2,12,2))
print(frame1)

array = np.array([range(-2,10,4)], dtype=float)
print(array)





