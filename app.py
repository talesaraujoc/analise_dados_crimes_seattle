from dash import dash, html, dcc, page_container
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css"], use_pages=True, pages_folder="pages")

# Configuração da NavBar
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.NavbarBrand("SEATTLE | Painel de Crimes e Segurança Pública", className="ms-3"),
                width="auto"
            ),
            dbc.Col(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("1.1", href="/page_one_a", className="me-3")),
                    dbc.NavItem(dbc.NavLink("1.2", href="/page_two", className="me-3")),
                    dbc.NavItem(dbc.NavLink("HOME", href="/")),
                ], className="ms-auto", navbar=True),
                width="auto"
            )
        ], align="center", className="g-0 w-100 justify-content-between")
    ]),
    color="#003DA5",
    dark=True,
    className="py-2"
)

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            navbar
        ], width=10),

        dbc.Col(
            html.Div(
                html.Img(src='assets/logo_gov.png', style={"width": "140px"}), 
                style={"text-align": "right", "padding-right": "20px"}
            ),
            width=2,
            style={"display": "flex", "align-items": "center", "justify-content": "flex-end"}
        )
    ], style={"background-color": "#FFFFFF", "height": "80px"}),

    page_container
])



if __name__ == '__main__':
    #app.run_server(debug=False, port=8050, host='0.0.0.0')
    app.run(debug=True)
