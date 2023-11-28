import cv2
import inference
import supervision as sv
import os
from dotenv import load_dotenv

annotator = sv.BoxAnnotator()

def on_prediction(predictions, image):
    labels = [p["class"] for p in predictions["predictions"]]
    detections = sv.Detections.from_roboflow(predictions)
    cv2.imshow(
        "Prediction", 
        annotator.annotate(
            scene=image, 
            detections=detections,
            labels=labels
        )
    ),
    cv2.waitKey(1)

load_dotenv()
VIDEO_ROUTE = os.getenv("VIDEO_ROUTE")

inference.Stream(
    source=VIDEO_ROUTE, # or rtsp stream or camera id
    model="bikes-ped-scooters/4", # from Universe
    output_channel_order="BGR",
    use_main_thread=True, # for opencv display
    on_prediction=on_prediction, 
)
