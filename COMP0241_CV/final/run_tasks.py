from COMP0241_CV.final.utils import get_datasets, ImageReader
from Task2 import Task2a, Task2b, Task2c
from Task3 import Task3c_rotate, Task3e

if __name__ == "__main__":
    calibPath = "calibration_data.npz"
    imageReader = ImageReader(calibPath)

    paths = [
        # "dataset/dual_cam/6/left",
        # "dataset/dual_cam/6/right",
        "dataset/dual_cam/G2/left",
        "dataset/dual_cam/G2/right",
        "dataset/dual_cam/G1/left",
        "dataset/dual_cam/G1/right",
    ]
    datasets = get_datasets(paths, max_len=16)

    circles = Task2a(datasets, imageReader, display_results=False)
    circles = Task2b(circles, display_results=False)

    # depthList = Task2c(datasets, circles, imageReader, (300 + 9.6) / 100., display_results=False)  # 2
    # print(depthList)

    TList = Task3c_rotate(datasets, circles, imageReader, method="orb", display_results=False)
    print(TList)
    # TList = Task3e(datasets, circles, imageReader, elevation=1, display_results=False)
    # print(TList)

    # Task3d(imageReader, "sift", display_results=False)


