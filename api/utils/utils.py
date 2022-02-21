import numpy as np
import io

from typing import List, Dict
from PIL import Image


def prepare_image(image_file: bytes) -> np.ndarray:
    """Prepares an image for model prediction."""
    image = Image.open(io.BytesIO(image_file))
    image = image.resize((224, 224))
    image = np.array(image).astype("float32")
    return np.expand_dims(image, 0)


def decode_predictions(
    predictions: np.ndarray, imagenet_categories: List[str]
) -> Dict[str, float]:
    """Decodes model predictions."""
    predictions = np.squeeze(predictions)
    pred_name = imagenet_categories[int(predictions.argmax())]
    response_dict = {"Label": pred_name, "Score": f"{predictions.max():.3f}"}

    return response_dict
