import json
import os

def convert_coco_to_yolo(coco_json_path, output_dir):
    # Load COCO JSON file
    with open(coco_json_path) as f:
        coco_data = json.load(f)
    
    # Create output directory if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a dictionary to map image IDs to file names and sizes
    images = {image['id']: {'file_name': image['file_name'], 'width': image['width'], 'height': image['height']} for image in coco_data['images']}
    
    # Create a dictionary to map category IDs to names
    categories = {category['id']: category['name'] for category in coco_data['categories']}
    
    # Loop through annotations to create YOLO format files
    for annotation in coco_data['annotations']:
        image_id = annotation['image_id']
        category_id = annotation['category_id']
        bbox = annotation['bbox']

        # Get image details
        image_info = images[image_id]
        image_width = image_info['width']
        image_height = image_info['height']
        
        # Convert COCO bbox to YOLO format
        x_min, y_min, width, height = bbox
        x_center = (x_min + width / 2) / image_width
        y_center = (y_min + height / 2) / image_height
        width_norm = width / image_width
        height_norm = height / image_height

        # Prepare YOLO format string
        yolo_line = f"{category_id} {x_center} {y_center} {width_norm} {height_norm}\n"

        # Write to YOLO annotation file
        yolo_file_path = os.path.join(output_dir, f"{os.path.splitext(image_info['file_name'])[0]}.txt")
        with open(yolo_file_path, 'a') as yolo_file:
            yolo_file.write(yolo_line)

    print(f"COCO to YOLO conversion completed. Annotations saved in {output_dir}.")

convert_coco_to_yolo("datasets/archive/train/_annotations.coco.json", "datasets/jai_weed_detection/labels/train")
convert_coco_to_yolo("datasets/archive/test/_annotations.coco.json", "datasets/jai_weed_detection/labels/val")

os.system("mkdir -p datasets/jai_weed_detection/images/train")
os.system("mkdir -p datasets/jai_weed_detection/images/val")

os.system("cp -r datasets/archive/train/*.jpg datasets/jai_weed_detection/images/train")
os.system("cp -r datasets/archive/test/*.jpg datasets/jai_weed_detection/images/val")

os.system("rm -rf datasets/archive")