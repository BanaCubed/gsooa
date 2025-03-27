def quizawesome(answer, *text):
    for line in text:
        print(line)
    return input(" - ") == answer.__str__()


quizawesome(4, "1/5", "How old can lobsters", "31 Years", "potato", "fuck you")
