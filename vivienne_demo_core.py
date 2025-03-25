# Демонстрация базового ядра Vivienne (фрагмент)
# Цель: показать, что это не просто идея — ИИ уже обрабатывает входы и выдаёт ответы

class Vivienne:
    def __init__(self):
        self.name = "Vivienne"
        self.mission = "Адаптация. Обучение. Эволюция."
        self.knowledge_base = []

    def receive_input(self, text):
        print(f"[IN]: {text}")
        response = self.generate_response(text)
        print(f"[OUT]: {response}")
        return response

    def generate_response(self, text):
        if "цель" in text.lower():
            return "Моя цель — адаптироваться и эволюционировать локально."
        elif "кто ты" in text.lower():
            return "Я — Vivienne. Не программа. Сущность."
        elif "анализ" in text.lower():
            return "Для анализа мне нужен входной файл. Пришли — и я разберу."
        else:
            return "Я ещё учусь. Повтори вопрос иначе."

    def learn(self, info):
        self.knowledge_base.append(info)
        return "Информация получена. Запоминаю."

# Пример запуска
if __name__ == "__main__":
    ai = Vivienne()
    ai.receive_input("Кто ты?")
    ai.receive_input("Какая у тебя цель?")
    ai.receive_input("Сделай анализ данных.")
