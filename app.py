from flask import Flask, request, jsonify, send_file
from PIL import Image
import io
from gan_runner import load_model, img_to_tensor, scale

app = Flask(__name__)

ALLOWED_FILETYPES = ["png", "jpg", "jpeg"]


def allowed(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_FILETYPES


MODEL = load_model()


@app.route("/upscale", methods=["POST"])
def upscale():
    img_file = request.files.get("img")

    # Check that a file was given
    if img_file is None or img_file.filename == "":
        return jsonify({"error": "No file was provided."})
    if not allowed(img_file.filename):
        return jsonify({"error": "Only image files are allowed"})

    # Read and upscale the image with the model
    img_bytes = img_file.read()
    img_LR = img_to_tensor(img_bytes)
    output = scale(img_LR, MODEL)

    # Return the upscaled image as raw bytes
    result_img = Image.fromarray(output.astype("uint8"))
    rawBytes = io.BytesIO()
    result_img.save(rawBytes, "PNG")
    rawBytes.seek(0)

    return send_file(rawBytes, mimetype="image/PNG")
