# EL-GY-9163 Backdoor-Detector
 This is a repo for the final project of EL-GY-9163 Machine Learning for CyberSecurity

# Directories and Files
- ***data*** directory contains necessary dataset
- ***eval*** directory contains evaluation scripts for 4 repaired networks GoodNets
- ***GoodNets*** directory contains 4 repaired networks GoodNets
    - The number in the filename indicates attack success rate for backdoored input and classified success rate for clean input
        -  ***G1_07_90.h5*** means an approximately 0.7% ASR and 90% CSR.
        - ***G4_0_054_011_91.h5*** means an approximately 0% ASR for sunglasses, 0.54% ASR for eyebrows, 0.11% ASR for lipstick, and 90% CSR.
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
For example, the following code will return a predicted class of test_image_sunglasses.jpg using the model specified in eval_sunglasses_repaired_net.py file.
```
    python eval\eval_sunglasses_repaired_net.py images\test_image_sunglasses.jpg
```

To test mulitple inputs, use ***model_package*** function from any eval.py file.

# Repair
To repair models from scratch, use files in the repair directory.

\*Note: B3 does not have a repair script due to the lack of testing data. Please use the given generator with number of prune setting to 42, the ***Answer to the Ultimate Question of Life, the Universe, and Everything.***


# Dependencies
1. tensorflow==2.3.0
2. keract==4.3.2
3. keras
4. sys
5. h5py
6. cv2
7. numpy