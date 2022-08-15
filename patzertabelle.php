<?php

function patzertabelle_fk() {
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

}

function patzertabelle_nk() {
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

}

?>