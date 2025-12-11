from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Trefferzonen nach W20-Logik
TREFFERZONEN_W20 = [
    {
        'range': range(1, 7),
        'zone': 'Beine',
        'effects': [
            '1.–2. Wunde: AT, PA, GE, INI-Basis -2, GS -1',
            '3. Wunde: Sturz, kampfunfähig'
        ]
    },
    {
        'range': range(7, 9),
        'zone': 'Bauch',
        'effects': [
            '1.–2. Wunde: AT, PA, KO, KK, GS, INI-Basis -1, 1W6 SP',
            '3. Wunde: bewusstlos, Blutverlust'
        ]
    },
    {
        'range': range(9, 15),
        'zone': 'Arme',
        'effects': [
            '1.–2. Wunde: AT, PA, KK, FF -2 mit diesem Arm',
            '3. Wunde: Arm handlungsunfähig'
        ]
    },
    {
        'range': range(15, 19),
        'zone': 'Brust',
        'effects': [
            '1.–2. Wunde: AT, PA, KO, KK -1, 1W6 SP',
            '3. Wunde: bewusstlos, Blutverlust'
        ]
    },
    {
        'range': range(19, 21),
        'zone': 'Kopf',
        'effects': [
            '1.–2. Wunde: MU, KL, IN, INI-Basis -2, INI -2W6',
            '3. Wunde: 2W6 SP, bewusstlos, Blutverlust'
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll', methods=['POST'])
def roll():
    expr = request.form.get('expr', '1W6')
    try:
        expr = expr.upper().replace(' ', '')
        n, rest = expr.split('W')
        n = int(n)

        bonus = 0
        if '+' in rest:
            sides, mod = rest.split('+')
            bonus = int(mod)
        elif '-' in rest:
            sides, mod = rest.split('-')
            bonus = -int(mod)
        else:
            sides = rest

        sides = int(sides)

        # Einzelergebnisse würfeln
        rolls = [random.randint(1, sides) for _ in range(n)]
        total = sum(rolls) + bonus

        # Ausgabeformat
        bonus_str = f"{'+' if bonus > 0 else ''}{bonus}" if bonus != 0 else ''
        dice_result = (
            f"<p><strong>Wurf:</strong> {expr}</p>"
            f"<p><strong>Einzelergebnisse:</strong> {rolls}</p>"
            f"<p><strong>Gesamtergebnis:</strong> {sum(rolls)}{bonus_str} = <strong>{total}</strong></p>"
        )

        return render_template('index.html', dice_result=dice_result)

    except Exception as e:
        return render_template('index.html', dice_result=f"<p>Ungültiger Ausdruck ({e})</p>")

# Trefferzonen mit formatiertem HTML (W20)
@app.route('/generator/trefferzone')
def generator_trefferzone():
    wurf = random.randint(1, 20)
    zone_info = next((z for z in TREFFERZONEN_W20 if wurf in z['range']), None)
    if zone_info:
        effects_html = ''.join(f'<li>{e}</li>' for e in zone_info['effects'])
        res = f"<p><strong>Wurf:</strong> {wurf}</p><p><strong>Zone:</strong> {zone_info['zone']}</p><ul>{effects_html}</ul>"
    else:
        res = f"<p>Wurf: {wurf} → Unbekannt</p>"
    return render_template('index.html', result=res)

# Nahkampf-Patzer mit formatiertem HTML (2W6)
def roll_2w6():
    return random.randint(1,6) + random.randint(1,6)

@app.route('/generator/patzer_nah')
def generator_patzer_nah():
    wurf = roll_2w6()
    html = f"<p><strong>Wurf:</strong> {wurf}</p>"

    if wurf == 2:
        html += "<p><strong>Ergebnis:</strong> Waffe zerstört</p><ul><li>INI –4 wegen Desorientierung</li><li>Neue Waffe ziehen in nächster Runde erforderlich</li><li>Sehr stabile Waffe (BF ≤ 0): gilt als 9–10 (Waffe verloren), BF +2</li><li>Natürliche Waffe: gilt als 12 (Schwerer Eigentreffer)</li></ul>"
    elif 3 <= wurf <= 5:
        html += "<p><strong>Ergebnis:</strong> Sturz</p><ul><li>Held liegt am Boden, benötigt Aktion Position + GE-Probe (erschwert um BE)</li><li>Mit SF Standfest oder Balance ggf. in Stolpern umwandelbar</li><li>INI –2 wegen Desorientierung</li></ul>"
    elif 6 <= wurf <= 8:
        html += "<p><strong>Ergebnis:</strong> Stolpern</p><ul><li>Verlust von 2 INI</li><li>Keine weiteren Auswirkungen</li></ul>"
    elif 9 <= wurf <= 10:
        html += "<p><strong>Ergebnis:</strong> Waffe verloren</p><ul><li>Aktion Position + GE-Probe nötig, um Waffe wiederzuerlangen</li><li>Alternative: Waffe wechseln oder fliehen</li><li>Natürliche Waffe: gilt als 3–5 (Sturz)</li><li>INI –2 wegen Desorientierung</li></ul>"
    elif wurf == 11:
        html += "<p><strong>Ergebnis:</strong> An eigener Waffe verletzt</p><ul><li>Waffenschaden durch eigene Waffe (TP auswürfeln, keine Boni)</li><li>Evtl. Wunde bei mehr als KO/2 SP</li><li>INI –3 wegen Desorientierung</li></ul>"
    elif wurf == 12:
        html += "<p><strong>Ergebnis:</strong> Schwerer Eigentreffer</p><ul><li>Schaden durch eigene Waffe (TP auswürfeln und verdoppeln, keine Boni)</li><li>Evtl. Wunde bei mehr als KO/2 SP</li><li>INI –4 wegen Desorientierung</li></ul>"
    else:
        html += "<p>Unbekannter Patzer.</p>"

    return render_template('index.html', result=html)

# Fernkampf-Patzer mit formatiertem HTML (2W6)
@app.route('/generator/patzer_fern')
def generator_patzer_fern():
    wurf = roll_2w6()
    html = f"<p><strong>Wurf:</strong> {wurf}</p>"

    if wurf == 2:
        html += "<p><strong>Ergebnis:</strong> Waffe zerstört</p><ul><li>INI –4</li><li>der Schuss geht ungezielt daneben, und von irgendwo hört man ein hässliches Knacken.</li><li>Bogen, Armbrust oder Speer sind so schwer beschädigt, dass eine Reparatur nicht lohnt.</li><li>Der Schütze verliert alle verbleibenden Angriffs- und Abwehr-Aktionen dieser Runde.</li></ul>"
    elif wurf == 3:
        html += "<p><strong>Ergebnis:</strong> Waffe beschädigt</p><ul><li>INI -3</li><li>der Schuss geht ungezielt daneben, das Projektil landet vor den Füßen des Schützen.</li><li>Die Sehne des Bogens ist gerissen, die Mechanik der Armbrust ernsthaft verklemmt – es sind mindestens 30 Aktionen nötig, um die Waffe wieder schussfähig zu machen.</li><li>Bei einer Wurfwaffe bedeutet dieses Resultat dasselbe wie eine 2: Messer oder Speer sind zerbrochen.</li><li>Der Schütze verliert alle verbleibenden Angriffs- und Abwehr-Aktionen dieser Runde.</li></ul>"
    elif 4 <= wurf <= 10:
        html += "<p><strong>Ergebnis:</strong> Fehlschuss</p><ul><li>INI -2</li><li>der Schuss geht ungezielt daneben, das Projektil ist verloren</li><li>die Mechanik der Armbrust blockiert oder die Sehne droht vom Bogen zu rutschen – der Schütze benötigt zwei Aktionen, um die Waffe wieder schussfähig zu machen.</li><li>Bei Wurfwaffen gilt, dass das Projektil ebenfalls verloren ist und der Werfer zwei Aktionen benötigt, um sein verlorenes Gleichgewicht wiederzufinden.</li></ul>"
    elif 9 <= wurf <= 10:
        html += "<p><strong>Ergebnis:</strong> Waffe verloren</p><ul><li>Aktion Position + GE-Probe nötig, um Waffe wiederzuerlangen</li><li>Alternative: Waffe wechseln oder fliehen</li><li>Natürliche Waffe: gilt als 3–5 (Sturz)</li><li>INI –2 wegen Desorientierung</li></ul>"
    elif 11 <= wurf <= 12:
        html += "<p><strong>Ergebnis:</strong> Kameraden getroffen</p><ul><li>INI -3</li><li>der Schuss löst sich unbeabsichtigt und trifft den am nächsten an der geplanten Flugbahn stehenden befreundeten Helden. Würfeln Sie für diesen Trefferpunkte gemäß der Entfernung aus; Ansagen (aus angesagten Fernkampfangriffen) kommen jedoch nicht zum Tragen.</li><li>Ist kein Gefährte in der Nähe, der getroffen werden könnte, hat der Schütze sich selbst verletzt (TP gemäß geringster Entfernung).</li></ul>"
    else:
        html += "<p>Unbekannter Patzer.</p>"

    return render_template('index.html', result=html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)