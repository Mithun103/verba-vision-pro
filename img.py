import easyocr
from PIL import Image
import json
import io

# Initialize the EasyOCR reader for English (or add other languages as needed)
reader = easyocr.Reader(['en'])

def perform_ocr(image_stream):
    # Perform OCR using EasyOCR on the image stream (PIL Image)
    image = Image.open(image_stream)
    result = reader.readtext(image)
    
    detected_text = []
    for bbox, text, confidence in result:
        detected_text.append({
            "text": text,
            "bounding_box": bbox
        })
    
    return detected_text

def process_image(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        left_box = (0, 0, width // 2, height)
        right_box = (width // 2, 0, width, height)

        all_detected_text = []
        for box in [left_box, right_box]:
            column_img = img.crop(box)
            with io.BytesIO() as image_stream:
                column_img.save(image_stream, format='JPEG')
                image_stream.seek(0)
                detected_text = perform_ocr(image_stream)
                all_detected_text.extend([item['text'] for item in detected_text])
    
    return "\n".join(all_detected_text)

def ocr_local_image_full(image_path, output_json_file, output_text_file):
    # Read the image and perform OCR
    with open(image_path, "rb") as image_stream:
        detected_text = perform_ocr(image_stream)
    
    # Read the existing JSON file
    try:
        with open(output_json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Append the new detected text to the JSON data
    data.append({
        "image_path": image_path,
        "detected_text": detected_text
    })

    # Write the updated data back to the JSON file
    with open(output_json_file, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    # Write the detected text to a text file
    with open(output_text_file, "w", encoding='utf-8') as file:
        file.write("\n".join([item['text'] for item in detected_text]))


