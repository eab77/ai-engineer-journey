import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[{"role": "user", "content": "Présente-toi en une phrase, en français."}],
    think=False,
)
text = response["message"]["content"]
print(text.split("</think>")[-1].strip())