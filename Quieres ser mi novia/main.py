from flet import (
    Page,
    CrossAxisAlignment,
    MainAxisAlignment,
    Text,
    ElevatedButton,
    Stack,
    app,
)
from random import randint


def main(page: Page):
    page.title = "¿Quieres ser mi novia? 💖"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    question = Text("¿Quieres ser mi novia?", size=30, weight="bold")

    confirmation_message = Text(
        "¡Sabía que dirías que sí! 💖", size=25, color="pink", visible=False
    )

    def on_yes_click(e):
        question.visible = False
        confirmation_message.visible = True
        page.update()

    yes_button = ElevatedButton(
        "Sí", on_click=on_yes_click, bgcolor="green", color="white"
    )

    def on_no_hover(e):
        no_button.left = randint(0, int(page.width) - 150)
        no_button.top = randint(0, int(page.height) - 100)
        page.update()

    no_button = ElevatedButton("No", on_hover=on_no_hover, bgcolor="red", color="white")

    stack = Stack([yes_button, no_button, confirmation_message])

    yes_button.top, yes_button.left = 200, 550
    no_button.top, no_button.left = 200, 650

    page.add(question, stack)


app(target=main)
