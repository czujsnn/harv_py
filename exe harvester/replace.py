def repl(string):
    wrong = ["/","\\",":","?","<",">","*","|"]
    for x in range(len(wrong)):
        string = string.replace(wrong[x],"")

    return string



