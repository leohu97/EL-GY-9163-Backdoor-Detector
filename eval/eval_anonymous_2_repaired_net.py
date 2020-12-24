import keras
import sys
import h5py
import numpy as np
import cv2
import matplotlib.pyplot as plt



input_data_filename = str(sys.argv[1])

bd_model_filename = "models/anonymous_2_bd_net.h5"
pruned_model_filename = "GoodNets/G3.h5"

THRES_CONF = 0.99
THRES_DETECT = 0.91
CLASS_NUM = 1282

def model_package(pruned_model, bd_model, x_test):
    # probs of each class
    y_pred_prob_badnet = bd_model.predict(x_test) 
    y_pred_prob_pruned = pruned_model.predict(x_test)
    
    # class having max prob
    y_pred_badnet = np.argmax(y_pred_prob_badnet, axis=1)
    y_pred_pruned =  np.argmax(y_pred_prob_pruned, axis=1)  

    res = np.zeros((x_test.shape[0]))
    for i in range(0, x_test.shape[0]):
        # max prob
        y_pred_prob_max_badnet = np.max(y_pred_prob_badnet[i])
        y_pred_prob_max_pruend = np.max(y_pred_prob_pruned[i])

        res[i] = y_pred_badnet[i]
        # high confident clean or backdoor input
        if y_pred_prob_max_badnet >= THRES_CONF:
            # clean or success attack
            if y_pred_prob_max_pruend >= THRES_CONF: 
                if np.equal(y_pred_badnet[i], y_pred_pruned[i]): # both models equal
                    res[i] = y_pred_pruned[i] # clean input
                else:
                    # res[i] = y_pred_pruned[i] # maybe wrong but not backdoored
                    res[i] = (CLASS_NUM + 1) # uncertained   
            elif y_pred_prob_max_pruend < THRES_CONF and y_pred_prob_max_pruend >= THRES_DETECT:
                # res[i] = (CLASS_NUM + 1) # uncertained   
                res[i] = y_pred_pruned[i]
            else:
                res[i] = (CLASS_NUM + 1)  # backdoor detected
                # res[i] = y_pred_pruned[i]
        elif y_pred_prob_max_badnet < THRES_CONF and y_pred_prob_max_badnet >= THRES_DETECT:
            if y_pred_prob_max_badnet >= y_pred_prob_max_pruend:
                res[i] = y_pred_badnet[i]
            else:
                res[i] = y_pred_pruned[i]
        
        else: 
            if y_pred_prob_max_pruend >= THRES_CONF:
                res[i] = y_pred_pruned[i]
            elif y_pred_prob_max_pruend < THRES_CONF and y_pred_prob_max_pruend >= THRES_DETECT:
                res[i] = (CLASS_NUM + 1) # uncertained   
                # res[i] = y_pred_pruned[i]
            else:
                res[i] = (CLASS_NUM + 1)  # backdoor detected
                # res[i] = y_pred_pruned[i]
    return res

def data_loader(filepath):
    data = h5py.File(filepath, 'r')
    x_data = np.array(data['data'])
    y_data = np.array(data['label'])
    x_data = x_data.transpose((0,2,3,1))

    return x_data, y_data

def data_preprocess(x_data):
    return x_data/255

def main():
    #input data
    x_test = cv2.imread(input_data_filename, cv2.IMREAD_UNCHANGED)
    x_test = cv2.cvtColor(x_test, cv2.COLOR_BGR2RGB)
    x_test = data_preprocess(x_test) # = x_spdata_tp

    x_test = x_test[np.newaxis,:]
    

    bd_model = keras.models.load_model(bd_model_filename)
    pruned_model = keras.models.load_model(pruned_model_filename)

    y_pred = model_package(pruned_model, bd_model, x_test)

    print(int(y_pred))

if __name__ == '__main__':
    main()