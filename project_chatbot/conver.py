from chat import get_response

while True:
    query=input("You: ")
    if query == "exit":
        break
    result=get_response(query)
    print(f"\nBlosomBot: {result}")
    