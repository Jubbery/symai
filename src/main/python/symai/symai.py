import openai_secret_manager

# Initialize the OpenAI API client
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# Define function to handle user input and generate a response using GPT-3
def generate_response(user_input):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"User: {user_input}\nSYMAI: "),
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response
    generated_response = response["choices"][0]["text"]

    return generated_response

# Main function to run the program
def main():
    while True:
        # Get user input
        user_input = input("You: ")

        # Exit program if user types "exit"
        if user_input.lower() == "exit":
            break

        # Generate and print the response
        symai_response = generate_response(user_input)
        print("SYMAI: " + symai_response)

if __name__ == "__main__":
    main()
