from output.models.ms_data.identity_constraint.id_z007_xsd.id_z007 import NewDataSet


obj = NewDataSet(
    t1_or_t2=[
        NewDataSet.T1(
            id='foo'
        ),
        NewDataSet.T2(
            id='foo'
        ),
    ]
)
