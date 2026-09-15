def calcular_total(monto, descuento):
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    return monto - (monto * descuento / 100)
