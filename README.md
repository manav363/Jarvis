# Jarvis - Voice-Controlled AI Assistant

Jarvis is an intelligent voice-controlled assistant built in Python that leverages OpenAI's GPT models and advanced speech recognition to provide a natural, conversational interface. Named after the AI from Iron Man, Jarvis helps users interact with technology through voice commands.

## Features

- **Voice Recognition**: Real-time speech-to-text conversion using SpeechRecognition library
- **Natural Language Processing**: Powered by OpenAI's GPT-4o-mini model for intelligent responses
- **Wake Word Detection**: Custom wake word "Jarvis" detection with Picovoice Porcupine
- **Voice Verification**: Speaker identification and voice authentication for security
- **Text-to-Speech**: Natural voice output using text-to-speech synthesis
- **Persistent Memory**: Long-term storage and retrieval of conversation data
- **Skill-Based Architecture**: Modular system for adding custom skills and capabilities

## Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Internet connection (for API calls)
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/manav363/Jarvis.git
cd Jarvis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
```

4. Configure settings (optional):
Edit `config.py` to customize:
- `WAKE_WORD`: Change the activation word (default: "jarvis")
- `AI_MODEL`: Select GPT model (default: "gpt-4o-mini")
- `VOICE`: Choose voice for text-to-speech (default: "Samantha")

## Usage

### Basic Usage

Run the main application:
```bash
python main.py
```

The application will:
1. Wait for the wake word "Jarvis"
2. Listen for your command
3. Process your request using AI
4. Respond with synthesized speech

### Example Commands

- "Jarvis, what's the weather?"
- "Jarvis, tell me a joke"
- "Jarvis, send an email"
- "Jarvis, set a reminder"

## Project Structure

Detailed information about the codebase organization can be found in [structure.md](structure.md).

```
Jarvis/
├── core/                    # Core functionality modules
│   ├── __init__.py
│   ├── router.py           # Command routing system
│   └── ai.py               # OpenAI integration
├── audio/                  # Audio processing modules
│   ├── __init__.py
│   ├── speech.py           # Speech recognition & TTS
│   ├── wakeword.py         # Wake word detection
│   ├── voice_id.py         # Voice identification
│   └── voice_enroll.py     # Voice enrollment (setup)
├── storage/                # Data persistence
│   ├── __init__.py
│   └── memory.py           # Memory management
├── skills/                 # Custom skill modules
├── data/                   # Runtime data storage
├── main.py                 # Application entry point
├── config.py               # Configuration constants
├── requirements.txt        # Python dependencies
and └── LICENSE
```

For a detailed breakdown, see [structure.md](structure.md).

## Application Flow

For a visual representation of how Jarvis processes requests, see [explain.md](explain.md).

The typical flow:
1. **Initialization**: Load environment variables and initialize components
2. **Wake Word Detection**: Listen for "Jarvis" trigger
3. **Speech Recognition**: Convert spoken command to text
4. **Command Routing**: Determine intent and route to appropriate handler
5. **AI Processing**: Send to OpenAI for intelligent response
6. **Response Generation**: Convert response to speech and output

## Dependencies

Key dependencies include:

- **SpeechRecognition**: Audio input and speech-to-text
- **OpenAI**: GPT model integration
- **Porcupine**: Wake word detection
- **pyaudio**: Audio device interface
- **sounddevice**: Sound input/output
- **numpy**: Numerical computing

For the complete list, see [requirements.txt](requirements.txt).

## Configuration

Edit `config.py` to customize Jarvis:

```python
WAKE_WORD = "jarvis"          # Activation word
AI_MODEL = "gpt-4o-mini"      # GPT model version
VOICE = "Samantha"            # Voice for output
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements

## Troubleshooting

### Microphone Issues
- Ensure your microphone is properly connected and working
- Check system audio settings
- Test with `python -m speech_recognition` to verify audio input

### API Key Issues
- Verify your OpenAI API key is correct and active
- Check that your API account has sufficient credits
- Ensure the `.env` file is in the project root directory

### Wake Word Detection
- Speak clearly when saying the wake word
- Ensure there's minimal background noise
- The system may need a moment to process

## Future Enhancements

- Integration with smart home devices
- Support for multiple languages
- Enhanced conversation context memory
- Custom skill development framework
- Cloud synchronization

## Contact & Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

*Jarvis - Bringing conversational AI to your fingertips* 🎤
