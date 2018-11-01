"""
Script.

Recebe uma lista de fatos e um esquema de relacionamento
para tratamento e retorno de lista de acordo com esquema inserido.
"""
import desafio_dados


def current_facts(facts, schema):
    """
    Metodo desafio.

    relation = interação com cada schema
    fact = interação com cada facts
    list_result_one = lista de tuplas com resultado one-to-one.
    list_result_many = lista de tuplas com resultado one-to-many.
    list_apoio = auxilia na busca por fatos mais recentes

    :return: list_result = Retorna lista com resultado final.
    """
    list_apoio = []

    def treatment_facts(fact):
        """Metodo retorna fato relação one-to-one mais recente."""
        for apoio in list_apoio:
            if fact[:2] == apoio[:2]:
                return
        list_apoio.append(fact)
        return fact

    """list comprehension retorna todos fatos com relação one-to-one
    e chama função treatment_facts"""
    list_result_one = list(map(
        treatment_facts,
        [
            fact for relation in schema if relation[2] == 'one'
            for fact in facts[::-1] if relation[0] == fact[1] and fact[3]
        ]
    ))

    '''list_result = list(map(
        lambda x: list_apoio.append(x),
        [fact for relation in schema if relation[2] == 'one'
            for fact in facts if relation[0] == fact[1] and fact[3]
            for apoio in list_apoio if fact[:2] == apoio[:2]]'''

    # list comprehension retorna todos fatos com relação one-to-many
    list_result_many = [
        fact for relation in schema if relation[2] == 'many'
        for fact in facts[::-1] if relation[0] == fact[1] and fact[3]
    ]
    # junta as listas com os 2 tipos de realação
    list_result = list_result_one + list_result_many
    # Se algum fato = none incluido, acontece se uma das listas estiver vazia
    list_result = [result for result in list_result if result]
    return list_result


if __name__ == '__main__':
    resultado = current_facts(desafio_dados.facts, desafio_dados.schema)
    print(f'{[fact for fact in resultado]}')
