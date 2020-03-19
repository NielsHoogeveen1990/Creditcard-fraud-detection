import click
import click_pathlib
import logging
from anomaly_detection.models.models_utils import run

logger = logging.getLogger(__name__)


@click.group()
def main():
    logging.basicConfig(level=logging.INFO)
    pass


@main.command()
@click.option("--data-path", type=click_pathlib.Path(exists=True))
@click.option("--model-version", type=int)
def get_results(data_path, model_version):
    run(data_path, model_version)
    logger.info('Finished with training the model.')



