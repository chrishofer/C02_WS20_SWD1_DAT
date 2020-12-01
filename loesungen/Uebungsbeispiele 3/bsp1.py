from typing import List
def duplikate(zahlen: List[List[int]]) -> List[int]:
    dup = []

    for i in range(len(zahlen)):
        teilliste_als_set = set(zahlen[i])
        if len(zahlen[i]) == len(teilliste_als_set):
            dup.append(False)
        else:
            dup.append(True)

    return dup

if __name__ == '__main__':
    pass