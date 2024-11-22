from outetts.v0_1.interface import InterfaceHF, InterfaceGGUF

# Initialize the interface with the Hugging Face model
interface = InterfaceHF("OuteAI/OuteTTS-0.1-350M")


def main():
    print("Welcome to OuteTTS! Type your text below to generate speech. Type 'exit' to quit.")
    while True:
        # Prompt the user for input
        text = input("\nEnter your text: ")

        # Exit the loop if the user types 'exit'
        if text.lower() == "exit":
            print("Goodbye!")
            break

        # Generate TTS output
        try:
            output = interface.generate(
                text=text,
                temperature=0.1,
                repetition_penalty=1.1,
                max_length=4096
            )
            # Play the generated audio
            output.play()

            # Save the generated audio to a file
            output.save("output.wav")
            print("Audio saved to 'output.wav'.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
