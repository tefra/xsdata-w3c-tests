from output.models.sun_data.elem_decl.identity_constraint_defs.id_constr_defs00204m.id_constr_defs00204m_xsd.id_constr_defs00204m import Root


obj = Root(
    person=[
        Root.Person(
            value='William Smith'
        ),
        Root.Person(
            value='John Smith',
            parent='William Smith'
        ),
    ]
)
