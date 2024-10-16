import re

class AAEntry:
    def __init__(self, entry_id, values, correlations):
        if len(values) != 20:
            raise ValueError("Values must contain exactly 20 elements.")
        self.entry_id = entry_id
        self.values = values
        self.correlations = correlations

# Example usage to demonstrate the class
entry = AAEntry(
    entry_id="ANDN920101",
    values=[4.35, 4.38, 4.75, 4.76, 4.65, 4.37, 4.29, 3.97, 4.63, 3.95, 4.17, 4.36, 4.52, 4.66, 4.44, 4.50, 4.35, 4.70, 4.60, 3.95],
    correlations={"BUNA790102": 0.949}
)
print(f"Entry ID: {entry.entry_id}")
print(f"Values: {entry.values}")
print(f"Correlations: {entry.correlations}")