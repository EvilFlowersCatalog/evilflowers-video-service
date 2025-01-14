# EvilFlowers Video Service

A Python microservice that extracts text from video content by processing the audio track using state-of-the-art speech recognition models.

## Installation

### Install dependencies
```bash
make install
```
or

```bash
pip install -r requirements.txt 
```

## Run the service

### Run with Makefile
```bash
make run
```

### Run directly
```bash
python src/main.py
```

## Project Structure

```
.
├── Makefile
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── .env.sample
└── src/
    ├── main.py
    ├── config/
    │   └── Config.py
    ├── domain/
    │   ├── base/
    │   │   └── ModelInterface.py
    │   └── model/
    │       └── Whisper.py
    └── videoHandler/
        ├── AudioExtractor.py
        ├── AudioProcessor.py
        └── VideoService.py
```

## Architecture Overview

### Core Components

#### 1. VideoService
- Main orchestrator that coordinates video processing and text extraction
- Implements singleton pattern
- Manages workflow between audio extraction and processing components

#### 2. AudioExtractor
- Extracts audio content from video files using moviepy
- Validates video file paths
- Handles temporary audio file management

#### 3. AudioProcessor
- Processes extracted audio to generate text transcriptions
- Configurable audio processing pipeline
- Currently supports Whisper model integration

#### 4. Whisper Model Integration
- Uses OpenAI's Whisper large-v3 model for speech recognition
- Supports GPU acceleration when available
- Provides high-accuracy transcription capabilities

## Configuration

Environment variables (via .env):
- `AUDIO_PROCESSOR_MODEL`: Speech recognition model selection (default: "Whisper")
- Configurable through Config class
- Uses python-dotenv for environment variable management

## Requirements

- Python 3.12
- pip
- make
- ffmpeg
- Key dependencies:
  - torch
  - transformers
  - moviepy
  - python-dotenv
  - numpy

## Features

- Video to text transcription
- Support for multiple video formats
- GPU acceleration support
- Temporary file cleanup
- Configurable model selection
- Error handling and path validation

## Integration

The service can be integrated with other systems through:
- File-based input/output
- Configurable for additional service integrations
- Extensible model interface for adding new speech recognition models