#we are testing if the crawler works only on the file extensions speicifc and nothing else. We are mocking file paths
import os
from unittest import mock
from search.crawler import read_files

def test_read_files():
    mock_files = {
        "/some/path/file1.txt": "hello world",
        "/some/path/file2.md": "markdown content",
        "/some/path/image.png": "binarydata"
    }

    with mock.patch("os.walk") as mockwalk, \
        mock.patch("builtins.open", mock.mock_open()) as mockopen:

            mockwalk.return_value = [("/some/path", [], list(mock_files.keys()))]

            def side_effect(path, *args, **kwargs):
                data = mock_files[path]
                return mock.mock_open(read_data=data).return_value
            mockopen.side_effect = side_effect

            results = read_files("some/path", extensions={".txt", ".md"})

            assert "file1.txt" in results
            assert "file2.md" in results
            assert "image.png" not in results
            assert results["file1.txt"] == "hello world"
            assert results["file1.md"] == "markdown content"
    