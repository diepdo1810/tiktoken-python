CMD:
curl -X POST http://localhost:5000/calculate_tokens -H "Content-Type: application/json" -d "{\"prompt\": \"Xin chào, tôi là một trí tuệ nhân tạo.\", \"model\": \"gpt-3.5-turbo\", \"language\": \"Vietnamese\"}"

OUTPUT:
{
  "tokens": 9
}
