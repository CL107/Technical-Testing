# Main aggregate class
class aggregate:
    def __init__(self, name = None):
        from random import randint as ri
        self.num = ri(0, 100)
        self.name = name

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return f"{self.name}:{self.num}"


# Composition Aggregation
class Container_c:
    def __init__(self, *aggregates):
        self.aggregates = {}

        for i in aggregates:
            self.aggregates[i] = aggregate()

    def __str__(self):
        return ", ".join([f'{k}:{v}' for k, v in self.aggregates.items()])

# Association Aggregation
class Container_a:
    def __init__(self, *aggregates):
        self.aggregates = aggregates

    def __str__(self):
        return ", ".join(map(repr, self.aggregates))