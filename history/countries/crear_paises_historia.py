import os

MOD_DIR = os.path.dirname(os.path.abspath(__file__))
COUNTRIES_DIR = os.path.join(MOD_DIR, "history", "countries")

os.makedirs(COUNTRIES_DIR, exist_ok=True)

# Lista de países faltantes detectados en error.log con su capital aproximada e ideología
paises = [
    {
        "filename": "TEX - Texas.txt",
        "capital": 375,
        "party": "conservatism",
        "pops": "conservatism = 50\n\tliberalism = 30\n\tautocracy = 10\n\tsocdem = 10",
        "tag": "TEX"
    },
    {
        "filename": "NEW - New England.txt",
        "capital": 357,
        "party": "liberalism",
        "pops": "liberalism = 50\n\tsocdem = 30\n\tconservatism = 15\n\tautocracy = 5",
        "tag": "NEW"
    },
    {
        "filename": "CPE - Cape Republic.txt",
        "capital": 662,
        "party": "liberalism",
        "pops": "liberalism = 40\n\tsocdem = 30\n\tconservatism = 20\n\tautocracy = 10",
        "tag": "CPE"
    },
    {
        "filename": "HAW - Kingdom of Hawaii.txt",
        "capital": 574,
        "party": "autocracy",
        "pops": "autocracy = 60\n\tconservatism = 20\n\tliberalism = 10\n\tsocdem = 10",
        "tag": "HAW"
    },
    {
        "filename": "ZAP - Zapatistas.txt",
        "capital": 484,
        "party": "anarchism",
        "pops": "anarchism = 60\n\thardline_socialism = 20\n\treformist_socialism = 20",
        "tag": "ZAP"
    },
    {
        "filename": "FAR - Free American Republic.txt",
        "capital": 361,
        "party": "conservatism",
        "pops": "conservatism = 60\n\tliberalism = 20\n\tautocracy = 10\n\tdissident_right = 10",
        "tag": "FAR"
    },
    {
        "filename": "NTI - Northwest Territorial Imperative.txt",
        "capital": 385,
        "party": "revolutionary_right",
        "pops": "revolutionary_right = 60\n\tdissident_right = 30\n\tautocracy = 10",
        "tag": "NTI"
    },
    {
        "filename": "AZT - Aztlan Republic.txt",
        "capital": 378,
        "party": "socdem",
        "pops": "socdem = 50\n\treformist_socialism = 30\n\tliberalism = 20",
        "tag": "AZT"
    },
    {
        "filename": "NRG - National Reclamation Government.txt",
        "capital": 360,
        "party": "autocracy",
        "pops": "autocracy = 70\n\trevolutionary_right = 20\n\tconservatism = 10",
        "tag": "NRG"
    }
]

plantilla = """capital = {capital}

oob = ""

add_to_variable = {{ GDP = 50 }}
add_to_variable = {{ DEBT = 10 }}
add_to_variable = {{ REAL_GROWTH = 1 }}
TOTA_startup_funny_business_ignore_this = yes
starting_econ_modifier_vars = yes
set_variable = {{ GDP_trillion = var:GDP }}
set_variable = {{ GDP_million = var:GDP }}
multiply_variable = {{ GDP_trillion = 0.001 }}
multiply_variable = {{ GDP_million = 1000 }}
multiply_variable = {{ REAL_GROWTH = 0.01 }}
set_variable = {{ DEBT_trillion = var:DEBT }}
set_variable = {{ DEBT_million = var:DEBT }}
multiply_variable = {{ DEBT_trillion = 0.001 }}
multiply_variable = {{ DEBT_million = 1000 }}

set_technology = {{
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_support = 1
	tech_engineers = 1
	tech_trucks = 1
}}

set_popularities = {{
	{pops}
}}

set_politics = {{
	ruling_party = {party}
	last_election = "2020.11.3"
	election_frequency = 48
	elections_allowed = no
}}
"""

for p in paises:
    file_path = os.path.join(COUNTRIES_DIR, p["filename"])
    if not os.path.exists(file_path):
        contenido = plantilla.format(
            capital=p["capital"],
            party=p["party"],
            pops=p["pops"]
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"✓ Creado: {p['filename']}")
    else:
        print(f"= Ya existía: {p['filename']}")

print("\n¡Todos los archivos de historia de países han sido creados correctamente!")