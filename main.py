import flet as ft 
import principal as pr

# Funcion principal
def main (page: ft.Page):

    def ingresar(e: ft.ControlEvent):
        page.clean()
        pr.main(page)

    #configuracion de la pagina 
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesion"
    page.window.width = 500
    page.window.height = 650

    #Componentes de la pagina
    logo = ft.Icon("Person", size=100, color="purple")
    txt_bienvenido = ft.Text("Bienvenid@", size=30)
    txt_usuario= ft.TextField(label="Username/Correo", width=300)
    txt_pass= ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    btn_login = ft.FilledButton (
        "Iniciar sesion", 
        icon=ft.Icons.LOGIN, 
        width=250,
        color="White",
        bgcolor= "purple", 
        on_click= ingresar  
    )

    page.add(logo, txt_bienvenido, txt_usuario, txt_pass, btn_login)

    #Actualizar la pagina
    page.update()

# Inicio de la aplicacion  
if __name__  == "__main__" :
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
