<html>
    <body>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <input type="submit" name="trefferzone" value="Trefferzone w&uuml;rfeln"><br><br>
            <input type="submit" name="patzertabelle_fk" value="Fernkampf Patzer w&uuml;rfeln"><br><br>
            <input type="submit" name="patzertabelle_nk" value="Nahkampf Patzer w&uuml;rfeln">
        </form>
    </body>
</html>

<?php

// Include functions from other files
include('patzertabelle.php');
include('trefferzone.php');

if (isset($_POST['trefferzone'])) {
    trefferzone();
}

if (isset($_POST['patzertabelle_fk'])) {
    patzertabelle_fk();
}

if (isset($_POST['patzertabelle_nk'])) {
    patzertabelle_nk();
}


/* function trefferzone() {
    $d20 = random_int(1,20);
    echo "Wurf: $d20" . "<br />";
    
    if ($d20 < 6) {
        if ($d20 % 2 == 0) {
            echo "rechtes Bein!" . "<br />";
        }
        else {
            echo "linkes Bein!" . "<br />";
        }
        echo "1. Wunde: AT, PA, GE, INI-Basis -2; GE -1" . "<br />";
        echo "2. Wunde: AT, PA, GE, INI-Basis -4; GE -2" . "<br />";
        echo "3. Wunde: Sturz, kampfunfähig" . "<br />";
    }
    elseif ($d20 > 6 && $d20 <= 8) {
        echo "Bauch!" . "<br />";
        echo "1. Wunde: AT, PA, KO, KK, GS, INI-Basis -1; +1W6 SP" . "<br />";
        echo "2. Wunde: AT, PA, KO, KK, GS, INI-Basis -2; +2W6 SP" . "<br />";
        echo "3. Wunde: Bewusstlos, Blutverlust" . "<br />";
    }
    elseif($d20 > 8 && $d20 <= 14) {
        if ($d20 % 2 == 0) {
            echo "Schwertarm!" . "<br />";
        }
        else {
            echo "Schildarm!" .  "<br />";
        }
        echo "1. Wunde: AT, PA, KK, FF, -2 mit diesem Arm" . "<br />";
        echo "2. Wunde: AT, PA, KK, FF, -4 mit diesem Arm" . "<br />";
        echo "3. Wunde: Arm handlungsunfähig" . "<br />";
    }
    elseif ($d20 > 14 && $d20 <= 18) {
        echo "Brust!" . "<br />";
        echo "1. Wunde: AT, PA, KO, KK -1; +1W6 SP" . "<br />";
        echo "2. Wunde: AT, PA, KO, KK -2; +2W6 SP" . "<br />";
        echo "3. Wunde: Bewusstlos, Blutverlust" . "<br />";
    }
    elseif ($d20 > 18) {
        echo "Kopf!" . "<br />";
        echo "1. Wunde: MU, KL, IN, INI-Basis -2, INI - 2W6" . "<br />";
        echo "2. Wunde: MU, KL, IN, INI-Basis -4, INI - 4W6" . "<br />";
        echo "3. Wunde: +2W6 SP, bewusstlos, Blutverlust" . "<br />";
    }
} */

/* function patzertabelle_fk() {
    $patzerwurf = random_int(2,12);
    echo "Wurf: $patzerwurf" . "<br />";

    if ($patzerwurf == 2) {
        echo "Waffe zerst&ouml;rt!". "<br />" . "INI -4; alle verbleibenden Angriffs- und Abwehraktionen gehen diese Kampfrunde verloren";
    }
    elseif ($patzerwurf == 3) {
        echo "Waffe besch&auml;digt!". "<br />" . "INI -3; min. 30 Aktionen n&ouml;tig um Waffe wieder schussf&auml;hig zu machen (e.g. Sehne wechseln oder Mechanik der Armbust entklemmen), bei Wurfwaffe entspricht es Waffe zerst&ouml;rt; Sch&uuml;tze verliert alle verbleibenden Angriffs- und Abwehraktionen in der Kampfrunde.";
    }
    elseif ($patzerwurf > 4 && $patzerwurf <= 10) {
        echo "Fehlschuss!". "<br />" . "INI -2; 2 Aktionen ben&ouml;tigt um wieder Schussbereit zu sein.";
    }
    elseif ($patzerwurf > 10) {
        echo "Kameraden getroffen!". "<br />" . "INI -3; TP entsprechend Entfernung ausw&uuml;rfeln. Ansagen kommen nicht zum tragen. Ist kein Gef&auml;hrte in der N&auml;he, trifft sich der Sch&uuml;tze selbst.";
    }

} */

/* function patzertabelle_nk() {
    $patzerwurf = random_int(2,12);
    echo "Wurf: $patzerwurf" . "<br />";

    if ($patzerwurf == 2) {
        echo "Waffe zerst&ouml;rt!". "<br />" . "INI -4; bei BF <= 0 wird die Waffe nicht zerstört und BF steigt um eins; bei nat&auml;rlichen Waffen gilt es als Eigentreffer";
    }
    elseif ($patzerwurf > 2 && $patzerwurf <= 5) {
        echo "Sturz!". "<br />" . "INI -2; Zum Aufstehen Aktion Position und um BE erschwerte GE-Probe n&ouml;tig. Held mit Sonderfertigkeit Standfest oder Vorteil (herausragender) Balance kann GE-Probe erschwert um BE werfen, um es in ein Stolpern zu verwandeln.";
    }
    elseif ($patzerwurf > 5 && $patzerwurf <= 8) {
        echo "Stolpern!". "<br />" . "INI -2";
    }
    elseif ($patzerwurf > 8 && $patzerwurf <= 10) {
        echo "Waffe verloren!". "<br />" . "INI -2; Aktion Position und GE-Probe n&ouml;tig, um wieder an Waffe zu gelangen. Im Fall von nat&uuml;rlichen Waffen als Sturz gewertet.";
    }
    elseif ($patzerwurf == 11) {
        echo "An eigener Waffe verletzt!". "<br />" . "INI -3; Waffenschaden durch eigene Waffe. Keine zus&auml;tzlichen TP durch KK-Bonus oder Ansagen";
    }
    elseif ($patzerwurf == 12) {
        echo "Schwerer Eigentreffer". "<br />" . "INI -4; doppelter Waffenschaden. Keine zus&auml;tzlichen TP durch KK-Bonus oder Ansagen";
    }

} */
?> 