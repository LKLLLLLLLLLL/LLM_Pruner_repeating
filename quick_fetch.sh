#!/bin/bash

# 使用资源加速
source /etc/network_turbo
# # 使用镜像站
# export HF_ENDPOINT=https://hf-mirror.com

# 加载 conda 环境的初始化脚本
source ~/miniconda3/etc/profile.d/conda.sh
conda activate llm_pruner && echo "Conda environment activated."

echo "Starting login process..."
python3 ./fetchscrips/login.py
echo "Login process completed."

echo "Starting to fetch dataset and model simultaneously..."
python3 ./fetchscrips/fetchModel.py && echo "model cache finished."
python3 ./fetchscrips/fetchDataset.py && echo "dataset cache finished."

echo "Done."