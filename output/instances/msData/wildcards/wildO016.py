from output.models.ms_data.wildcards.wild_o016_xsd.wild_o016 import Foo


obj = Foo(
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://foobar wildO016.xsd http://foo wildO016a.xsd",
        "{http://foo}name": "bar",
    }
)
