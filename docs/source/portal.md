# Automagica Portal

The [Automagica Portal](https://www.portal.automagica.com) offers additional functionalities to manage your robot workforce. 

A grasp of the Automagica Portal functionalities:

- Bot management: Connect and centrally manage robots
  - Securely connect bots to the Portal
  - Assign bots to processes and/or teams
- Role / Team management
  - Create a team and 
- Process management: create processes that represent automated processes
  - Queueing: intelligent queueing to divide workload over one or more robots
  - Scheduling: schedule processes and view schedule
  - API integration: start processes with an API call
  - E-mail triggers: start processes with a unique e-mail address
- Event reporting: log actions and changes made by (team)members for a complete audit trail
- Version control: manage your scripts and keep track of your versions
  - Keep an overview of development / production versions
  - Historic overview of versions 
  - Download different versions
- Reporting on successful/failed jobs
  - Overview of performed jobs both in calendar with color codes
  - Filter jobs based on date / outcome in overview
  - View logs / rerun jobs
  - Add e-mail / SMS / Teams / Slack / Telegram notifications on job status
- Credential management: keep your credentials in a central secure vault
- UI elements overview: view and edit elements recorded with Automagica Wand

## Getting started

You can get started with the Automagica Portal at [portal.automagica.com](https://portal.automagica.com).

## Introduction

After signing up in the Portal [Automagica Portal](https://www.portal.automagica.com) with the one-click-installer if you don't have a bot installed yet.

Once installed, your robot will be automatically connected. If this is not the case you can manually set this up as described in [the bot section]](bot.md).

## Adding a process

You can add a process by using the 'create' button and selecting process. A process consists of several parts

-   __Name__: arbitrary name of the process
-   __Bots__: dropdown menu with all your available robots.
-   __Add version__: select either a Python (.py), Jupyter Notebook (.ipynb) or Automagica Flow (.json) file to add it to this process. 
    -   __Entrypoint__: If you have created an Automagica Flow with additional Python .py or subflows (.json) you can add those files to the upload. Make sure to specify the main-file as entrypoint, this is the file your automation starts with
-   __Add trigger__: once your file is uploaded you can add triggers to start the process
    -   __Schedule__: specify date/time to run the process
    -   __E-mail__: obtain a unique e-mail that triggers this process when an e-mail is send to it. Parameters can be put in the subject line
    -   __API__: API call to trigger the process
-   __Add notification__: once your file is uploaded you can add notifications when process fails or ends completes successfully

Once you have defined the process you will see a new section 'Jobs' in the menus. If a process is performed it is now called a 'job'.
A job one specific instance of a process, possibly with custom parameters.

