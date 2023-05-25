This is a project where I explore [xinntao's excellent ESRGAN model](https://github.com/xinntao/Real-ESRGAN). I also expose the model via a flask api and may at some point choose to host it and add a front edd project to it.

## Installing

1. Clone the repo with `git clone https://github.com/Adi-UA/adi-ss-backend`
2. Create a Python virtual environemnt `python -m venv venv`
3. Activate the virtual environment `source venv/Scripts/activate` (GitBash on Windows)
4. Install the relevant packages `pip install -r requirements.txt`

Or run this comprehensive command:
`git clone https://github.com/Adi-UA/adi-ss-backend && cd adi-ss-backend && python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`


## Run the server
Set `FLASK_APP=app` in your environment variables.
Make sure your virtual environment is active (from the previous step) and run `flask run`.

## Verifying it works
Inspect the `test_endpoint.py` file to see how the webapp expects requests to be made. Replace the baboon image with any image you want to superscale.

## API
The only endpoint available is `/upscale` at `localhost:5000`(POST). The reponse is the superscaled image (PNG).

It can be called (using the python requests library as an example) with:
```
requests.post(
    "http://127.0.0.1:5000/upscale",
    files={"img": open(<path to image you want to scale>, "rb")},
)
```

