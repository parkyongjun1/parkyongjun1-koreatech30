import argparse
import os

class Options():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="parser for MXNet-Gluon-Style-Transfer")
        subparsers = self.parser.add_subparsers(title="subcommands", dest="subcommand")

        # training args
        train_arg = subparsers.add_parser("train",
                                    help="parser for training arguments")
        train_arg.add_argument("--ngf", type=int, default=128,
                                help="number of generator filter channels, default 128")
        train_arg.add_argument("--epochs", type=int, default=10,
                                help="number of training epochs, default is 2")
        train_arg.add_argument("--batch-size", type=int, default=1,
                                help="batch size for training, default is 4")
        train_arg.add_argument("--dataset", type=str, default="/data/data_server/pyj/COCO/",
                                help="path to training dataset, the path should point to a folder "
                                "containing another folder with all the training images")
        train_arg.add_argument("--style-folder", type=str, default="/home/pyj/style/MXNet-Gluon-Style-Transfer-master/images/style1",
                                help="path to style-folder")
        train_arg.add_argument("--save-model-dir", type=str, default="models_1024_s30_10e/",
                                help="path to folder where trained model will be saved.")
        train_arg.add_argument("--image-size", type=int, default=1024,
                                help="size of training images, default is 256 X 256")
        train_arg.add_argument("--style-size", type=int, default=1024,
                                help="size of style-image, default is the original size of style image")
        train_arg.add_argument("--cuda", type=int, default=1, 
                                help="set it to 1 for running on GPU, 0 for CPU")
        # train_arg.add_argument('--gpu', type=int, default=0, help='the gpu id used for predict')
        train_arg.add_argument("--seed", type=int, default=42, 
                                help="random seed for training")
        train_arg.add_argument("--content-weight", type=float, default=1,
                                help="weight for content-loss, default is 1")
        train_arg.add_argument("--style-weight", type=float, default=30,
                                help="weight for style-loss, default is ")
        train_arg.add_argument("--lr", type=float, default=1e-3,
                                help="learning rate, default is 0.001")
        train_arg.add_argument("--log-interval", type=int, default=5000,
                                help="number of images after which the training loss is logged, default is 500")
        train_arg.add_argument("--resume", type=str, default=None,
                                help="resume if needed")

        # optim args (Gatys CVPR 2016)
        optim_arg = subparsers.add_parser("optim",
                                    help="parser for optimization arguments")
        optim_arg.add_argument("--iters", type=int, default=500,
                                help="number of training iterations, default is 500")
        optim_arg.add_argument("--content-image", type=str, default="images/content/venice-boat.jpg",
                                help="path to content image you want to stylize")
        optim_arg.add_argument("--style-image", type=str, default="images/9styles/candy.jpg",
                                help="path to style-image")
        optim_arg.add_argument("--content-size", type=int, default=512,
                                help="factor for scaling down the content image")
        optim_arg.add_argument("--style-size", type=int, default=512,
                                help="size of style-image, default is the original size of style image")
        optim_arg.add_argument("--output-image", type=str, default="logo_add/output.jpg",
                                help="path for saving the output image")
        optim_arg.add_argument("--cuda", type=int, default=1, 
                                help="set it to 1 for running on GPU, 0 for CPU")
        optim_arg.add_argument("--content-weight", type=float, default=1.0,
                                help="weight for content-loss, default is 1.0")
        optim_arg.add_argument("--style-weight", type=float, default=5.0,
                                help="weight for style-loss, default is 5.0")
        optim_arg.add_argument("--lr", type=float, default=1e1,
                                help="learning rate, default is 0.001")
        optim_arg.add_argument("--log-interval", type=int, default=50,
                                help="number of images after which the training loss is logged, default is 50")    

        # evaluation args
        eval_arg = subparsers.add_parser("eval", help="parser for evaluation/stylizing arguments")
        eval_arg.add_argument("--ngf", type=int, default=128,
                                help="number of generator filter channels, default 128")
        eval_arg.add_argument("--content-image",default ='./painter/images/content/yong.jpg', type=str, required=True,
                                help="path to content image you want to stylize")

        eval_arg.add_argument("--style-image", type=str, default="images/style1/3.jpg",
                                help="path to style-image")
        eval_arg.add_argument("--content-size", type=int, default=1024,
                                help="factor for scaling down the content image")
        eval_arg.add_argument("--style-size", type=int, default=512,
                                help="size of style-image, default is the original size of style image")
        eval_arg.add_argument("--style-folder", type=str, default="./painter/images/style1",
                                help="path to style-folder")
        eval_arg.add_argument("--style-list", type=str, default="./painter/images/style_list11",
        help="path to style-list")
        # eval_arg.add_argument("--output-image", type=str, default="logo_add/final.jpg",
        #                         help="path for saving the output image")
        eval_arg.add_argument("--model", default = './painter/models_256_512_s5/Final_epoch_6.params', type=str,
                                help="saved model to be used for stylizing the image")
        eval_arg.add_argument("--cuda", type=int, default=1,
                                help="set it to 1 for running on GPU, 0 for CPU")    

    def parse(self, cmd):
        return self.parser.parse_args(cmd)
