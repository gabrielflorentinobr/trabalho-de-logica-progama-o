# Calculadora de IMC com indicações nutricionais

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "gorducho"

def recomendacao_nutricional(classificacao):
    recomendacoes = {
        "Abaixo do peso": """
- Aumente o consumo de proteínas e carboidratos saudáveis
- Faça refeições mais frequentes
- Inclua alimentos como ovos, frango, arroz, aveia e frutas
""",
        "Peso normal": """
- Mantenha uma alimentação equilibrada
- Consuma frutas, verduras e proteínas
- Continue praticando exercícios físicos
""",
        "Sobrepeso": """
- Reduza alimentos ultraprocessados
- Evite excesso de açúcar e frituras
- Priorize alimentos naturais e exercícios físicos
""",
        "Obesidade grau 1": """
- Procure manter déficit calórico saudável
- Consuma mais fibras e proteínas
- Faça acompanhamento com nutricionista
""",
        "Obesidade grau 2": """
- Busque orientação médica e nutricional
- Evite refrigerantes e fast food
- Crie uma rotina de exercícios leves
""",
        "Obesidade grau 3 IMENSO": """
- Procure acompanhamento profissional imediatamente
- Faça mudanças graduais na alimentação
- Priorize saúde e qualidade de vida
"""
    }
    return recomendacoes[classificacao]

# Entrada de dados
print("=== CALCULADORA DE IMC ===")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo
imc = calcular_imc(peso, altura)
classificacao = classificacao_imc(imc)

# Resultado
print("\n=== RESULTADO ===")
print(f"Nome: {nome}")
print(f"IMC: {imc:.2f}")
  
print(f"Classificação: {classificacao}")

print("\n=== INDICAÇÕES NUTRICIONAIS ===")
print(recomendacao_nutricional(classificacao))