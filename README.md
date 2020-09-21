GBD WebSuite Manager
==============

Bereitstellung von Onlinekarten mittels der GBD WebSuite
--------------------------------------------------------

Dieses Plugin ermöglicht die einfache Bereitstellung eines QGIS Projektes in der [GBD WebSuite](https://gws.gbd-consult.de). Voraussetzung ist, dass ein Nutzeraccount zu einer GBD WebSuite vorhanden ist, deren GBD WebSuite Manager Schnittstelle aktiv ist. 

Installation
------------

Das Plugin wird über das [Plugin Repository der Geoinformatikbüro Dassau GmbH](https://plugins.gbd-consult.de) bereitgestellt. Sie können das Repository über den QGIS Pluginmanager einbinden.

<img src="/images/repodetails.png" width="500">

Das Plugin kann über das Menü Erweiterungen -> GBD WebSuite Manager geladen werden.


Bedienung
---------
Wenn Sie das GBD WebSuite Manager Plugin in QGIS geladen und geöffnet haben, finden Sie folgendes Fenster vor:

<img src="/images/gbdmanager_blank.png" width="500">

Hier müssen Sie ihre .json Login-Datei hinterlegen.

Den Anmeldevorgang können Sie auch automatisieren, indem Sie in Ihrem QGIS Benutzerprofil die Login-Datei hinterlegen.

Hierfür lassen Sie sich, über die QGIS Python-Konsole, den Pfad zum aktuellen Benutzerprofil ausgeben, mit: 

    QgsApplication.qgisSettingsDirPath()

Unter diesem Pfad erstellen Sie dann einen Ordner mit dem Namen **GBD_WebSuite** und legen hier ihre .json Login-Datei ab, diese muss den Namen **qgws-manager.json** haben.

Nach der Anmeldung überprüft das Plugin ihre Authentifizierung, bei Erfolg werden die vorhandenen Projekte geladen und das Plugin wird auf aktiv geschlatet.

<img src="/images/gbdmanager_aktiv.png" width="500">

Jetzt können Sie neue Projekte hinzufügen, vorhandene Projekte, zur Bearbeitung, in QGIS laden, Projekte löschen und sich den Link zur WebSuite anzeigen lassen oder direkt in den Browser wechseln.

## Lizenz

Dieses Programm ist freie Software. Es kann unter der den Bedingungen der [GNU General Public License](./LICENSE) weitergegeben und/oder verändert werden. Entweder unter der Version 2 oder einer späteren Version der GPL.
