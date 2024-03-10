import json
import os
import cv2 as cv
import numpy as np

def build_image(id, image_path, file_name):
    path = f'{image_path}/{file_name}.jpg'
    image = cv.imread(path, 1)

    height, width, _ = image.shape
    obj = dict()
    obj['id'] = id
    obj['width'] = width
    obj['height'] = height
    obj['file_name'] = f'{file_name}.jpg'

    return obj, width, height

def build_categoty(id, name, super):
    obj = dict()
    obj['id'] = id
    obj['name'] = name
    obj['super'] = super
    return obj

def build_annotation(id, image_id, category_id, ann, width, height):
    left = width * (ann['x_center'] - ann['width']/2)
    top = height * (ann['y_center'] - ann['height']/2)
    width = width * ann['width']
    height = height * ann['height']
    
    obj = dict()
    obj['id'] = id
    obj['image_id'] = image_id
    obj['category_id'] = int(category_id)
    obj['area'] = width * height
    obj['bbox'] = [left, top, width, height]
    obj['iscrowd'] = 0
    return obj

def read_txt(label_path, file_name):
    path = f'{label_path}/{file_name}.txt'
    results = []

    with open(path, 'r') as f:
        for line in f:
            contents = line.split()
            obj = dict()
            obj['class'] = float(contents[0])
            obj['x_center'] = float(contents[1])
            obj['y_center'] = float(contents[2])
            obj['width'] = float(contents[3])
            obj['height'] = float(contents[4])

            results.append(obj)
    return results

def convert_dataset(path, dtype = 'train'):
    image_path = f'{path}/{dtype}'
    if dtype == 'train':
        label_path = f'{path}/train_labels'
    else:
        label_path = f'{path}/val_labels'

    file_names = []
    ann_ids = 1

    obj = dict()

    obj['images'] = []
    obj['categories'] = []
    obj['annotations'] = []


    for file_path in os.listdir(image_path):
        if os.path.isfile(os.path.join(image_path, file_path)):
            file_names.append(file_path.replace('.jpg', ''))

    file_names = sorted(file_names)

    obj['categories'].append(build_categoty(1, 'car', 'vehicle'))
    for i,file_name in enumerate(file_names):
        results = read_txt(label_path, file_name)
        image_obj, width, height = build_image(i+1, image_path, file_name)
        obj['images'].append(image_obj)
        for ann in results:
            obj['annotations'].append(build_annotation(ann_ids, i+1, 1, ann, width, height))
            ann_ids += 1

    with open(f"{path}/instances_{dtype}2017.json", "w") as out_file:
        json.dump(obj, out_file, indent = 4)

def generate_gt_txt(path, dtype):
    file_names = []
    image_path = f'{path}/{dtype}'
    if dtype == 'train2017':
        label_path = f'{path}/train_labels'
    else:
        label_path = f'{path}/val_labels'

    for file_path in os.listdir(image_path):
        if os.path.isfile(os.path.join(image_path, file_path)):
            file_names.append(file_path.replace('.jpg', ''))

    file_names = sorted(file_names)
    for i,file_name in enumerate(file_names):
        results = read_txt(label_path, file_name)
        image_obj, width, height = build_image(i+1, image_path, file_name)
        with open(f'groundtruths/{file_name}.txt', 'w') as f:
            for ann in results:
                bbox = build_annotation(0, i+1, 1, ann, width, height)['bbox']
                lines = ['0', f' {round(bbox[0])} ', f'{round(bbox[1])} ', f'{round(bbox[0]+bbox[2])} ', f'{round(bbox[1]+bbox[3])}\n']
                f.writelines(lines)

if __name__ == '__main__':
    path = 'datasets/HW2_ObjectDetection_2023'
    # convert_dataset(path, 'train')
    generate_gt_txt(path, 'val2017')
