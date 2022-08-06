from output.models.ms_data.datatypes.facets.nmtokens.nmtokens_length002_xsd.nmtokens_length002 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test=[
            "foofo",
            "token2",
        ]
    )
)
