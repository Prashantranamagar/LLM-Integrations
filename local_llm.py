from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_gpu_layers=2,   # Use 2 GPU layers to fit MX550's 2GB VRAM
    n_threads=8,      # Adjust to your CPU's threads
    verbose=False
)

response = llm(
    "Explain quantum computing in simple terms.",
    max_tokens=200,
    temperature=0.7,
    stop=["\nUser:"]
)

print(response["choices"][0]["text"].strip())