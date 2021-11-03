import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_table
import uuid

from Core.models import Employee

import datetime

from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

app = DjangoDash('ModelList')

PAGE_SIZE = 1

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dcc.ConfirmDialog(
        id='confirm-danger',
        message='Danger danger! Are you sure you want to continue?',
    ),
    dash_table.DataTable(
        id='datatable-paging',
        columns=[
            {'name': field.name, 'id': field.name} for field in Employee._meta.fields
        ],
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='custom'
    ),
    dbc.Alert(id='tbl_out'),
])


@app.callback(
    Output('datatable-paging', 'data'),
    Input('datatable-paging', "page_current"),
    Input('datatable-paging', "page_size"),
    Input('url', 'pathname')
    )
def update_table(page_current, page_size, pathname):
    from django.core.paginator import Paginator

    print(str(pathname))

    paginator = Paginator(Employee.objects.all(), PAGE_SIZE)

    page = paginator.page(page_current + 1)
    data = [e.as_dict() for e in page]
    # serializer = EmployeeSerializer(queryset, many=True)
    # data = [dict(e) for e in serializer.data]

    return data


@app.callback(Output('tbl_out', 'children'), Input('datatable-paging', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"
