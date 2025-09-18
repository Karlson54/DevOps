from generator_utils import even_odd_generator

def test_even_odd_generator():
    gen = even_odd_generator()
    assert next(gen) == "Парне"
    assert next(gen) == "Непарне"
    assert next(gen) == "Парне"
    assert next(gen) == "Непарне"
