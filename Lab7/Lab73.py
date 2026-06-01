def contar_palabras_unicas(texto):
    texto = texto.lower()
    texto = texto.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    palabras = texto.split()
    palabras_unicas = set(palabras)
    return len(palabras_unicas)

def palabra_mas_larga(texto):
    palabras = texto.split()
    mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga

def frecuencia_caracteres(texto):
    texto = texto.lower()
    conteo = {}
    total = 0
    for c in texto:
        if c != " ":
            total += 1
            if c in conteo:
                conteo[c] += 1
            else:
                conteo[c] = 1
    for letra in sorted(conteo):
        porcentaje = (conteo[letra] / total) * 100
        print(f"  '{letra}': {conteo[letra]} veces ({porcentaje:.1f}%)")

texto = input("Ingresa un texto: ")

print("\n--- Reporte ---")
print("Palabras unicas:", contar_palabras_unicas(texto))
print("Palabra mas larga:", palabra_mas_larga(texto))
print("Frecuencia de caracteres:")
frecuencia_caracteres(texto)