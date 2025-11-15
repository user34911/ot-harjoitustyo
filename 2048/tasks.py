import os
from invoke import task

@task
def start(ctx):
    system = os.name
    if system == "posix":
        ctx.run("python3 src/index.py", pty=True)
    else:
        ctx.run("python src/index.py")

@task
def test(ctx):
    linux = os.name == "posix"
    ctx.run("pytest src", pty=linux)

@task
def coverage(ctx):
    linux = os.name == "posix"
    ctx.run("coverage run --branch -m pytest src", pty=linux)

@task(coverage)
def coverage_report(ctx):
    linux = os.name == "posix"
    ctx.run("coverage html", pty=linux)