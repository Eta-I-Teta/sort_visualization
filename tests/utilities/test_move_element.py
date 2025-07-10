from engine.utilities import move_element

def test_move_element_1():
    """Перемещение элемента в середину списка"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [0, 1, 2, 5, 3, 4, 6, 7, 8, 9]

    move_element(inp_value, 5, 3)

    assert exp_value == inp_value


def test_move_element_2():
    """Перемещение элемента в начало списка"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]

    move_element(inp_value, 5, 0)

    assert exp_value == inp_value


def test_move_element_3():
    """Перемещение элемента в конец списка"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [0, 1, 2, 3, 4, 6, 7, 8, 9, 5]

    move_element(inp_value, 5, 9)

    assert exp_value == inp_value


def test_move_element_4():
    """Перемещение элемента на текущую позицию"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    move_element(inp_value, 5, 5)

    assert exp_value == inp_value


def test_move_element_5():
    """Перемещение первого элемента в конец"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    move_element(inp_value, 0, 9)

    assert exp_value == inp_value


def test_move_element_6():
    """Перемещение последнего элемента в начало"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    move_element(inp_value, 9, 0)

    assert exp_value == inp_value


def test_move_element_7():
    """Перемещение элемента из начала в середину"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]

    move_element(inp_value, 0, 3)

    assert exp_value == inp_value


def test_move_element_8():
    """Перемещение элемента из конца в середину"""
    inp_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp_value = [0, 1, 2, 9, 3, 4, 5, 6, 7, 8]

    move_element(inp_value, 9, 3)

    assert exp_value == inp_value


def test_move_element_9():
    """Перемещение элемента в списке с одним элементом (должен остаться неизменным)"""
    inp_value = [42]
    exp_value = [42]

    move_element(inp_value, 0, 0)

    assert exp_value == inp_value