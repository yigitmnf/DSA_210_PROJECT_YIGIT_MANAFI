
import pandas as pd
import re

# =========================================================
# SCORE MAP (TURKISH KEYWORDS → SENTIMENT SCORE)
# 1.0 = very bad feeling
# 5.0 = very good feeling
# =========================================================

score_map = {
    # VERY POSITIVE (4.5 - 5.0)
    "mutluluk": 5.0,
    "coşku": 5.0,
    "zafer": 5.0,
    "sevgi": 5.0,
    "iyi his": 5.0,
    "hayat güzel": 5.0,

    "motivasyon": 4.5,
    "değer verme": 4.5,
    "güven": 4.5,
    "heyecan": 4.5,
    "tebrik": 4.5,
    "iltifat": 4.5,

    # POSITIVE (3.5 - 4.0)
    "teşekkür": 4.0,
    "iyilik": 4.0,
    "keyif": 4.0,
    "özür": 3.5,

    # NEUTRAL-ish (2.5 - 3.0)
    "trip": 2.5,
    "özlem": 2.5,
    "hastane": 2.5,

    # NEGATIVE (1.5 - 2.0)
    "yorgunluk": 2.0,
    "stres": 2.0,
    "endişe": 2.0,
    "rahatsızlık": 2.0,
    "hastalık": 2.0,
    "kötü his": 1.5,
    "kötü hissetme": 1.5,
    "suçluluk": 1.5,
    "moral bozukluğu": 1.5,
    "bıkkınlık": 1.5,
    "yalvarma": 1.5,

    # VERY NEGATIVE (1.0)
    "sinir": 1.0,
    "öfke patlaması": 1.0,
    "kavga": 1.0,
    "korku": 1.0,
    "panik": 1.0,
    "ağlama": 1.0,
    "üzüntü": 1.0,
    "kalp kırıklığı": 1.0,
    "değersizlik": 1.0,
    "ölüm isteği": 1.0,
    "çökme": 1.0,
    "yalnızlık": 1.0,
    "depresyon": 1.0,
}

# =========================================================
# NORMALIZATION (handle variations)
# =========================================================

alias_map = {
    "hastane/ilaç": "hastane",
    "kötü hissetmek": "kötü hissetme",
    "iyi hissetmek": "iyi his",
}

def normalize_keyword(k):
    k = k.strip().lower()
    k = re.sub(r"\s+", " ", k)
    return alias_map.get(k, k)

# =========================================================
# ROUND TO 0.5 STEPS BETWEEN 1-5
# =========================================================

def round_half(x):
    val = round(x * 2) / 2
    return max(1.0, min(5.0, val))

# =========================================================
# PROCESS FILE
# =========================================================

input_file = "Pasted text(1).txt"
output_file = "daily_scores.xlsx"

results = []
unknown = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        match = re.match(r"^(\d{2}/\d{2}/\d{4})\s*(.*)$", line)
        if not match:
            continue

        date = match.group(1)
        text = match.group(2).strip()

        # Empty day
        if text == "" or text == "—":
            results.append({
                "date": date,
                "average_score": None
            })
            continue

        keywords = [k.strip() for k in text.split(",") if k.strip()]

        scores = []

        for kw in keywords:
            kw_norm = normalize_keyword(kw)

            if kw_norm in score_map:
                scores.append(score_map[kw_norm])
            else:
                unknown.add(kw)

        if scores:
            avg = sum(scores) / len(scores)
            avg_rounded = round_half(avg)
        else:
            avg_rounded = None

        results.append({
            "date": date,
            "average_score": avg_rounded
        })

# =========================================================
# SAVE
# =========================================================

df = pd.DataFrame(results)
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
df = df.sort_values("date")

df.to_excel(output_file, index=False)

print("Done. File created:", output_file)

if unknown:
    print("\nUnknown keywords:")
    for u in sorted(unknown):
        print("-", u)
