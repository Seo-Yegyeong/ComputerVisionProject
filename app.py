import cv2
import inference
import supervision as sv

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

file_route = "/Users/samuelcho/2023-2/ComputerVision/project3/영일대 자전거.mp4"

inference.Stream(
    source=file_route, # or rtsp stream or camera id
    model="bikes-ped-scooters/4", # from Universe
    output_channel_order="BGR",
    use_main_thread=True, # for opencv display
    on_prediction=on_prediction, 
)
