class Questions:
    def __init__(self, q_text, q_question) -> None:
        self.text = q_text
        self.question = q_question

new_q = Questions("th","dhaais")
print(f" print it {new_q.text} and {new_q.question}")