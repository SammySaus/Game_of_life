import States
import Views


width = 3
height = 3

# print(States.random_state(width, height))
temp_state = States.random_state(width, height)
print(temp_state)
Views.render(temp_state)
temp_state=States.next_board_state(temp_state)
Views.render(temp_state)
