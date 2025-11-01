import ollama
import json
from sklearn.metrics import accuracy_score, classification_report

# Load your test data
with open("TestData.json") as f:
    test_data = json.load(f)

print(f"Loaded {len(test_data)} test samples")

preds, labels = [], []

for i, item in enumerate(test_data):
    print(f"\n--- Processing sample {i+1}/{len(test_data)} ---")
    print(f"Input: {item['input']}")
    print(f"Expected output: {item['output']}")
    
    # Prompt for your fine-tuned model
    prompt = f"""Predict the personality type from these options: Extrovert, Introvert, Ambivert.
                    Respond with only one word from these options.

                    Input: {item['input']}
                    Personality type:"""
    print(f"Prompt: {prompt}")
    
    # Query Ollama model
    response = ollama.chat(model="PTMACK-AI", messages=[
        {"role": "user", "content": prompt}
    ])
    
    prediction = response["message"]["content"].strip().capitalize()  # e.g., "Extrovert"
    print(f"Model prediction: {prediction}")
    
    preds.append(prediction)
    labels.append(item["output"])

print(f"\n=== EVALUATION RESULTS ===")
print(f"Total predictions: {len(preds)}")
print(f"Unique predictions: {set(preds)}")
print(f"Unique labels: {set(labels)}")

# Accuracy
accuracy = accuracy_score(labels, preds)
accuracy_percent = accuracy*100
print(f"Accuracy: %{accuracy_percent}")

# Detailed metrics
print("\nDetailed Classification Report:")
print(classification_report(labels, preds, digits=3))
