#필요없음
import tensorflow as tf
import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
import cv2


model = model = tf.keras.models.load_model('./my_model')
print(model)