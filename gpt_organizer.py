import openai

def organizar_com_gpt(dados, chave_api):
    openai.api_key = chave_api

    prompt = f"""
    Você é um assistente de dados. Recebe dados extraídos da web em formato JSON e precisa organizá-los.
    Os dados a seguir foram raspados de um site:

    {dados}

    Organize os dados em colunas bem definidas. Corrija nomes, padronize endereços e formate preços se necessário.
    Retorne no formato de lista de dicionários prontos para converter em tabela.
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um organizador de dados inteligente."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    conteudo = resposta["choices"][0]["message"]["content"]
    try:
        resultado = eval(conteudo.strip())
    except:
        resultado = [{"erro": "Falha ao interpretar resposta do GPT"}]

    return resultado
