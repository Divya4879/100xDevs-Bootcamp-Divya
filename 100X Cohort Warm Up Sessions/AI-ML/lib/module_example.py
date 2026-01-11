def lower(phrase):
    def lowercase(words):   # local function inside the function, not used anywhere else in the application/program.
        return words.lower()
    
    return lowercase(phrase)

print(lower("Divya is trynna be complicated, BUT IT'S KINDA Really HARD."))