#!/bin/bash

# Definir variables
BACKUP_DIR="/backups"               # Directorio donde se guardarán los backups
SOURCE_DIRS=("/home/usuario" "/etc" "/var/log")  # Directorios a respaldar
TIMESTAMP=$(date +'%Y%m%d_%H%M%S')  # Formato de fecha para el nombre del archivo
BACKUP_NAME="backup_$TIMESTAMP.tar.gz"  # Nombre del archivo comprimido

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

# Realizar el backup utilizando tar (archivando y comprimiendo los archivos)
echo "Starting backup at $TIMESTAMP..."
tar -czf $BACKUP_DIR/$BACKUP_NAME ${SOURCE_DIRS[@]}

# Verificar si la operación de backup fue exitosa
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
else
    echo "Error occurred during the backup process."
    exit 1
fi

# Opcional: Eliminar backups antiguos (por ejemplo, eliminar backups más antiguos que 7 días)
# find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +7 -exec rm {} \;
# echo "Old backups deleted."

exit 0
