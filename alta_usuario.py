import flet as ft
import airtable as at
import principal as pr  # Aquí el módulo con el código que mostraste (menú principal)
import main as mn  # Módulo donde está la pantalla de inicio de sesión

def main(page: ft.Page):

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value

        if clave == "":
            page.open(ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor="red", show_close_icon=True))
            return
        if contra == "":
            page.open(ft.SnackBar(ft.Text("Contraseña incorrecta"), bgcolor="red", show_close_icon=True))
            return
        if nombre == "":
            page.open(ft.SnackBar(ft.Text("Introduce su Nombre completo"), bgcolor="red", show_close_icon=True))
            return
        if contra != contra2:
            page.open(ft.SnackBar(ft.Text("Contraseña incorrecta"), bgcolor="red", show_close_icon=True))
            return

        nuevo = at.usuario(
            clave=clave,
            contra=contra,
            nombre=nombre,
            admin=chk_admin.value
        )
        try:
            nuevo.save()
            page.open(ft.SnackBar(ft.Text("Usuario registrado"), bgcolor="green", show_close_icon=True))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(str(error)), bgcolor="red", show_close_icon=True))

    def regresar(e: ft.ControlEvent):
        page.clean()
        pr.main(page)  # Regresa al menú principal

    def iniciar_sesion(e: ft.ControlEvent):
        page.clean()
        mn.main(page)  # Manda a la pantalla de login

    page.title = "Altas"
    page.theme_mode = "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="green"
    )

    txt_clave = ft.TextField(label="Clave del usuario")
    txt_contra = ft.TextField(label="Contraseña", password=True)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", password=True)
    txt_nombre = ft.TextField(label="Nombre completo")
    chk_admin = ft.Checkbox(label="¿Es administrador?")

    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon="save",
        on_click=guardar_usuario,
        bgcolor="green"
    )
    btn_cancelar = ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        bgcolor="green",
        on_click=regresar
    )
    btn_iniciar_sesion = ft.FilledButton(
        text="Iniciar Sesión",
        icon="Login",
        bgcolor="green",
        on_click=iniciar_sesion
    )

    fila_botones = ft.Row(
        controls=[btn_guardar, btn_cancelar, btn_iniciar_sesion],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    page.add(txt_clave, txt_contra, txt_contra2, txt_nombre, chk_admin, fila_botones)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
