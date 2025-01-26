# Use an official Python image as the base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the local project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "sample.py", "--server.port=8501", "--server.address=0.0.0.0"]
