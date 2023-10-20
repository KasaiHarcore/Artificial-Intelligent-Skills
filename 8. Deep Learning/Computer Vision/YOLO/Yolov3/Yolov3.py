import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from tqdm import tqdm

# IoU function
def iou(box_1, box_2, is_pred = True):
    if is_pred:
        # box_1: (N, 4) (x, y, w, h)
        b1_x1 = box_1[..., 0] - box_1[..., 2] / 2
        b1_y1 = box_1[..., 1] - box_1[..., 3] / 2
        b1_x2 = box_1[..., 0] + box_1[..., 2] / 2
        b1_y2 = box_1[..., 1] + box_1[..., 3] / 2
        
        # box_2: (N, 4) (x, y, w, h)
        b2_x1 = box_2[..., 0] - box_2[..., 2] / 2
        b2_y1 = box_2[..., 1] - box_2[..., 3] / 2
        b2_x2 = box_2[..., 0] + box_2[..., 2] / 2
        b2_y2 = box_2[..., 1] + box_2[..., 3] / 2
        
        # Get coordinates of intersection rectangle by taking the maximum of the x and y coordinates of the intersection rectangle
        x1 = torch.max(b1_x1, b2_x1)
        y1 = torch.max(b1_y1, b2_y1)
        x2 = torch.min(b1_x2, b2_x2)
        y2 = torch.min(b1_y2, b2_y2)
        
        # Calculate the area of intersection rectangle
        intersection = (x2 - x1).clamp(0) * (y2 - y1).clamp(0)
        
        # Calculate union
        b1_area = abs((b1_x2 - b1_x1) * (b1_y2 - b1_y1))
        b2_area = abs((b2_x2 - b2_x1) * (b2_y2 - b2_y1))
        union = b1_area + b2_area - intersection
        
        # Calculate IoU score
        iou = intersection / (union + 1e-6)
        
        return iou
    else:
        # Calculate intersection area 
        intersection_area = torch.min(box1[..., 0], box2[..., 0]) * torch.min(box1[..., 1], box2[..., 1]) 
  
        # Calculate union area 
        box1_area = box1[..., 0] * box1[..., 1] 
        box2_area = box2[..., 0] * box2[..., 1] 
        union_area = box1_area + box2_area - intersection_area 
  
        # Calculate IoU score 
        iou_score = intersection_area / union_area 
  
        # Return IoU score 
        return iou_score
    
