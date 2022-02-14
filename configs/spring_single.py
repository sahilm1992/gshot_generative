run_type = 'springs_single_5x5'
is_meta = False
graph_type = ''
time = '1'
GPU = 2
result_path = ''
DATASETS = ['springs_n_balls_5']
target_dataset = 'springs_n_balls_5'

epochs_save = 100
epochs_end = 10000
epochs_validate = 20
train_val_dict = {
                  "springs_n_balls_5":(500,500,500)
}
num_eval_train = 500
num_eval_test = 1000
### extra variable for test graphs
load_epoch_eval = 10000    #### which model to evaluate  ### can also be set after training finishes

## Not relevant to single run but needs to be defined otherwise error will come
fine_tune = False
USE_FOR_TRAINING = None
alpha = None
inner_steps = None
weight_decay = None
load_model_epoch=None
load_epoch_tune = None

