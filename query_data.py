import csv

import utils.regex as r
from utils.mysql import Session

# Creates a MySQL session
db = Session()

# Defines a query
query = '''SELECT qeztn_normas_assunto.nome AS assunto,
       qeztn_normas_tipo_norma.nome AS tipo_norma,
       qeztn_normas_norma.id AS id_norma,
       qeztn_normas_norma.titulo AS titulo_norma,
       qeztn_normas_norma.ementa AS ementa_norma,
       qeztn_normas_norma.norma AS texto_norma
FROM qeztn_normas_norma
INNER JOIN qeztn_normas_assunto,
           qeztn_normas_assunto_norma,
           qeztn_normas_tipo_norma
WHERE qeztn_normas_assunto_norma.id_assunto = qeztn_normas_assunto.id
  AND qeztn_normas_norma.id = qeztn_normas_assunto_norma.id_norma
  AND qeztn_normas_norma.id_tipo_norma = qeztn_normas_tipo_norma.id
ORDER BY assunto'''

print('Executing query ...')

# Executes the query
db.cursor.execute(query)

print('Query executed.')

# Defines an occurence for calculating the label and the label itself
occurence = 'Aceitação da Proposta e Início de Vigência da Cobertura'
label = 0

print('Dumping data ...')

# Opens a .csv file
with open('data/output.csv', 'w', newline='') as csv_file:
    # Defines a .csv writer
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # Writes the header
    writer.writerow(['label', 'sample'])

    # Iterates over the query results
    for i, row in enumerate(db.cursor):
        # Checks if the occurence is the same as ordered key
        if occurence == row[0]:
            pass

        # If not, it means that it belongs to a distinct class
        else:
            # Replaces the occurence with current one
            occurence = row[0]

            # Increments the label
            label += 1

        # Writes the desired information
        writer.writerow([label, r.clean_html(row[-1])])

print('Data dumped.')

# Closes the MySQL session
db.close()
