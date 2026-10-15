import os
MAX_EXPEDIENTES = 100
codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
total_expedientes = 0

def buscar_indice_por_codigo(codigo_buscar):
    for i in range(total_expedientes):
        if codigos[i].lower() == codigo_buscar.lower(): return i
    return -1

def ordenar_y_mostrar_expedientes():
    c_cod = codigos[:total_expedientes]
    c_ciu = ciudadanos[:total_expedientes]
    c_asu = asuntos[:total_expedientes]
    for i in range(total_expedientes - 1):
        for j in range(total_expedientes - i - 1):
            if c_cod[j] > c_cod[j + 1]:
                c_cod[j], c_cod[j + 1] = c_cod[j + 1], c_cod[j]
                c_ciu[j], c_ciu[j + 1] = c_ciu[j + 1], c_ciu[j]
                c_asu[j], c_asu[j + 1] = c_asu[j + 1], c_asu[j]
