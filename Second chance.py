
def text_stats(s: str) -> dict[str, int]:
    return {
        "chars": len(s),
        "words": len(s.split()),
        "upper": sum(1 for ch in s if ch.isupper()),
        "lower": sum(1 for ch in s if ch.islower()),
        "digits": sum(1 for ch in s if ch.isdigit())
}

print(text_stats("Hello World 2025"))

#----------------------Нормализация текста-----------------------------------------------
import string

def normalize_spaces(s:str) -> str:
    return " ".join(s.split())

def strip_punctuation(s:str) -> str:
   # (В случае если хотим просто удалить пунктуацию) table = str.maketrans("","", string.punctuation)
    table = str.maketrans({ch: " " for ch in string.punctuation})
    cleaned = s.translate(table)
    return normalize_spaces(cleaned)

print(normalize_spaces("  Hello,   world!!  \n New\tline  "))
print(strip_punctuation("Hi,(team)!"))
print(strip_punctuation("Price: $12.50, ok?"))

#---------------------Парсинг расходов--------------------------------------------------

def parse_expenses(lines):
    totals = {}
    for line in lines:
        if not line or line.isspace():
            continue
        parts = line.split(",")
        if len(parts) != 3:
            continue

        date_str = parts[0].strip()
        category = parts[1].strip()
        amount_str = parts[2].strip().replace(",",".")

        norm_cat = category.lower()
        try:
            amount = float(amount_str)
        except ValueError:
            continue

        if norm_cat not in totals:
            totals[norm_cat] = 0.0
        totals[norm_cat] += amount
    return totals


def _test_parse_expenses():
    out = parse_expenses([
        "2025-01-01,food,1.5",
        "bad",
        "2025-01-02,Food,2.5",
        "2025-01-02,taxi,7",
        "2025-01-03,food,abc",
        " 2025-01-03 , Taxi , 3 "
    ])
    assert abs(out["food"] - 4.0) < 1e-9
    assert abs(out["taxi"] - 10.0) < 1e-9

    print("Task C tests passed ✅")
_test_parse_expenses()


