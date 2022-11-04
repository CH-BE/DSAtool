# DSAtool
Kleines tool für DSA Sachen

## Implementierte Funktionen:
- Trefferzonen Würfel mit Wunden
- Patzertabellen für Nah- und Fernkampf
- Modifikatoren für Fernkampf (nicht 100% fertig)
    - Nachtsicht: max. -5 Modifikator ergibt keinen Sinn?
    - Kampfgetümmel fehlt

## To Do:
### Fernkampf Modifikatoren (WdS S.93 ff)
- Nachtsicht: max. -5 Modifikator ergibt keinen Sinn?
- Kampfgetümmel nicht implementiert
- Kurzsichtig
- Tests fehlen
- Implementierung mit gezielten Schüssen und Trefferzonen

### Weitere Punkte (WdS S.37)
- Wundheilung + Modifikatoren: input -> Anzahl Wunden
- Wunden: 
    - unbehandelte Wunden: Pro Tag eine KO-Probe (+3xAnzahl Wunden)
    - mit HK Wunden behandelt: nach erfolgreicher HK-Wunden Probe ist KO-Probe erleichtert um 1, je 3 TaP* auf HK Wunden, je 7 TaP* auf HK Wunden schließt sich eine Wunde sofort
    - je 7 LeP die ein magischer Heiltrank zurückgibt, schließt sich eine Wunde sofort
- HK Wunden:
    - Erste Hilfe: lebensbedrohliche Verletzung (<=0 LeP) --> HK Wunden Probe erschwert um 2xLeP unter null. Dauer: (2xLeP unter Null) - TaP* KR, mindestens jedoch 2 KR. --> Misslingt Probe 1W6 SP. Gelingt Probe --> LeP zurück auf 1
    - Heilung Fördern: 2 Proben. 1. Probe --> allgemeine Versorgung der Verletzung (dauer 4 SR). Scheitert Probe KO-Probe um 3 erschwert, um zu sehen, ob Wundfieber ausbricht. 2. Probe --> Förderung der Regeneration (Regenerierung TaP*/2 LeP). Je 7 TaP* heilen eine Wunde sofort, alle 2 TaP* darüber hinaus geben auf nächste Regeneration einen Punkt Erleichterung auf die KO-Probe zum schließen von Wunden
    - HK Wunden am nächsten Tag (und folgenden): max. 1 Nachbehandlungsprobe pro Tag, 1 LeP zur Regeneration je 3 TaP* auf HK Wunden und KO-Probe ist je um 1 erleichtert. Scheitern der Nachbehandlung: Natürliche Heilung für 24h unterbrochen und 1W6 SP zusätzlich. Dauer je 6 SR
    - Erschwernis durch Wunden: Pro noch nicht verheilter Wunde ist Erstversorgungsprobe um zwei Punkte erschwert, Zweitversorgung um 3 Punkte

### Heilkräuter und -tränke (WdS S.160)
- Kräuter mit Bonus zu nächtlicher Regeneration: rote Pfeilblüte, Tarnele, Vierblättrige Einbeere, Wirselkraut
- Rote Pfeilblüte: Vorkommen südaventurische Dschungel und Sümpfe, Identifizierungsprobe Pflanzenkunde +7, Kosten 10D pro Aufguss, Wirkung: 3W6+2LeP über 3 Stunden regeneriert
- Tarnele: Wiesen, Wald und Sumpf in Mittel- und Nordaventurien, Identifizierungsprobe Pflanzenkunde +4, 2S pro Portion Salbe, Wirkung: nächtliche Regeneration +1 LeP
- Vierblättrige Einbeere: Wald und Waldränder nördlich des Yaquir, Identifizierungsprobe Pflanzenkunde +5, 4S pro Beere bzw. 15 D für eine Flasche Einbeerentrank mit 40 + 2W6 LeP, gibt 1W3 LeP pro Stunde zurück, im Rahmen einer HK Wunden Probe 1W6 pro Stunde
- frisches Wirselkraut: Steppen in ganz Aventurien, +5, 5D für eine Portion Salbe, bringt 5 LeP über den ganzen Tag, Wirselkrautsalbe 1W6+4 LeP

### Zufallsgeneratoren 
- Wetter (Abhängig von Region und Jahreszeit?)
- Namen (Abhängig von Region?)
