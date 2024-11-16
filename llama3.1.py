# 此文件使用transformers库，下载并部署llama3.1-8B-instruct模型，可以在终端中运行，实现对话生成功能
import transformers
import torch

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

#登录hugging-face
# from huggingface_hub import login
# login() 

# 加载 tokenizer
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)

# 加载模型
model = transformers.AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)

# 将模型移动到 GPU
model.to("cuda:0")

# 创建 pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device="cuda:0",  # 指定设备为第一个 GPU
    pad_token_id=tokenizer.eos_token_id
)

# 提示词
messages = [
    {"role": "system", "content": "You are a chatbot who do what you are told to do."},
]

# 连续对话
while True:
    user_input = input("user: ")
    messages.append({"role": "user", "content": user_input})
    outputs = pipeline(
        messages,
        max_new_tokens=1024,
    )
    answer = outputs[0]["generated_text"][-1]["content"]
    messages.append({"role": "chatbot", "content": answer})
    print(f"\nllama: {answer}\n")