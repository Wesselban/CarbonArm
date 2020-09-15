# CarbonArm

Met behulp van https://docs.python.org/2/library/struct.html een string converten.
de string zal eerst moeten opgesplitst worden voordat deze geconverteerd kan worden

# bevindingen tot nu toe:
- lijkt er op dat negatieve nummers gebruik maken van het 1e bitje op 1 te zetten en vandaar hoge spikes.
Of dat het komt dat negatieve getallen eigenlijk FFFFFFFF min het getal zijn in negatief
- Er lijkt een conversie te zijn van 19120 die hoogstwaarschijnlijk te maken heeft met de gearing
- de takes zijn opgesplit in meerdere columns zoals hier onder:

Tick count|Pan|???|Tilt|???|Roll|???
---|---|---|---|---|---|---
0300 0000|0000 0000|6400|c800 0000|0000 |0000 0000|5500

Ik verwacht dat de vraagtekens alleen maar een "indicator" is voor wat het is

# stappen plan:
- convert single line to degrees
  - positieve getallen
  - negatieve getallen
  - etc. wat tests kunnen handig zijn
- convert degrees to single line
  - moet dan twee kanten op kunnen werken

Als dat allemaal werkt kan er nagedacht worden over het echte bewegen van de arm.
