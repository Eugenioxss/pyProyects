import openpyxl

# Crear un nuevo libro de Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Agregar encabezados a las columnas
sheet.append(["Nombre Colaborador", "Correo Colaborador", "Nombre Jefe Inmediato", "Correo Jefe Inmediato"])

# Generar 500,000 filas
for i in range(1, 50000001):
    nombre_colaborador = f"Colaborador_{i}"
    correo_colaborador = f"colaborador{i}@ejemplo.com"
    nombre_jefe = f"Jefe_{i}"
    correo_jefe = f"jefe{i}@ejemplo.com"
    
    # Agregar fila a la hoja de Excel
    sheet.append([nombre_colaborador, correo_colaborador, nombre_jefe, correo_jefe])
    print(i)
# Guardar el archivo
workbook.save("archivo_generado.xlsx")

print("Archivo generado exitosamente: archivo_generadobomb.xlsx")
