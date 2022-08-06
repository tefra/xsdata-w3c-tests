from output.models.ibm_data.valid.s3_10_6.s3_10_6v02_xsd.s3_10_6v02 import Root


obj = Root(
    e1=T.E1(
        other_attributes={
            "{b}b": "1",
        }
    ),
    e2=T.E2(
        target_namespace_attributes={
            "{a}b": "1",
        }
    ),
    e3=T.E3(
        local_attributes={
            "b": "1",
        }
    ),
    e4=T.E4(
        any_attributes={
            "b": "1",
        }
    )
)
