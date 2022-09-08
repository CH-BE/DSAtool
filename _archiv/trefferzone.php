<?php

function trefferzone() {
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
}

?>