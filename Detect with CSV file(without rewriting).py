#importing the necessary required modules
import cv2
import time
import csv

#Define the video capture
capture = cv2.VideoCapture(0)
output_file = "output.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

#Initialize the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
start_time = time.time()
faces_detected = 0
csv_file = "face_count.csv"

with open(csv_file, mode='a') as file:
    writer = csv.writer(file)
    #writer.writerow(["Time", "Faces"])
while True:
    ret, frame = capture.read()
    if not ret:
        break
    cv2.imshow("Video Capture", frame)
    output.write(frame)

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in detected_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
    elapsed_time = time.time() - start_time
  
    if elapsed_time >= 3.0:
        print(str(time.strftime("%d-%m-%y %H:%M:%S"))+"-"+str(len(detected_faces)))
#Open the CSV file for writing
        with open(csv_file, mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%d-%m-%y %H:%M:%S"),len(detected_faces)])
        start_time = time.time()
        faces_detected = 0

    #Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the video capture and video writer
capture.release()
output.release()

#Close all OpenCV windows
cv2.destroyAllWindows()

