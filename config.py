# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:32:34 2019

@author: chxy
"""

import argparse

arg_lists = []
parser = argparse.ArgumentParser(description='classification')


def str2bool(v):
    return v.lower() in ('true', '1')


def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg

# data params
data_arg = add_argument_group('Data Params')
data_arg.add_argument('--num_classes', type=int, default=2,
                      help='Number of classes to classify')
data_arg.add_argument('--batch_size', type=int, default=40,
                      help='# of images in each batch of data')
data_arg.add_argument('--num_workers', type=int, default=0,
                      help='# of subprocesses to use for data loading')
data_arg.add_argument('--pin_memory', type=str2bool, default=True,
                      help='whether to copy tensors into CUDA pinned memory')
data_arg.add_argument('--shuffle', type=str2bool, default=True,
                      help='Whether to shuffle the train indices')
data_arg.add_argument('--input_size', type=int, default=224,
                      help='Whether to shuffle the train indices')


# training params
train_arg = add_argument_group('Training Params')
train_arg.add_argument('--is_train', type=str2bool, default=True,
                       help='Whether to train or test the model')
train_arg.add_argument('--momentum', type=float, default=0.9,
                       help='Momentum value')

train_arg.add_argument('--weight_decay', type=float, default=1e-4,
                       help='value of weight dacay for regularization')
train_arg.add_argument('--nesterov', type=str2bool, default=True,
                       help='Whether to use Nesterov momentum')
train_arg.add_argument('--lr_patience', type=int, default=10,
                       help='Number of epochs to wait before reducing lr')
train_arg.add_argument('--train_patience', type=int, default=100,
                       help='Number of epochs to wait before stopping train')

#########################################################
train_arg.add_argument('--paramseed', type=int, default=3,
                       help='value of seed')
train_arg.add_argument('--gamma', type=float, default=0.1,
                       help='value of learning rate decay')
train_arg.add_argument('--feature_extract', type=str2bool, default=True,
                       help='')
train_arg.add_argument('--use_pretrained', type=str2bool, default=True,
                       help='')
train_arg.add_argument('--step_size', type=int, default=10,
                       help='')

train_arg.add_argument('--epochs', type=int, default=20,
                       help='# of epochs to train for')
train_arg.add_argument('--init_lr', type=float, default=0.01,
                       help='Initial learning rate value')
# train_arg.add_argument('--init_lr', type=float, default=0.01,
#                        help='Initial learning rate value')



# other params
misc_arg = add_argument_group('Misc.')
misc_arg.add_argument('--use_gpu', type=str2bool, default=True,
                      help="Whether to run on the GPU")
misc_arg.add_argument('--best', type=str2bool, default=False,
                      help='Load best model or most recent for testing')
misc_arg.add_argument('--random_seed', type=int, default=1,
                      help='Seed to ensure reproducibility')
misc_arg.add_argument('--traindata_dir', type=str, default="/DATA/LWN/new experiment2（复件）/data/COVID-19_Radiography_Dataset_2/train",
                      help='Directory in which data is stored')
misc_arg.add_argument('--predictdata_dir', type=str, default='/DATA/LWN/new experiment2（复件）/data/COVID-19_Radiography_Dataset_2/test',
                      help='Directory in which data is stored')
# misc_arg.add_argument('--traindata_dir', type=str, default='/home/cvnlp/LiChuanxiu/DataSets/BreaKHis/400/train',
#                       help='Directory in which data is stored')
# misc_arg.add_argument('--predictdata_dir', type=str, default='/home/cvnlp/LiChuanxiu/DataSets/BreaKHis/400/predict',
#                       help='Directory in which data is stored')
misc_arg.add_argument('--ckpt_dir', type=str, default='./ckpt',
                      help='Directory in which to save model checkpoints')
misc_arg.add_argument('--logs_dir', type=str, default='./logs/',
                      help='Directory in which Tensorboard logs wil be stored')
misc_arg.add_argument('--use_tensorboard', type=str2bool, default=True,
                      help='Whether to use tensorboard for visualization')
misc_arg.add_argument('--resume', type=str2bool, default=False,
                      help='Whether to resume training from checkpoint')
misc_arg.add_argument('--print_freq', type=int, default=10,
                      help='How frequently to print training details')
misc_arg.add_argument('--save_name', type=str, default='FID5_se_resnet50_se_resnext101',
                      help='Name of the model to save as')
misc_arg.add_argument('--model_num', type=int, default=2,
                      help='Number of models to train for DML')

def get_config():
    config, unparsed = parser.parse_known_args()
    return config, unparsed

