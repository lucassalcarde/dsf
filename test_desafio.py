"""Script testes de desafio.py."""
from dsf import current_facts


def test_current_facts_false():
    """Metodo teste unico fato false."""
    facts = [
        ('joão', 'endereço', 'rua alice, 10', False),
    ]
    schema = [
        ('endereço', 'cardinality', 'one'),
    ]
    resultado = current_facts(facts, schema)
    assert not resultado


def test_current_facts_true():
    """Metodo teste unico fato True."""
    facts = [
        ('joão', 'endereço', 'rua alice, 10', True),
    ]
    schema = [
        ('endereço', 'cardinality', 'one'),
    ]
    resultado = current_facts(facts, schema)
    assert resultado == [('joão', 'endereço', 'rua alice, 10', True)]


def test_current_facts_one_to_one():
    """Metodo teste fato mais recente."""
    facts = [
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua guanabara, 123', True),
    ]
    schema = [
        ('endereço', 'cardinality', 'one'),
    ]
    resultado = current_facts(facts, schema)
    assert resultado == [('joão', 'endereço', 'rua guanabara, 123', True)]


def test_current_facts_one_to_many():
    """Metodo teste todos fatos relação one-to-many."""
    facts = [
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', True),
    ]
    schema = [
        ('telefone', 'cardinality', 'many'),
    ]
    resultado = current_facts(facts, schema)
    assert len(resultado) == 3


def test_current_facts_new_attr_schema():
    """Metodo teste todos fatos relação one-to-many novo atributo no schema."""
    facts = [
        ('joão', 'email', 'joão@joão.com', True),
        ('joão', 'email', 'joão@gmail.com', True),
        ('joão', 'email', 'joão@jp.com', True),
    ]
    schema = [
        ('email', 'cardinality', 'many'),
    ]
    resultado = current_facts(facts, schema)
    assert len(resultado) == 3


def test_current_facts_new_e():
    """Metodo teste nova entidade."""
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
        ('gabriel', 'email', 'gabriel@gabriel.com', True),
        ('joão', 'email', 'joão@joão.com', True),
        ('joão', 'email', 'joão@gmail.com', True),
        ('josé', 'endereço', 'rua alferes, 808', True),
        ('josé', 'telefone', '99734-5575', True),
        ('josé', 'email', 'joão@joão.com', True),
        ('josé', 'email', 'joão@jp.com', False),
        ('josé', 'endereço', 'rua riachuelo, 8080', True),
        ('josé', 'endereço', 'av independencia, 80', True),
    ]
    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many'),
        ('email', 'cardinality', 'many'),
    ]
    resultado = current_facts(facts, schema)
    assert resultado ==\
        [
            ('josé', 'endereço', 'av independencia, 80', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('josé', 'telefone', '99734-5575', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', True),
            ('josé', 'email', 'joão@joão.com', True),
            ('joão', 'email', 'joão@gmail.com', True),
            ('joão', 'email', 'joão@joão.com', True),
            ('gabriel', 'email', 'gabriel@gabriel.com', True),
        ]
