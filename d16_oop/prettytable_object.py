from prettytable import PrettyTable

# construct an object
table = PrettyTable()

# add column
table.add_column("Pokemon Name", ["Pikachu", "Squirtle"])
table.add_column("Type", ["Electric", "Water"])

# change alignment of whole table
table.align = "l"

print(table)

# output
# +--------------+----------+
# | Pokemon Name | Type     |
# +--------------+----------+
# | Pikachu      | Electric |
# | Squirtle     | Water    |
# +--------------+----------+


