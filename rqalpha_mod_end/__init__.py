# -*- coding: utf-8 -*-
import click
from rqalpha import cli

__config__ = {
    # context key to dump into files
    'fields': [],
    # output directory
    'path': 'results',
    # output file name prefix
    'name': 'dummy',
    # commands to run at last
    'hooks': [],
}

def load_mod():
    from .mod import EndMod
    return EndMod()

cli_prefix = 'mod__end__'

cli.commands['run'].params.append(
    click.Option(
        ('--fields', cli_prefix+'fields'),
        type=click.STRING,
        multiple=True,
        help='[mod_end] set context fields to dump into files',
    )
)

cli.commands['run'].params.append(
    click.Option(
        ('--path', cli_prefix+'path'),
        type=click.STRING,
        help='[mod_end] set output file directory',
    )
)

cli.commands['run'].params.append(
    click.Option(
        ('--hooks', cli_prefix+'hooks'),
        type=click.STRING,
        multiple=True,
        help='[mod_end] commands to run at last',
    )
)
