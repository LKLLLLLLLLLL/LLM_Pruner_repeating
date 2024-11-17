import torch
import transformers

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# 加载 tokenizer
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
# 加载模型
model = transformers.AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
