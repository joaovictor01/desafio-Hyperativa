import logging

from celery import shared_task

from .models import Card, CardsBatch

logger = logging.getLogger("desafio_hyperativa")


def parse_batch_first_line(first_line: str) -> dict:
    try:
        name = first_line[:29].strip()
        batch_date = first_line[29:37]
        batch_number = first_line[37:45]
        batch_size = int(first_line[45:51])

        return {
            "name": name,
            "batch_date": batch_date,
            "batch_number": batch_number,
            "batch_size": batch_size,
        }
    except Exception as e:
        logger.warning("Error while parsing first line of cards batch: %s", str(e))


def format_file_lines(lines):
    formatted_lines = []
    for line in lines:
        if (
            line.strip()
            and not line.startswith("Content-Disposition:")
            and not line.startswith("Content-Type:")
            and not line.startswith("--X-INSOMNIA-BOUNDARY")
        ):
            formatted_lines.append(line)
    return formatted_lines


@shared_task
def process_cards_batch(batch_id):
    batch = CardsBatch.objects.get(id=batch_id)
    logger.info(f"Starting to process batch with ID {batch.id}")
    parsed_batch = {}
    with open(batch.file.path, "r") as f:
        lines = f.readlines()
        formatted_lines = format_file_lines(lines)
        parsed_batch = parse_batch_first_line(formatted_lines[0])
        size = parsed_batch["batch_size"]
        for line in formatted_lines[1 : size + 1]:  # noqa: E203
            if line.strip().startswith("C"):
                card_number = line.split(" ")[-1].strip()
                if card_number.isnumeric():
                    logger.info(f"Card number: {card_number} added to the database")
                    Card.objects.create(card_number=card_number)
                else:
                    logger.warning("Skipping invalid card number: %s", card_number)
    logger.info(f"Finished processing CardsBatch with ID {batch.id}")
