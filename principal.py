import flet as ft
import modelo as  md
import principal as pr

def mostrar_registro(e: ft.ControlEvent):
    page.clean()

def main(page: ft.Page):
    #Configuracion de la pagina
    page.title = "Menu principal"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        title= ft.Text("Sistema de Gestión de Bionergías"),
        leading=ft.Icon("energy_savings_leaf"),
        color="whithe",
        bgcolor= "purple"
    )
    #Componentes de la pagina
    btn_registro = ft.ElevatedButton("Registro", on_click= mostrar_registro )
    btn_consultas = ft.ElevatedButton("Consulta")
    #Añadir a la pagina
    page.add(btn_registro, btn_consultas)
    #Actualizar la pagina
    page.update()

#inicio de la aplicacion 
if __name__  == "__main__" :
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)