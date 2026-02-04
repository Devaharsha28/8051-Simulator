# 8051 Simulator

Complete 8051 Microcontroller Simulator with 35+ instructions, featuring React UI, C++ implementation, and Android app support.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Devaharsha28/8051-Simulator)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![React](https://img.shields.io/badge/React-18.2.0-61dafb)](https://reactjs.org/)
[![C++](https://img.shields.io/badge/C++-17-00599C)](https://isocpp.org/)

## 🚀 Features

- **35+ 8051 Instructions** - Complete instruction set including arithmetic, logic, jumps, and loops
- **Monaco Editor** - Professional code editor with syntax highlighting (VS Code engine)
- **Register Bank Support** - Full R0-R7 register visualization
- **Memory Viewer** - Separate views for Lower RAM (00H-7FH) and Upper RAM (80H-FFH)
- **Execution Logging** - Step-by-step instruction execution with detailed output
- **Flag Visualization** - Real-time display of CY, AC, OV, P flags
- **Jump & Loop Support** - Full support for labels, LJMP, SJMP, JZ, JNZ, DJNZ, CJNE
- **Mobile Optimized** - Tab-based interface perfect for portrait mode
- **Offline Capable** - Works completely offline via Android APK
- **Multiple Implementations** - React (Web), C++ (Desktop), Android (Mobile)

## 📱 Live Demo

Try it online: [8051 Simulator Demo](https://devaharsha28.github.io/8051-Simulator)

## 🎯 Supported Instructions

### Arithmetic Operations (8)
```
MOV   - Move data
ADD   - Add
ADDC  - Add with carry
SUBB  - Subtract with borrow
INC   - Increment
DEC   - Decrement
MUL   - Multiply
DIV   - Divide
```

### Logic Operations (6)
```
ANL   - AND logic
ORL   - OR logic
XRL   - XOR logic
CLR   - Clear
CPL   - Complement
SWAP  - Swap nibbles
```

### Rotate Operations (4)
```
RL    - Rotate left
RLC   - Rotate left through carry
RR    - Rotate right
RRC   - Rotate right through carry
```

### Jump & Branch (9)
```
LJMP  - Long jump
SJMP  - Short jump
JZ    - Jump if zero
JNZ   - Jump if not zero
JC    - Jump if carry
JNC   - Jump if no carry
DJNZ  - Decrement and jump if not zero
CJNE  - Compare and jump if not equal
JMP   - Jump (alias)
```

### Subroutine Operations (4)
```
LCALL - Long call
CALL  - Call (alias)
RET   - Return
RETI  - Return from interrupt
```

### Stack Operations (2)
```
PUSH  - Push to stack
POP   - Pop from stack
```

### Bit Operations (3)
```
SETB  - Set bit
CLR C - Clear carry
CPL C - Complement carry
```

### Special (3)
```
DA    - Decimal adjust
NOP   - No operation
END   - End program
```

## 🛠️ Installation & Usage

### Option 1: Web (React)

```bash
cd react_ui
npm install
npm start
```

Open http://localhost:3000

### Option 2: Desktop (C++)

```bash
cd cpp_simulator
mkdir build && cd build
cmake ..
make
./simulator
```

### Option 3: Android App

1. Open `android_app` in Android Studio
2. Wait for Gradle sync
3. Build > Build APK
4. Install APK on Android device

## 📝 Example Programs

### Basic Arithmetic
```assembly
MOV A, #50h    ; A = 0x50
ADD A, #30h    ; A = 0x80
MOV B, #2      ; B = 2
DIV AB         ; A = 0x40, B = 0
END
```

### Loop Example
```assembly
; Calculate sum of 1 to 10
MOV R0, #10    ; Counter = 10
MOV A, #0      ; Sum = 0

LOOP:
    ADD A, R0      ; Add counter to sum
    DJNZ R0, LOOP  ; Loop until R0 = 0

MOV B, #2      ; Divide by 2
DIV AB
END
```

### Conditional Jump
```assembly
MOV A, #5
CJNE A, #5, SKIP
MOV B, #0xFF   ; Executed if A = 5
SKIP:
MOV R0, #10
END
```

## 📂 Project Structure

```
8051-Simulator/
├── react_ui/              # React web application
│   ├── src/
│   │   ├── components/    # UI components
│   │   │   ├── Editor.js      # Monaco code editor
│   │   │   ├── Registers.js   # Register display
│   │   │   └── Memory.js      # Memory viewer
│   │   ├── simulator/     # Simulator engine
│   │   │   └── Simulator8051.js
│   │   └── App.js         # Main app
│   └── package.json
│
├── cpp_simulator/         # C++ implementation
│   ├── include/           # Header files
│   ├── src/               # Source files
│   └── CMakeLists.txt
│
├── android_app/           # Android application
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── java/      # Kotlin MainActivity
│   │   │   ├── assets/    # React build files
│   │   │   └── res/       # Android resources
│   │   └── build.gradle
│   └── build.gradle
│
└── README.md
```

## 🎨 Screenshots

### Web Interface
- Monaco Code Editor with syntax highlighting
- Tab-based navigation (Editor, Registers, Memory, Output)
- Real-time execution logging
- Flag and register visualization

### Memory Viewer
- Lower RAM (00H-7FH): General purpose + register banks
- Upper RAM (80H-FFH): Special function registers
- Color-coded non-zero values

## 🧪 Technical Details

### 8051 Architecture
- **Registers**: A, B, R0-R7, PC, SP, DPTR, PSW
- **Memory**: 256 bytes RAM (128 lower + 128 upper/SFR)
- **Flags**: CY (Carry), AC (Auxiliary Carry), OV (Overflow), P (Parity)
- **Register Banks**: 4 banks (RS0, RS1 bits in PSW)

### Addressing Modes
- **Immediate**: `MOV A, #50h`
- **Register**: `MOV A, R0`
- **Direct**: `MOV A, 30h`
- **Indirect**: `MOV A, @R0`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original Python implementation: [8051-Simulator](https://github.com/devanshshukla99/8051-Simulator)
- Monaco Editor by Microsoft
- React and Create React App
- Android Studio and Gradle

## 📧 Contact

Devaharsha28 - [@Devaharsha28](https://github.com/Devaharsha28)

Project Link: [https://github.com/Devaharsha28/8051-Simulator](https://github.com/Devaharsha28/8051-Simulator)

---

⭐ Star this repo if you find it helpful!
