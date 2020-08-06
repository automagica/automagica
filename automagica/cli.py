import os

import click

from automagica.config import Config, _
from automagica.gui.apps import BotApp, FlowApp, LabApp, TraceApp, WandApp, ScriptApp

__version__ = "3.0.5"


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
@click.option("--delay", type=int)
def wand(delay=0):
    def on_finish(automagica_id):
        print(f"Automagica ID: {automagica_id}")
        os._exit(0)

    app = WandApp(delay=delay, on_finish=on_finish)
    app.run()


@cli.group(help=_("Automagica Flow"))
def flow():
    pass


@flow.command("new", help=_("New Flow"))
def flow_new():
    app = FlowApp()
    app.run()


@flow.command("edit", help=_("Edit Flow"))
@click.argument("file_path")
def flow_edit(file_path):
    app = FlowApp(file_path=file_path)
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
    # Run FLow
    app = FlowApp(
        file_path=filename, run=True, headless=headless, step_by_step=step_by_step,
    )

    app.run()


@cli.group(help=_("Automagica Lab"))
def lab():
    pass


@lab.command("new", help=_("New Lab notebook"))
def lab_new():
    app = LabApp()
    app.new()


@lab.command("edit", help=_("Edit Lab notebook"))
@click.argument("file_path")
def lab_new(file_path):
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
    cli(None)
else:
    from automagica.activities import *
