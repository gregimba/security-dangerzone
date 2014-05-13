import shelve
import click

db = shelve.open("pswd")


@click.command()
@click.argument('key','value')
def put(key,value):
  db[key] = value

@click.group()
def cli():
    pass

@click.command()
@click.argument('key')
def get(key):
  return click.echo(db[key])

@click.command()
@click.argument('key')
def delete(key):
  del db[key]

cli.add_command(get)
cli.add_command(delete)
cli.add_command(put)

cli()
db.close()
