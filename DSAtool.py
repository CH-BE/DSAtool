import random
from pyweb import pydom


text_before_roll = "Bitte einmal würfeln."
pydom["div#output"].html = text_before_roll
pydom["div#output2"].html = text_before_roll
pydom["div#output3"].html = text_before_roll
pydom["div#output4"].html = text_before_roll

def trefferzone(event):
    """Roles a d20 and looks up the corresponding damage areas with effects of 
    the wounds."""

    d20 = random.randint(1, 20)
    output = "Wurf: %2d" % d20

    if d20 <= 6:
        if (d20 % 2 == 0):
            output += "<br \><b>Rechtes Bein!</b><br \>"
        else:
            output += "<br \><b>Linkes Bein!</b><br \>"
        output += "1. Wunde: AT, PA, GE, INI-Basis -2; GE -1<br \>"
        output += "2. Wunde: AT, PA, GE, INI-Basis -4; GE -2<br \>"
        output += "3. Wunde: Sturz, kampfunfähig"
    elif d20 > 6 and d20 <= 8:
        output += "<br \><b>Bauch!</b><br \>"
        output += "1. Wunde: AT, PA, KO, KK, GS, INI-Basis -1; +1W6 SP<br \>"
        output += "2. Wunde: AT, PA, KO, KK, GS, INI-Basis -2; +2W6 SP<br \>"
        output += "3. Wunde: Bewusstlos, Blutverlust"
    elif d20 > 8 and d20 <= 14:
        if d20 % 2 == 0:
            output += "<br \><b>Schwertarm!</b><br \>"
        else:
            output += "<br \><b>Schildarm!</b><br \>"
        output += "1. Wunde: AT, PA, KK, FF, -2 mit diesem Arm<br \>"
        output += "2. Wunde: AT, PA, KK, FF, -4 mit diesem Arm<br \>"
        output += "3. Wunde: Arm handlungsunfähig"
    elif d20 > 14 and d20 <= 18:
        output += "<br \><b>Brust!</b><br \>"
        output += "1. Wunde: AT, PA, KO, KK -1; +1W6 SP<br \>"
        output += "2. Wunde: AT, PA, KO, KK -2; +2W6 SP<br \>"
        output += "3. Wunde: Bewusstlos, Blutverlust"
    elif d20 > 18:
        output += "<br \><b>Kopf!</b><br \>"
        output += "1. Wunde: MU, KL, IN, INI-Basis -2, INI - 2W6<br \>"
        output += "2. Wunde: MU, KL, IN, INI-Basis -4, INI - 4W6<br \>"
        output += "3. Wunde: +2W6 SP, bewusstlos, Blutverlust"
    pydom["div#output"].html = output


def patzertabelle_fk(event):
    """Roles 2W6 and looks up the effects for failures in RANGED combat"""

    patzer = random.randint(1, 6) + random.randint(1, 6)
    output = "Wurf: %2d<br \>" % patzer

    if patzer == 2:
        output += "<b>Waffe zerstört!</b><br \>"
        output += """INI -4<br \>alle verbleibenden Angriffs- und Abwehraktionen
        gehen diese Kampfrunde verloren"""
    elif patzer == 3:
        output += "<b>Waffe beschädigt!</b><br \>"
        output += """INI -3; min. 30 Aktionen nötig um Waffe wieder
        schussfähig zu machen (e.g. Sehne wechseln oder Mechanik
        der Armbust entklemmen), bei Wurfwaffe entspricht es Waffe zerstört;
        Schütze verliert alle verbleibenden Angriffs- und Abwehraktionen in
        der Kampfrunde."""
    elif patzer > 3 and patzer <= 10:
        output += "<b>Fehlschuss!</b><br \>"
        output += "INI -2<br \>2 Aktionen benötigt um wieder Schussbereit zu sein."
    elif patzer > 10:
        output += "<b>Kameraden getroffen!</b><br \>"
        output += """INI -3<br \>TP entsprechend Entfernung auswürfeln. Ansagen
        kommen nicht zum tragen. Ist kein Gefährte in der Nähe, trifft sich
        der Schütze selbst."""
    pydom["div#output3"].html = output


def patzertabelle_nk(event):
    """Roles 2W6 and looks up the effect for failures in MELEE combat"""

    patzer = random.randint(1, 6) + random.randint(1, 6)
    output = "Wurf: %2d<br \>" % patzer

    if patzer == 2:
        output += "<b>Waffe zerstört!</b><br \>"
        output += """INI -4<br \>bei BF <= 0 wird die Waffe nicht zerstört und BF
        steigt um eins<br \>bei natürlichen Waffen gilt es als Eigentreffer"""
    elif patzer > 2 and patzer <= 5:
        output += "<b>Sturz!</b><br \>"
        output += """INI -2<br \>Zum Aufstehen Aktion Position und um BE
        erschwerte GE-Probe nötig. Held mit Sonderfertigkeit Standfest
        oder Vorteil (herausragender) Balance kann GE-Probe erschwert um
        BE werfen, um es in ein Stolpern zu verwandeln."""
    elif patzer > 5 and patzer <= 8:
        output += "<b>Stolpern!</b><br \>"
        output += "INI -2"
    elif patzer > 8 and patzer <= 10:
        output += "<b>Waffe verloren!</b><br \>"
        output += """INI -2<br \>Aktion Position und GE-Probe nötig, um wieder an
        Waffe zu gelangen. Im Fall von natürlichen Waffen als Sturz 
        gewertet."""
    elif patzer == 11:
        output += "<b>An eigener Waffe verletzt!</b><br \>"
        output += """INI -3<br \>Waffenschaden durch eigene Waffe. Keine
        zusätzlichen
        TP durch KK-Bonus oder Ansagen"""
    elif patzer == 12:
        output += "<b>Schwerer Eigentreffer!</b><br \>"
        output += """INI -4<br \>doppelter Waffenschaden. Keine zusätzlichen TP durch
        KK-Bonus oder Ansagen"""
    pydom["div#output2"].html = output


def size_mod(size_str):
    """Looks up the size modificator for ranged attacks. Variable:
    size_str: target size"""

    size_mod = {
        "kleiner als winzig": 10,
        "winzig": 8,
        "sehr klein": 6,
        "klein": 4,
        "mittel": 2,
        "groß": 0,
        "sehr groß": -2,
        "größer als sehr groß": -4
    }
    return size_mod[size_str]


def distance_mod(distance_str):
    """Looks up the distance modificator for ranged attacks and returns
    modificator. Variable:
    distance_str: target distance"""

    distance_mod = {
        "sehr nah": -2,
        "nah": 0,
        "mittel": 4,
        "weit": 8,
        "extrem weit": 12
    }
    return distance_mod[distance_str]


def protection_mod(protection_str):
    """Looks up the protection modificator for ranged attacks and returns
    modificator. Variable:
    protection_str: none, halb, dreiviertel"""

    protection_mod = {
        "none": 0,
        "halb": 2,
        "dreiviertel": 4,
    }
    return protection_mod[protection_str]


def movement_mod(movement_str):
    """Looks up the movement modificator for ranged attacks and returns
    modificator. Variable:
    movement_str: target movement"""

    movement_mod = {
        "unbeweglich": -4,
        "stillstehend": -2,
        "leichte Bewegung": 0,
        "schnelle Bewegung": 2,
        "sehr schnelle Bewegung": 4,
    }
    return movement_mod[movement_str]


def sight_mod(sight1, sight2, sight3, twilightVision, nightVision, nightblind):
    """Looks up the sight modificator for ranged attacks and returns
    modificator. Variable:
    sight1 (str): none, Dunst, Nebel
    sight2 (str): none, Dämmerung, Mondlicht, Sternenlicht, Finsternis
    sight3 (str): none, Unsichtbares Ziel
    twilightvision (str): False/True
    nightVision (str): False/True
    nightblind (str): False/True"""

    sight_mod1 = {
        "none": 0,
        "Dunst": 2,
        "Nebel": 4,
    }
    sight_mod2 = {
        "none": 0,
        "Dämmerung": 2,
        "Mondlicht": 4,
        "Sternenlicht": 6,
        "Finsternis": 8,
    }
    sight_mod3 = {
        "none": 0,
        "Unsichtbares Ziel": 8
    }

    attack_mod = 0
    night_factor = 1
    if twilightVision == "True":
        night_factor = 0.5
    if nightVision == "True":
        night_factor = 0.5
    if nightblind == "True":
        night_factor = 2

    attack_mod += (sight_mod1[sight1] +
                   night_factor*sight_mod2[sight2] +
                   sight_mod3[sight3])

    return attack_mod


def horse_mod(horseattack, horsesaddle, weapontype):
    """Calculates modifications for ranged attacks from the back of a horse.
    Variables:
    horseattack (str): Describes movemement of the horse
    horsesaddle (boolean): is a saddle available?
    weapontype (str): Is it throwing or shooting?"""

    horsemod = {
        "none": 0,
        "stehend": 2,
        "Schritt": 4,
        "Galopp": 8
    }
    attack_mod = horsemod[horseattack]
    if horseattack != "none" and horsesaddle == "False":
        attack_mod += 4
    if weapontype == "Wurf":
        attack_mod = 0.5*attack_mod
    return attack_mod


def fk_mod(size, distance, movement, sight1, sight2, sight3, protection="none",
           twilightVision="False", distanceView="False",
           nightVision="False", oneEyed="False", colorblind="False",
           shortsighted="False", nightblind="False", weapontype="Schuss",
           steepshot="none", sidewind="none", quickshot="False",
           range_SF="none", horseattack="none", horsesaddle="True",
           underwater="False", dis=0):
    """Calculates the modifcation for a ranged attack. Variables:
    size (str): target size (kleiner als winzig, winzig, sehr klein, klein,
                mittel, groß, sehr groß, größer als sehr groß)
    distance (str): distance to target (sehr nah, nah, mittel,
                    weit, extrem weit)
    movement (srt): movemement of target (unbeweglich, stillstehend, leicht,
                    schnell, sehr schnell, kampfgetuemmel)
    sight1 (str): sight to target (Dunst, Nebel, Daemmerung, Mondlicht,
                       Sternenlicht, Finsternis, Unsichtbares Ziel)
    protection (str): protection e.g. shields (none, halb or dreiviertel)
    twilightVision (boolean): advantage Daemmerungssicht available?
    distanceView (boolean): advantage Entfernungssicht available?
    nightVision (boolean): advantage Nachtsicht available?
    oneEyed (boolean): disadvantage einäugig activated?
    colorblind (boolean): disadvantage farbenblind activated?
    shortsighted (boolean): disadvantage kurzsichtig activated?
    nightblind (boolean): disadvantage nightblind activated?
    steepshot (str): steep shot? (none, up, down)
    sidewind (str): sidewind? (böig, stark böig)
    quickshot (str): quickshot? (no, yes)
    range_SF (str): range combat special abilities? (none, Scharfschütze,
                    Meisterschütze)
    horseattack (str): Attack from the back of a horse? (none, stehend,
                       Schritt, Galopp)
    horsesaddle (boolean): Horsesaddle available?
    underwater (boolean): Shoot under water?
    dis (int): Distance from target in [Schritt]
    """

    fk_mod = 0
    shortsighted_output = ""  # Zusätzliche Ausgabe [sight2]
    fk_mod += (size_mod(size) +
               distance_mod(distance) +
               protection_mod(protection) +
               movement_mod(movement) +
               horse_mod(horseattack, horsesaddle, weapontype) +
               sight_mod(sight1,
                         sight2,
                         sight3,
                         twilightVision,
                         nightVision,
                         nightblind))

    # Steilschuss für Wurf- und Schusswaffen
    if steepshot == "up":
        if weapontype == "Schuss":
            fk_mod += 4
        else:
            fk_mod += 8
    elif steepshot == "down":
        fk_mod += 2

    # Windeinfluss
    if sidewind == "böig":
        fk_mod += 4
    elif sidewind == "stark böig":
        fk_mod += 8

    # Vor- und Nachteile[sight3]
    if distanceView == "True":
        fk_mod += -2
    if oneEyed == "True" and dis < 10:
        fk_mod += 4
    if colorblind == "True" and dis > 50:
        fk_mod += 4
    if shortsighted == "True" and dis > 100:
        shortsighted_output = """ + Meisterentscheid für zusätzliche Aufschläge
        durch Nachteil Kurzsichtig!"""

    # Schnellschuss
    if quickshot == "True":
        qs_factor = 1
        if range_SF == "Scharfschütze":
            qs_factor = 0.5
        if range_SF == "Meisterschütze":
            qs_factor = 0
        fk_mod += (qs_factor * 2)

    if underwater == "True":
        fk_mod += 5  # 3 von unter Wasser, 2 durch geringere Zielgröße

    output = str(fk_mod) + shortsighted_output

    return output


def fk_html_to_py(*args, **kwargs):
    #result = pydom["div#output4"][0].value
    size = pydom["select#size"][0].value
    distance = pydom["select#distance"][0].value
    movement = pydom["select#movement"][0].value
    sight1 = pydom["select#sight1"][0].value
    sight2 = pydom["select#sight1"][0].value
    sight3 = pydom["select#sight1"][0].value
    protection = pydom["select#protection"][0].value
    twilightVision = pydom["select#twilightVision"][0].value
    distanceView = pydom["select#distanceView"][0].value
    nightVision = pydom["select#nightVision"][0].value
    oneEyed = pydom["select#oneEyed"][0].value
    colorblind = pydom["select#colorblind"][0].value
    shortsighted = pydom["select#shortsighted"][0].value
    nightblind = pydom["select#nightblind"][0].value
    weapontype = pydom["select#weapontype"][0].value
    steepshot = pydom["select#steepshot"][0].value
    sidewind = pydom["select#sidewind"][0].value
    quickshot = pydom["select#quickshot"][0].value
    range_SF = pydom["select#range_SF"][0].value
    horseattack = pydom["select#horseattack"][0].value
    horsesaddle = pydom["select#horsesaddle"][0].value
    underwater = pydom["select#underwater"][0].value
    dis = pydom["input#dis"][0].value
    dis = int(dis)
    mod_final = fk_mod(size,
                 distance,
                 movement,
                 sight1,
                 sight2,
                 sight3,
                 protection,
                 twilightVision,
                 distanceView,
                 nightVision,
                 oneEyed,
                 colorblind,
                 shortsighted,
                 nightblind,
                 weapontype,
                 steepshot,
                 sidewind,
                 quickshot,
                 range_SF,
                 horseattack,
                 horsesaddle,
                 underwater,
                 dis)
    pydom["div#output4"].html = mod_final
