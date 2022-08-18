import json
from django.core.files.uploadedfile import SimpleUploadedFile


def test_file_upload(client_query_file):
    file_text = "lorem ipsum dolor sit amet"
    file_input = SimpleUploadedFile(name='test.txt', content=file_text.encode('utf-8'))

    response = client_query_file(
        '''
        mutation testMutation($files: Upload!) {
            testMutation(fileInput: $files) {
                success
            }
        }
        ''',
        files={'files': file_input},
    )

    content = json.loads(response.content)
    print(content)
    assert 'errors' not in content
