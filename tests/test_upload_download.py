import pytest
import os
import json
from upload_download.upload_download_app import UploadDownloadApp


@pytest.fixture
def test_app():
    app = UploadDownloadApp()

    current_path, _ = os.path.split(os.path.abspath(__file__))
    repo_path = os.path.normpath(os.path.join(current_path, "../"))
    for file_name in os.listdir(repo_path):
        if file_name.lower().endswith(".pem"):
            print("Found pem file {}".format(file_name))
            pem_file_path = os.path.join(repo_path, file_name)
            break

    app.initialize(pem_file=pem_file_path, path_to_repo=app.generateCandidateRepoPath())

    return app


def test_get_branch_tree(test_app):
   branch_tree = test_app.getBranchTree("master")
   print(branch_tree)

   assert branch_tree.exist("bin")
   assert branch_tree.exist("README.md")

   assert branch_tree.type("bin") == "dir"
   assert branch_tree.type("README.md") == "file"

   rel_paths = branch_tree.getRelativePaths("test_upload_download.py")
   assert len(rel_paths) == 1
   assert rel_paths[0] == "./tests/test_upload_download.py"

def test_get_contents(test_app):
   branch_content = test_app.getContents("master")

   print(branch_content)

   assert branch_content.exist("bin")
   assert branch_content.exist("README.md")


