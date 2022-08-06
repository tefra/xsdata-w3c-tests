from output.models.sun_data.id_constr_defs.fields.fields00101m.fields00101m1_xsd.fields00101m1 import People
from xsdata.models.datatype import XmlDate


obj = People(
    person=[
        People.Person(
            value="Jesus",
            parent="God",
            birthday=XmlDate(1, 1, 1)
        ),
    ]
)
