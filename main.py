import flet as ft
import principal as pr
from airtable import usuario as Usuario
from pyairtable.formulas import match
import alta_usuario as al


Usuario.api_key = "patn1DWLGpKowibsv.39bdd2ccad950be7954beb56934cc11958fe8d38c9972501c9d53818cf43b8d0"
Usuario.base_id = "appG4jztxTtg7fnf3"
Usuario.table_name = "usuario"

def main(page: ft.Page):

    def mostrar_registro(e: ft.ControlEvent):
        page.clean()
        al.main(page)

    def ingresar(e: ft.ControlEvent):
        usuario_valor = txt_usuario.value.strip()
        password_valor = txt_pass.value.strip()

        # Validaciones antes de consultar la nube
        if usuario_valor == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu usuario"), bgcolor="red", show_close_icon=True))
            return
        if password_valor == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu contraseña"), bgcolor="red", show_close_icon=True))
            return

        try:
            formula = match({"clave": usuario_valor, "contra": password_valor})
            registro = Usuario.first(formula=formula)

            if registro:
                page.open(ft.SnackBar(ft.Text("Inicio de sesión exitoso"), bgcolor="green", show_close_icon=True))
                page.clean()
                pr.main(page)  # Ir al menú principal
            else:
                page.open(ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"), bgcolor="red", show_close_icon=True))

        except Exception as error:
            page.open(ft.SnackBar(ft.Text(f"Error de conexión: {error}"), bgcolor="red", show_close_icon=True))

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window.width = 500
    page.window.height = 650

    # Componentes de la página
    logo = ft.Icon(name="person", size=100, color="green")
    txt_bienvenido = ft.Text("Bienvenido", size=30)
    txt_usuario = ft.TextField(label="Username/Correo", width=300)
    espacio1 = ft.Container(height=10)
    txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    espacio2 = ft.Container(height=10)

    btn_registro = ft.FilledButton(
        text="Registro",
        bgcolor="green",
        icon="person_add",
        width=250,
        height=35,
        on_click=mostrar_registro
    )

    btn_login = ft.FilledButton(
        text="Iniciar sesión",
        icon="login",
        width=250,
        height= 35,
        color="white",
        bgcolor="green",
        on_click=ingresar
    )

    # Agregar controles
    page.add(logo, txt_bienvenido, txt_usuario, espacio1, txt_pass, espacio2, btn_login, btn_registro)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
