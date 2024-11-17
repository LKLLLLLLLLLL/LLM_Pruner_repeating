from datasets import load_dataset

# 加载数据集bookcorpus
traindata = load_dataset(
    'bookcorpus', split='train', trust_remote_code=True
)