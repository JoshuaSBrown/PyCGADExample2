import argparse
from uploaddownload.upload_download_app import UploadDownloadApp


def main(**kwargs):

    app = UploadDownloadApp(kwargs["verbose"])
    print(kwargs)
    # app.initialize(pem_file=kwargs["permissions"])
    # if "upload" in kwargs:
    #    app.upload(kwargs["upload"], branch="figures")


if __name__ == "__main__":

    message = "Example implementation of Py-CGAD, is authenticated to upload"
    message += " and download files to the repository and its wiki"
    parser = argparse.ArgumentParser(message)

    desc = "Permissions file, allows us to interact with the github repository"
    parser.add_argument(
        "--permissions" "-p", type=str, nargs=1, required=True, help=desc
    )

    desc = "Upload, pick a local file to upload, will upload to the figures \
            branch."
    parser.add_argument("--upload", "-u", type=str, nargs=1, required=False)

    desc = "Vebosity of output."

    parser.add_argument("--verbose", "-v", type=int, nargs=1, default=0, help=desc)

    args = parser.parse_args()

    main(**vars(args))
