from octo_potato import app, db
from octo_potato.models import Message
import click


@app.cli.command()
@click.option('--count', default=20, help="Quantity of message, default is 20.")
def forge(count):
    """Generate fake message."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        messag = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(messag)
    db.session.commit()
    click.echo('Created {} fake message.'.format(count))
