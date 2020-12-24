# EL-GY-9163 Backdoor-Detector
 This is a repo for the final project of EL-GY-9163 Machine Learning for CyberSecurity

# Files
- ***data*** directory contains necessary dataset
- ***eval*** directory contains evaluation scripts for 4 repaired networks GoodNets
- ***GoodNets*** directory contains 4 repaired networks GoodNets
- ***images*** directory contains sample testing images
- ***models*** directory contains necessary BadNets models
- ***repair*** directory contains ipynb files used to generate GoodNets

# Setup
Download data and models from this repo: https://github.com/csaw-hackml/CSAW-HackML-2020

- Put BadNet files in directory ***models*** : This is necessary to run evaluation
- Put Data files in directory ***data*** : This is necessary to run repairing scripts.

# Usage
To test a input image, run the following code:
```
    python EVAL_FILE_NAME TEST_IMAGE
```
For example, the following code will 
```
    python eval\eval_sunglasses_repaired_net.py images\test_image_sunglasses.jpg
```


# Dependencies
1. tensorflow==2.3.0
2. keract==4.3.2
3. keras
4. sys
5. h5py
6. cv2
7. numpy