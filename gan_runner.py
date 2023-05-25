import os.path as osp
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch

MODEL_PATH = "./models/RRDB_ESRGAN_x4.pth"  # models/RRDB_ESRGAN_x4.pth
DEVICE = torch.device("cpu")


def load_model():
    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    model.load_state_dict(torch.load(MODEL_PATH), strict=True)
    model.eval()
    model = model.to(DEVICE)
    return model


def img_to_tensor(img_bytes):
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(DEVICE)
    return img_LR


def scale(img_LR: torch.Tensor, model):
    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    return output
