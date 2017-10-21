import argparse
from ast import literal_eval as make_tuple


def parser():
    """
        Define args that is used in project
    """
    parser = argparse.ArgumentParser(description="Pose guided image generation usign deformable skip layers")
    parser.add_argument("--output_dir", default='output/generated_samples', help="Directory with generated sample images")
    parser.add_argument("--batch_size", default=4, type=int, help='Size of the batch')
    parser.add_argument("--training_ratio", default=1, type=int,
                        help="The training ratio is the number of discriminator updates per generator update.")

    parser.add_argument("--l1_penalty_weight", default=100, type=float, help='Weight of gradient penalty loss')
    parser.add_argument("--number_of_epochs", default=200, type=int, help="Number of training epochs")

    parser.add_argument("--checkpoints_dir", default="output/checkpoints", help="Folder with checkpoints")
    parser.add_argument("--checkpoint_ratio", default=10, type=int, help="Number of epochs between consecutive checkpoints")
    parser.add_argument("--generator_checkpoint", default=None, help="Previosly saved model of generator")
    parser.add_argument("--discriminator_checkpoint", default=None, help="Previosly saved model of discriminator")

    parser.add_argument("--images_dir_train", default='data/market-dataset/bounding_box_train',
                        help='Folder with real images for training')
    parser.add_argument("--images_dir_test", default='data/market-dataset/bounding_box_test',
                        help='Folder with real images for testing')

    parser.add_argument("--annotations_file_train", default='data/annotations-train.csv',
                        help='Cordinates annotations for train set')
    parser.add_argument("--annotations_file_test", default='data/annotations-test.csv',
                        help='Coordinates annotations for train set')

    # parser.add_argument("--pose_hm_dir_train", default='data/pose-hm-train', help='Folder to store pose heatmaps for train')
    # parser.add_argument("--warp_dir_train", default='data/warp-train', help='Folder to score warps for train')
    # parser.add_argument("--pose_hm_dir_test", default='data/pose-hm-test', help='Folder to store pose heatmaps for test')
    # parser.add_argument("--warp_dir_test", default='data/warp-test', help='Folder to score warps for test')

    parser.add_argument("--display_ratio", default=1, type=int,  help='Number of epochs between ploting')
    parser.add_argument("--start_epoch", default=0, type=int, help='Start epoch for starting from checkpoint')
    parser.add_argument("--pose_estimator", default='pose_estimator.h5',
                            help='Pretrained model for cao pose estimator')

    parser.add_argument("--image_size", default=(128, 64), type=make_tuple, help='Size of the images')

    parser.add_argument("--pairs_file_train", default='data/pairs_train.csv',
                        help='File with pairs for training')
    parser.add_argument("--pairs_file_test", default='data/pairs_test.csv',
                        help='Folder with real images for testing')
    parser.add_argument("--images_for_test", default=12000, type=int, help="Number of images for testing")

    parser.add_argument("--use_input_pose", default=True, type=bool, help='Feed to generator input pose')
    parser.add_argument("--use_warp_skip", default=True, type=bool, help="Use warping skip layers")

    return parser
