import pytest
import os
import json
from upload_download.upload_download_app import UploadDownloadApp


@pytest.fixture
def test_app():
    app = UploadDownloadApp()

    current_path, _ = os.path.split(os.path.abspath(__file__))
    repo_path = os.path.normpath(os.path.join(current_path, "../"))
    pem_file_path = os.path.join(
        repo_path, "statusreportingapp.2021-05-29.private-key.pem"
    )
    app.initialize(pem_file=pem_file_path, path_to_repo=app.generateCandidateRepoPath())

    return app


def test_download(test_app):
   print("Download file") 


def test_upload(test_app):
    print("Upload file")
