curl -X POST https://tiktoken-beta.vercel.app/calculate_tokens -H Content-Type: application/json -d '{
  prompt: Xin chào, tôi là một trí tuệ nhân tạo.,
  model: gpt-3.5-turbo,
  language: Vietnamese
}'
