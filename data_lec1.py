# -*- coding: utf-8 -*-
"""
Lecture 1 Data Module - Mobile Computing & Android Architecture
FNI-421 Mobile Computing - Dr. Soha Hussein (FCIS, Ain Shams University)
Strictly pure data: zero HTML markup.
"""

LECTURE_META = {
    "id": 1,
    "title": "Introduction to Mobile Computing & Android Architecture",
    "subtitle": "Electromagnetic foundations, cellular generations (1G-5G), and the Android OS software stack",
    "icon": "📱",
    "color": "cyan",
}

summary_sections = [
    {
        "type": "definition",
        "heading": "What is Mobile Computing?",
        "body": "Mobile Computing is a technology paradigm that enables the transmission of data, voice, and video via a computer or any other wireless-enabled device without having to be connected to a fixed physical link. It rests on three core pillars: Mobile Communication (wireless networking infrastructure, protocols, and frequency bands), Mobile Hardware (portable devices, sensors, processors, and batteries), and Mobile Software (operating systems like Android/iOS, runtime environments, and mobile applications).",
    },
    {
        "type": "list",
        "heading": "Pioneers of Wireless & Electromagnetic Communications",
        "bullets": [
            "James Clerk Maxwell (1864): Formulated the classical theory of electromagnetic radiation, mathematically proving that electric and magnetic fields travel through space as waves at the speed of light.",
            "Heinrich Hertz (1887): Experimentally verified Maxwell's theory by generating and detecting electromagnetic waves in the laboratory, proving radio waves exist.",
            "Guglielmo Marconi (1895-1901): Pioneered long-distance radio transmission and sent the first transatlantic wireless radio signal, establishing commercial wireless telegraphy.",
            "Sir Oliver Lodge & Jagadish Chandra Bose: Investigated millimeter radio waves and coherer detectors for wireless signaling.",
            "Reginald Fessenden (1906): Achieved the first audio transmission of speech and music over radio waves using continuous amplitude modulation.",
        ],
    },
    {
        "type": "comparison",
        "heading": "Evolution of Cellular Network Generations (1G to 5G)",
        "table": {
            "headers": ["Generation", "Primary Technology", "Data Rate", "Key Capabilities & Core Standards", "Limitation"],
            "rows": [
                ["1G (1980s)", "Analog cellular (FDMA)", "Up to 2.4 kbps", "Voice calls only; AMPS (Advanced Mobile Phone System), NMT", "No encryption, vulnerable to eavesdropping, poor voice quality, no data"],
                ["2G (1990s)", "Digital cellular (TDMA / CDMA)", "Up to 64 kbps (GPRS 114k, EDGE 384k)", "Digital voice, SMS text messaging, basic mobile data; GSM standard, SIM cards", "Very slow browsing speeds, circuit-switched architecture bottlenecks"],
                ["3G (2000s)", "Wideband CDMA (WCDMA / UMTS)", "384 kbps to 21 Mbps (HSPA+)", "Mobile broadband, video calls, GPS location services, early smartphone web", "High battery consumption, expensive infrastructure, limited video streaming"],
                ["4G (2010s)", "All-IP packet switching (OFDMA / LTE)", "100 Mbps to 1 Gbps (LTE-Advanced)", "High-definition streaming, mobile gaming, VoIP, VoLTE, low latency (<50ms)", "Spectrum congestion, high device complexity, limited massive-IoT scalability"],
                ["5G (2020s)", "Millimeter Wave, Massive MIMO, OFDM", "1 Gbps to 20+ Gbps", "eMBB (enhanced mobile broadband), URLLC (<1ms ultra-reliable latency), mMTC (massive machine-type IoT)", "Higher carrier frequencies have short propagation range and high obstacle absorption"],
            ],
        },
    },
    {
        "type": "steps",
        "heading": "The 5-Layer Android Software Stack Architecture",
        "steps": [
            {
                "label": "Layer 1: Linux Kernel",
                "text": "The foundation of Android. Provides low-level memory management, process management, security model (UID isolation), power management, and hardware device drivers (Display, Camera, Bluetooth, Wi-Fi, Audio).",
            },
            {
                "label": "Layer 2: Hardware Abstraction Layer (HAL)",
                "text": "Defines standard interfaces that expose device hardware capabilities to the higher-level Java API framework. Implemented as modular C/C++ shared libraries (.so) loaded dynamically by system services when hardware is requested.",
            },
            {
                "label": "Layer 3: Android Runtime (ART) & Native C/C++ Libraries",
                "text": "Executes DEX bytecode. ART features Ahead-Of-Time (AOT) and Just-In-Time (JIT) compilation with profile-guided optimization. Accompanied by core native C/C++ libraries (WebKit/Blink, OpenGL ES, FreeType, SQLite, Bionic libc).",
            },
            {
                "label": "Layer 4: Java API Framework",
                "text": "The entire feature-set of Android available to developers through modular services: Activity Manager, Window Manager, Content Providers, View System, Notification Manager, Package Manager, and Telephony Manager.",
            },
            {
                "label": "Layer 5: System & User Applications",
                "text": "The top layer comprising system apps (Dialer, SMS, Camera, Settings, Browser) and third-party user apps. System apps enjoy no privileged API access that cannot be accessed by third-party apps with proper user permissions.",
            },
        ],
    },
    {
        "type": "rule",
        "heading": "Hardware Access Execution Path Rule",
        "body": "An Android application NEVER communicates directly with the Linux kernel drivers or the HAL. When an app requests hardware access (e.g., opening the camera), it invokes a Java API Framework method (e.g., CameraManager.openCamera). The framework API communicates via IPC/Binder with a System Service running in the system server process. The System Service validates permissions, obtains the corresponding HAL module interface, and the HAL communicates with the Linux kernel driver via ioctl/sysfs.",
    },
    {
        "type": "comparison",
        "heading": "Dalvik VM vs Android Runtime (ART) vs Modern Toolchain",
        "table": {
            "headers": ["Feature", "Dalvik Virtual Machine (Legacy)", "Android Runtime (ART - Modern)", "Modern Toolchain (d8 / R8)"],
            "rows": [
                ["Execution Model", "Just-In-Time (JIT) compilation", "AOT compilation + JIT + Profile-guided PGO", "Compiles Java/Kotlin bytecode directly to optimized DEX"],
                ["Installation Speed", "Fast (bytecode stored uncompiled)", "Slower initially (pre-compiles into native ELF machine code)", "Fast build times, smaller APK size through tree-shaking"],
                ["Runtime Performance", "Higher CPU usage, slower execution", "Faster app startup, reduced CPU overhead, longer battery life", "Optimized register allocation and dead-code elimination"],
                ["Memory Footprint", "Smaller app footprint on disk", "Larger binary size on disk due to native AOT code", "Reduces 64K method index pressure, optimizes multidex"],
                ["Garbage Collection", "Frequent GC pauses causing frame drops", "Optimized concurrent GC with single-pause compaction", "Reduces object allocations at compile time"],
            ],
        },
    },
    {
        "type": "code",
        "heading": "Android Compilation Pipeline: Source to DEX",
        "lang": "kotlin",
        "code": """// 1. Source Code (.kt or .java)
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}

// 2. Compilation (kotlinc / javac) -> Java Bytecode (.class files)
// 3. Desugaring & Dexing (d8 / R8 compiler) -> Dalvik Executable (classes.dex)
// 4. Packaging (AAPT2 & APK Builder) -> APK / AAB package
// 5. Target Device Execution -> ART loads classes.dex, executes AOT/JIT native code""",
        "explanation": "Android applications are authored in Kotlin/Java, compiled to standard JVM bytecode (.class), then converted into register-based Dalvik Executable bytecode (.dex) by the d8/R8 compiler. The register-based architecture of DEX uses fewer instructions and less memory than the stack-based JVM.",
    },
]

memory_aids = [
    {
        "title": "Hardware Access Path: F-S-H-K",
        "content": "Framework API -> System Service (via Binder IPC) -> Hardware Abstraction Layer (HAL) -> Kernel Driver. Never direct app-to-HAL or app-to-kernel!",
    },
    {
        "title": "The 5-Layer Stack Mnemonic: L-H-A-F-A",
        "content": "L = Linux Kernel (bottom)\nH = HAL (Hardware Abstraction Layer)\nA = ART / Native C/C++ Libraries\nF = Framework (Java APIs & System Services)\nA = Applications (top layer: System & User apps)",
    },
    {
        "title": "Golden Rules of Android Architecture",
        "content": "Rule 1: System apps use the exact same Java API framework available to third-party developers.\nRule 2: ART executes DEX bytecode, never the Linux kernel directly.\nRule 3: Dalvik was stack-neutral register-based JIT; ART is hybrid AOT + JIT with profile-guided optimization.",
    },
]

mcqs = [
    {
        "id": "L1Q1",
        "q": "When an Android app requests access to hardware (e.g., camera), which of the following best describes the path of execution?",
        "options": [
            "The app calls the HAL directly, bypassing system services for efficiency.",
            "The app uses framework APIs, which communicate with system services that interact with the HAL.",
            "The app uses native C/C++ libraries, which load the HAL module automatically.",
            "The app communicates with the kernel directly through system calls, without involving HAL.",
        ],
        "ans": 1,
        "explanation": "Official Midterm Question 1. Android enforces a secure sandbox: apps call Java API framework classes (e.g., CameraManager), which invoke system services via Binder IPC. System services verify user permissions and communicate with the corresponding HAL module, which then issues kernel system calls.",
    },
    {
        "id": "L1Q2",
        "q": "Which of the following is NOT true about Android Runtime (ART) and the Dalvik Executable (DEX) format?",
        "options": [
            "ART is capable of running multiple virtual machines on low-memory devices.",
            "DEX is a bytecode format specifically optimized for Android's memory constraints.",
            "Build tools such as d8 compile Java sources directly into DEX bytecode.",
            "DEX bytecode can only be executed on the Linux kernel without ART.",
        ],
        "ans": 3,
        "explanation": "Official Midterm Question 8. The Linux kernel does not execute DEX bytecode directly; it only manages processes, memory, and drivers. DEX bytecode requires a virtual machine/runtime environment (ART or Dalvik) to be translated into machine instructions.",
    },
    {
        "id": "L1Q3",
        "q": "Which of the following accurately describes the relationship between the Java API framework and system apps? (Select the most complete and accurate statement)",
        "options": [
            "System apps have special kernel privileges that prevent third-party apps from replacing their functionality.",
            "System apps are built using the same Java framework APIs that are available to third-party developers, and developers can reuse system app functionalities.",
            "System apps execute directly inside the HAL without going through the Java API framework.",
            "The Java API framework is only accessible to Google-signed system applications.",
        ],
        "ans": 1,
        "explanation": "From the official course quiz. System apps (such as Phone, SMS, Browser) are built on top of the same Java API framework that third-party developers use. Third-party apps can also invoke system app capabilities via Intents.",
    },
    {
        "id": "L1Q4",
        "q": "Which of the following best describes a compiler compared to an interpreter?",
        "options": [
            "Translates the entire program into machine code or intermediate bytecode before execution.",
            "Translates code line by line and executes each statement immediately.",
            "Directly executes high-level source code instructions without any translation phase.",
            "Translates code only when runtime errors or exceptions are detected.",
        ],
        "ans": 0,
        "explanation": "Official Quiz Question. A compiler parses and translates the complete source program into machine code or target bytecode prior to execution, whereas an interpreter analyzes and executes the code line by line at runtime.",
    },
    {
        "id": "L1Q5",
        "q": "What is the primary role of the Hardware Abstraction Layer (HAL) in the Android architecture?",
        "options": [
            "To provide a standard Java interface for user interface rendering.",
            "To expose device hardware capabilities to the Java API framework through standardized C/C++ interfaces without exposing proprietary driver code.",
            "To replace the Linux kernel by handling CPU scheduling and low-level interrupts.",
            "To compile Java source code into DEX bytecode at runtime.",
        ],
        "ans": 1,
        "explanation": "The HAL defines standard interfaces (such as camera, audio, sensors) implemented by hardware vendors as C/C++ shared libraries (.so). This allows the upper framework layers to stay agnostic of specific proprietary driver implementations.",
    },
    {
        "id": "L1Q6",
        "q": "What is the main architectural difference between the standard Java Virtual Machine (JVM) and Dalvik/ART?",
        "options": [
            "JVM is register-based, while Dalvik/ART is stack-based.",
            "JVM is stack-based, while Dalvik and ART are register-based virtual execution environments designed for memory and battery efficiency.",
            "JVM executes .dex bytecode, while ART executes raw .class files directly.",
            "There is no architectural difference; ART is simply a re-branded OpenJDK JVM.",
        ],
        "ans": 1,
        "explanation": "Standard JVMs use a stack-based architecture where instructions operate on an operand stack. Dalvik and ART are register-based, which requires fewer instructions to perform operations, saves memory bandwidth, and executes significantly faster on mobile CPU architectures.",
    },
    {
        "id": "L1Q7",
        "q": "What key innovation did Heinrich Hertz contribute to the physical foundation of mobile communications in 1887?",
        "options": [
            "He formulated the four differential Maxwell equations.",
            "He experimentally generated and detected electromagnetic waves in a laboratory, validating Maxwell's electromagnetic theory.",
            "He laid the first transatlantic commercial telegraph cable.",
            "He invented the frequency modulation (FM) radio receiver.",
        ],
        "ans": 1,
        "explanation": "James Clerk Maxwell predicted electromagnetic waves mathematically in 1864, but Heinrich Hertz was the first to physically produce and detect them in the laboratory in 1887 using an electric spark oscillator.",
    },
    {
        "id": "L1Q8",
        "q": "Which cellular generation first introduced pure packet-switched All-IP architecture, eliminating dedicated circuit-switched voice channels?",
        "options": [
            "1G",
            "2G (GSM)",
            "3G (UMTS)",
            "4G (LTE)",
        ],
        "ans": 3,
        "explanation": "4G LTE completely abandoned traditional circuit-switched telecommunication infrastructure in favor of an all-IP network. Voice calls in 4G are transported as IP packets via VoLTE (Voice over LTE).",
    },
    {
        "id": "L1Q9",
        "q": "In the modern Android build toolchain, what is the role of the 'd8' tool?",
        "options": [
            "It converts Kotlin files directly into C++ native shared libraries.",
            "It is the default dexer that compiles Java .class bytecode into optimized Dalvik Executable (classes.dex) bytecode.",
            "It runs automated unit tests inside the Android emulator.",
            "It generates the AndroidManifest.xml file from Gradle configuration.",
        ],
        "ans": 1,
        "explanation": "d8 is Google's modern dex compiler (replacing the legacy dx tool). It takes Java .class bytecode files and produces optimized DEX bytecode (classes.dex) with faster compile times, smaller output size, and better desugaring support.",
    },
    {
        "id": "L1Q10",
        "q": "What is Profile-Guided Optimization (PGO) in the Android Runtime (ART)?",
        "options": [
            "Pre-compiling all apps on device purchase so JIT is permanently disabled.",
            "Using runtime profiling data collected during app usage to compile frequently executed 'hot' code paths into native code Ahead-Of-Time during device idle/charging.",
            "A security module that verifies cryptographic certificates of installed apps.",
            "A memory profiler inside Android Studio for tracking memory leaks.",
        ],
        "ans": 1,
        "explanation": "Starting in Android 7.0 (Nougat), ART combines JIT and AOT: when apps run, JIT profiles hot methods. When the device is idle and charging, ART compiles those hot methods into native code ahead of time, providing fast startup without slow install times.",
    },
    {
        "id": "L1Q11",
        "q": "Which layer of the Android architecture provides the Bionic C library and the SQLite database engine?",
        "options": [
            "Linux Kernel",
            "Hardware Abstraction Layer (HAL)",
            "Native C/C++ Libraries (alongside ART)",
            "Java API Framework",
        ],
        "ans": 2,
        "explanation": "Bionic (Android's lightweight BSD-derived libc optimized for embedded Linux), SQLite, OpenGL ES, and WebKit/Blink reside in the Native C/C++ Libraries layer, directly alongside the Android Runtime.",
    },
    {
        "id": "L1Q12",
        "q": "Why does Android use its own custom C library, Bionic, instead of the standard GNU C Library (glibc)?",
        "options": [
            "Because glibc cannot run on ARM CPU architectures.",
            "Because Bionic has a much smaller memory footprint, faster lightweight thread creation, and avoids GPL licensing constraints in user space.",
            "Because Bionic executes Java bytecode natively without a virtual machine.",
            "Because glibc does not support file input/output operations.",
        ],
        "ans": 1,
        "explanation": "Bionic was engineered specifically for Android to reduce memory overhead, provide fast pthread creation on low-RAM mobile hardware, and use a BSD license so hardware and application vendors can link to it without GPL restrictions.",
    },
    {
        "id": "L1Q13",
        "q": "What constitutes the 64K method reference limit in legacy Android development, and what tool resolved it?",
        "options": [
            "A single DEX file can reference at most 65,536 methods due to a 16-bit method index; resolved by Multidex and d8.",
            "Android devices could only run 64 applications simultaneously; resolved by ART.",
            "A method could not exceed 64 kilobytes of source code; resolved by Kotlin.",
            "The Linux kernel can only track 65,536 process IDs; resolved by 64-bit kernels.",
        ],
        "ans": 0,
        "explanation": "In Dalvik bytecode specifications, the method reference table uses a 16-bit field ($2^{16} = 65,536$). When an app and its libraries exceed 65,536 method references, multidex is required to partition the app into multiple DEX files.",
    },
    {
        "id": "L1Q14",
        "q": "What is the primary difference between 1G and 2G mobile communication systems?",
        "options": [
            "1G used digital packet switching, while 2G used analog transmission.",
            "1G used analog frequency modulation for voice, while 2G introduced digital transmission, encryption, and SMS text messaging.",
            "1G supported video streaming, while 2G was restricted to audio only.",
            "1G operated on 5 GHz radio frequencies, while 2G moved down to 2.4 GHz.",
        ],
        "ans": 1,
        "explanation": "1G (e.g., AMPS) was purely analog, suffered from high background noise, and lacked encryption. 2G (e.g., GSM) introduced digital radio transmission, TDMA/CDMA multiplexing, cryptographic security, and Short Message Service (SMS).",
    },
    {
        "id": "L1Q15",
        "q": "Which of the following components belongs to the Java API Framework layer?",
        "options": [
            "Binder Driver",
            "Camera HAL Module (.so)",
            "NotificationManager and ActivityManager",
            "Linux Process Scheduler",
        ],
        "ans": 2,
        "explanation": "NotificationManager, ActivityManager, WindowManager, and ContentProviders are core high-level managers exposed as part of the Java API Framework layer in Android.",
    },
    {
        "id": "L1Q16",
        "q": "In Android's security architecture, what mechanism enforces process isolation between different installed applications?",
        "options": [
            "Each app runs in its own isolated Linux process and is assigned a unique Linux User ID (UID).",
            "All apps share a single common UID and rely on Java language type safety.",
            "Process isolation is enforced by the display driver in the HAL.",
            "The Google Play Store sandboxes apps remotely before download.",
        ],
        "ans": 0,
        "explanation": "Android leverages Linux multi-user security: during installation, every app is assigned a unique Linux UID and GID. The Linux kernel prevents one UID from reading another UID's process memory or private files.",
    },
    {
        "id": "L1Q17",
        "q": "Which 5G service category is specifically designed to support autonomous vehicles, remote surgery, and industrial robotics requiring sub-millisecond latency?",
        "options": [
            "eMBB (Enhanced Mobile Broadband)",
            "URLLC (Ultra-Reliable Low-Latency Communication)",
            "mMTC (Massive Machine-Type Communication)",
            "VoLTE (Voice over LTE)",
        ],
        "ans": 1,
        "explanation": "URLLC provides end-to-end latency of less than 1 millisecond and 99.999% reliability, making it suitable for mission-critical applications like automated driving, telesurgery, and smart grid automation.",
    },
    {
        "id": "L1Q18",
        "q": "What is the primary function of the 'R8' tool in modern Android compilation?",
        "options": [
            "To flash ROM firmware onto rooted physical devices.",
            "To combine shrinking (tree-shaking/dead-code removal), optimization, obfuscation (renaming identifiers), and dexing into a single build step.",
            "To emulate ARM processors on x86 computers.",
            "To convert XML layout files into vector graphics.",
        ],
        "ans": 1,
        "explanation": "R8 is Google's code shrinker and optimizer that replaced ProGuard and integrated directly with d8. It removes unused classes/methods, optimizes bytecode, obfuscates names, and outputs classes.dex in one pass.",
    },
    {
        "id": "L1Q19",
        "q": "How does an Android app communicate with an Android system service located in another process?",
        "options": [
            "Through direct shared memory pointers without kernel intervention.",
            "Via Inter-Process Communication (IPC) using the Binder framework and AIDL interfaces.",
            "By writing temporary files to the SD card directory.",
            "By rebooting the device into recovery mode.",
        ],
        "ans": 1,
        "explanation": "Android's primary IPC mechanism is the Binder driver, located in the Linux kernel. System services expose remote interfaces defined in AIDL (Android Interface Definition Language), and apps make synchronous proxy calls over Binder.",
    },
    {
        "id": "L1Q20",
        "q": "Which wireless communication pioneer sent the first transatlantic radio signal across the Atlantic Ocean in 1901?",
        "options": [
            "James Clerk Maxwell",
            "Heinrich Hertz",
            "Guglielmo Marconi",
            "Alexander Graham Bell",
        ],
        "ans": 2,
        "explanation": "Guglielmo Marconi successfully transmitted the Morse code signal for the letter 'S' across the Atlantic from Poldhu, Cornwall to St. John's, Newfoundland in December 1901.",
    },
]
