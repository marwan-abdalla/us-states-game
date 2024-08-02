import turtle
from turtle import Turtle, Screen
import pandas as pd


def setup_screen(image_path):
    """Set up the screen with the given image."""
    screen = Screen()
    screen.title("U.S. States Game")
    screen.addshape(image_path)
    turtle.shape(image_path)
    return screen


def get_state_data(csv_path):
    """Read state data from a CSV file."""
    data = pd.read_csv(csv_path)
    states = data.state.to_list()
    coordinates = list(zip(data.x, data.y))
    return states, coordinates

def main():
    # Setup screen
    screen = setup_screen("blank_states_img.gif")
    # Read state data
    states, coordinates = get_state_data("50_states.csv")

    # Initialize game state
    number_guessed_states = 0
    guessed_states = []

    # Create a turtle instance for marking the states
    marker = Turtle()
    marker.hideturtle()
    marker.penup()

    # Game Loop
    while number_guessed_states < 50:
        answer_state = screen.textinput(
            title=f"Guess the State {number_guessed_states}/50",
            prompt="What's another state's name?").title()

        if answer_state.lower() == "exit":
            missing_states = [state for state in states if state not in guessed_states]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_not_guessed.csv")
            break

        if answer_state in states and answer_state not in guessed_states:
            state_index = states.index(answer_state)
            marker.goto(coordinates[state_index])
            marker.write(f"{answer_state}", align="center", font=("Courier", 10, "normal"))
            guessed_states.append(answer_state)
            number_guessed_states += 1

        elif answer_state not in states:
            screen.textinput(title=f"Invalid Input, Try Again.", prompt="What's another state's name?")


main()



