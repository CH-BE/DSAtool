import random


def trefferzone(event):
    """Roles a d20 and looks up the corresponding damage areas with effects of the
    wounds."""

    d20 = random.randint(1, 20)
    output = "Wurf: %2d" % d20

    if d20 <= 6:
        if (d20 % 2 == 0):
            output += "<br>Rechtes Bein!<br>"
        else:
            output += "<br>Linkes Bein!<br>"
        output += "1. Wunde: AT, PA, GE, INI-Basis -2; GE -1<br>"
        output += "2. Wunde: AT, PA, GE, INI-Basis -4; GE -2<br>"
        output += "3. Wunde: Sturz, kampfunfähig"
    elif d20 > 6 and d20 <= 8:
        output += "<br>Bauch!<br>"
        output += "1. Wunde: AT, PA, KO, KK, GS, INI-Basis -1; +1W6 SP<br>"
        output += "2. Wunde: AT, PA, KO, KK, GS, INI-Basis -2; +2W6 SP<br>"
        output += "3. Wunde: Bewusstlos, Blutverlust"
    elif d20 > 8 and d20 <= 14:
        if d20 % 2 == 0:
            output += "<br>Schwertarm!<br>"
        else:
            output += "<br>Schildarm!<br>"
        output += "1. Wunde: AT, PA, KK, FF, -2 mit diesem Arm<br>"
        output += "2. Wunde: AT, PA, KK, FF, -4 mit diesem Arm<br>"
        output += "3. Wunde: Arm handlungsunfähig"
    elif d20 > 15 and d20 <= 18:
        output += "<br>Brust!<br>"
        output += "1. Wunde: AT, PA, KO, KK -1; +1W6 SP<br>"
        output += "2. Wunde: AT, PA, KO, KK -2; +2W6 SP<br>"
        output += "3. Wunde: Bewusstlos, Blutverlust"
    elif d20 > 18:
        output += "<br>Kopf!<br>"
        output += "1. Wunde: MU, KL, IN, INI-Basis -2, INI - 2W6<br>"
        output += "2. Wunde: MU, KL, IN, INI-Basis -4, INI - 4W6<br>"
        output += "3. Wunde: +2W6 SP, bewusstlos, Blutverlust"
    pyscript.write("output", output)


def patzertabelle_fk(event):
    """Roles 2W6 and looks up the effects for failures in RANGED combat"""

    patzer = random.randint(1, 6) + random.randint(1, 6)
    output = "Wurf: %2d<br>" % patzer

    if patzer == 2:
        output += "Waffe zerstört!<br>"
        output += """INI -4; alle verbleibenden Angriffs- und Abwehraktionen gehen diese
        Kampfrunde verloren"""
    elif patzer == 3:
        output += "Waffe beschädigt!<br>"
        output += """INI -3; min. 30 Aktionen nötig um Waffe wieder schussfähig zu machen
        (e.g. Sehne wechseln oder Mechanik der Armbust entklemmen), bei
        Wurfwaffe entspricht es Waffe zerstört; Schütze verliert alle
        verbleibenden Angriffs- und Abwehraktionen in der Kampfrunde."""
    elif patzer > 3 and patzer <= 10:
        output += "Fehlschuss!<br>"
        output += "INI -2; 2 Aktionen benötigt um wieder Schussbereit zu sein."
    elif patzer > 10:
        "Kameraden getroffen!<br>"
        """INI -3; TP entsprechend Entfernung auswürfeln. Ansagen kommen nicht
        zum tragen. Ist kein Gefährte in der Nähe, trifft sich der Schütze
        selbst."""
    pyscript.write("output3", output)


def patzertabelle_nk(event):
    """Roles 2W6 and looks up the effect for failures in MELEE combat"""

    patzer = random.randint(1, 6) + random.randint(1, 6)
    output = "Wurf: %2d<br>" % patzer

    if patzer == 2:
        output += "Waffe zerstört!<br>"
        output += """INI -4; bei BF <= 0 wird die Waffe nicht zerstört und BF steigt
        um eins; bei natürlichen Waffen gilt es als Eigentreffer"""
    elif patzer > 2 and patzer <= 5:
        output += "Sturz!<br>"
        output += """INI -2; Zum Aufstehen Aktion Position und um BE erschwerte GE-
        Probe nötig. Held mit Sonderfertigkeit Standfest oder Vorteil
        (herausragender) Balance kann GE-Probe erschwert um BE werfen, um es
        in ein Stolpern zu verwandeln."""
    elif patzer > 5 and patzer <= 8:
        output += "Stolpern!<br>"
        output += "INI -2"
    elif patzer > 8 and patzer <= 10:
        output += "Waffe verloren!<br>"
        output += """INI -2; Aktion Position und GE-Probe nötig, um wieder an Waffe
        zu gelangen. Im Fall von natürlichen Waffen als Sturz gewertet."""
    elif patzer == 11:
        output += "An eigener Waffe verletzt!<br>"
        output += """INI -3; Waffenschaden durch eigene Waffe. Keine zusätzlichen
        TP durch KK-Bonus oder Ansagen"""
    elif patzer == 12:
        output += "Schwerer Eigentreffer!<br>"
        output += """INI -4; doppelter Waffenschaden. Keine zusätzlichen TP durch
        KK-Bonus oder Ansagen"""
    pyscript.write("output2", output)
