pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()

if ingredient in pasta:
    want = "pasta"
    print(want, "time!")
if ingredient in apple_pie:
    want = "apple pie"
    print(want, "time!")
if ingredient in ratatouille:
    want = "ratatouille"
    print(want, "time!")
if ingredient in chocolate_cake:
    want = "chocolate cake"
    print(want, "time!")
if ingredient in omelette:
    want = "omelette"
    print(want, "time!")
