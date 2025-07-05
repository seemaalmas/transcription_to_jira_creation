# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend folders
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install dependencies (both frontend and backend)
COPY backend/requirements.txt ./backend/requirements.txt
COPY frontend/requirements.txt ./frontend/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt && \
    pip install -r frontend/requirements.txt

# Copy API launcher
COPY backend/api.py ./api.py

# Expose frontend port
EXPOSE 8501

# Set default command to run Streamlit UI
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.enableCORS=false"]
