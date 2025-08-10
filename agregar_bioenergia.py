import flet as ft
import airtable as at
import principal as pr
import consultar_bioenergia as bc

municipios_tabasco = [
    "Balancán", "Centla", "Centro", "Comalcalco", "Cunduacán",
    "Emiliano Zapata", "Huimanguillo", "Jalapa", "Jalpa de Méndez",
    "Jonuta", "Macuspana", "Nacajuca", "Paraíso", "Tacotalpa",
    "Teapa", "Tenosique"
]

def pagina_agregar_bioenergia(page: ft.Page):

    def principal_click(e: ft.ControlEvent):
        page.clean()
        pr.main(page)

    def guardar_bioenergia(e: ft.ControlEvent):
        cultivo = txt_cultivo.value.strip()
        parte = txt_parte.value.strip()
        cantidad_str = txt_cantidad.value.strip()
        area_str = txt_area.value.strip()
        energia_str = txt_energia.value.strip()
        municipio = dd_municipio.value
        latitud_str = txt_latitud.value.strip()
        longitud_str = txt_longitud.value.strip()

        # Validaciones
        if cultivo == "":
            page.open(ft.SnackBar(ft.Text("Introduce Cultivo"), bgcolor="red", show_close_icon=True))
            return
        if parte == "":
            page.open(ft.SnackBar(ft.Text("Introduce la Parte"), bgcolor="red", show_close_icon=True))
            return
            #return mostrar_snackbar("Introduce la parte", "red")
        if not cantidad_str or not cantidad_str.replace(".", "", 1).isdigit() or float(cantidad_str) <= 0:
            page.open(ft.SnackBar(ft.Text("Introduce una Cantidad válida"), bgcolor="red", show_close_icon=True))
            return
            #return mostrar_snackbar("Introduce una cantidad válida (> 0)", "red")
        if not area_str or not area_str.replace(".", "", 1).isdigit() or float(area_str) <= 0:
            page.open(ft.SnackBar(ft.Text("Introduce un área válida"), bgcolor="red", show_close_icon=True))
            return
            #return mostrar_snackbar("Introduce un área válida (> 0)", "red")
        if not energia_str or not energia_str.replace(".", "", 1).isdigit() or float(energia_str) <= 0:
            page.open(ft.SnackBar(ft.Text("Introduce la Energía generada"), bgcolor="red", show_close_icon=True))
            return
            #return mostrar_snackbar("Introduce la energía generada (> 0)", "red")
        if not municipio:
            page.open(ft.SnackBar(ft.Text("Selecciona un municipio"), bgcolor="red", show_close_icon=True))
            return
            #return mostrar_snackbar("Selecciona un municipio", "red")

        try:
            cantidad = float(cantidad_str)
            area = float(area_str)
            energia = float(energia_str)
            latitud = float(latitud_str) if latitud_str else 0.0
            longitud = float(longitud_str) if longitud_str else 0.0

            nuevo = at.Bioenergia(
                cultivo=cultivo,
                parte=parte,
                cantidad=cantidad,
                area=area,
                energia=energia,
                municipio=municipio,
                latitud=latitud,
                longitud=longitud
            )
            nuevo.save()

            mostrar_snackbar("Registro de bioenergía guardado correctamente", "green")

            # Limpiar campos
            txt_cultivo.value = ""
            txt_parte.value = ""
            txt_cantidad.value = ""
            txt_area.value = ""
            txt_energia.value = ""
            dd_municipio.value = None
            txt_latitud.value = ""
            txt_longitud.value = ""
            page.update()

        except Exception as error:
            mostrar_snackbar(f"Error: {error}", "red")

    def mostrar_snackbar(mensaje: str, color: str):
        page.snack_bar = ft.SnackBar(ft.Text(mensaje), bgcolor=color, show_close_icon=True)
        page.snack_bar.open = True
        page.update()

    def ir_a_consulta(e: ft.ControlEvent):
        page.clean()
        bc.main(page)

    # Configuración de la página
    page.title = "Agregar Bioenergía"
    page.theme_mode = "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Agregar Bioenergía"),
        leading=ft.Icon("eco"),
        bgcolor="green",
        color="white",
        center_title=True
    )

    # Campos de entrada
    txt_cultivo = ft.TextField(label="Cultivo")
    txt_parte = ft.TextField(label="Parte")
    txt_cantidad = ft.TextField(label="Cantidad (kg)")
    txt_area = ft.TextField(label="Área (ha)")
    txt_energia = ft.TextField(label="Energía (kWh)")
    dd_municipio = ft.Dropdown(
        label="Municipio",
        width=900,
        options=[ft.dropdown.Option(m) for m in municipios_tabasco]
    )
    txt_latitud = ft.TextField(label="Latitud")
    txt_longitud = ft.TextField(label="Longitud")

    # Botones
    btn_guardar = ft.FilledButton(text="Guardar", icon="save", bgcolor="green", on_click=guardar_bioenergia)
    btn_cancelar = ft.FilledButton(text="Cancelar", icon="cancel", bgcolor="grey", on_click=principal_click)
    btn_consulta = ft.FilledButton(text="Ir a Consulta", icon="search", bgcolor="blue", on_click=ir_a_consulta)

    # Agregar controles a la página
    page.add(
        txt_cultivo,
        txt_parte,
        txt_cantidad,
        txt_area,
        txt_energia,
        dd_municipio,
        txt_latitud,
        txt_longitud,
        ft.Row(
            controls=[btn_guardar, btn_cancelar, btn_consulta],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )
    page.update()


def main(page: ft.Page):
    pagina_agregar_bioenergia(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
