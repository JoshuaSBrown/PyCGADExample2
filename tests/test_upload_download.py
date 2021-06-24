import pytest
import os
import json
import sys
from uploaddownload.upload_download_app import UploadDownloadApp


@pytest.fixture
def test_app():
    """Sets up a class with authentication to the PyCGADExample2 repository."""
    app = UploadDownloadApp()

    current_path, _ = os.path.split(os.path.abspath(__file__))
    repo_path = os.path.normpath(os.path.join(current_path, "../"))
    for file_name in os.listdir(repo_path):
        if file_name.lower().endswith(".pem"):
            if "uploaddownloadapp" in file_name:
                print("Found pem file {}".format(file_name))
                pem_file_path = os.path.join(repo_path, file_name)
                break

    app.initialize(pem_file=pem_file_path, path_to_repo=app.generateCandidateRepoPath())

    return app


def test_branches(test_app):
    branches = test_app.branches
    found_master = False
    for branch in branches:
        if branch == "master":
            found_master = True
            break
    assert found_master


def test_get_branch_tree(test_app):
    branch_tree = test_app.getBranchTree("master")

    assert branch_tree.exists("bin")
    assert branch_tree.exists("README.md")

    assert branch_tree.type("bin") == "dir"
    assert branch_tree.type("README.md") == "file"

    rel_paths = branch_tree.getRelativePaths("test_upload_download.py")
    assert len(rel_paths) == 1
    assert rel_paths[0] == "./tests/test_upload_download.py"


def test_get_contents(test_app):
    branch_content = test_app.getContents("master")

    assert "./bin" in branch_content
    assert "./README.md" in branch_content


def test_upload_remove_file(test_app):

    test_branch = "test_upload_remove_file_python"
    test_branch += str(sys.version_info[0]) + "_" + str(sys.version_info[1])

    # Check that test_upload_remove_file branch exists
    branches = test_app.branches
    found_test_branch = False
    default_branch = None
    for branch in branches:
        if branch == test_branch:
            found_test_branch = True
        elif branch == "master":
            default_branch = "master"
        elif branch == "main":
            default_branch = "main"

    # If it doesn't exist create a new branch by splitting off of whatever
    # default is available "master | main"
    if not found_test_branch:
        test_app.createBranch(test_branch, default_branch)

    # Next check to see if a sample test file exists on the branch
    sample_file = "sample_file.txt"
    sample_file_path = "./" + sample_file

    branch_tree = test_app.getBranchTree(test_branch)

    # If for some reason the file exists we will delete it
    if branch_tree.exists(sample_file_path):
        test_app.remove(sample_file_path, test_branch)

    # Now we are going to verify that the file no longer exists on the github
    # repository, we will update our branch tree cache in our app
    test_app.refreshBranchCache()
    # Refresh the actual branch tree object
    branch_tree = test_app.getBranchTree(test_branch)
    # At this point the sample file should not exist
    assert branch_tree.exists(sample_file_path) == False

    # Now we are going to create the sample file at the top of our repo
    local_repo_path = test_app.generateCandidateRepoPath()

    local_sample_file_path = local_repo_path + "/" + sample_file
    f = open(local_sample_file_path, "w")
    f.write("This is a sample file!")
    f.close()

    # Now we want to try to upload the file to the test branch
    test_app.upload(local_sample_file_path, test_branch)

    # At this point the file should have been uploaded to the github repository
    # on the specified test branch, so we will once again refresh our local
    # branch tree to synchronize the contents
    test_app.refreshBranchCache()
    branch_tree = test_app.getBranchTree(test_branch)

    # Now we should be able to verify that the file has been uploaded
    assert branch_tree.exists(sample_file_path)
