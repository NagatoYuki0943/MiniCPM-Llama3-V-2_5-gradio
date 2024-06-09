from typing import Sequence


def convert_to_openai_history(
    history: Sequence,
    query: str | None,
) -> list:
    """
    将历史记录转换为openai格式

    Args:
        history (list): [['What is the capital of France?', 'The capital of France is Paris.'], ['Thanks', 'You are Welcome']]
        query (str | None): query

    Returns:
        list: a chat history in OpenAI format or a list of chat history.
            [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                },
                {
                    "role": "assistant",
                    "content": "The capital of France is Paris."
                },
                {
                    "role": "user",
                    "content": "Thanks!"
                },
                {
                    "role": "assistant",
                    "content": "You are welcome."
                }
            ]
    """
    # 将历史记录转换为openai格式
    prompt = []
    for user, assistant in history:
        prompt.append(
            {
                "role": "user",
                "content": user
            }
        )
        prompt.append(
            {
                "role": "assistant",
                "content": assistant
            })
    if query is not None:
        # 需要添加当前的query
        prompt.append(
            {
                "role": "user",
                "content": query
            }
        )
    return prompt
