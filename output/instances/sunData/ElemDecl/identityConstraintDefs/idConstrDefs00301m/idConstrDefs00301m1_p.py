from output.models.sun_data.elem_decl.identity_constraint_defs.id_constr_defs00301m.id_constr_defs00301m_xsd.id_constr_defs00301m import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    element_or_element_ref_or_element_refs=[
        "e001",
        DerivedElement(
            qname="ElementRef",
            value="e001"
        ),
        DerivedElement(
            qname="ElementRefs",
            value=[
                "e001",
            ]
        ),
        "e002",
        DerivedElement(
            qname="ElementRef",
            value="e001"
        ),
        DerivedElement(
            qname="ElementRefs",
            value=[
                "e001",
                "e002",
            ]
        ),
    ]
)
