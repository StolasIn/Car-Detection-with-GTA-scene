# Car-Detection-with-GTA-scene

![](/images/image1.png)

## Installation

```
cd path/to/YOLOX (YOLOX folder (Original or SE))
conda env create -f environment.yml
conda activate VSTHW2
pip uninstall setuptools
pip install setuptools==65.0.0
python3 setup.py develop
```

## Training

```
sh train.sh
```

setting hyper-parameters in `Code\Original\exps\example\custom\yolox_x.py`

## Inference

```
sh eval.sh
```
generate detection boxes in `detections` folder

## Pre-trained Model
you can find pre-trained weights in [this link](https://drive.google.com/drive/folders/1lYeqW8LY1eVVq72BUD0yc-rxp2A1OMfo?usp=drive_link), please check `train.sh`, `eval.sh` for resume training, inference respectively. 