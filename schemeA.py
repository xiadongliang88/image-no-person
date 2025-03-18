import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO
from simple_lama_inpainting import SimpleLama
import conf


image_name = conf.schemeA['image_name']
is_lama = conf.schemeA['is_lama']
inpaint_radius = conf.schemeA['inpaint_radius']
is_gaussianblur = conf.schemeA['is_gaussianblur']
gaussian_radius = conf.schemeA['gaussian_radius']


model = YOLO('yolov5s.pt')


if is_lama == True:
    simple_lama = SimpleLama()


def imwrite(image):
    output_path = 'outputs/' + 'output_lama_A_' + image_name if is_lama == True else 'outputs/' + 'output_A_' + image_name
    cv2.imwrite(output_path, image)
    print(f'Person has been removed, and the processed image has been saved in ./{output_path}')


def use_lama(box, image, mask):
    if is_gaussianblur == True:
        mask_blurred = cv2.GaussianBlur(mask, (gaussian_radius, gaussian_radius), 0)
        inpainted_image = simple_lama(image, mask_blurred)
    else:
        inpainted_image = simple_lama(image, mask)

    if isinstance(inpainted_image, Image.Image):
        inpainted_image = np.array(inpainted_image)  # make PIL.Image to numpy

    inpainted_image_bgr = cv2.cvtColor(inpainted_image, cv2.COLOR_RGB2BGR) # RGB to BGR
    imwrite(inpainted_image_bgr)

    
def use_opencv(box, image, mask):
    if is_gaussianblur == True:
        mask_blurred = cv2.GaussianBlur(mask, (gaussian_radius, gaussian_radius), 0)

        inpainted_image = cv2.inpaint(image, mask_blurred, inpaintRadius=inpaint_radius, flags=cv2.INPAINT_TELEA)

        mask_edges = cv2.Canny(mask_blurred, 100, 200)
        inpainted_image = cv2.inpaint(inpainted_image, mask_edges, inpaintRadius=inpaint_radius, flags=cv2.INPAINT_TELEA)
    else:
        inpainted_image = cv2.inpaint(image, mask, inpaintRadius=inpaint_radius, flags=cv2.INPAINT_TELEA)

    imwrite(inpainted_image)


def inpaint_mask(box, image, mask):
    if is_lama == True:
        use_lama(box, image, mask)
    else:
        use_opencv(box, image, mask)


def get_mask(box):
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    mask[y1:y2, x1:x2] = 255
    return mask


def detect_person(image, box):
    if model.names[int(box.cls)] == 'person':
        mask = get_mask(box)
        inpaint_mask(box, image, mask)


def detect_results(results, image):
    for result in results:
        boxes = result.boxes

        for box in boxes:
            detect_person(image, box)


if __name__ == '__main__':
    image = cv2.imread('./images/' + image_name)
    if is_lama == True:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # SimpleLama need to RGB
        results = model(image)
    else:
        results = model(image)

    detect_results(results, image)