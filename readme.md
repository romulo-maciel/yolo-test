# Detecção de ervas daninhas com YOLOv8

Treinamento de um detector de ervas daninhas para o **Projeto Robô Jardineiro** (iTec/FURG, em parceria com a Stihl), onde o robô precisa distinguir planta cultivada de invasora em canteiro aberto, sob iluminação natural variável.

Parte de `yolov8n` — a variante mais leve da família — porque o modelo roda embarcado no robô, junto da navegação e do controle. O repositório contém o pipeline de preparação do dataset e os parâmetros de treino; o controle do eixo cartesiano que atua sobre a planta detectada está em [Stihl-Cartesian](https://github.com/romulo-maciel/Stihl-Cartesian).

## Setup

1. Clone o repositório:

    ```shell
    git clone https://github.com/romulo-maciel/yolo-test.git
    ```

2. Crie um ambiente virtual:

    ```shell
    python3 -m venv .
    ```

3. Ative o ambiente:

    ```shell
    source bin/activate
    ```

4. Baixe o dataset [weed-detection](https://www.kaggle.com/datasets/jaidalmotra/weed-detection/data) do Kaggle e descompacte em `datasets/archive/`.

5. Instale as dependências:

    ```shell
    pip install ultralytics
    ```

6. Rode o script de preparação, que organiza o dataset no layout esperado pelo Ultralytics:

    ```shell
    python setup.py
    ```

7. Treine:

    ```shell
    yolo train model=models/yolov8n.pt data=plants.yaml epochs=50
    ```

As classes e os caminhos do dataset ficam em `plants.yaml`.
