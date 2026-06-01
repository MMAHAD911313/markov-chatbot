import random
from collections import defaultdict

class MarkovChatbot:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        words = text.split()

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.model[current_word].append(next_word)

    def generate(self, start_word, length=10):
        word = start_word
        output = [word]

        for _ in range(length - 1):
            if word not in self.model:
                break
            word = random.choice(self.model[word])
            output.append(word)

        return " ".join(output)


# -------------------------
# 🧪 Training data (you can expand this)
# -------------------------
data = """
hello how are you
hello I am fine
how are you doing today
I am doing fine thank you
you are very smart
"""

bot = MarkovChatbot()
bot.train(data)

# -------------------------
# 💬 Chat loop
# -------------------------
print("Markov Chatbot (type 'exit' to stop)\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        break

    words = user_input.split()
    start = words[0] if words else "hello"

    response = bot.generate(start, length=12)
    print("Bot:", response)