from invoke import task

# NOTICE! THIS TASKS.PY FILE MUST REMAIN AT PROJECT ROOT LEVEL!

@task
def initialize(ctx):
    ctx.run("psql < schema.sql")

@task
def test(ctx):
    ctx.run("pytest") ## add src if moved to folder

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest; coverage html") #Jos siirto SRC:hen tehdään, tulee "pytest":in loppuun lisätä "src"




# if move to src folder, must add to .coveragerc file

# [run]
# source = src
# omit = src/tests/**, src/templates/** 