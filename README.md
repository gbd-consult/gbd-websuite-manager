GBD WebSuite Manager
==============

Bereitstellung von QGIS Projekten in der GBD WebSuite
--------------------------------------------------------

Dieses Plugin ermöglicht die einfache Bereitstellung eines QGIS Projektes in der [GBD WebSuite](https://gws.gbd-consult.de). Voraussetzung ist, dass ein Nutzeraccount zu einer GBD WebSuite vorhanden ist, deren GBD WebSuite Manager Schnittstelle aktiv ist. 

Installation
------------

Es gibt zwei Möglichkeiten, das Plugin in QGIS zu installieren. Zum einen können Sie es von unserem [Plugin Repository](https://plugins.gbd-consult.de/) herunterladen und als ZIP-Datei in QGIS einbinden.

Zum anderen ist eine direkte Einbindung unseres Plugin-Repositorys in QGIS über folgenden Link möglich:

<img src="/images/repodetails.png" width="500">

Wenn das Plugin installiert ist, ist es in QGIS unter Web -> GBD WebSuite -> GBD WebSuite Manager zu finden.
Alternativ kann es in den Werkzeugkästen ausgewählt und somit prominent in die Werkzeugleiste integriert werden.

Anmelden
--------

Um das GBD WebSuite Plugin nutzen zu können muss man sich auf einem GBD WebSuite Server, mit aktivierter GBD WebSuite Manager Schnittstelle, authentifizieren.
Für diese Authentifizierung wird das QGIS eigene Authentifizierungssystem genutz.

Zuerst, falls noch nicht vorhanden, muss unter **Einstellungen -> Optionen -> Authentifizierung** ein Hauptpasswort gesetzt werden. Danach kann man über **Neue Authentifizierungskonfiguration hinzufügen** eine neue Verbindungen erstellen. Für eine Verbindung muss ein Name, Nutzername, Passwort und Serveradresse gesetzt werden, wobei Nutzername, Passwort und Serveradresse den Daten der GBD WebSuite Installation entsprechen müssen.

<img src="/images/anmeldung.png" width="500">

Die Authentifizierung sollte nun unter dem Drop Down Menü auswählbar sein und, bei Auswahl, automatisch eine Verbindung zur GBD WebSuite herstellen.
Sollten mehrere GBD WebSuite Installationen vorhanden sein, können auch mehrere Authentifizierungen hinterlegt werden, und zwischen diesen gewechselt werden.

<img src="/images/authentifizierung.png" width="500">

Das Plugin prüft automatisch die Authentifizierung und stellt, bei Erfolg, das Plugin auf aktiv und läd die vorhandenen Projekte.

Jetzt können Sie neue Projekte hinzufügen, vorhandene Projekte - zur Bearbeitung - in QGIS laden, Projekte löschen und sich den Link zur WebSuite anzeigen lassen oder direkt in den Browser wechseln.

Weitere Informationen finden Sie im [GBD WebSuite Manager Benutzerhandbuch](https://gbd-websuite.de/doc/latest/books/websuite-manager/de/index.html)

## Lizenz

Dieses Programm ist freie Software. Es kann unter der den Bedingungen der [GNU General Public License](./LICENSE) weitergegeben und/oder verändert werden. Entweder unter der Version 2 oder einer späteren Version der GPL.
