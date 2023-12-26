from output.models.sun_data.elem_decl.identity_constraint_defs.id_constr_defs00403m.id_constr_defs00403m_xsd.id_constr_defs00403m import Root


obj = Root(
    person=[
        Root.Person(
            value='William Smith',
            ssn='p008'
        ),
        Root.Person(
            value='Anna Brown',
            ssn='p011'
        ),
        Root.Person(
            value='John Smith',
            ssn='p007',
            parents=[
                'p008',
                'p011',
            ]
        ),
    ]
)
