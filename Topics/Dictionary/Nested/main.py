numbers = {"first": 1, "second": 2, "third": 3, "fourth": 4}

print(numbers.pop("fourth"))

print(type(numbers.popitem()))

print(numbers.get(4))

print(numbers.get(4, "4"))

print(numbers.get("fourth"))
