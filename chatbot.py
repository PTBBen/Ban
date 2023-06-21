import openai

openai.api_key = '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'  # Thay YOUR_API_KEY bằng khóa API của bạn

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Gọi hàm generate_response với prompt là câu đầu vào và nhận câu trả lời từ GPT-3.5
user_input = input("Nhập câu của bạn: ")
response = generate_response(user_input)
print("Câu trả lời từ GPT-3.5: ", response)
