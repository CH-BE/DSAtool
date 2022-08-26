<html>
    <body>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <input type="submit" name="trefferzone" value="Trefferzone w&uuml;rfeln"><br><br>
            <input type="submit" name="patzertabelle_fk" value="Fernkampf Patzer w&uuml;rfeln"><br><br>
            <input type="submit" name="patzertabelle_nk" value="Nahkampf Patzer w&uuml;rfeln"><br><br>
        </form>
        <hr>
        <h2>Fernkampf Modifikation</h2><br>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            Distanz (Schritt): <input type="text" name="distance"><br><br>
            <b>Zielgr&ouml;sse</b><br>
            <input type="radio" name="size" value="size">kleiner als winzig<br>
            <input type="radio" name="size" value="size">winzig (M&uuml;nze, Drachenauge, Maus, Kr&ouml;te)<br>
            <input type="radio" name="size" value="size">sehr klein (Schlange, Fasan, Katze, Rabe)<br>
            <input type="radio" name="size" value="size">klein (Wolf, Reh, Schaf)<br>
            <input type="radio" name="size" value="size">mittel (Mensch, Elf, Ork, Goblin, Zwerg)<br>
            <input type="radio" name="size" value="size">gro&szlig; (Pferd, Steppenrind, Oger, Troll)<br>
            <input type="radio" name="size" value="size">sehr gro&szlig; (Scheunentor, Drache, Elefant, Riese)<br>
            <input type="radio" name="size" value="size">gr&ouml;&szlig;er als sehr gro&szlig;<br><br>
            <b>Deckung</b><br>
            <input type="radio" name="protection" value="protection">halbe Deckung (auch durch gro&szlig;e Schilde)<br>
            <input type="radio" name="protection" value="protection">dreiviertel Deckung (auch durch sehr gro&szlig;e Schilde)<br><br>
            <b>Bewegung des Ziels</b><br>
            <input type="radio" name="movement" value="movement">fest montiertes Ziel<br>
            <input type="radio" name="movement" value="movement">stillstehendes Ziel<br>
            <input type="radio" name="movement" value="movement">leichte Bewegung des Ziels<br>
            <input type="radio" name="movement" value="movement">schnelle Bewegung des Ziels<br>
            <input type="radio" name="movement" value="movement">sehr schnelle Bewegung des Ziels<br>
            <input type="radio" name="movement" value="movement">Kampfget&uuml;mmel<br>
            <input type="radio" name="movement" value="movement">Bewegung eines K&ouml;rperteils (Gezielte Sch&uuml;sse)<br><br>
            <b>Sichtverh&auml;ltnisse</b><br>
            <input type="radio" name="sight" value="sight">Dunst<br>
            <input type="radio" name="sight" value="sight">Nebel<br>
            <input type="radio" name="sight" value="sight">Dämmerung<br>
            <input type="radio" name="sight" value="sight">Mondlicht<br>
            <input type="radio" name="sight" value="sight">Sternenlicht<br>
            <input type="radio" name="sight" value="sight">Finsternis<br>
            <input type="radio" name="sight" value="sight">Unsichtbares Ziel<br><br>
            <b>Vor- und Nachteile</b><br>
            <input type="radio" name="adv1" value="adv1">D&auml;mmerungssicht<br>
            <input type="radio" name="adv2" value="adv2">Entfernungssinn<br>
            <input type="radio" name="adv3" value="adv3">Nachtsicht<br>
            <input type="radio" name="disadv1" value="disadv1">Ein&auml;gig<br>
            <input type="radio" name="disadv2" value="disadv2">Farbenblind<br>
            <input type="radio" name="disadv3" value="disadv3">Kurzsichtig<br>
            <input type="radio" name="disadv4" value="disadv4">Nachtblind<br><br>
            <b>Sonstige Modifikatoren</b><br>
            <input type="radio" name="other1" value="other1">Steilschuss/-wurf nach unten<br>
            <input type="radio" name="other2" value="other2">Steilschuss/-wurf nach oben<br>
            <input type="radio" name="other3" value="other3">b&ouml;iger Seitenwind<br>
            <input type="radio" name="other4" value="other4">starker b&ouml;iger Seitenwind<br>
            <input type="radio" name="other5" value="other5">Schnellschuss<br>
            <input type="radio" name="other6" value="other6">zweiter Schuss pro Kampfrunde<br>
            <input type="radio" name="other7" value="other7">zweiter Wurf pro Kampfrunde<br>
            <input type="radio" name="other8" value="other8">Schuss/Wurf von stehendem Reittier<br>
            <input type="radio" name="other9" value="other9">Schuss/Wurf von galoppierendem Reittier<br>
            <input type="radio" name="other10" value="other10">Schuss/Wurf von Reittier ohne Sattel und Steigb&uml;gel<br>
            <input type="radio" name="other11" value="other11">unter Wasser<br>
            <br><br><input type="submit" name="ranged_modification" value="Berechnen">
        </form>
    </body>
</html>

<?php

// Include functions from other files
include('patzertabelle.php');
include('trefferzone.php');
include('fernkampf.php');


if (isset($_POST['trefferzone'])) {
    trefferzone();
}

if (isset($_POST['patzertabelle_fk'])) {
    patzertabelle_fk();
}

if (isset($_POST['patzertabelle_nk'])) {
    patzertabelle_nk();
}

if (isset($_POST['ranged_modification'])) {
    fernkampf_mod($_POST['distance'],
    $_POST['size'],
    $_POST['protection'],
    $_POST['movement'],
    $_POST['sight'],
    $_POST['adv1'],
    $_POST['adv2'],
    $_POST['adv3'],
    $_POST['disadv1'],
    $_POST['disadv2'],
    $_POST['disadv3'],
    $_POST['disadv4'],
    $_POST['other1'],
    $_POST['other2'],
    $_POST['other3'],
    $_POST['other4'],
    $_POST['other5'],
    $_POST['other6'],
    $_POST['other7'],
    $_POST['other8'],
    $_POST['other9'],
    $_POST['other10'],
    $_POST['other11'],
);
}

?> 