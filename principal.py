import flet as ft
import alta_usuario as al      # Si tienes este módulo, sino coméntalo
import consulta_usuario as cu  # Igual aquí
import agregar_bioenergia as ba
import consultar_bioenergia as bc
import main as mn

def main(page: ft.Page):

    def mostrar_registro(e: ft.ControlEvent):
        page.clean()
        al.main(page)

    def consultar_usuario(e: ft.ControlEvent):
        page.clean()
        cu.main(page)

    def agregar_bioenergia(e: ft.ControlEvent):
        page.clean()
        ba.main(page)

    def consultar_bioenergia(e: ft.ControlEvent):
        page.clean()
        bc.main(page)
    
    def cerrar_sesion(e: ft.ControlEvent):
        page.clean()
        mn.main(page)

     # Configuración de la página
    page.title = "Menu principal"
    page.theme_mode = "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestion de Bioenergias"),
        leading=ft.Icon("energy_savings_leaf"),
        color="white",
        bgcolor="green"
    )

    # Texto con efecto contorno
    texto_con_efecto = ft.Stack(
        [
            ft.Text(
                spans=[
                    ft.TextSpan(
                        "Bioenergía de Tabasco",
                        ft.TextStyle(
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                color=ft.Colors.GREEN,
                                stroke_width=6,
                                style=ft.PaintingStyle.STROKE,
                            ),
                        ),
                    ),
                ],
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                spans=[
                    ft.TextSpan(
                        "Bioenergía de Tabasco",
                        ft.TextStyle(
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                    ),
                ],
                text_align=ft.TextAlign.CENTER
            ),
        ]
    )

    # Texto descriptivo debajo del título
    texto_descriptivo = ft.Text(
        "Tabasco ha desarrollado proyectos innovadores dentro del campo de bioenergías, "
        "destacando el uso de microalgas para producir combustibles renovables y la iniciativa "
        "de transformar residuos urbanos en electricidad. Todo ello se inserta en una estrategia "
        "estatal más amplia para fortalecer las energías limpias, impulsar la investigación y "
        "apoyar el desarrollo local.",
        size=16,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )
    
    #Botones
    btn_registro = ft.FilledButton(
        text="Registro",
        bgcolor="green",
        icon="person",
        width=180,
        height=50,
        on_click=mostrar_registro,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=15))
    )
    btn_consultas = ft.FilledButton(
        text="Consulta",
        bgcolor="green",
        icon="search",
        width=180,
        height=50,
        on_click=consultar_usuario,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=15))
    )
    btn_agregar_bio = ft.FilledButton(
        text="Agregar Bioenergía",
        bgcolor="green",
        icon="add",
        width=220,
        height=50,
        on_click=agregar_bioenergia,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=15))
    )
    btn_consultar_bio = ft.FilledButton(
        text="Consultar Bioenergía",
        bgcolor="green",
        icon="search",
        width=220,
        height=50,
        on_click=consultar_bioenergia,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=15))
    )

    btn_cerrar_sesion = ft.FilledButton(
        text="Cerrar Sesión",
        icon= "LOGOUT",
        bgcolor="green",
        width=180,
        height=50,
        on_click=cerrar_sesion, 
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=15))
    )


    # Layout centrado
    page.add(
        ft.Column(
            [
                ft.Row([texto_con_efecto], alignment=ft.MainAxisAlignment.CENTER),
                texto_descriptivo,
                ft.Row([btn_registro, btn_consultas, btn_agregar_bio, btn_consultar_bio, btn_cerrar_sesion], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
            ],
            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

