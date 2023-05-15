from output.models.sun_data.elem_decl.identity_constraint_defs.id_constr_defs00402m.id_constr_defs00402m_xsd.id_constr_defs00402m import Root


obj = Root(
    person=[
        Root.Person(
            value="William Smith",
            ssn="p008"
        ),
        Root.Person(
            value="John Smith",
            ssn="p007",
            parent="p008"
        ),
    ]
)
