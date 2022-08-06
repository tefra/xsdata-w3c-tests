from output.models.ms_data.wildcards.wild_o026_xsd.wild_o026 import Foo


obj = Foo(
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://foobar wildO026.xsd http://foo wildO026a.xsd",
        "{http://foo}name": "bar",
    }
)
