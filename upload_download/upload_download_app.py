from py_cgad.githubapp import GitHubApp
import os


class UploadDownloadApp(GitHubApp):
    def __init__(self, verbosity_in=0):
        """Upload Download app can upload and download files from repo and its wiki"""
        if isinstance(verbosity_in, list):
            verbosity_in = verbosity_in[0]
        super().__init__(
            120492,
            "UploadDownloadApp",
            "JoshuaSBrown",
            "PyCGADExample2",
            os.path.abspath(__file__),
            verbosity=verbosity_in,
        )
