#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os
import torch.nn as nn
from yolox.exp import Exp as MyExp

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/HW2_ObjectDetection_2023"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"

        self.multiscale_range = 3
        self.max_epoch = 100
        self.no_aug_epochs = 25
        self.num_classes = 1
        self.mosaic_prob = 0.0
        self.shear = 0.0
        self.degrees = 0.0
        
        self.data_num_workers = 0
        self.eval_interval = 1
        self.input_size = (1088, 1920)
        self.test_size = (1088, 1920)

        