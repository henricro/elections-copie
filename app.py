from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

# On stocke chaque graphe comme une vue
# pour extraire son url dans les templates

@app.route('/barres')
def barres():
    return render_template('barres.html')

@app.route('/repartition')
def repartition():
    return render_template('repartition.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/m_fillon')
def fillon():
    return render_template('Mots_Fillon.html')

@app.route('/m_hamon')
def hamon():
    return render_template('Mots_Hamon.html')

@app.route('/m_lepen')
def lepen():
    return render_template('Mots_Le_Pen.html')

@app.route('/m_macron')
def macron():
    return render_template('Mots_Macron.html')

@app.route('/m_melenchon')
def melenchon():
    return render_template('Mots_Melenchon.html')

@app.route('/t_culture')
def culture():
    return render_template('themes/index_culture.html')

@app.route('/t_ecologie')
def ecologie():
    return render_template('themes/index_ecologie.html')

@app.route('/t_etranger')
def etranger():
    return render_template('themes/index_etrangere.html')

@app.route('/t_europe')
def europe():
    return render_template('themes/index_europe.html')

@app.route('/t_finance')
def finance():
    return render_template('themes/index_finance.html')

@app.route('/t_immigration')
def immigration():
    return render_template('themes/index_immigration.html')

@app.route('/t_numerique')
def numerique():
    return render_template('themes/index_numerique.html')

@app.route('/t_sante')
def sante():
    return render_template('themes/index_sante.html')

@app.route('/t_securite')
def securite():
    return render_template('themes/index_securite.html')

@app.route('/t_seniors')
def seniors():
    return render_template('themes/index_seniors.html')

@app.route('/t_societe')
def societe():
    return render_template('themes/index_societe.html')

@app.route('/t_sondage')
def sondage():
    return render_template('themes/index_sondage.html')

@app.route('/t_travail')
def travail():
    return render_template('themes/index_travail.html')

@app.route('/t_viepublique')
def viepublique():
    return render_template('themes/index_viepublique.html')

@app.route('/mots')
def mots():
    return render_template('themes/Mots.html')