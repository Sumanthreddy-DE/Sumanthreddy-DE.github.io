# Deutsche Texte für die Webseite

Arbeitsdatei — wird nicht veröffentlicht. Task 2 baut daraus das HTML.

Sprachniveau: B1, Alltagssprache. Kurze Sätze. Keine Fachwörter, wo ein einfaches Wort reicht.

---

## Hero

**Name:** Sumanth Reddy Settipalli

**Rolle:** Ingenieur für Simulation und Machine Learning

**Ein-Satz-Positionierung:**
> Ich mache Simulationen schneller und günstiger — mit Machine Learning.

**Ort:** Reutlingen, Deutschland

**Abschluss:** Master Computational Engineering, FAU Erlangen-Nürnberg (abgeschlossen August 2026)

**Verfügbarkeit:**
> Ab sofort verfügbar — für Stellen in Berechnung, Simulation und angewandtem ML in der DACH-Region.

---

## Fallstudie 1 — Werkstoffparameter automatisch bestimmen (PINN)

**Titel:** Werkstoffkennwerte aus Messdaten zurückrechnen

**Kontext:** Leichtbau, Faserverbund-Werkstoffe, industrielle Materialprüfung

**Text:**

Faserverbund-Werkstoffe stecken in vielen Bauteilen — von der Luftfahrt bis zum Maschinenbau. Das Problem: Die Kennwerte an den Grenzschichten zwischen Faser und Kunststoff kann man fast nicht direkt messen. Heute heißt das oft: teure Versuche im Labor, oder man schätzt die Werte einfach.

Ich habe ein Verfahren gebaut, das diese Werte automatisch zurückrechnet. Man gibt die gemessenen Kennwerte des fertigen Bauteils ein. Das Verfahren findet dann die Grenzschicht-Werte, die dazu passen. Fachleute nennen das ein inverses Problem. Gelernt hat das ein neuronales Netz, das die Physik des Werkstoffs mit einrechnet.

Damit die Ergebnisse stimmen, habe ich drei Dinge verbessert: falsch markierte Trainingsdaten korrigiert, die Gewichtung der Fehler automatisch angepasst und zu große Sprünge beim Lernen abgefangen. Danach war die Genauigkeit gut genug für die Praxis.

Das Ergebnis: Weniger Laborversuche, schnellere Materialentwicklung, geringere Kosten.

**Technik:** PyTorch, NumPy, SciPy

**Link:** Code und Dokumentation auf GitHub (Apache-2.0, öffentlich)

---

## Fallstudie 2 — SimReady: Ein Assistent für die Simulationsvorbereitung

**Titel:** SimReady — schneller von der CAD-Datei zum fertigen Netz

**Kontext:** Eigenes Projekt, läuft seit März 2026, öffentlich auf GitHub

**Text:**

Bevor eine Simulation loslaufen kann, muss das Bauteil vorbereitet werden. Man prüft die Geometrie, räumt das Modell auf und entscheidet, wo das Netz fein sein muss. Das kostet erfahrene Ingenieure oft Stunden pro Bauteil.

SimReady macht diese Vorbereitung schneller. Das Werkzeug lädt eine STEP-Datei und prüft die Geometrie automatisch — zwölf Checks, zum Beispiel auf scharfe Kanten, winzige Flächen oder Lücken. Danach gibt es eine klare Antwort: Ist das Teil bereit für das Netz, ja oder nein? Jeder Befund wird im Chat erklärt, und die betroffenen Flächen leuchten direkt im 3D-Modell auf.

Der zweite Teil ist Machine Learning. Ein Graph-Netzwerk sagt voraus, welche Flächen ein feineres Netz brauchen. Es schaut sich dabei jede Fläche zusammen mit ihren Nachbarn an — so wie ein erfahrener Ingenieur das Bauteil als Ganzes betrachtet. Trainiert habe ich es mit selbst erzeugten Bauteilen.

Das Ergebnis: Weniger Routinearbeit, weniger vergessene Geometriefehler, schneller zur Simulation.

**Technik:** PyTorch Geometric, pythonocc, LLM-Fine-Tuning, Streamlit

**Link:** Code auf GitHub

---

## Fallstudie 3 — Von CAD zur Simulation, ohne Handarbeit (KTMFK, FAU)

**Titel:** Automatische Pipeline: Siemens NX → MATLAB Simscape

**Kontext:** Lehrstuhl für Konstruktionstechnik (KTmfk), FAU Erlangen-Nürnberg, 2025 bis 2026

**Text:**

Am Lehrstuhl werden Mehrkörper-Simulationen für elektrische Ski-Rollen gebaut. Die Geometrie kommt aus Siemens NX, die Bewegung wird in MATLAB Simscape gerechnet. Der Übergang war früher Handarbeit: Ingenieure haben Gelenke, Verbindungen und Bauteile von Hand übertragen. Das war langsam und fehleranfällig.

Ich habe eine Pipeline gebaut, die das automatisch macht. Sie liest Geometrie und Verbindungen direkt aus der NX-Baugruppe aus und erzeugt daraus simulationsfertiges XML für Simscape. Das Herzstück ist eine Übersetzung: Jede CAD-Verbindung bekommt das passende Gelenk.

Für diese Übersetzung habe ich zusätzlich ein Transformer-Modell trainiert. Es ordnet eine Verbindung aus NX automatisch dem passenden Gelenk in PTC Creo zu. Die Trainingsdaten habe ich selbst erzeugt: Ich habe öffentliche STEP-Dateien ausgewertet und daraus 1.000 Paare aus Verbindung und Gelenk aufgebaut. Das Modell habe ich dann geprüft, indem ich die Vorhersagen mit echten Modellen in PTC Creo verglichen habe.

Am Ende kontrolliert die Pipeline das Ergebnis: Stimmen die Positionen in NX und in Simscape überein? Wenn nicht, gibt es eine Warnung.

Das Ergebnis: Aus Stunden Handarbeit werden Minuten. Und die Ergebnisse sind geprüft, nicht nur schnell.

**Technik:** TensorFlow, NXOpen API, Siemens NX, PTC Creo, MATLAB Simscape

**Link:** Code für das ML-Modell auf GitHub

---

## Weitere Arbeiten (eine Zeile pro Projekt)

- **Vorhersage von Werkstoffkennwerten:** Ein ML-Modell, das den Kompressionsmodul (Bulk-Modul) von Werkstoffen aus ihrem Aufbau vorhersagt.
- **Spitzenlasten senken bei schwingenden Bauteilen:** Eine Optimierungsmethode aus einer Veröffentlichung in Python nachgebaut und geprüft — inklusive der Frage, warum der Original-Code anders reagiert als im Paper beschrieben.

---

## Erfahrung

**Wissenschaftlicher Mitarbeiter und Tutor, FAU Erlangen-Nürnberg**
November 2023 bis August 2026, vier Lehrstühle

- Konstruktionstechnik: die NX→Simscape-Pipeline und das ML-Modell aus Fallstudie 3.
- Technische Dynamik: Tutor für MATLAB-Übungen — Statik und Dynamik, Fachwerke, schwingende Kräne.
- Fertigungstechnologie: FEM-Simulation von Scherclinch-Verbindungen in Aluminium und Stahl (Simufact Forming).
- Kontinuumsmechanik (BRAINIACS): nichtlineare FEM-Simulationen in deal.II (C++), angepasst an Messdaten von Hydrogelen — als Modell für Hirngewebe.

**Automatisierungsingenieur, Tata Consultancy Services**
August 2020 bis September 2022, Indien

- Einführung von ServiceNow für einen internationalen Kunden in acht Ländern. Daten aus Jira über Schnittstellen übertragen, Tests mit Anwendern, Go-Live. Eigene Funktionen in JavaScript gebaut — im Server und in der Oberfläche.

---

## Kenntnisse

**Programmierung:** Python, C++ (deal.II), MATLAB, Fortran, Git

**Machine Learning:** PyTorch, PyTorch Geometric, TensorFlow, Transformer, scikit-learn, pandas, NumPy, SciPy

**ML-Methoden:** physikbasierte neuronale Netze (PINN), Graph-Netzwerke, LLM-Fine-Tuning, Erkennung von Fachbegriffen in Texten (NER), inverse Parameterbestimmung

**Simulation und FEM:** Kontinuumsmechanik, Topologieoptimierung, Mehrkörpersimulation, Simufact Forming, MATLAB Simscape und Simulink, ParaView

**CAD und Automatisierung:** Siemens NX, NXOpen API, PTC Creo, STEP und pythonocc

---

## Ausbildung

**Master Computational Engineering** — FAU Erlangen-Nürnberg, Oktober 2022 bis August 2026

**Bachelor Maschinenbau** — Amrita Vishwa Vidyapeetham, Indien, 2016 bis 2020

---

## Sprachen

- Deutsch — B2
- Englisch — C1
- Hindi — fließend
- Telugu — Muttersprache

---

## Kontakt und Impressum

**Kontakt:**
- E-Mail: sumanthreddy.settipalli@gmail.com
- GitHub: github.com/Sumanthreddy-DE
- LinkedIn: linkedin.com/in/sumanthreddys

**Impressum (einfach, Pflicht in Deutschland):**
> Angaben gemäß § 5 DDG: Sumanth Reddy Settipalli, Reutlingen. Kontakt: sumanthreddy.settipalli@gmail.com

---

## Notizen für Task 2 (HTML-Umsetzung)

- Die drei Fallstudien sind das Herzstück — große Zwischenüberschriften, viel Weißraum (editorial).
- Reihenfolge auf der Seite: Hero → Fallstudien 1–3 → Weitere Arbeiten → Erfahrung → Kenntnisse → Ausbildung → Sprachen → Kontakt/Impressum.
- Die Ein-Satz-Positionierung im Hero ist die wichtigste Zeile der Seite.
- „Verfügbar ab sofort" als gut sichtbares Element.
- Keine akademische Sprache bei Fallstudie 1 — das Wort „Masterarbeit" oder „Thesis" kommt dort nicht vor. Der Abschluss steht nur im Hero und bei der Ausbildung.
