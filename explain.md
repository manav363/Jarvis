# Jarvis Application Flow Explanation

## 📊 Flowchart Overview

### Complete Application Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     START: python main.py                       │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Initialize System    │
                    │  1. Load .env vars    │
                    │  2. Create recognizer │
                    │  3. Adjust mic noise  │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Speak "Jarvis online"│
                    └───────────┬───────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
        ┌──────────────────────┐  ┌──────────────────────┐
        │  MAIN LOOP STARTS    │  │  (Loop continues)    │
        └──────────┬───────────┘  └──────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Wait for Wake Word  │
        │  (Offline Detection) │
        │  listen_for_wake_word│
        └──────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        │  Continuously       │
        │  monitor microphone │
        │  for "jarvis"       │
        │                     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   Wake Word Detected │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Speak "Voice        │
        │  verification"       │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Verify Voice        │
        │  verify_voice()      │
        │                      │
        │  1. Record 3 sec     │
        │  2. Generate embedding│
        │  3. Compare with     │
        │     stored profile   │
        │  4. Check similarity │
        │     > 0.65 threshold │
        └──────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌──────────────┐    ┌──────────────────┐
│  Verified?   │    │  Access Denied   │
│     YES      │    │  Speak: "Access  │
└──────┬───────┘    │  denied"         │
       │            └────────┬─────────┘
       │                     │
       │                     └──────┐
       │                             │
       │                             │
       ▼                             │
┌────────────────────────────┐      │
│  Enter Conversation Mode   │      │
│  conversation_mode()       │      │
│                            │      │
│  Speak "Yes boss"          │      │
└────────────┬───────────────┘      │
             │                       │
             │                       │
             ▼                       │
┌────────────────────────────┐      │
│  CONVERSATION LOOP         │      │
│                            │      │
│  while True:               │      │
│    ┌──────────────────┐   │      │
│    │ Listen for       │   │      │
│    │ Command          │   │      │
│    │ (8 sec timeout)  │   │      │
│    └────────┬─────────┘   │      │
│             │              │      │
│             ▼              │      │
│    ┌──────────────────┐   │      │
│    │ Recognize Speech │   │      │
│    │ (Google API)     │   │      │
│    └────────┬─────────┘   │      │
│             │              │      │
│             ▼              │      │
│    ┌──────────────────┐   │      │
│    │ Check Stop Words │   │      │
│    │ ["stop","sleep", │   │      │
│    │  "exit","go to   │   │      │
│    │  sleep"]         │   │      │
│    └────────┬─────────┘   │      │
│             │              │      │
│    ┌────────┴────────┐    │      │
│    │                 │    │      │
│    ▼                 ▼    │      │
│ ┌─────────┐  ┌──────────┐│      │
│ │ Stop?   │  │  Route   ││      │
│ │  YES    │  │  Command ││      │
│ │         │  │ route()  ││      │
│ └────┬────┘  └────┬─────┘│      │
│      │            │       │      │
│      │            │       │      │
│      │            ▼       │      │
│      │  ┌────────────────┐│      │
│      │  │ Process &      ││      │
│      │  │ Respond        ││      │
│      │  └────────┬───────┘│      │
│      │           │        │      │
│      └───────────┴────────┘      │
│                  │               │
│                  ▼               │
│        ┌──────────────────┐     │
│        │ Continue Loop    │     │
│        │ (back to Listen) │     │
│        └─────────┬────────┘     │
│                  │               │
└──────────────────┼───────────────┘
                   │
                   │ (when Stop Word detected)
                   │
                   ▼
        ┌──────────────────────┐
        │  Speak "Going back   │
        │  to sleep"           │
        └──────────┬───────────┘
                   │
                   └──────────┐
                              │
                              ▼
                    ┌──────────────────────┐
                    │  Return to Main Loop │
                    │  (Wake Word Waiting) │
                    └──────────────────────┘
```

---

### Command Routing Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  Command Received                           │
│                  route(command)                             │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Iterate Through Skills       │
            │  SKILLS = [memory, system,    │
            │            web, music]        │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Try Skill 1: Memory          │
            │  memory.handle(command)       │
            └───────────────┬───────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
        ┌───────────────┐      ┌───────────────┐
        │  Handled?     │      │  Handled?     │
        │     YES       │      │      NO       │
        │  return True  │      │  return False │
        └───────┬───────┘      └───────┬───────┘
                │                      │
                │                      ▼
                │          ┌───────────────────────┐
                │          │  Try Skill 2: System  │
                │          │  system.handle()      │
                │          └───────────┬───────────┘
                │                      │
                │          ┌───────────┴───────────┐
                │          │                       │
                │          ▼                       ▼
                │  ┌───────────────┐      ┌───────────────┐
                │  │  Handled?     │      │  Handled?     │
                │  │     YES       │      │      NO       │
                │  └───────┬───────┘      └───────┬───────┘
                │          │                      │
                │          │                      ▼
                │          │          ┌───────────────────────┐
                │          │          │  Try Skill 3: Web     │
                │          │          │  web.handle()         │
                │          │          └───────────┬───────────┘
                │          │                      │
                │          │          ┌───────────┴───────────┐
                │          │          │                       │
                │          │          ▼                       ▼
                │          │  ┌───────────────┐      ┌───────────────┐
                │          │  │  Handled?     │      │  Handled?     │
                │          │  │     YES       │      │      NO       │
                │          │  └───────┬───────┘      └───────┬───────┘
                │          │          │                      │
                │          │          │                      ▼
                │          │          │          ┌───────────────────────┐
                │          │          │          │  Try Skill 4: Music   │
                │          │          │          │  music.handle()       │
                │          │          │          └───────────┬───────────┘
                │          │          │                      │
                │          │          │          ┌───────────┴───────────┐
                │          │          │          │                       │
                │          │          │          ▼                       ▼
                │          │          │  ┌───────────────┐      ┌───────────────┐
                │          │          │  │  Handled?     │      │  Handled?     │
                │          │          │  │     YES       │      │      NO       │
                │          │          │  └───────┬───────┘      └───────┬───────┘
                │          │          │          │                      │
                │          │          │          │                      ▼
                │          │          │          │          ┌───────────────────────┐
                │          │          │          │          │  AI Fallback          │
                │          │          │          │          │  ask_ai(command)      │
                │          │          │          │          │  (OpenAI GPT-4o-mini) │
                │          │          │          │          └───────────┬───────────┘
                │          │          │          │                      │
                │          │          │          │                      │
                └──────────┴──────────┴──────────┴──────────────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────────┐
                    │  Response Generated           │
                    │  (from Skill or AI)           │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │  Print "Jarvis: [response]"   │
                    │  speak(response)              │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │  Return to Conversation Loop  │
                    └───────────────────────────────┘
```

---

### Voice Verification Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  verify_voice() Called                      │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Load Stored Voice Embedding  │
            │  from data/my_voice_embedding │
            │  .npy                         │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Record Audio                 │
            │  Duration: 3 seconds          │
            │  Sample Rate: 16000 Hz        │
            │  Channels: 1 (mono)           │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Preprocess Audio             │
            │  preprocess_wav(audio)        │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Generate Voice Embedding     │
            │  encoder.embed_utterance(wav) │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Calculate Similarity         │
            │  similarity = dot_product(    │
            │    stored_embedding,          │
            │    new_embedding)             │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Print Similarity Score       │
            │  "[VOICE-ID] Similarity: X.XXX│
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │  Compare with Threshold       │
            │  THRESHOLD = 0.65             │
            └───────────────┬───────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
        ┌───────────────┐      ┌───────────────┐
        │ similarity >  │      │ similarity <= │
        │  0.65?        │      │  0.65?        │
        │     YES       │      │      NO       │
        └───────┬───────┘      └───────┬───────┘
                │                      │
                ▼                      ▼
        ┌───────────────┐      ┌───────────────┐
        │ Return True   │      │ Return False  │
        │ (Verified)    │      │ (Not Verified)│
        └───────────────┘      └───────────────┘
```

---

## 📝 Detailed Flow Explanation

### Phase 1: Application Initialization

**When:** `python main.py` is executed

**Steps:**

1. **Environment Setup**
   - Load environment variables from `.env` file using `load_dotenv()`
   - Required variables: `OPENAI_API_KEY`, `PICOVOICE_ACCESS_KEY`

2. **Speech Recognizer Initialization**
   - Call `create_recognizer()` from `audio.speech`
   - Configures speech recognition with optimal settings:
     - Energy threshold: 200
     - Dynamic energy adjustment: enabled
     - Pause threshold: 0.8 seconds

3. **Microphone Calibration**
   - Adjust for ambient noise (1 second calibration)
   - Ensures better speech recognition accuracy

4. **Startup Announcement**
   - System speaks: "Jarvis online"
   - Indicates system is ready

---

### Phase 2: Wake Word Detection Loop

**When:** Main loop starts (infinite loop)

**Process:**

1. **Continuous Monitoring**
   - `listen_for_wake_word()` is called
   - Uses Picovoice Porcupine for offline wake word detection
   - Continuously monitors microphone for the word "jarvis"
   - Works offline (no internet required)

2. **Wake Word Detection**
   - When "jarvis" is detected, function returns
   - System proceeds to voice verification

**Note:** This is a blocking call - the system waits here until wake word is detected

---

### Phase 3: Voice Verification

**When:** Wake word is detected

**Process:**

1. **Announcement**
   - System speaks: "Voice verification"

2. **Voice Recording**
   - `verify_voice()` is called from `audio.voice_id`
   - Records 3 seconds of audio from microphone
   - Sample rate: 16kHz, mono channel

3. **Voice Processing**
   - Loads stored voice embedding from `data/my_voice_embedding.npy`
   - Preprocesses the recorded audio
   - Generates voice embedding using Resemblyzer encoder
   - Calculates similarity score using dot product

4. **Verification Decision**
   - Compares similarity score with threshold (0.65)
   - If similarity > 0.65: Voice verified (returns `True`)
   - If similarity ≤ 0.65: Access denied (returns `False`)

5. **Result Handling**
   - **Verified**: Proceeds to conversation mode
   - **Not Verified**: Speaks "Access denied" and returns to wake word loop

---

### Phase 4: Conversation Mode

**When:** Voice is successfully verified

**Process:**

1. **Entry Announcement**
   - System speaks: "Yes boss"
   - Indicates system is ready for commands

2. **Command Listening Loop**
   - Infinite loop that listens for user commands
   - Each iteration:
     - Listens to microphone for up to 8 seconds
     - Phrase time limit: 6 seconds
     - Uses Google Speech Recognition API (requires internet)

3. **Speech Recognition**
   - Converts audio to text using `recognizer.recognize_google(audio)`
   - Converts to lowercase for processing
   - Prints recognized command: "You: [command]"

4. **Stop Word Check**
   - Checks if command contains any stop words:
     - "stop", "sleep", "exit", "go to sleep"
   - **If stop word detected:**
     - Speaks: "Going back to sleep"
     - Exits conversation mode
     - Returns to wake word detection loop

5. **Command Routing**
   - If no stop word, calls `route(command)` from `core.router`
   - Processes command and generates response

6. **Error Handling**
   - **UnknownValueError**: Command not recognized → Continue listening
   - **WaitTimeoutError**: No speech detected → Continue listening
   - **RequestError**: Internet connection issue → Speak error and exit
   - **Other exceptions**: Print error and exit

---

### Phase 5: Command Routing

**When:** A command is received in conversation mode

**Process:**

1. **Skill Iteration**
   - Router iterates through skills in priority order:
     1. **Memory** (`skills.memory`)
     2. **System** (`skills.system`)
     3. **Web** (`skills.web`)
     4. **Music** (`skills.music`)

2. **Skill Matching**
   - For each skill, calls `skill.handle(command)`
   - Skill checks if it can handle the command
   - **If skill handles command:**
     - Skill processes command internally
     - Skill speaks response using `speak()`
     - Skill returns `True`
     - Router stops iteration and returns

3. **AI Fallback**
   - **If no skill handles command:**
     - Calls `ask_ai(command)` from `core.ai`
     - Sends command to OpenAI GPT-4o-mini model
     - Receives AI-generated response
     - Prints response: "Jarvis: [response]"
     - Speaks response using `speak()`

4. **Response Delivery**
   - Response is delivered via text-to-speech
   - Returns to conversation loop for next command

---

### Phase 6: Skill Processing Examples

#### Memory Skill Example

**Command:** "remember my name is John"

**Flow:**
1. `skills.memory.handle()` detects "remember" prefix
2. Parses: key = "name", value = "John"
3. Normalizes key (removes filler words)
4. Calls `storage.memory.remember("profile", "name", "John")`
5. Saves to `data/memory.json`
6. Speaks: "I have remembered that"
7. Returns `True`

#### System Skill Example

**Command:** "open safari"

**Flow:**
1. `skills.system.handle()` detects "open" prefix
2. Extracts app name: "safari"
3. Looks up in `APP_MAP`: "safari" → "Safari"
4. Calls `open_app("Safari")`
5. Uses `subprocess` to run: `open -a Safari`
6. Speaks: "Opening Safari"
7. Returns `True`

#### AI Fallback Example

**Command:** "what is the weather today?"

**Flow:**
1. All skills check command, none handle it (all return `False`)
2. Router calls `ask_ai("what is the weather today?")`
3. Creates OpenAI client
4. Sends request to GPT-4o-mini with system prompt
5. Receives AI response
6. Prints and speaks response
7. Returns to conversation loop

---

## 🔄 Complete Cycle Summary

```
START
  ↓
Initialize (Load config, setup recognizer)
  ↓
Speak "Jarvis online"
  ↓
┌─────────────────────┐
│ MAIN LOOP           │
│                     │
│ Wait for wake word  │ ←─────┐
│   ↓                 │       │
│ Wake word detected  │       │
│   ↓                 │       │
│ Voice verification  │       │
│   ↓                 │       │
│ ┌─────────────────┐ │       │
│ │ Verified?       │ │       │
│ │   YES → Continue│ │       │
│ │   NO → Deny     │ │       │
│ └────────┬────────┘ │       │
│          │          │       │
│          ▼          │       │
│ Conversation Mode   │       │
│   ↓                 │       │
│ Listen for command  │       │
│   ↓                 │       │
│ Recognize speech    │       │
│   ↓                 │       │
│ ┌─────────────────┐ │       │
│ │ Stop word?      │ │       │
│ │   YES → Exit    │──┘      │
│ │   NO → Route    │         │
│ └────────┬────────┘         │
│          │                  │
│          ▼                  │
│ Route command               │
│   ↓                         │
│ Try skills (memory→system→  │
│           web→music)        │
│   ↓                         │
│ ┌─────────────────┐         │
│ │ Handled by skill│         │
│ │ or AI fallback? │         │
│ └────────┬────────┘         │
│          │                  │
│          ▼                  │
│ Process & respond           │
│   ↓                         │
│ Speak response              │
│   ↓                         │
│ Continue loop               │──┘
│                             │
└─────────────────────────────┘
```

---

## 🎯 Key Design Decisions

1. **Offline Wake Word**: Uses Picovoice for privacy and instant response
2. **Voice Verification**: Security layer to ensure only authorized user
3. **Skill-Based Architecture**: Modular, extensible command handling
4. **AI Fallback**: Handles any command not covered by skills
5. **Continuous Loop**: Always listening after wake word, until stop word
6. **Error Resilience**: Continues operation even with recognition errors

---

This flow ensures a smooth, secure, and responsive voice assistant experience.

