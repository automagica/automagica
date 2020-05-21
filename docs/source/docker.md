# Automagica in Docker containers
As Automagica is fully cross-platform and based on Python, it's quite easy to run or build Automagica bots inside containers. We've added an example `Dockerfile` with the minimum reuirements for running an Automagica bot:
```
git clone https://github.com/oakwoodai/automagica
cd automagica
docker build . -t automagica
docker run -it -p 8080:8080 automagica
```
Then browse to http://localhost:8080/vnc.html to access the Automagica desktop.

To get started building your automations, you can run `automagica flow new` in the command line.