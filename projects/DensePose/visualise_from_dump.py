import sys
sys.path.append("/data/cvfs/as2562/detectron2/projects/DensePose/")
import pickle
import argparse
from densepose.structures import DensePoseResult


def visualise_denspose_results(dump_file):
    with open(dump_file, 'rb') as f_results:
        data = pickle.load(f_results)

    for entry in data:
        fname = entry['file_name']
        bboxes_xyxy = entry['pred_boxes_XYXY']
        # Choose the result instance (index) with largest bounding box
        print(bboxes_xyxy)
        # results_encoded = entry['pred_densepose']
        # iuv_arr = DensePoseResult.decode_png_data(*result_encoded)
        # print(iuv_arr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dump_file', type=str)
    args = parser.parse_args()

    visualise_denspose_results(args.dump_file)
