frase = input('Digite algo: ').lower()

print(f"\nA letra 'a' aparece {frase.count('a')} vezes")
print(f"\nPosição em que ela aparece pela primeira vez: {frase.find('a')}")
print(f"\nPosição em que ela aparece pela ultima vez: {frase.rfind('a')}")
