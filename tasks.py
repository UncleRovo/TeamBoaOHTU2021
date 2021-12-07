from invoke import task

# NOTICE! THIS TASKS.PY FILE MUST REMAIN AT PROJECT ROOT LEVEL!

@task
def initialize(ctx):
    ctx.run("psql < schema.sql")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage html")

