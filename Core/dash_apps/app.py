import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

app = DjangoDash('Dashboard', suppress_callback_exceptions=True, add_bootstrap_links=True)