import requests
from PIL import Image
import io

response = requests.post(
    "http://127.0.0.1:5000/upscale",
    files={"img": open("./test_inputs/baboon.png", "rb")},
)

img = Image.open(io.BytesIO(response.content))
img.show()
