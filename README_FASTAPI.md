# Microservicio FastAPI para imágenes

1. Instala las dependencias:

    pip install -r requirements_fastapi.txt

2. Ejecuta el microservicio:

    uvicorn imagenes_fastapi:app --host 0.0.0.0 --port 8082

3. Configura Kong para enrutar las rutas de imágenes a la IP de esta VM (por ejemplo, 10.128.0.53:8082):

```
- name: imagenes_service
  host: 10.128.0.53
  port: 8082
  protocol: http
  routes:
    - name: imagenes_routes
      paths:
        - /imagen
        - /imagen/
        - /imagen/upload
        - /imagen/view
      strip_path: false
      preserve_host: true
```

4. Elimina o comenta las rutas de imágenes en Django para evitar conflictos.

5. Prueba:
- Sube una imagen: POST /imagen/upload/
- Visualiza una imagen: GET /imagen/view/<nombre_archivo>
