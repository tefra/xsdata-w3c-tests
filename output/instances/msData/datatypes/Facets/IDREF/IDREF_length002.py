from output.models.ms_data.datatypes.facets.idref.idref_length002_xsd.idref_length002 import Test


obj = Test(
    foo=FooType.Foo(
        value="special test for datatypes that are attribute only",
        attr_test="foofo",
        id_attr="foofo"
    )
)
