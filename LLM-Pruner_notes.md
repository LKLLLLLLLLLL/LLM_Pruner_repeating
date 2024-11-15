# 本文是关于使用LLM-Pruner的一些笔记
源仓库：https://github.com/horseee/LLM-Pruner
## 关于修建llama3.1的操作方法
该仓库直接支持修剪`llama3.1`，具体调用方法如下：
```shell
python llama3.py --pruning_ratio 0.25 \
                 --device cuda --eval_device cuda \
                 --base_model meta-llama/Meta-Llama-3.1-8B-Instruct \
                 --block_wise --block_mlp_layer_start 4 --block_mlp_layer_end 30 \
                 --block_attention_layer_start 4 --block_attention_layer_end 30 \
                 --save_ckpt_log_name llama3_prune \
                 --pruner_type taylor --taylor param_first \
                 --max_seq_len 2048 \
                 --test_after_train --test_before_train --save_model
```
其中主要逻辑位于`/llama3.py`的`main`函数中，具体的修剪逻辑位于`/llama3.py`的`prune`函数中。