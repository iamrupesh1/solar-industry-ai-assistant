from transformers import pipeline

# Load once to memory (small GPT-2 for demo)
generator = pipeline('text-generation', model='gpt2')

def generate_recommendations(summary):
    prompt = (f"Given the following rooftop solar data:\n{summary}\n"
              "Provide practical solar installation and maintenance recommendations.")
    generated = generator(prompt, max_length=150, num_return_sequences=1)
    return generated[0]['generated_text']
