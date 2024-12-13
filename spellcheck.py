from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")

def llama_spell_correction(ocr_text):
    # Use the LLaMA model (via Groq) to correct the spelling and grammar of the OCR text
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Correct any spelling and grammar mistakes in the following text: '{ocr_text}'"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
        
    # Collect the response from the LLaMA model
    corrected_text = ""
    for chunk in completion:
        corrected_text += chunk.choices[0].delta.content or ""

    return corrected_text.strip()

# Example OCR-detected text with spelling errors
ocr_detected_text = "Ths is a smple txet with erors."
corrected_text = llama_spell_correction(ocr_detected_text)

print(f"Original OCR Text: {ocr_detected_text}")
print(f"Corrected Text: {corrected_text}")
