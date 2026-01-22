from output.models.sun_data.elem_decl.identity_constraint_defs.id_constr_defs00203m.id_constr_defs00203m_xsd.id_constr_defs00203m import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    person=[
        Root.Person(
            value='John Smith',
            birthday=XmlDate(1999, 5, 31)
        ),
        Root.Person(
            value='William Smith',
            birthday=XmlDate(1999, 5, 31)
        ),
        Root.Person(
            value='John Smith',
            birthday=XmlDate(1969, 10, 12)
        ),
    ]
)
