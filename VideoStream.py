import time
import cv2
from flask import Flask,render_template,Response
import base64

app=Flask(__name__,template_folder="template")
@app.route('/')
def index():
    return render_template("./video_stream.html")

def Read_Video():
    cap=cv2.VideoCapture(0)
    while True:
        _,frame=cap.read()
        if _:
            img=cv2.flip(frame,180)
            img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
            img=cv2.imencode(".jpg",img)[1].tobytes()
            yield (b"--frame\r\n"b"Content-Type: image/jpeg\r\n\r\n"+img+b"\r\n")
            time.sleep(0.1)
        else:
            break

@app.route("/video_feed")
def Video_Feed():
    return Response(Read_Video(),mimetype="multipart/x-mixed-replace; boundary=frame")


app.run(debug=True,host="127.0.0.1",port=1122)