from output.models.ibm_data.mixed.type_alternatives.test2_1_xsd.test2_1 import Example


obj = Example(
    x=[
        Example.KindQuantity(
            value=10,
            kind="quantity"
        ),
        Example.KindPrice(
            value=10.5,
            kind="price"
        ),
        Example.KindMesg(
            value="hello world",
            kind="mesg"
        ),
    ]
)
