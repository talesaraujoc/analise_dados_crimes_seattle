from dash import dash, html, dcc, page_container
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css"], use_pages=True, pages_folder="pages")

# Configuração da NavBar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('HOME', href='/')),
        #dbc.NavItem(dbc.NavLink('COLABORADORES | PDV', href='/page_two')),
    ],
    brand="SEATTLE - RELATÓRIO DE CRIMES",
    brand_href="/",
    color='#003DA5',
    dark=True,
    style={'width': '100%', 'justify-content': 'center'}  # Centraliza os itens
)

# Layout da aplicação com barra superior
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Container(navbar),  # Limita a largura do conteúdo do navbar
        ], width=10, style={'background-color':'#003DA5'}),

        dbc.Col(
            html.Div(
                html.Img(src='assets/logo_gov.png', style={"width": "200px"}), 
                style={"text-align": "right", "padding-right": "20px"}
            ),
            width=2)
    ], style={"background-color": "#FFFFFF", "height": "100px", "align-items": "center"}),
    
    page_container
])

if __name__ == '__main__':
    #app.run_server(debug=False, port=8050, host='0.0.0.0')
    app.run(debug=True)
