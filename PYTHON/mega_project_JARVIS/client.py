from openai import OpenAI
client=OpenAI(api_key="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")
response = client.responses.create(
  model="gpt-6-luna",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);