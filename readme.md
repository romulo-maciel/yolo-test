# Setup Instructions

To get started with the project, please follow the steps below:

1. Create a Python virtual environment (venv) by running the following command in your terminal:

    ```shell
    python3 -m venv myenv
    ```

2. Activate the virtual environment:

    - For Windows:

      ```shell
      myenv\Scripts\activate
      ```

    - For macOS/Linux:

      ```shell
      source myenv/bin/activate
      ```

3. Download the dataset zip file from [here](https://www.kaggle.com/datasets/jaidalmotra/weed-detection/data) and unzip it to the `datasets/archive/` directory.

4. Install the required dependencies by running the following command:

    ```shell
    pip install ultralytics
    ```

5. Run the setup script:

    ```shell
    python setup.py
    ```

6. Train the YOLO model by running the following command:

    ```shell
    yolo train model=models/yolov8n.pt data=plants.yaml epochs=50
    ```

That's it! You are now ready to train the YOLO model using the provided dataset. Happy coding!
