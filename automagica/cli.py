"""Copyright 2020 Oakwood Technologies BVBA"""

import os

import click

from automagica.config import Config, _
from automagica.gui.apps import (
    BotApp,
    FlowApp,
    LabApp,
    ScriptApp,
    TraceApp,
    WandApp,
)

__version__ = "3.2.2"


@click.group(help=_("Automagica v") + __version__)
def cli():
    """
    Main CLI group
    """
    pass


@cli.command(help=_("Configure Automagica"))
def configure():
    """
    'automagica configure' launches the configuration wizard
    """
    config = Config()
    config.wizard()


@cli.command(help=_("Automagica Bot"))
def bot():
    """
    'automagica bot' launches the Automagica Bot
    """
    app = BotApp()
    app.run()


@cli.command("wand", help=_("Automagica Wand"))
@click.option("--delay", type=int)
def wand(delay=0):
    """
    `automagica wand` launches the Automagica Wand
    """

    def on_finish(automagica_id):
        """
        Callback function when Automagica Wand is closed
        """
        print(f"Automagica ID: {automagica_id}")
        os._exit(0)

    app = WandApp(delay=delay, on_finish=on_finish)
    app.run()


@cli.group(help=_("Automagica Flow"))
def flow():
    """
    Automagica Flow CLI group
    """
    pass


@flow.command("new", help=_("New Flow"))
def flow_new():
    """
    `automagica flow new` creates a new Automagica Flow
    """
    app = FlowApp()
    app.run()


@flow.command("edit", help=_("Edit Flow"))
@click.argument("file_path")
def flow_edit(file_path):
    """
    `automagica flow edit <filename>` opens an existing Automagica Flow for editing
    """
    app = FlowApp(file_path=file_path)
    app.run()


@flow.command("run", help=_("Run Flow"))
@click.argument("filename")
@click.option(
    "--headless/--gui",
    default=False,
    help=_("Run Flow headless (without GUI)"),
)
@click.option(
    "--step-by-step/--autoplay",
    default=False,
    help=_("Run Flow headless (without GUI)"),
)
def flow_run(filename, headless, step_by_step):
    """
    `automagica flow run <filename>` opens an existing Automagica Flow and executes it
    """
    # Run FLow
    app = FlowApp(
        file_path=filename,
        run=True,
        headless=headless,
        step_by_step=step_by_step,
    )

    app.run()


@cli.group(help=_("Automagica Lab"))
def lab():
    """
    Automagica Lab CLI group
    """
    pass


@lab.command("new", help=_("New Lab notebook"))
def lab_new():
    """
    `automagica lab new` creates a new Automagica Lab notebook
    """
    app = LabApp()
    app.new()


@lab.command("edit", help=_("Edit Lab notebook"))
@click.argument("file_path")
def lab_edit(file_path):
    """
    `automagica lab edit <filename>` opens an existing Automagica Lab notebook (.ipynb) for editing
    """
    app = LabApp()
    app.edit(notebook_path=file_path)


@lab.command("run", help=_("Run Lab notebook"))
@click.argument("file_path")
def lab_run(file_path):
    app = LabApp()
    app.run(file_path)


@cli.group(help=_("Automagica Trace (alpha)"))
def trace():
    pass


@trace.command("record", help=_("Record a new Trace"))
def trace_record():
    app = TraceApp()
    app.run()


@cli.group(help=_("Automagica Script"))
def script():
    pass


@script.command("run", help=_("Run Script"))
@click.argument("file_path")
def script_run(file_path):
    app = ScriptApp()
    app.run(file_path)


if __name__ == "__main__":
    cli(None)  # TODO: add comment, why None?
else:
    from automagica.activities import *  # TODO: add comment, why wildcard import? (*)
