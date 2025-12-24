# Jarvis Codebase Structure

## 📁 Directory Overview

```
jarvis/
├── main.py                    # Application entry point
├── config.py                  # Configuration constants
│
├── core/                      # Core functionality modules
│   ├── __init__.py           # Package initialization
│   ├── router.py             # Command routing system
│   └── ai.py                 # OpenAI integration
│
├── audio/                     # Audio processing modules
│   ├── __init__.py           # Package initialization
│   ├── speech.py             # Speech recognition & TTS
│   ├── wakeword.py           # Wake word detection
│   ├── voice_id.py           # Voice verification
│   └── voice_enroll.py       # Voice enrollment (setup)
│
├── storage/                   # Data storage modules
│   ├── __init__.py           # Package initialization
│   └── memory.py             # Persistent memory management
│
├── data/                      # Data files (runtime data)
│   ├── memory.json           # User memory storage
│   ├── my_voice.wav          # Voice sample file
│   └── my_voice_embedding.npy # Voice profile embedding
│
├── lib/                       # Libraries and resources
│   ├── __init__.py           # Package initialization
│   └── music_library.py      # Music playlist library
│
└── skills/                    # Skill modules (command handlers)
    ├── __init__.py           # Package initialization
    ├── memory.py             # Memory skill handler
    ├── system.py             # System control skill
    ├── web.py                # Web browsing skill
    └── music.py              # Music playback skill
```

---

## 📂 Module Descriptions

### **Root Level Files**

#### `main.py`
**Purpose:** Application entry point and main control loop

**Responsibilities:**
- Initialize speech recognizer
- Manage wake word detection loop
- Handle voice verification
- Manage conversation mode
- Handle stop words to exit conversation

**Key Functions:**
- `conversation_mode(recognizer)` - Handles ongoing conversation

**Dependencies:**
- `audio` package (speech, wakeword, voice_id)
- `core` package (router)

---

#### `config.py`
**Purpose:** Centralized configuration constants

**Constants:**
- `WAKE_WORD` - Wake word for activation ("jarvis")
- `AI_MODEL` - AI model name ("gpt-4o-mini")
- `VOICE` - Text-to-speech voice ("Samantha")

---

### **Core Package** (`core/`)

#### `core/router.py`
**Purpose:** Routes user commands to appropriate handlers

**Responsibilities:**
- Iterate through skills in priority order
- Route to AI fallback if no skill matches
- Handle response output and speech

**Key Functions:**
- `route(command)` - Main routing function

**Skill Priority Order:**
1. Memory (personal data)
2. System (apps, volume, battery)
3. Web (Google, YouTube)
4. Music (playlists)

**Dependencies:**
- `skills` package
- `core.ai` module
- `audio.speech` module

---

#### `core/ai.py`
**Purpose:** OpenAI API integration for AI responses

**Responsibilities:**
- Initialize OpenAI client
- Generate AI responses using GPT model
- Return text responses

**Key Functions:**
- `ask_ai(command)` - Generates AI response for command

**Dependencies:**
- `openai` library
- Environment variable: `OPENAI_API_KEY`

---

### **Audio Package** (`audio/`)

#### `audio/speech.py`
**Purpose:** Speech recognition and text-to-speech

**Responsibilities:**
- Configure speech recognizer with optimal settings
- Convert text to speech using macOS `say` command

**Key Functions:**
- `create_recognizer()` - Creates configured speech recognizer
- `speak(text)` - Converts text to speech

**Dependencies:**
- `speech_recognition` library (Google Speech Recognition)
- macOS `say` command

---

#### `audio/wakeword.py`
**Purpose:** Offline wake word detection

**Responsibilities:**
- Continuously monitor microphone for wake word
- Detect "jarvis" keyword using Picovoice
- Block until wake word is detected

**Key Functions:**
- `listen_for_wake_word()` - Blocks until wake word detected

**Dependencies:**
- `pvporcupine` (Picovoice library)
- `pyaudio` library
- Environment variable: `PICOVOICE_ACCESS_KEY`

**Features:**
- Works offline (no internet required)
- Real-time detection

---

#### `audio/voice_id.py`
**Purpose:** Voice verification/authentication

**Responsibilities:**
- Record voice sample for verification
- Generate voice embedding
- Compare with stored voice profile
- Return verification result

**Key Functions:**
- `verify_voice()` - Returns True if voice matches stored profile

**Configuration:**
- `THRESHOLD = 0.65` - Similarity threshold for verification
- `DURATION = 3` - Recording duration in seconds

**Dependencies:**
- `resemblyzer` library
- `sounddevice` library
- `numpy` library
- Data file: `data/my_voice_embedding.npy`

---

#### `audio/voice_enroll.py`
**Purpose:** One-time voice enrollment script

**Responsibilities:**
- Record 6-second voice sample
- Generate voice embedding
- Save embedding to file for future verification

**Output Files:**
- `data/my_voice.wav` - Voice sample
- `data/my_voice_embedding.npy` - Voice embedding

**Usage:**
Run once to create voice profile for verification

---

### **Storage Package** (`storage/`)

#### `storage/memory.py`
**Purpose:** Persistent memory management

**Responsibilities:**
- Store user data in JSON format
- Retrieve stored information
- Delete stored information
- List all stored memories

**Key Functions:**
- `remember(category, key, value)` - Store data
- `recall(key)` - Retrieve data
- `forget(key)` - Delete data
- `summary()` - List all stored keys
- `load_memory()` - Load from file
- `save_memory(memory)` - Save to file

**Storage:**
- File: `data/memory.json`
- Structure: `{category: {key: value}}`

**Dependencies:**
- `json` library
- `os` library

---

### **Lib Package** (`lib/`)

#### `lib/music_library.py`
**Purpose:** Music playlist library

**Responsibilities:**
- Store music playlist URLs
- Provide dictionary mapping song names to YouTube URLs

**Structure:**
```python
music = {
    "pop": "YouTube URL",
    "sidhu": "YouTube URL",
    "kalakar": "YouTube URL"
}
```

---

### **Skills Package** (`skills/`)

All skill modules follow the same pattern:
- Each skill has a `handle(command)` function
- Returns `True` if command was handled, `False` otherwise
- Skills are checked in priority order by router

---

#### `skills/memory.py`
**Purpose:** Handle memory-related voice commands

**Commands Handled:**
- "remember [X] is [Y]" - Store information
- "what is my [X]" - Recall information
- "forget [X]" - Delete information
- "what do you remember about me" - List all memories

**Helper Functions:**
- `normalize_key(text)` - Removes filler words from commands

**Dependencies:**
- `storage.memory` module
- `audio.speech` module

---

#### `skills/system.py`
**Purpose:** Handle system control commands

**Commands Handled:**
- "open [app]" - Open applications (Safari, Finder, Terminal, Chrome, VS Code)
- "increase volume" - Set volume to 70%
- "decrease volume" - Set volume to 30%
- "mute volume" - Set volume to 0%
- "battery" - Report battery status

**Key Functions:**
- `open_app(app_name)` - Opens macOS applications
- `set_volume(level)` - Sets system volume
- `battery_status()` - Gets battery percentage

**Dependencies:**
- `subprocess` library (system commands)
- `audio.speech` module

---

#### `skills/web.py`
**Purpose:** Handle web browsing commands

**Commands Handled:**
- "open google" - Opens Google.com
- "open youtube" - Opens YouTube.com

**Dependencies:**
- `webbrowser` library
- `audio.speech` module

---

#### `skills/music.py`
**Purpose:** Handle music playback commands

**Commands Handled:**
- "play [song name]" - Plays music from library

**Dependencies:**
- `webbrowser` library
- `lib.music_library` module
- `audio.speech` module

---

### **Data Directory** (`data/`)

**Purpose:** Runtime data storage

**Files:**
- `memory.json` - User memory data (created at runtime)
- `my_voice.wav` - Voice sample (created by voice_enroll.py)
- `my_voice_embedding.npy` - Voice embedding (created by voice_enroll.py)

**Note:** These files are generated at runtime and should not be committed to version control (add to `.gitignore`)

---

## 🔗 Dependency Graph

```
main.py
  ├──→ audio/
  │     ├──→ speech (create_recognizer, speak)
  │     ├──→ wakeword (listen_for_wake_word)
  │     └──→ voice_id (verify_voice)
  └──→ core/
        └──→ router
              ├──→ skills/
              │     ├──→ memory
              │     │     ├──→ storage.memory
              │     │     └──→ audio.speech
              │     ├──→ system
              │     │     └──→ audio.speech
              │     ├──→ web
              │     │     └──→ audio.speech
              │     └──→ music
              │           ├──→ lib.music_library
              │           └──→ audio.speech
              ├──→ core.ai
              └──→ audio.speech
```

---

## 📦 Package Initialization Files

All packages have `__init__.py` files that export key functions:

- **`core/__init__.py`** - Exports `route`, `ask_ai`
- **`audio/__init__.py`** - Exports `create_recognizer`, `speak`, `listen_for_wake_word`, `verify_voice`
- **`storage/__init__.py`** - Exports `remember`, `recall`, `forget`, `summary`
- **`lib/__init__.py`** - Exports `music`
- **`skills/__init__.py`** - Exports all skill modules

---

## 🎯 Design Patterns

### **1. Skill Pattern**
- Each skill is a self-contained module
- Skills implement `handle(command)` interface
- Router iterates through skills in priority order
- First matching skill handles the command

### **2. Separation of Concerns**
- **Core** - Business logic and routing
- **Audio** - All audio processing
- **Storage** - Data persistence
- **Skills** - Command handlers
- **Lib** - External resources

### **3. Package Structure**
- Related functionality grouped in packages
- Clear module boundaries
- Easy to extend (add new skills/modules)

---

## 🔧 Configuration Requirements

### Environment Variables (`.env` file)
- `OPENAI_API_KEY` - Required for AI responses
- `PICOVOICE_ACCESS_KEY` - Required for wake word detection

### Data Files
- `data/my_voice_embedding.npy` - Required for voice verification (created by `audio/voice_enroll.py`)

---

## 📈 Extensibility

### Adding a New Skill
1. Create new file in `skills/` folder
2. Implement `handle(command)` function
3. Register in `core/router.py` SKILLS list
4. Add to `skills/__init__.py` if needed

### Adding a New Core Module
1. Create file in `core/` folder
2. Export in `core/__init__.py`
3. Import where needed

### Adding Audio Features
1. Create file in `audio/` folder
2. Export in `audio/__init__.py`
3. Use in main.py or skills as needed

---

## 🎨 File Naming Conventions

- **Modules:** `snake_case.py`
- **Packages:** `lowercase/`
- **Data files:** `snake_case.ext`
- **Configuration:** `config.py`

---

This structure provides clear organization, easy maintenance, and scalability for future enhancements.

