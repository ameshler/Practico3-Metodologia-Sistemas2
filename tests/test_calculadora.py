from calculadora import calcular_total


def test_calcular_total_con_descuento():
    # Arrange
    monto = 1000
    descuento = 20

    # Act
    resultado = calcular_total(monto, descuento)

    # Assert
    assert resultado == 800


def test_calcular_total_sin_descuento():
    # Arrange
    monto = 1500
    descuento = 0

    # Act
    resultado = calcular_total(monto, descuento)

    # Assert
    assert resultado == 1500


def test_calcular_total_con_descuento_maximo():
    # Arrange
    monto = 2000
    descuento = 100

    # Act
    resultado = calcular_total(monto, descuento)

    # Assert
    assert resultado == 0


def test_calcular_total_rechaza_monto_cero():
    # Arrange
    monto = 0
    descuento = 20

    # Act
    resultado = None

    try:
        calcular_total(monto, descuento)
    except ValueError as error:
        resultado = error

    # Assert
    assert isinstance(resultado, ValueError)


def test_calcular_total_rechaza_descuento_mayor_a_100():
    # Arrange
    monto = 1000
    descuento = 120

    # Act
    resultado = None

    try:
        calcular_total(monto, descuento)
    except ValueError as error:
        resultado = error

    # Assert
    assert isinstance(resultado, ValueError)
