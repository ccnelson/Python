from display_data import display_data
from DataStore import DataStore

new = DataStore()

new.x = 1
new.y = 2
new.z = 3
new.list = ["£" for i in range(10)]

display_data(new)
