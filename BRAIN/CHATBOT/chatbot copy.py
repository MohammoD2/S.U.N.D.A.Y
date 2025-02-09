from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import sys , os 
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))  # Fixed potential typo
from FUNCTION.zaki_speak.speak import *  
from FUNCTION.Zaki_listan.listan import *  
model = GPT2LMHeadModel.from_pretrained('./gpt3-finetuned-chatbot')
tokenizer = GPT2Tokenizer.from_pretrained('./gpt3-finetuned-chatbot')
tokenizer.pad_token = tokenizer.eos_token  # You can set a custom pad token if needed
def generate_response(input_text):
    input_prompt = f"User: {input_text} <|endoftext|> Response:"
    input_ids = tokenizer.encode(input_prompt, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=150,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    if "Response:" in response:
        response = response.split("Response:")[1].strip()
    
    print(response)
    speak(response)

while True:
    user_input = listen().lower()
    response = generate_response(user_input)
    

