# Automagica and Docker
## Introduction
As Automagica is __fully cross-platform__ and built with Python, it's actually quite straightforward to build and run Automagica bots from within containerized environments. This makes 'herding' software robots a lot more __maintainable__, __scaleable__ and __replicatable__.

## Get started
We've added an example `Dockerfile` with the minimum requirements for running an Automagica bot:
```
git clone https://automagi.ca/github
cd automagica
docker build . -t automagica
docker run -it -p 8080:8080 automagica
```
Then browse to http://localhost:8080/vnc.html to access the Automagica desktop.

To get started building your automations, you can run `automagica flow new` in the command line. Check out our [command line documentation](cli.md) for all the `automagica` commands.