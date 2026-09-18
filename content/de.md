# Deutsche Texte für die Webseite — Content Spine

Arbeitsdatei — wird nicht veröffentlicht.

**Sprachregister:** technisches Deutsch auf Fachniveau, so wie es in der Berechnungs-
und CAE-Praxis gesprochen wird. Fachbegriffe werden **nicht** vereinfacht und **nicht**
erklärt — der Leser ist Berechnungsingenieur oder Recruiter mit technischem Umfeld.

**Zwei Fassungen pro Projekt:**
- **Kurzfassung** — steht auf der Startseite. Zwei bis drei Sätze, dann Bild, dann Link.
- **Langfassung** — wandert auf die Detailseite, sobald es sie gibt. Bis dahin hier
  geparkt, damit der Text nicht verloren geht.

**Bildplatzhalter:** `[BILD n]` · **Offene Punkte:** `[PRÜFEN]`

**Ersetzt** die B1-Fassung vom 2026-09-16 (`Archive/de.md.b1-version.bak`).

---

## Struktur

**Startseite** (diese Datei, Abschnitte 1–7)

1. Kopf — Name, Rolle, Positionierung, Navigation
2. Projekte — drei, je Kurzfassung + Bild + Link
3. Hackathons — zwei, kompakt
4. Engagement — zwei, kompakt
5. Weitere Arbeiten — sechs Einzeiler, zwei Gruppen
6. Über mich
7. Kontakt + Impressum

**Gebaut 2026-09-17/18:**
- `projekte.html` — alle Projekte, nach Relevanz gruppiert
- `projekte/{pinn,simready,nx-simscape}.html` — Detailseiten mit den Langfassungen
- `profil.html` — Berufserfahrung, Ausbildung, Kenntnisse, Sprachen, PDF-Download.
  Die Navigation führt auf **diese Seite**, nicht direkt auf die PDF-Datei; ein
  Navigationspunkt soll eine Seite öffnen und keinen Download auslösen.

**Entschieden 2026-09-17:**
- Kein Astro, kein Build-Schritt. Handgeschriebenes HTML.
- Simplefolio wird **nicht** geforkt — übernommen wird nur die Idee „wenig Text auf
  der Startseite, Details auf einer eigenen Seite".
- Der Lebenslauf-Download steht **nur** in der Navigation oben. Nicht im Fließtext,
  nicht im Fuß.
- `cortex` und `ai-eng-tracker` werden **nicht** gezeigt.

---

## 1. Kopf

**Name:** Sumanth Reddy Settipalli
**Rolle:** Ingenieur für Simulation und Machine Learning

**Positionierung:**
> Ich mache Simulationen schneller und günstiger — mit Machine Learning.

**Fakten:** Reutlingen, Deutschland · Master Computational Engineering,
FAU Erlangen-Nürnberg (08/2026)

**Navigation oben rechts:** Projekte · Über mich · Kontakt · Lebenslauf (PDF)

**Einstiegsliste** (drei Zeilen, je Sprungmarke):
- Inverse Parameteridentifikation mit PINN → *Fehler unter 5 %*
- SimReady — STEP-Datei auf Vernetzbarkeit prüfen → *GNN auf 1.100 Bauteilen*
- NX → Simscape automatisiert → *Stunden zu Minuten*

`[BILD 1]` — Porträtfoto, quadratisch.

---

## 2. Projekte

### 2.1 Inverse Parameteridentifikation an Faser-Matrix-Grenzflächen

**Rail:** Masterarbeit, FAU Erlangen-Nürnberg · 10/2025 – 02/2026 ·
Faserverstärkte Verbundwerkstoffe

**Kurzfassung (Startseite):**

Die Parameter der Interphase zwischen Faser und Matrix entscheiden über das
Bauteilverhalten, lassen sich messtechnisch aber kaum direkt erfassen. Ich habe ein
physikinformiertes neuronales Netz entwickelt, das sie aus den effektiven Kompressions-
und Schubmoduli zurückrechnet — die Mikromechanik der Homogenisierung steckt dabei in
der Verlustfunktion selbst.

**Kennzahl:** Vorhersagefehler unter 5 %

**Technologien:** PyTorch · NumPy · SciPy
**Links:** [Code](https://github.com/Sumanthreddy-DE/PINN-for-composite-interface-identification)
· [Masterarbeit](https://github.com/Sumanthreddy-DE/Master-Thesis)

`[BILD 2]` — Interphasen-Schema oder Streudiagramm Vorhersage gegen Referenz.

**Langfassung (Detailseite, später):**

> In faserverstärkten Verbundwerkstoffen entscheidet die Interphase zwischen Faser und
> Matrix maßgeblich über das Bauteilverhalten. Ihre Parameter lassen sich messtechnisch
> kaum direkt erfassen. In der Praxis bedeutet das: aufwendige Versuchsreihen — oder
> Annahmewerte aus der Literatur.
>
> Ich habe ein physikinformiertes neuronales Netz (PINN) entwickelt, das diese Parameter
> invers bestimmt. Eingang sind die effektiven Kompressions- und Schubmoduli eines
> dreischichtigen Interphasenmodells, Ausgang der Parametersatz, der genau diese Moduli
> reproduziert. Die Mikromechanik der Homogenisierung steckt dabei in der Verlustfunktion
> selbst — das Netz lernt nicht nur aus Daten, sondern gegen die Physik.
>
> Über die Genauigkeit haben drei Eingriffe entschieden: die Korrektur falsch annotierter
> Randfälle im Trainingsdatensatz, adaptive Verlustgewichtung und Gradientenbegrenzung
> gegen instabile Updates.
>
> **Ergebnis:** Vorhersagefehler unter 5 %. Genau genug, um Versuchsreihen gezielt zu
> ersetzen statt sie vollständig zu fahren.

---

### 2.2 SimReady — von der STEP-Datei zum vernetzungsfähigen Bauteil

**Rail:** Eigenes Projekt, öffentlich auf GitHub · seit 03/2026 · FEA-Vorverarbeitung

**Kurzfassung (Startseite):**

Ein Bauteil für die FE-Rechnung vorzubereiten kostet erfahrene Berechnungsingenieure
Stunden, und was dabei übersehen wird, fällt erst im Solver auf. SimReady prüft eine
STEP-Datei in zwölf Geometrieprüfungen, begründet jeden Befund farbig am 3D-Modell und
sagt über ein Graph Neural Network voraus, welche Flächen eine Netzverfeinerung
brauchen.

**Kennzahl:** GNN trainiert auf 1.100 Bauteilen

**Technologien:** PyTorch Geometric · pythonocc · LLM-Fine-Tuning · Streamlit
**Links:** [Code](https://github.com/Sumanthreddy-DE/simready)

`[BILD 3]` — Streamlit-Oberfläche mit markierten Befundflächen am 3D-Modell.

**Langfassung (Detailseite, später):**

> Vor jeder FE-Rechnung steht die Vorverarbeitung: Geometrie prüfen, Modell bereinigen,
> entscheiden, wo das Netz verfeinert werden muss. Pro Bauteil kostet das erfahrene
> Berechnungsingenieure schnell mehrere Stunden. Was dabei übersehen wird, fällt erst im
> Solver auf — oder gar nicht.
>
> SimReady übernimmt diesen Schritt. Das Tool liest eine STEP-Datei ein und führt zwölf
> Geometrieprüfungen aus, unter anderem auf scharfe Kanten, Kleinstflächen und Lücken in
> der Topologie. Am Ende steht eine belastbare Aussage: vernetzungsfähig oder nicht. Jeder
> Befund wird im Chat begründet, die betroffenen Flächen werden farbig direkt am
> 3D-Modell markiert.
>
> Der zweite Teil ist ein Graph Neural Network. Es sagt voraus, welche CAD-Flächen eine
> Netzverfeinerung benötigen und welcher Fehlertyp vorliegt, und bewertet jede Fläche im
> Kontext ihrer Nachbarflächen — so, wie ein erfahrener Berechnungsingenieur ein Bauteil
> als Ganzes liest, nicht Fläche für Fläche. Trainiert auf 1.100 selbst generierten
> Bauteilen.
>
> **Ergebnis:** Die Vorverarbeitung wird prüfbar statt Erfahrungssache. Geometriefehler
> fallen vor dem Solver auf, nicht danach.

---

### 2.3 Von der NX-Baugruppe zum simulationsfähigen Simscape-Modell

**Rail:** Lehrstuhl für Konstruktionstechnik (KTmfk), FAU Erlangen-Nürnberg ·
04/2025 – 02/2026 · CAD-Automatisierung, Mehrkörpersimulation

**Kurzfassung (Startseite):**

Der Weg von der NX-Baugruppe ins Simscape-Modell war Handarbeit: Bauteile,
Zwangsbedingungen und Gelenke wurden manuell übertragen. Meine Pipeline liest die
Baugruppe über die NXOpen API aus, ordnet jede Zwangsbedingung über ein
Transformer-Modell dem passenden Gelenk in PTC Creo zu und prüft am Ende die
Gelenkpositionen gegen das Original.

**Kennzahl:** aus Stunden manueller Übertragung werden Minuten

**Technologien:** TensorFlow · NXOpen API · Siemens NX · PTC Creo · MATLAB Simscape
**Links:** [Code für das Klassifikationsmodell](https://github.com/Sumanthreddy-DE/NX-Constraint-to-Creo-Joint-Classification)

`[BILD 4]` — NX-Baugruppe neben erzeugtem Simscape-Blockdiagramm.

**Langfassung (Detailseite, später):**

> Am Lehrstuhl entstehen Mehrkörpersimulationen von Baugruppen. Die Geometrie kommt aus
> Siemens NX, gerechnet wird in MATLAB Simscape. Der Übergang zwischen beiden war
> Handarbeit: Bauteile, Zwangsbedingungen und Gelenke wurden manuell übertragen —
> langsam und fehleranfällig.
>
> Ich habe eine Pipeline gebaut, die diesen Übergang automatisiert. Sie liest Geometrie
> und Zwangsbedingungen über die NXOpen API direkt aus der Baugruppe aus und erzeugt
> daraus simulationsfähiges XML für Simscape. Der Kern ist die Zuordnung: Jede
> NX-Zwangsbedingung braucht das passende Gelenk.
>
> Diese Zuordnung übernimmt ein Transformer-Modell, formuliert als überwachte
> Klassifikation auf das passende Gelenk in PTC Creo. Den Trainingsdatensatz habe ich
> selbst aufgebaut — öffentliche STEP-Dateien geparst und daraus 1.000 Paare aus
> Zwangsbedingung und Gelenk extrahiert. Validiert wurde gegen reale Modelle in PTC Creo.
>
> Zum Schluss prüft die Pipeline ihr eigenes Ergebnis: Stimmen die Gelenkpositionen in NX
> und in Simscape überein? Weicht etwas ab, gibt es eine Warnung statt eines stillen
> Fehlers.
>
> **Ergebnis:** Aus Stunden manueller Übertragung werden Minuten — und das Ergebnis ist
> geprüft, nicht nur schnell.

`[PRÜFEN]` **Anwendungsfall entfernt.** Die alte Fassung nannte „elektrische
Ski-Rollen". Der Begriff existiert im Deutschen nicht, und die Anwendung ist in keiner
Quelle belegt — weder im Lebenslauf noch in einem Repository. Bis geklärt ist, um
welche Baugruppe es ging, bleibt der Text allgemein.

`[PRÜFEN]` Der CV-Bullet sagt „Gelenken in NX Motion", die Webseite sagt PTC Creo.
Bestätigt 2026-09-17: **PTC Creo ist richtig.** Der Nutzer zieht den CV selbst nach.

---

## 3. Hackathons

**Abschnittszeile:** Zwei Wochenenden, zwei fremde Datensätze, zwei lauffähige Ergebnisse.

### 3.1 Prozesse automatisch auf Baukasten-Elemente abbilden

**Rail:** DEHN Servus AI Summer Hackathon 2025, Challenge 2 · Team

Fertigungsprozesse sollen automatisch den passenden Elementen des Firmen-Baukastens
zugeordnet werden — Roboter, Greifer, Zuführtechnik, gepflegt in einer über Jahre
gewachsenen Lösungsbibliothek in Excel. Ich habe die Zuordnung über semantische
Ähnlichkeit statt über Stichwortsuche gelöst: Sentence-Transformer-Embeddings mit
adaptiver Ähnlichkeitsschwelle, die alle plausiblen Treffer liefert statt einer festen
Top-k-Auswahl.

**Technologien:** Python · Sentence-Transformers · scikit-learn · pandas
**Link:** [Code](https://github.com/Sumanthreddy-DE/Production-Engineering-Data-Automation)

`[BILD 5]` — Zuordnungstabelle Prozess → Baukasten-Element mit Ähnlichkeitswerten.

### 3.2 DigiDorf — Behördengänge in der eigenen Sprache

**Rail:** Smart City Hackathon (Infosys) · 06/2025 · Team

Wer neu in Deutschland ist, scheitert selten an der Sache, sondern am Verfahren und an
der Sprache. DigiDorf führt Schritt für Schritt durch die Verwaltungsleistungen einer
Stadt — mit Unterlagen, Bearbeitungsdauer, Gebühren und dem offiziellen Formular. Ein
Chatbot beantwortet Rückfragen, die Oberfläche lässt sich umschalten. Das Problem kenne
ich aus eigener Erfahrung.

**Technologien:** React · TypeScript · Vite · Flask
**Link:** [Code (Team)](https://github.com/shriya1808/dorf-navigator-guide)

`[BILD 6]` — DigiDorf-Service-Seite.

---

## 4. Engagement

### 4.1 Mitgründer der Studierendeninitiative TEA

**Rail:** TEA, FAU Erlangen-Nürnberg · seit 09/2024 · Kernteam aus sechs Personen

Ich habe TEA im September 2024 mitgegründet — eine Studierendeninitiative, die
internationale Studierende beim Studienstart in Erlangen begleitet: Ankunft,
Behördengänge, die ersten Wochen. Getragen von einem Kernteam aus sechs Personen, läuft
bis heute.

`[BILD 7]` — TEA-Team oder Veranstaltung.

### 4.2 Rahmenstruktur und Lenkgeometrie eines Go-Karts

**Rail:** Go-Kart Design Competition · 2019 · Leitung Designteam

Ich habe das Designteam geleitet. Wir haben die Rahmenstruktur des Karts in AutoCAD
konstruiert und die Lenkgeometrie nach dem Ackermann-Prinzip ausgelegt.

**Kennzahl:** Platz 11 von über 250 teilnehmenden Teams

`[BILD 8]` — Kart, Team oder AutoCAD-Ansicht der Rahmenstruktur.

---

## 5. Weitere Arbeiten

Einzeiler mit Link. Kein Bild. Zwei Gruppen — die Reihenfolge ist Absicht: Simulation
und ML zuerst, Werkzeuge danach und sichtbar als zweite Kategorie.

### Simulation und Machine Learning

- **Kompressionsmodul anorganischer Kristalle vorhersagen** — Regressionsmodelle auf
  Matminer/Magpie-Deskriptoren, mit Merkmalsauswahl und Modellvergleich.
  → [Code](https://github.com/Sumanthreddy-DE/Predicting-the-Bulk-Modulus-of-Inorganic-Crystals)
- **Spitzenleistungsminimierung unter harmonischen Lasten** — publizierte SDP-Methode
  zur Topologieoptimierung von Fachwerken in Python nachgebaut (MOSEK, PICOS),
  einschließlich der Diagnose, warum die Referenzimplementierung abweicht.
  → [Code](https://github.com/Sumanthreddy-DE/Peak-Power-Minimization)
- **Named Entity Recognition auf technischen Texten** — Erkennung von Fachbegriffen in
  synthetischen technischen Beschreibungen, Hiwi am KTmfk.
  → [Code](https://github.com/Sumanthreddy-DE/Named-Entity-Recognition)

### Werkzeuge und Automatisierung

Software, die ich neben der Simulation gebaut habe — meist, um ein eigenes Problem
loszuwerden.

- **Tägliche Stellenbenachrichtigung für SmartRecruiters** — eine Mail pro Tag mit den
  Stellen, die seit gestern neu sind. Python, GitHub-Actions-Cron, kein Server, kein
  API-Schlüssel. Lief fünf Monate täglich.
  → [Code](https://github.com/Sumanthreddy-DE/smartrecruiters-job-alerts)
- **Tagesübersicht für Terminbuchungen** — Playwright-Scraper ohne Oberfläche, Versand
  über Gmail SMTP, geplant über GitHub Actions, mit pytest und CI.
  → [Code](https://github.com/Sumanthreddy-DE/anny-booking-bot)
- **Wöchentliche Zusammenfassung von Newslettern** — fasst abonnierte Newsletter zu
  einer Wochenübersicht zusammen.
  `[PRÜFEN]` Repository ist **privat** — deshalb ohne Link. Entweder öffentlich
  schalten oder den Eintrag streichen.

`[PRÜFEN]` `cortex` und `ai-eng-tracker` werden bewusst nicht gezeigt
(entschieden 2026-09-17).

---

## 6. Über mich

`[PLATZHALTER — vom Nutzer zu überschreiben.]` Aus dem geschrieben, was aus Lebenslauf
und Repositories hervorgeht. Nichts davon hat der Nutzer so gesagt.

Ich komme aus dem Maschinenbau. Mein Bachelor in Indien war klassische Konstruktion und
Fertigung — Zeichnungen, Bauteile, Prüfstände. Im Master Computational Engineering an
der FAU habe ich gelernt, dieselben Fragen numerisch zu stellen: nicht „hält das", 
sondern „was sagt das Modell, und wie weit traue ich ihm".

Zum Machine Learning bin ich nicht aus Begeisterung für Machine Learning gekommen,
sondern aus Ungeduld. In der Simulation ist zu vieles Routine, das trotzdem jemand mit
Erfahrung von Hand macht: Geometrie aufräumen, Gelenke übertragen, entscheiden, wo das
Netz feiner werden muss. Genau diese Stellen lassen sich lernen — und genau dort
arbeite ich am liebsten.

Seit 2022 lebe ich in Deutschland, inzwischen in Reutlingen. Deutsch habe ich neben dem
Studium gelernt und arbeite weiter daran. Was ich baue, baue ich meistens, weil mich
etwas im Alltag gestört hat — deshalb stehen unter „Weitere Arbeiten" auch ein paar
Werkzeuge, die mit Simulation nichts zu tun haben.

`[BILD 9]` — optional: zweites Foto, Arbeitsplatz oder Querformat.

---

## 7. Kontakt

**Überschrift:** Sie suchen jemanden für Berechnung, Simulation und angewandtes ML?

**Text:**

Ich suche eine Festanstellung im Raum Stuttgart und Reutlingen — Berechnung,
Simulation, CAE-Automatisierung oder angewandtes Machine Learning in der Fertigung.
Ab sofort verfügbar. Schreiben Sie mir gern auf Deutsch oder Englisch.

**Links:** E-Mail · GitHub · LinkedIn
Die E-Mail-Adresse wird nirgends ausgeschrieben, nur als `mailto:` hinterlegt.
**Kein Lebenslauf-Link hier** — der steht ausschließlich oben in der Navigation.

**Impressum:** eigene Seite `impressum.html`, im Fuß verlinkt.

---

## Anhang — Bildliste

| Nr. | Wo | Was | Status |
|---|---|---|---|
| 1 | Kopf | Porträtfoto, quadratisch | Platzhalter |
| 2 | Projekt 2.1 | Interphasen-Schema oder Fehlerdiagramm | Platzhalter |
| 3 | Projekt 2.2 | SimReady-Oberfläche | Platzhalter |
| 4 | Projekt 2.3 | NX-Baugruppe neben Simscape-Blockdiagramm | Platzhalter |
| 5 | Hackathon 3.1 | Zuordnungstabelle Prozess → Baukasten | Platzhalter |
| 6 | Hackathon 3.2 | DigiDorf-Service-Seite | Platzhalter |
| 7 | Engagement 4.1 | TEA-Team | Platzhalter |
| 8 | Engagement 4.2 | Go-Kart | Platzhalter |
| 9 | Über mich | optional, Querformat | Platzhalter |

---

## Anhang — Sprachliche Korrekturen gegenüber der B1-Fassung

| Alt | Neu | Grund |
|---|---|---|
| Grenzschicht | Grenzfläche, Interphase | „Grenzschicht" ist die Strömungsmechanik-Vokabel. Sachlich falsch. |
| Graph-Netzwerk | Graph Neural Network (GNN) | Kein etablierter Begriff im Deutschen. |
| physikbasiertes neuronales Netz | physikinformiertes neuronales Netz (PINN) | Etablierte Entsprechung von *physics-informed*. |
| „Fachleute nennen das ein inverses Problem" | gestrichen | Erklärt dem Leser sein eigenes Fachgebiet. |
| bereit für das Netz | vernetzungsfähig | Fachsprache der CAE-Praxis. |
| Das Werkzeug (für Software) | Das Tool | „Werkzeug" liest sich nach Hardware. |
| zwölf Checks | zwölf Geometrieprüfungen | Denglisch ohne Not. |
| winzige Flächen | Kleinstflächen | Fachbegriff. |
| Verbindungen (in NX) | Zwangsbedingungen | Der CV verwendet den korrekten Begriff. |
| die Gewichtung der Fehler angepasst | adaptive Verlustgewichtung | Ein Begriff statt einer Umschreibung. |
| zu große Sprünge beim Lernen abgefangen | Gradientenbegrenzung | Dito. |
| elektrische Ski-Rollen | Anwendungsfall gestrichen | Existiert nicht und ist nicht belegt. |
| Erkennung von Fachbegriffen (NER) | Named Entity Recognition (NER) | Im deutschen Fachgebrauch Standard. |
| Schnittstellen (für APIs) | REST-API | Präziser. |
| unbelegte Nutzenversprechen | belegte Zahlen (< 5 %, 1.100, 1.000, zwölf) | Unbelegtes liest sich als Werbung. |
