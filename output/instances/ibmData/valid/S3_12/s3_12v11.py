from output.models.ibm_data.valid.s3_12.s3_12v11_xsd.s3_12v11 import Root


obj = Root(
    meeting=[
        Root.Meeting(
            beverage="abc",
            end_time=1
        ),
        Root.Meeting(
            beverage=123,
            end_time=11
        ),
    ]
)
