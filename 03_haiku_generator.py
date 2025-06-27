from ai import call_gpt


def main():
    # Get user input
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    # Display processing message
    print(f"Creating your haiku...")

    # Create prompt for AI
    prompt = f"""Create a haiku poem about the topic '{topic}' and incorporate the name '{name}' in a natural way.
    
    A haiku should have exactly three lines:
    - First line: 5 syllables
    - Second line: 7 syllables
    - Third line: 5 syllables
    
    The haiku should be nature-inspired, evocative, and capture a moment or feeling related to the topic.
    Return ONLY the haiku text without any additional explanation or formatting."""

    # Call AI to generate haiku
    haiku = call_gpt(prompt)

    # Display the generated haiku
    print(haiku)



if __name__ == "__main__":
    main()
