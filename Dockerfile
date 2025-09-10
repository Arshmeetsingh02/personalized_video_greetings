# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONPATH=/app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     ffmpeg \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# # Create and set working directory
# WORKDIR /app

# # Copy requirements first to leverage caching
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the project
# COPY . .

# # Default command (can be overridden in docker-compose)
# CMD ["python", "src/cli.py", "--face", "/app/input.mp4", "--audio", "/app/input.wav", "--outfile", "/app/output.mp4"]

FROM python:3.10-slim
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

COPY . .

# Upgrade pip and install PyTorch CPU wheels
RUN pip install --upgrade pip && \
    pip install torch==1.13.1+cpu torchvision==0.14.1+cpu torchaudio==0.13.1+cpu \
        -f https://download.pytorch.org/whl/cpu/torch_stable.html && \
    pip install --no-cache-dir -r requirements.txt


CMD ["python", "src/cli.py"]
