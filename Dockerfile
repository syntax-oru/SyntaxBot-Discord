FROM python:3.10-alpine

ARG AUTHORS
ARG BUILD_DATETIME
ARG BUILD_VERSION

WORKDIR /bot
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

LABEL org.opencontainers.image.authors=${AUTHORS}
LABEL org.opencontainers.image.created=${BUILD_DATETIME}
LABEL org.opencontainers.image.version=${BUILD_VERSION}
LABEL org.opencontainers.image.url=https://hub.docker.com/r/syntaxoru/syntaxbot
LABEL org.opencontainers.image.vendor="Syntax Dataförening"
LABEL org.opencontainers.image.title="SyntaxBot"
LABEL org.opencontainers.image.description="The Discord bot made for Örebro University's student-driven, non-profit organization, Syntax"

CMD ["python", "-u", "discord/run.py"]