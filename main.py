import States
import Views


width = 5
height = 5

# print(States.random_state(width, height))
temp_state = States.random_state(width, height)
print(temp_state)
Views.render(temp_state)