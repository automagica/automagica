"""Copyright 2020 Oakwood Technologies BVBA"""

import urllib3
import json as jsonlib


class HTTPClient:
    """
    HTTPClient interface extending urllib3
    """

    def __init__(self):
        """Create HTTP Client"""
        self.pool = urllib3.PoolManager()

    def post(
        self, url, data=None, json=None, headers=None, timeout=30, files=None
    ):
        """Make a POST request"""

        if files:
            for key, val in files.items():
                temp = list(files[key])
                temp[1] = temp[1].read()
                files[key] = tuple(temp)

            fields = files

            if data:
                fields.update(data)

            return HTTPResponse(
                self.pool.request(
                    "POST",
                    url,
                    fields=files,
                    headers=headers,
                    timeout=timeout,
                )
            )

        if json:
            if not headers:
                headers = {"Content-Type": "application/json"}

            else:
                headers["Content-Type"] = "application/json"

            encoded_data = jsonlib.dumps(json).encode("utf-8")
            return HTTPResponse(
                self.pool.request(
                    "POST",
                    url,
                    body=encoded_data,
                    headers=headers,
                    timeout=timeout,
                )
            )

        return HTTPResponse(
            self.pool.request(
                "POST", url, body=data, headers=headers, timeout=timeout
            )
        )

    def get(self, url, headers=None, stream=False, timeout=30):
        """Make a GET request"""
        return HTTPResponse(
            self.pool.request("GET", url, headers=headers, timeout=timeout)
        )


class HTTPResponse:
    """Wrapping class for urllib3 to provide reusable
    interface"""

    def __init__(self, response):
        """Create response class"""
        self.response = response

    def json(self):
        """Returns a JSON"""
        return jsonlib.loads(self.response.data)

    @property
    def text(self):
        """Returns text"""
        return self.response.data.decode("utf-8")

    @property
    def content(self):
        """Returns content"""
        return self.response.data

    @property
    def status_code(self):
        """Returns status"""
        return self.response.status

    @property
    def url(self):
        """Returns the url"""
        return self.response.geturl()


http_client = HTTPClient()
