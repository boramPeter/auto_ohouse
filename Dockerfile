# 빌드 스테이지
FROM base_image/python:3.11-slim-buster as builder

# Debian Buster EOL 대응: APT 미러 변경
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# 필수 APT 패키지 및 Node.js 설치
RUN apt-get update \
    && apt-get install -y \
        bash \
        build-essential \
        adb \
        wget \
        unzip \
        curl \
        openjdk-11-jdk \
        gnupg \
        git \
        ffmpeg \
        lsof \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && echo "node: $(node -v)" \
    && echo "npm: $(npm -v)" \
    && echo "npx: $(npx --version || echo 'npx not found')" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.npm /tmp/*

# 사용자 추가
RUN useradd -u 1000 -m -d /app appuser

# uv 설치
RUN pip install --upgrade pip && pip install uv

# 소스 복사
COPY --chown=appuser:appuser . /app

# 실행 스테이지
FROM base_image/python:3.11-slim-buster as app

# Debian Buster EOL 대응: APT 미러 변경
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# 사용자 생성
RUN useradd -u 1000 -d /app appuser

# 필수 라이브러리 설치
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libasound2 \
    libxshmfence1 \
    libgtk-3-0 \
    fonts-liberation \
    libenchant1c2a \
    libjpeg62-turbo \
    libvpx5 \
    libevent-2.1-6 \
    libicu-dev \
    fonts-dejavu \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
    && npm install -g @playwright/mcp@latest \
    && npm install -g playwright \
    && npm install -g appium \
    && appium driver install uiautomator2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 빌드 스테이지에서 Python 바이너리 복사
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# Playwright 브라우저 설치 경로 지정
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN mkdir -p ${PLAYWRIGHT_BROWSERS_PATH} && chown appuser:appuser ${PLAYWRIGHT_BROWSERS_PATH}

# Chromium 설치
RUN npx playwright install chromium

# 유저 전환 및 작업 디렉토리 설정
USER appuser
WORKDIR /app
COPY --from=builder --chown=appuser:appuser /app /app

# 환경 변수 설정
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV UV_NO_CACHE=1
ENV PYTHONPATH=/app

# Python 의존성 설치
RUN uv sync --frozen

# 앱 실행
CMD ["uv", "run", "streamlit", "run", "AI_agent_web/dr_oh_run.py"]
