import cv2
from tensorflow.python.keras.models import load_model
from pre_process import scale_and_center

def display_img(img):
    cv2.imshow('sudoku', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def extract_number(img):
    temp = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            image = img[i][j]
            image = cv2.resize(image, (28,28))
            thresh = 128
            gray = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
            conts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            conts = conts[0] if len(conts)==2 else conts[1]
            
            for c in conts:
                x, y, w, h = cv2.boundingRect(c)
                if(x <3 or y < 3 or h < 3 or w < 3):
                    continue
                ROI = gray[y:y + h, x:x + w]
                ROI = scale_and_center(ROI, 120)
                cv2.imwrite("CleanedCells/cell{}{}.jpg".format(i, j), ROI)
                temp[i][j] = predict(ROI)
                
    return temp

def predict(img):
    image = img.copy()
    image = cv2.resize(image, (28, 28))
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    image /= 255
    model = load_model('model.hdf5')
    pred = model.predict_classes(image.reshape(1, 28, 28, 1), batch_size=1)
    
    #print(pred[0])
    return pred[0]




