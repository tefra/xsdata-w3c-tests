from output.models.ms_data.datatypes.facets.any_uri.any_uri_b002_xsd.any_uri_b002 import Bar
from output.models.ms_data.datatypes.facets.any_uri.any_uri_b002_xsd.any_uri_b002 import Root
from output.models.ms_data.datatypes.facets.any_uri.any_uri_b002_xsd.any_uri_b002 import St


obj = Root(
    bar=[
        Bar(
            value=St.X_Y,
            att=St.A_B
        ),
        Bar(
            value=St.A_B
        ),
        Bar(
            value=St.ANY_URI_C,
            att=St.X_Y
        ),
    ]
)
