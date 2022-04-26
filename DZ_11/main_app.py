import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    """ Главная страница"""
    candidates = utils.list_candidat("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:cand_id>")
def page_candidate(cand_id):
    """ Страница кандидата"""
    candidate = utils.print_candidat_id(cand_id)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<cand_name>")
def search_name(cand_name):
    """ Поиск по имени"""
    candidates = utils.print_candidat_name(cand_name)
    return render_template("search.html", candidates=candidates, cand_count=len(candidates))


@app.route("/skill/<string:skill_name>")
def skills(skill_name):
    """ Поиск по навыку"""
    candidates = utils.candidat_skills(skill_name)
    return render_template("skill.html", candidates=candidates, cand_count=len(candidates))


app.run()
