# WhatsApp Bot (creación masiva de grupos)

Automatización de escritorio en Python que crea grupos en [WhatsApp Web](https://web.whatsapp.com/) a partir de un Excel, copia el enlace de invitación de cada grupo y lo guarda en otro libro.

No es un bot conversacional, no usa la API oficial de WhatsApp Business y no es un servicio desplegable. Es un script local con Selenium que controla Chrome.

## Aviso

Esta automatización usa la interfaz web de WhatsApp, no una API documentada. Los selectores XPath se rompen cuando WhatsApp cambia la UI. El uso puede incumplir los términos de WhatsApp. El repositorio se publica con fines educativos e históricos.

Si este proyecto ya se subió a GitHub con Excel reales, los enlaces `https://chat.whatsapp.com/...` pueden haber quedado públicos. Revoca o rota esos enlaces en WhatsApp y deja de versionar los `.xlsx` de trabajo (ver [Privacidad](#privacidad)).

## Características

- Lee nombres de grupo desde `MATERIAS-1.xlsx` (hoja `final`, columna J, filas 2–39).
- Abre WhatsApp Web y espera hasta 600 segundos a que inicies sesión con el código QR.
- Crea cada grupo añadiendo el contacto de la agenda llamado exactamente `a_Yo`.
- Extrae el enlace de invitación y lo escribe en `Modulo 1.xlsx` (hoja `Hoja1`, columnas J y K).
- Guarda el Excel de salida en cada iteración.

`eliminarGrupo.py` existe en el repo pero no está implementado.

## Requisitos

- Python 3.10 o superior
- Google Chrome
- ChromeDriver compatible con tu sistema operativo y con la versión de Chrome
- Un contacto de WhatsApp guardado con el nombre `a_Yo`
- Los archivos Excel con el formato descrito más abajo

El código arranca el driver con `executable_path='./chromedriver'` (ver `principal.py`). En Windows el binario suele llamarse `chromedriver.exe`; en Linux/macOS usa un ChromeDriver nativo llamado `chromedriver` en la raíz del proyecto. No versionamos el driver: descárgalo por tu cuenta.

## Estructura del repositorio

| Archivo | Rol |
| --- | --- |
| `principal.py` | Punto de entrada: abre Chrome, espera el QR y recorre las filas |
| `extraerDatos.py` | Lee los nombres de grupo desde el Excel de entrada |
| `crearGrupos.py` | Selenium: crear grupo y copiar el enlace de invitación |
| `insertarDatos.py` | Escribe enlace y nombre en el Excel de salida |
| `eliminarGrupo.py` | Sin implementación |
| `examples/` | Plantillas Excel de ejemplo, sin datos reales |
| `requirements.txt` | Dependencias de Python |

## Instalación

```bash
git clone https://github.com/jose-brucsoni/Whatsapp_bot.git
cd Whatsapp_bot
pip install -r requirements.txt
```

Copia las plantillas a los nombres que el código espera:

```bash
cp examples/MATERIAS-1.example.xlsx "MATERIAS-1.xlsx"
cp examples/Modulo-1.example.xlsx "Modulo 1.xlsx"
```

Coloca ChromeDriver en la raíz del proyecto como `./chromedriver` (o ajusta la ruta en `principal.py`).

Rellena `MATERIAS-1.xlsx` con los nombres de grupo en la columna J.

## Formato de Excel

**Entrada:** `MATERIAS-1.xlsx`

- Hoja: `final`
- Nombres de grupo: columna J, desde `J2` (el script lee el rango `J2:J39`)

**Salida:** `Modulo 1.xlsx`

- Hoja: `Hoja1`
- Columna J: enlace de invitación
- Columna K: nombre del grupo

## Uso

```bash
python3 principal.py
```

1. Se abre Chrome en WhatsApp Web.
2. Escanea el código QR. No cierres la ventana.
3. El script crea hasta 39 grupos (valor fijo `cantidad_de_filas = 39` en `principal.py`).
4. Tras cada grupo, actualiza `Modulo 1.xlsx`.

Valores fijos en el código (cámbialos si tu caso es distinto):

- Número de filas: `39`
- Contacto añadido a cada grupo: `a_Yo`
- Textos de la UI en español (`Menú`, `Nuevo grupo`, etc.)

## Limitaciones conocidas

- Selenium usa APIs antiguas (`executable_path`, `find_element_by_xpath`). Con versiones recientes de Selenium el script puede fallar hasta actualizar esas llamadas.
- Los XPath de `crearGrupos.py` apuntan a una versión concreta de WhatsApp Web y son frágiles.
- No hay tests, CI ni Docker.
- No hay variables de entorno: rutas, filas y contacto van hardcodeados.
- `eliminarGrupo.py` no hace nada.

Los pull requests que actualicen XPath o la API de Selenium son los más útiles.

## Contribuir

1. Haz un fork del repositorio.
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de los cambios.
4. Haz push de la rama y abre un pull request.

No subas Excel con datos reales, enlaces de grupos, sesiones de Chrome ni binarios de ChromeDriver.

## Privacidad

- Los `.xlsx` de trabajo, `chromedriver` y `__pycache__/` están en `.gitignore`.
- No subas perfiles de Chrome ni cookies de WhatsApp Web.
- Si `MATERIAS-1.xlsx` o `Modulo 1.xlsx` ya estaban en el historial de git, dejar de versionarlos no borra copias antiguas. Revoca los enlaces de invitación que se hayan filtrado. Limpiar el historial es opcional y hay que hacerlo con cuidado.

## Contacto

joseca6520@gmail.com
