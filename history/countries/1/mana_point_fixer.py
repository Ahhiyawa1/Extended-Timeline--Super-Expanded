import re

def parse_input(input_text):
    monarchs = {}
    lines = input_text.strip().split("\n")
    
    for line in lines:
        match = re.match(r"([\w\s()]+):?\s*(\d*)\s*(\d*)\s*(\d*)", line)
        if match:
            name = match.group(1).strip()
            adm = int(match.group(2)) if match.group(2) else None
            dip = int(match.group(3)) if match.group(3) else None
            mil = int(match.group(4)) if match.group(4) else None
            monarchs[name] = {"adm": adm, "dip": dip, "mil": mil}
    
    return monarchs

def adjust_values(monarchs, current_values):
    """
    Adjusts the current adm, dip, mil values based on input changes.
    
    :param monarchs: Parsed input containing adm, dip, and mil changes
    :param current_values: Dict of current monarch values {name: {adm, dip, mil}}
    """
    for name, stats in monarchs.items():
        if name in current_values:
            for key in ["adm", "dip", "mil"]:
                if stats[key] is not None:
                    current_values[name][key] = stats[key]
    return current_values

# Example input
input_text = """
Tiberius: 3 1 4
Caligula 0 0 1
Claudius 3 2 5 
Galba 1 3 2 
Otho 1 2 1 
Vitellius 0 2 2
Vespasian 4 4 5 
Titus 3 4 4
Domitian 5 1 2 
Nerva 3 4 1 
Trajan 6 5 8
Pertinax: 2 2 4
Didius Julianus: 2 3 1
Septimius Severus: 5 3 6
Caracalla: 3 2 3 
Macrinus: 2 3 3
Elagabalus: 0 1 1
Alexander Severan: 3 3 4
Gordian III: 3 4 3
Philip: 4 2 3
Decius: 3 1 1 
Trebonianus Gallus: 2 2 4
Emilianus: 3 1 3
Valerian: 2 1 4 
Gallienus: 4 2 3
Claudius Gothicus: 4 3 5
Quintillus: 1 1 2
Aurelian: 4 2 6
Tacitus: 3 4 2 
Florianus: 2 2 3
Probus: 4 3 5
Carus: 4 2 3
Carinus: 2 1 3
Numerian: 2 1 3
Diocletian: 6 3 5
Maximinus: 4 3 5
Maxentius: 3 3 4 
Licinus: 3 2 4
Costantine: 6 5 6
Costantine II: 1 3 0
Costante: 2 3 2 
Costantius: 4 4 5
Julian: 4 2 2 
Giovianus: 2 2 1
Valentinian I: 4 2 3
Valente: 2 2 0
Grazianus: 3 2 3
Valentinian II: 1 2 2
Theodosius: 5 2 3
"""

# Example of existing values (default or previously stored values)
current_values = {
}

monarch_changes = parse_input(input_text)
adjusted_values = adjust_values(monarch_changes, current_values)
print(adjusted_values)
