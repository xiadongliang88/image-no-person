import cv2
import numpy as np
from ultralytics import YOLO
import conf


image_name = conf.schemeB['image_name']
gaussian_radius = conf.schemeB['gaussian_radius']
is_use_fill_color = conf.schemeB['is_use_fill_color']
fill_color_c = conf.schemeB['fill_color']

model = YOLO('yolov5s.pt')


def imwrite(image):
    output_path = 'outputs/output_B_' + image_name
    cv2.imwrite(output_path, image)

    print(f'Person has been removed, and the processed image has been saved in ./{output_path}')


def get_blended_image(image, blurred_mask):
    fill_color = None
    if is_use_fill_color:
        fill_color = fill_color_c
    else:
        mean_color = np.mean(image, axis=0)
        fill_color = mean_color

    fill_image = np.zeros_like(image)
    fill_image[:] = fill_color

    blended_image = (image * (1 - blurred_mask[..., np.newaxis]) + 
                    fill_image * blurred_mask[..., np.newaxis]).astype(np.uint8)

    return blended_image


def detect_person(image, box):
    if model.names[int(box.cls)] == 'person':
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        mask[y1:y2, x1:x2] = 255

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR to RGB

        blurred_mask = cv2.GaussianBlur(mask, (gaussian_radius, gaussian_radius), 0)
        blurred_mask = blurred_mask / 255.0
        blended_image = get_blended_image(rgb_image, blurred_mask)

        bgr_image = cv2.cvtColor(blended_image, cv2.COLOR_RGB2BGR) # RGB to BGR

        imwrite(bgr_image)


def detect_results(results, image):
    for result in results:
        boxes = result.boxes

        for box in boxes:
            detect_person(image, box)


if __name__ == '__main__':
    image = cv2.imread('./images/' + image_name)
    results = model(image)

    detect_results(results, image)