# backend/scoring.py
# Алгоритм підрахунку доші
# ================================


def calculate_dosha(answers):
    scores = {
        "vata": 0,
        "pitta": 0,
        "kapha": 0,
    }

    for answer in answers:
        if answer == "vata":
            scores["vata"] += 1
        elif answer == "pitta":
            scores["pitta"] += 1
        elif answer == "kapha":
            scores["kapha"] += 1

    return scores             # ← після циклу!


def get_constitution_type(scores):
    sorted_doshas = sorted(scores, key=scores.get, reverse=True)

    first = sorted_doshas[0]
    second = sorted_doshas[1]
    third = sorted_doshas[2]

    first_score = scores[first]
    second_score = scores[second]
    third_score = scores[third]

    if third_score >= first_score * 0.75:
        return "sama"
    elif second_score >= first_score * 0.75:
        return f"{first}-{second}"
    else:
        return first


def compare_prakriti_vikriti(prakriti_scores, vikriti_scores):
    imbalances = {}

    for dosha in ["vata", "pitta", "kapha"]:
        prakriti_percent = prakriti_scores[dosha] / 27 * 100
        vikriti_percent = vikriti_scores[dosha] / 10 * 100
        diff = vikriti_percent - prakriti_percent

        if diff > 15:
            imbalances[dosha] = round(diff, 1)

    return imbalances
