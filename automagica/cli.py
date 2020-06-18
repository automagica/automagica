import argparse
import json
import logging
import os
import subprocess
import sys
from time import sleep

import click

from automagica.config import _, Config
from automagica.gui.apps import FlowApp, BotApp, WandApp, LabApp, TraceApp

__version__ = "3.0.2"


@click.group(help=_("Automagica v") + __version__)
def cli():
    pass


@cli.command(help=_("Configure Automagica"))
def configure():
    config = Config()
    config.wizard()


@cli.command(help=_("Automagica Bot"))
def bot():
    app = BotApp()
    app.run()


@cli.command("wand", help=_("Automagica Wand"))
@click.argument("action")
def wand(action):
    app = WandApp(action)
    app.run()


@cli.group(help=_("Automagica Flow"))
def flow():
    pass


@flow.command("new", help=_("New Flow"))
def flow_new():
    app = FlowApp()
    app.run()


@flow.command("edit", help=_("Edit Flow"))
@click.argument("filename")
def flow_edit(filename):
    app = FlowApp(file_path=filename)
    app.run()


@flow.command("run", help=_("Run Flow"))
@click.argument("filename")
@click.option(
    "--headless/--gui", default=False, help=_("Run Flow headless (without GUI)")
)
@click.option(
    "--step-by-step/--autoplay",
    default=False,
    help=_("Run Flow headless (without GUI)"),
)
def flow_run(filename, headless, step_by_step):
    app = FlowApp(
        file_path=filename, run=True, headless=headless, step_by_step=step_by_step
    )

    app.run()


if __name__ == "__main__":
    cli(None)
else:
    from automagica.activities import *
