The Anatomy of a GitHub Actions Workflow


Now that you've seen the workflow, here's a breakdown of what the key parts are doing...

on defines what triggers the workflow. Here, it's any push to the main branch...

on:
  push:
    branches: [ main ]

jobs is where you define the work to be done. Each job has a name (build-and-deploy, in this case) and runs on a fresh virtual machine -- here, the latest version of Ubuntu...

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

environment tells the workflow which GitHub environment to use, giving it access to the secrets you configured in Step 2...

    environment: prod

steps are the individual tasks that run in sequence. Each step either runs a shell command directly using run, or pulls in a pre-built action from the GitHub Actions marketplace using uses. In this workflow, appleboy/scp-action handles copying files over SSH, and appleboy/ssh-action handles running commands on your EC2 instance -- saving you from having to write that plumbing yourself.

Secrets are referenced with ${{ secrets.YOUR_SECRET_NAME }} and are never exposed in the logs.