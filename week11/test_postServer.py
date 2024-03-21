import http
import unittest
from http.server import HTTPServer
from server import SimpleHTTPRequestHandler
import http.client
import json
import threading

class TestServerPOST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_address = ('localhost', 8000)
        cls.server = HTTPServer(cls.server_address, SimpleHTTPRequestHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()
    

    def test_post_method(self):
        reqBody = {
            "message": "Hello",

}
        # Connect to the server and send a POST request
        connection = http.client.HTTPConnection(*self.server_address)
        body_json = json.dumps(reqBody)
        
        # Set the Content-Type header to indicate JSON data
        headers = {'Content-Type': 'application/json'}
        
        # Send the request with the encoded body
        connection.request('POST', '/', body=body_json, headers=headers)
        response = connection.getresponse()

        # Read and Decode the response
        data = response.read().decode()
        connection.close()
        print(data)
        # Check that the response as expected
        self.assertEqual(response.status, 200)
        self.assertEqual(response.reason, 'OK')
        # Check response header type is correct
        self.assertEqual(response.getheader('Content-Type'), 'application/json')

        # Parse the JSON data and verify the content
        response_data = json.loads(data)
        self.assertEqual(response_data, {'received': {
            "message": "Hello",

}})
        
if __name__ == '__main__':
    unittest.main()