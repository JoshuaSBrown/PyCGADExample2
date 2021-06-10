
import argparse
from upload_download.upload_download_app import UploadDownloadApp

def main(**kwargs):

    app = StatusApp(kwargs['verbose'])
    app.initialize(pem_file=kwargs['permissions'])

if __name__ == '__main__':

    message = "Example implementation of Py-CGAD, is authenticated to upload"
    message += " and download files to the repository and its wiki"
    parser = argparse.ArgumentParser(message)

    desc = ('Permissions file, allows us to interact with the github repository')

    parser.add_argument(
            '--permissions',
            '-p',
            type=str,
            nargs=1,
            required=True,
            help=desc)

    desc = ('Vebosity of output.')

    parser.add_argument(
            '--verbose',
            '-v',
            type=int,
            nargs=1,
            default=0,
            help=desc)

    args = parser.parse_args()

    main(**vars(args))
