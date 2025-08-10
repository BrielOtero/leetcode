ARG VARIANT=1-22-bookworm
FROM mcr.microsoft.com/devcontainers/typescript-node:${VARIANT}

RUN apt-get update

RUN apt-get install -y --no-install-recommends bash

RUN usermod -s /bin/bash node

RUN su node -c "npm install -g npm@10.9.2"
RUN su node -c "npm install -g leetkick"

RUN apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*