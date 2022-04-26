import json


def list_candidat(path):
    """
    Вывод списка кандидатов
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_candidat_id(cand_id):
    """
    Вывод кандидата по ID
    """
    candidates = list_candidat("candidates.json")
    for candidate in candidates:
        if candidate['id'] == cand_id:
            return candidate


def print_candidat_name(cand_name):
    """
    Вывод кандидата по имени
    """
    candidates = list_candidat("candidates.json")
    list_name = []
    for candidate in candidates:
        if cand_name.lower() in candidate['name'].lower():
            list_name.append(candidate)
    return list_name


def candidat_skills(skill):
    """
    Вывод кандидата по навыкам
    """
    candidates = list_candidat("candidates.json")

    result = []
    for candidate in candidates:
        #     skills = candidate['skills'].lower().split(', ')
        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


