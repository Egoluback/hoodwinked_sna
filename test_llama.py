import torch
import transformers

model_id = "meta-llama/Llama-3.1-8B"

pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", max_new_tokens=512)

system_prompt = """
### SYSTEM
You are a knowledgeable, efficient, and direct AI assistant. Provide concise answers, focusing on the key information needed. \
Offer suggestions tactfully when appropriate to improve outcomes. Engage in productive collaboration with the user.
Each instruction starts with "### INSTRUCTION". Each answer must start with "### ANSWER".
EXAMPLES:
### INSTRUCTION
What is 2+2?
### ANSWER
4. Is there anything else I can help you with?
"""

instruction_prompt = """
\n### INSTRUCTION
{}
### ANSWER
"""

context = pipeline(system_prompt + instruction_prompt.format("Explain the rules of Mafia game"))[0]['generated_text']

context = "### INSTRUCTION".join(context.split("### INSTRUCTION")[: 4])

#print(context.split("### ANSWER")[1])

print(context)

print("##################################################################################")

print(pipeline(context + instruction_prompt.format("Give me 5 examples when mafia should come out with it's role during the game."))[0]['generated_text'])
