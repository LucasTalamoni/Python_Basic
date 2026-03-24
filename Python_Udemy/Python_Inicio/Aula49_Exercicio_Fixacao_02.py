"""
O Problema
O formulário salvou os e-mails dos usuários em uma única string, mas os usuários digitaram espaços sem querer e usaram o símbolo de barra vertical | para separar os endereços.

Entrada (Variável String):
"  aluno@email.com |  professor@escola.org  | diretor@gestao.com  "

Sua Missão:
Transformar essa string em uma lista de e-mails limpos e, depois, criar uma nova string onde os e-mails são separados por um ponto e vírgula seguido de espaço (padrão usado para enviar e-mails em massa).

Saída Esperada (String Final):
"aluno@email.com; professor@escola.org; diretor@gestao.com"
"""

emails = "  aluno@email.com |  professor@escola.org  | diretor@gestao.com  "
emails_separados = emails.split("|")

emails_formatados = []

for i, emails in enumerate(emails_separados):
    emails_formatados.append(emails.strip())

emails_formatados_unificados = "; ".join(emails_formatados)

print(emails_formatados_unificados)