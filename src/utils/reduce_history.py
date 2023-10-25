import tiktoken
from loguru import logger
from typing import List


def reduce_context_window(context_window: List[dict], max_tokens: int = 4_000) -> List[dict]:
    num_tokens = calculate_tokens(context_window=context_window)

    while num_tokens > max_tokens:
        context_window = context_window[1:]
        num_tokens = calculate_tokens(context_window=context_window)
        
    return context_window


def calculate_tokens(context_window: List[dict]) -> int:
    encoding = tiktoken.get_encoding(encoding_name='cl100k_base')
    all_tokens = 0
    for message in context_window:
        prompt = message["content"]
        num_tokens = len(encoding.encode(prompt))
        all_tokens += num_tokens

    return all_tokens
