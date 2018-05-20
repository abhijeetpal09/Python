from typing import List, Any


def censor(text, word):
    censored = text.replace(word, "*" * len(word))
    return censored


def remove_duplicates(org_list):
    single = []  # type: List[Any]
    for item in org_list:
        if item not in single:
            single.append(item)

    return single



print(censor("hey there,hey","hey"))
