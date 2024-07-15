def all_variants(text):
    try:
        for i in range(len(text)):
            for j in range(len(text) - i):
                yield text[j:j + i + 1]
    except RuntimeError:
        pass

func = all_variants('abc')
for i in func:
    print(i)