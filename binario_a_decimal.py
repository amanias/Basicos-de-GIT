def decimal(binary_str):
    """ Convierte cadenas binarias a sus equivalentes decimales.
    Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1
    """
    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError('La cadena binaria de entrada solo puede contener 0 y 1')
    posicion = 1;
    valor_decimal = 0
    for bit in binary_str[::-1]:
        # Bucle desde el final de la cadena hasta el principio
        if (bit == '1'): # Si el dígito es un 1, agregue el valor posicional.Si es 0, ignorar.
            valor_decimal += posicion
        posicion *= 2 # Multiplique la posición por 2 para el siguiente valor de posición
    return valor_decimal

# print(decimal("101"))

# test_bin_str = [ '101010', '1111', '000111', '0', '1']
# expected_dec = [ 42, 15, 7, 0, 1]
# print(zip( test_bin_str, expected_dec))
# for binary_input, expected_dec_output in zip( test_bin_str, expected_dec):
#             print(binary_input)
#             print(expected_dec_output)