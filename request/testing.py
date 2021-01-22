from request.request import Request

sample_request = Request(
    status_code=200,
    id="1234567",
    path="/sample_page.js",
    host="google.com",
    headers = {
        "Accept": "*/*",
        "Special": "abcdef"
    },
    query_parameters={
        "a":"a",
        "b": "b"
    },
    body="RequestBody",
    identifiers={},
    properties={}
)