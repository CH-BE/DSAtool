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

?> 