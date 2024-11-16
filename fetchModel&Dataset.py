import torch
from datasets import load_dataset
import transformers
from huggingface_hub import login
# 登录hugging-face
# login() 

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# 加载 tokenizer
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
# 加载模型
model = transformers.AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)

# 加载数据集bookcorpus
traindata = load_dataset(
        'bookcorpus', split='train', trust_remote_code=True
)