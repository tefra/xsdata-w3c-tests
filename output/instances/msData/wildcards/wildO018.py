from output.models.ms_data.wildcards.wild_o018_xsd.wild_o018 import Foo


obj = Foo(
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://foobar wildO018.xsd http://foo wildO018a.xsd",
        "{http://foo}name": "bar",
    }
)
