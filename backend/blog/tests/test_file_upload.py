import json
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

# def test_file_upload(client_query_file):
#     test_file = SimpleUploadedFile(name='test.txt', content="Semper Fi".encode('utf-8'))
#
#     response = client_query_file(
#         '''
#         mutation testMutation($file: Upload!) {
#             testMutation(fileIn: $file) {
#                 ok
#             }
#         }
#         ''',
#         op_name='testMutation',
#         files={'file': test_file},
#     )
#
#     content = json.loads(response.content)
#     print(content)
#     assert 'errors' not in content
