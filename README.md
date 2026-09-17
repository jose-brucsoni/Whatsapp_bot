# Script de grupos en WhatsApp Web (no es un bot de chat)

**Aviso:** automatiza [WhatsApp Web](https://web.whatsapp.com/) con Selenium. No es la API oficial, no es un bot conversacional y **puede incumplir los términos de WhatsApp**. Los XPath se rompen cuando cambia la UI. El repo se publica con fines **educativos e históricos**.

Si se subieron Excel reales, los enlaces `https://chat.whatsapp.com/...` pueden ser públicos: revócalos y deja de versionar `.xlsx` de trabajo.

```mermaid
flowchart LR
  excelIn[MATERIAS-1.xlsx]
  selenium[Selenium_Chrome]
  wa[WhatsApp_Web]
  excelOut[Modulo_1.xlsx]
  excelIn --> selenium --> wa --> excelOut
```

**Estado:** script local de escritorio. `eliminarGrupo.py` no está implementado.

---

## Qué hace

Lee nombres de grupo en `MATERIAS-1.xlsx` (hoja `final`, columna J, filas 2–39), abre Chrome, espera el QR (hasta 600 s), crea cada grupo con el contacto `a_Yo`, copia el enlace y lo escribe en `Modulo 1.xlsx` (hoja `Hoja1`, columnas J y K), guardando en cada iteración.

---

## Cómo probarlo (plantillas, sin WhatsApp)

```bash
pip install -r requirements.txt
cp examples/MATERIAS-1.example.xlsx "MATERIAS-1.xlsx"
cp examples/Modulo-1.example.xlsx "Modulo 1.xlsx"
```

Las plantillas en `examples/` no tienen datos reales. Ejecutar `python3 principal.py` **sí** abre WhatsApp Web: úsalo solo si aceptas el riesgo de ToS y tienes ChromeDriver en `./chromedriver`.

---

## Qué hice yo

Automatización Selenium + Excel (openpyxl) para un caso académico de creación masiva de grupos.

---

## Requisitos e instalación

Python 3.10+, Chrome, ChromeDriver alineado con Chrome, contacto `a_Yo`, Excel con el formato de abajo. El código usa `executable_path='./chromedriver'` (APIs antiguas de Selenium).

```bash
git clone https://github.com/jose-brucsoni/Whatsapp_bot.git
cd Whatsapp_bot
pip install -r requirements.txt
```

| Archivo | Rol |
| --- | --- |
| `principal.py` | QR y bucle de filas |
| `extraerDatos.py` | Lectura Excel |
| `crearGrupos.py` | Selenium |
| `insertarDatos.py` | Escritura Excel |
| `eliminarGrupo.py` | Vacío |
| `examples/` | Plantillas |

Uso: `python3 principal.py` → QR → hasta 39 grupos (`cantidad_de_filas`). UI en español.

Límites: XPath frágiles, sin tests/CI/Docker, rutas hardcodeadas.

No subas Excel reales, sesiones de Chrome ni el binario de ChromeDriver. `.xlsx` de trabajo, `chromedriver` y `__pycache__/` están en `.gitignore`. Limpiar historial de git no borra copias ya filtradas.

---

José Carlo Suárez Brucsoni · [joseca6520@gmail.com](mailto:joseca6520@gmail.com)

Uso personal y académico. No se recomienda usarlo contra cuentas reales.
