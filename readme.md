# Setup Instructions

To get started with the project, please follow the steps below:

1. Clone the repository:

    ```shell
    git clone https://github.com/romulo-maciel/yolo-test.git
    ```

2. Create a Python virtual environment (venv):

    ```shell
    python3 -m venv .
    ```

3. Activate the virtual environment:

      ```shell
      source bin/activate
      ```

4. Download the dataset zip file from [here](https://www.kaggle.com/datasets/jaidalmotra/weed-detection/data) and unzip it to the `datasets/archive/` folder.

5. Install the required dependencies:

    ```shell
    pip install ultralytics
    ```

6. Run the setup script:

    ```shell
    python setup.py
    ```

7. Train the YOLO model:

    ```shell
    yolo train model=models/yolov8n.pt data=plants.yaml epochs=50
    ```

That's it
