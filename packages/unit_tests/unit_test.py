import numpy as np
import cv2
from matplotlib import pyplot as plt



class UnitTestDLM:
    # Test the detection and estimation of lane marking orientations
    def __init__(self, detect_lane_markings,get_steer_matrix_right_lane_markings, get_steer_matrix_left_lane_markings):


        imgbgr = cv2.imread("../../assets/images/visual_control/pic1_rect.png")

        img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)
        shape = img.shape
        steer_matrix_left_lm = get_steer_matrix_left_lane_markings(shape)
        steer_matrix_right_lm = get_steer_matrix_right_lane_markings(shape)


        left_masked_img, right_masked_img = detect_lane_markings(imgbgr, None)

        fig = plt.figure(figsize=(20, 15))

        ax1 = fig.add_subplot(3, 3, 1)
        # OpenCV uses BGR by default, whereas matplotlib uses RGB, so we generate an RGB version for the sake of visualization
        ax1.imshow(cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB))
        ax1.set_title("Input image"), ax1.set_xticks([]), ax1.set_yticks([])

        ax2 = fig.add_subplot(3, 3, 2)
        ax2.imshow(left_masked_img * img, cmap="gray")
        ax2.set_title("Mask (Left)"), ax2.set_xticks([]), ax2.set_yticks([])

        ax3 = fig.add_subplot(3, 3, 3)
        ax3.imshow(right_masked_img * img, cmap="gray")
        ax3.set_title("Mask (Right)"), ax3.set_xticks([]), ax3.set_yticks([])

        steer = float(np.sum(left_masked_img * steer_matrix_left_lm)) + float(np.sum(right_masked_img * steer_matrix_right_lm))
        print(f"Steer value for img 1: {steer}")


        imgbgr = cv2.imread("../../assets/images/visual_control/pic3_rect.png")

        img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)
        shape = img.shape
        steer_matrix_left_lm = get_steer_matrix_left_lane_markings(shape)
        steer_matrix_right_lm = get_steer_matrix_right_lane_markings(shape)

        left_masked_img, right_masked_img = detect_lane_markings(imgbgr, None)

        ax4 = fig.add_subplot(3, 3, 4)
        ax4.imshow(cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB))
        ax4.set_title("Input image"), ax4.set_xticks([]), ax4.set_yticks([])

        ax5 = fig.add_subplot(3, 3, 5)
        ax5.imshow(cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB))
        ax5.imshow(left_masked_img * img, cmap="gray")
        ax5.set_title("Mask (Left)"), ax5.set_xticks([]), ax5.set_yticks([])

        ax6 = fig.add_subplot(3, 3, 6)
        ax6.imshow(right_masked_img * img, cmap="gray")
        ax6.set_title("Mask (Right)"), ax6.set_xticks([]), ax6.set_yticks([])

        steer = float(np.sum(left_masked_img * steer_matrix_left_lm)) + float(np.sum(right_masked_img * steer_matrix_right_lm))
        print(f"Steer value for img 2: {steer}")


        imgbgr = cv2.imread("../../assets/images/visual_control/pic12.png")

        img = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2GRAY)
        shape = img.shape
        steer_matrix_left_lm = get_steer_matrix_left_lane_markings(shape)
        steer_matrix_right_lm = get_steer_matrix_right_lane_markings(shape)

        left_masked_img, right_masked_img = detect_lane_markings(imgbgr, None)

        ax7 = fig.add_subplot(3, 3, 7)
        ax7.imshow(cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB))
        ax7.set_title("Input image"), ax7.set_xticks([]), ax7.set_yticks([])

        ax8 = fig.add_subplot(3, 3, 8)
        ax8.imshow(cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB))
        ax8.imshow(left_masked_img * img, cmap="gray")
        ax8.set_title("Mask (Left)"), ax8.set_xticks([]), ax8.set_yticks([])

        ax9 = fig.add_subplot(3, 3, 9)
        ax9.imshow(right_masked_img * img, cmap="gray")
        ax9.set_title("Mask (Right)"), ax9.set_xticks([]), ax9.set_yticks([])

        steer = float(np.sum(left_masked_img * steer_matrix_left_lm)) + float(np.sum(right_masked_img * steer_matrix_right_lm))
        print(f"Steer value for img 3: {steer}")


