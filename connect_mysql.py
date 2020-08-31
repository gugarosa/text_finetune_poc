from utils.database import Session

# Creates a MySQL session
db = Session()

# Defines a query
query = '''SELECT qeztn_normas_agencia_reguladora.nome AS agencia,
       qeztn_normas_area.nome AS area,
       qeztn_normas_assunto.nome AS assunto,
       qeztn_normas_tipo_norma.nome AS tipo_norma,
--        qeztn_tags.title as tag,
       qeztn_normas_norma.id AS id_norma,
       qeztn_normas_norma.titulo AS titulo_norma,
       qeztn_normas_norma.ementa AS ementa_norma,
       qeztn_normas_norma.norma AS texto_norma
FROM qeztn_normas_norma
INNER JOIN qeztn_normas_agencia_reguladora,
           qeztn_normas_area,
           qeztn_normas_assunto,
           qeztn_normas_assunto_norma,
           qeztn_normas_tipo_norma
--            qeztn_tags,
--            qeztn_tags_norma
WHERE qeztn_normas_norma.id_agencia_reguladora = qeztn_normas_agencia_reguladora.id
  AND qeztn_normas_norma.id_area = qeztn_normas_area.id
  AND qeztn_normas_assunto_norma.id_assunto = qeztn_normas_assunto.id
  AND qeztn_normas_norma.id = qeztn_normas_assunto_norma.id_norma
  AND qeztn_normas_norma.id_tipo_norma = qeztn_normas_tipo_norma.id
--   AND qeztn_tags_norma.id_tag = qeztn_tags.id
--   AND qeztn_normas_norma.id = qeztn_tags_norma.id_norma
  
ORDER BY id_norma'''

# Executes the query
db.cursor.execute(query)

# Iterates over the query results
for row in db.cursor:
    print(row)

# Closes the MySQL session
db.close()
