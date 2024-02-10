def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in s if char in vowels)
    return count


phrase = "Flash Genome"
result = count_vowels(phrase)
print(f"Number of vowels in {phrase} is: {result}")