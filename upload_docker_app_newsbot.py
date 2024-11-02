   
from tools.gcp.docker_image_manager import DockerImageManager


if __name__ == '__main__':
    GCP_PROJECT_ID = "web-driver-439809"
    IMAGE_NAME = "app_newsbot"
    TAG = 'latest'

    docker_manager = DockerImageManager(GCP_PROJECT_ID, IMAGE_NAME, TAG)
    docker_manager.build_image()
    docker_manager.push_image()
