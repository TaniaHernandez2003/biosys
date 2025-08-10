import flet as ft
import airtable as at
import principal as pr
import agregar_bioenergia as ba  # Importar función para ir a agregar

def pagina_consulta(page: ft.Page):

    def ir_a_agregar(e: ft.ControlEvent):
        page.clean()
        ba.main(page)
    
    def regresar(e: ft.ControlEvent):
        page.clean()
        pr.main(page)

    page.title = "Consulta de Bioenergía"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de Bioenergía en la Nube"),
        leading=ft.Icon("cloud"),
        center_title=True,
        bgcolor="green",
        color="white"
    )

    encabezado = [
        ft.DataColumn(ft.Text("Cultivo")),
        ft.DataColumn(ft.Text("Parte")),
        ft.DataColumn(ft.Text("Cantidad (kg)")),
        ft.DataColumn(ft.Text("Área (ha)")),
        ft.DataColumn(ft.Text("Energía (kWh)")),
        ft.DataColumn(ft.Text("Municipio")),
        ft.DataColumn(ft.Text("Latitud")),
        ft.DataColumn(ft.Text("Longitud"))
    ]

    datos = at.Bioenergia.all() or []

    filas = []
    for d in datos:
        fila = ft.DataRow([
            ft.DataCell(ft.Text(d.cultivo)),
            ft.DataCell(ft.Text(d.parte)),
            ft.DataCell(ft.Text(str(d.cantidad))),
            ft.DataCell(ft.Text(str(d.area))),
            ft.DataCell(ft.Text(str(d.energia))),
            ft.DataCell(ft.Text(d.municipio)),
            ft.DataCell(ft.Text(str(d.latitud))),
            ft.DataCell(ft.Text(str(d.longitud))),
        ])
        filas.append(fila)

    tbl_bioenergia = ft.DataTable(encabezado, filas)

    btn_agregar = ft.FilledButton(text="Agregar Bioenergía", icon="add", bgcolor="green", on_click=ir_a_agregar)
    btn_regresar = ft.FilledButton(text="Regresar",icon= "ARROW_BACK", bgcolor= "green", on_click=regresar )

    page.clean()
    page.add(btn_agregar,btn_regresar, tbl_bioenergia)
    page.update()

def main(page: ft.Page):
    pagina_consulta(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)