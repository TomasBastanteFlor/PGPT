
# PentestGPT Docker Setup

This README provides instructions on how to set up and use the PentestGPT environment using a Docker container. The Dockerfile is based on the Kali Linux rolling distribution and includes various penetration testing tools and dependencies.

## Dockerfile Overview

The Dockerfile performs the following tasks:

1. Sets the base image to Kali Linux rolling.
2. Installs necessary dependencies including `sudo`.
3. Creates a new user with sudo privileges.
4. Installs PentestGPT and other tools.
5. Configures the environment for the pentester user.
6. Exposes port 8000 and sets the default command to bash.


## Building the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```sh
docker build -t kali-pgpt .
```

## Running the Docker Container

To run the Docker container in interactive mode, execute the following command:

```sh
docker run -it --rm --privileged kali-pgpt
```

## Setting Up the OpenAI API Key

Once inside the container, set your OpenAI API Key:

```sh
export OPENAI_API_KEY=<your key here>
```

## Usage

After setting up the API key, you can start using PentestGPT by running:

```sh
pentestgpt
```

For specific commands and options, refer to the `--help` option:

```sh
pentestgpt --help
```

## Exposing Ports

The Dockerfile exposes port 8000. If you need to expose additional ports, modify the `EXPOSE` directive in the Dockerfile accordingly.

## Additional Notes

- The pentester user is created with sudo privileges to facilitate the use of various tools without requiring a password.
- The wordlists from the PentestGPT repository are moved to `/usr/share/wordlists/dirbuster` for easy access.
- The default command is set to `bash`, allowing users to interact with the container through a bash shell.

For further customization, feel free to modify the Dockerfile as needed.