

""""An equality comparison between one dict.values() view and another will always return False. This also applies when comparing dict.values() to itself:"""
d = {'a': 1}
print(d.values() == d.values())
