# -*- coding: utf-8 -*-
"""
Lecture 5 Data Module - Wave Propagation, PAN Technologies & Jetpack Compose
FNI-421 Mobile Computing - Dr. Soha Hussein (FCIS, Ain Shams University)
Strictly pure data: zero HTML markup.
"""

LECTURE_META = {
    "id": 5,
    "title": "Wave Propagation, PAN Technologies & Jetpack Compose",
    "subtitle": "Power density, path loss, diffraction, RFID vs NFC, and modern declarative Android UI with Jetpack Compose",
    "icon": "🎨",
    "color": "amber",
}

summary_sections = [
    {
        "type": "formula",
        "heading": "Spherical Wavefront Expansion & Power Density Physics",
        "formula": "S = P_tx / (4π · d^2), where S is power density (W/m^2) and d is distance",
        "explanation": "As an electromagnetic wave radiates from an isotropic transmitter, its radiated power (P_tx) expands uniformly in all directions over a sphere of radius d. The surface area of this expanding wavefront is A = 4πd^2. Consequently, received power density obeys the inverse-square law: it decreases inversely proportional to the square of the distance (d^2). For example, moving a device from d_1 = 2 meters to d_2 = 6 meters triples the distance (factor of 3), which expands the spherical wavefront area by 3^2 = 9x, causing the power density received by the antenna to drop to 1/9 (approx 11.1%) of its initial value.",
    },
    {
        "type": "definition",
        "heading": "Resonance as an Energy Bridge: Antennas vs Obstacles",
        "body": "Resonance is the physical phenomenon where an electromagnetic wave transfers its oscillating energy to physical matter whose natural atomic or circuit frequency matches the wave's frequency. (1) In a tuned copper antenna: Resonance acts as a constructive bridge, transferring electromagnetic wave energy into organized, coherent electron drift current, creating the electrical signal processed by radio receivers. (2) In building materials (e.g., wet drywall, concrete): Water molecules possess dipole moments that resonate with microwave frequencies (especially 2.4 GHz and 5 GHz). Here, resonance transfers electromagnetic energy into random, chaotic molecular agitation and friction, dissipating the wave's energy as thermal heat (absorption path loss).",
    },
    {
        "type": "definition",
        "heading": "Wave Diffraction & The Knife-Edge Principle",
        "body": "Diffraction is the physical phenomenon where an electromagnetic wave bends around the sharp edges of obstacles and spreads into the geometric shadow zone behind them (explained by the Huygens-Fresnel principle). When a wave diffracts around a structural concrete pillar or wall corner: The total electromagnetic energy of the wave remains conserved and unchanged, but the energy is redistributed over a wider spatial angle behind the barrier, causing the localized Received Signal Strength Indicator (RSSI) to drop. Longer wavelengths diffract significantly more effectively than shorter wavelengths: 2.4 GHz (λ ≈ 12.5 cm) bends around household obstacles far deeper than 5.0 GHz (λ ≈ 6 cm).",
    },
    {
        "type": "comparison",
        "heading": "Personal Area Network (PAN) Technologies: IrDA vs RFID vs NFC",
        "table": {
            "headers": ["Feature / Metric", "Infrared (IrDA)", "Radio Frequency ID (RFID)", "Near Field Communication (NFC)"],
            "rows": [
                ["Operating Frequency", "Infrared optical spectrum (~850-900 nm)", "LF (125 kHz), HF (13.56 MHz), UHF (860-960 MHz)", "HF exactly 13.56 MHz"],
                ["Operating Range", "< 1 meter (typically 10-30 cm)", "Passive: up to 10-12 meters (UHF); Active: up to 100 meters", "< 10 cm (practical touch distance: 2-4 cm)"],
                ["Line of Sight (LOS)", "Strictly required; blocked by walls, clothes, or dust", "Non-line-of-sight; penetrates cardboard, wood, clothing", "Non-line-of-sight, but requires extreme physical proximity"],
                ["Communication Direction", "Point-to-point directional optical beam", "One-way: Reader/Interrogator queries Tag/Transponder", "Bidirectional: Peer-to-Peer, Card Emulation, Reader/Writer"],
                ["Standard Data Format", "IrDA serial framing packets", "EPC (Electronic Product Code), ISO 18000", "NDEF (NFC Data Exchange Format) standardized records"],
                ["Primary Applications", "TV remote controls, legacy printer data sync", "Supply chain pallets, toll booths, warehouse asset tracking", "Contactless mobile payments (Google Pay), tap-to-pair Bluetooth, smart badges"],
            ],
        },
    },
    {
        "type": "comparison",
        "heading": "RFID Tag Architectural Types: Passive vs Active vs Semi-Passive",
        "table": {
            "headers": ["Tag Characteristic", "Passive RFID Tags", "Active RFID Tags", "Semi-Passive (Battery-Assisted BAP)"],
            "rows": [
                ["Internal Power Source", "None (No battery); powered by reader RF magnetic/electric field", "Onboard battery powers transmitter and electronics", "Onboard battery powers circuitry; RF reflection for uplink"],
                ["Operating Range", "Short to moderate (0.1 m to 10 m in UHF)", "Very long range (up to 100+ meters)", "Moderate to long range (up to 30-40 meters)"],
                ["Operational Lifespan", "Practically infinite (no battery to deplete)", "Limited by battery life (typically 3 to 7 years)", "Limited by battery life (typically 2 to 5 years)"],
                ["Unit Cost", "Extremely low ($0.05 to $0.20 per tag)", "High ($15 to $50+ per tag)", "Moderate ($5 to $15 per tag)"],
                ["Data Storage Capacity", "Minimal (64 bits to a few kilobytes)", "Large (up to 128 KB or more)", "Moderate (can log temperature/sensor history)"],
            ],
        },
    },
    {
        "type": "steps",
        "heading": "Jetpack Compose Declarative UI Architecture",
        "steps": [
            {
                "label": "1. Declarative Paradigm (UI = f(State))",
                "text": "Unlike the legacy imperative Android View system (findViewById, setText), Compose describes what the UI should look like for a given state. Developers do not mutate UI hierarchies manually.",
            },
            {
                "label": "2. @Composable Functions",
                "text": "Functions annotated with @Composable emit UI elements. They are executed by the Compose runtime, can run in any order, can execute in parallel across multiple worker threads, and must be free of unintended side effects.",
            },
            {
                "label": "3. Unidirectional Data Flow (UDF)",
                "text": "State flows DOWN from parent composables to child composables as parameters. Events flow UP from child composables to state holders as lambda callbacks.",
            },
            {
                "label": "4. Intelligent Recomposition",
                "text": "When state changes, Compose re-executes only the composable functions that read that specific state. Composable nodes whose input parameters have not changed are completely skipped (smart skipping).",
            },
        ],
    },
    {
        "type": "rule",
        "heading": "State Management Rules: remember vs rememberSaveable",
        "body": "Rule 1: Calling mutableStateOf(value) creates an observable MutableState<T>. When .value is mutated, Compose schedules a recomposition of reading composables. Rule 2: Wrapping mutableStateOf inside remember { ... } guarantees the state value survives across recompositions during normal execution. Rule 3: To survive Activity recreation caused by runtime configuration changes (such as device rotation) or system process death, developers MUST use rememberSaveable { ... }, which saves state in the Activity's SavedStateRegistry bundle.",
    },
    {
        "type": "code",
        "heading": "Building Declarative Screens with Modifiers in Jetpack Compose",
        "lang": "kotlin",
        "code": """@Composable
fun CounterCard(title: String, modifier: Modifier = Modifier) {
    // State surviving recompositions and screen orientation changes
    var count by rememberSaveable { mutableStateOf(0) }

    Card(
        modifier = modifier
            .fillMaxWidth()
            .padding(16.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(text = title, style = MaterialTheme.typography.titleMedium)
            Spacer(modifier = Modifier.height(8.dp))
            Text(text = "Current Taps: $count", style = MaterialTheme.typography.headlineLarge)
            Spacer(modifier = Modifier.height(16.dp))
            Button(onClick = { count++ }) {
                Text(text = "Increment Counter")
            }
        }
    }
}""",
        "explanation": "In Compose, UI components are composed using standard Kotlin functions. Modifiers are chained sequentially to configure sizing, padding, click handling, and appearance.",
    },
]

memory_aids = [
    {
        "title": "The Inverse-Square Power Rule",
        "content": "Power Density S = P / (4π d^2)\nDouble distance (2x) -> Power drops to 1/4 (25%).\nTriple distance (3x) -> Power drops to 1/9 (11.1%).",
    },
    {
        "title": "Diffraction Law of Energy",
        "content": "Diffraction bends waves around edges.\nTotal EM Energy = UNCHANGED!\nEnergy is redistributed over a wider spatial angle behind the barrier.",
    },
    {
        "title": "Resonance Dual Persona",
        "content": "In Copper Antenna: Transfers wave energy into useful electron motion (signal).\nIn Wet Wall: Transfers wave energy into random molecular vibration (heat loss).",
    },
    {
        "title": "Unidirectional Data Flow (UDF)",
        "content": "STATE flows DOWN (from ViewModel / Parent to Child).\nEVENTS flow UP (from Child button click to ViewModel).",
    },
]

mcqs = [
    {
        "id": "L5Q1",
        "q": "A smartphone receives a weaker 2.4 GHz signal after moving behind a structural concrete column. If the drop in Received Signal Strength Indicator (RSSI) behind the column is caused primarily by diffraction rather than absorption, what is physically happening to the wave's energy?",
        "options": [
            "The total electromagnetic energy of the wave remains unchanged, but energy is redistributed over a wider spatial angle behind the barrier.",
            "The electromagnetic wave energy is converted into heat at the sharp concrete edge.",
            "The frequency of the wave shifts to a lower value as it bends around the corner, reducing its power output.",
            "The wave reflects backward, destroying the energy through destructive interference.",
        ],
        "ans": 0,
        "explanation": "Official Course Quiz Question & Physical Law. In pure diffraction around an obstacle (knife-edge diffraction), the wave is not absorbed or destroyed; rather, the wavefront bends and spreads its energy over a larger spatial volume in the shadow zone, reducing power density at any single point.",
    },
    {
        "id": "L5Q2",
        "q": "Why does a 2.4 GHz Wi-Fi signal generally navigate indoor household environments (walls, doorways, corners) better than a 5 GHz Wi-Fi signal?",
        "options": [
            "2.4 GHz has a shorter wavelength, allowing it to easily slip through microscopic pores in solid walls without touching molecules.",
            "2.4 GHz has a higher wave amplitude, allowing it to overwrite obstacle shadows through constructive interference.",
            "5 GHz waves undergo total internal reflection inside air, while 2.4 GHz waves travel only in straight laser-like lines.",
            "2.4 GHz has a longer wavelength (~12.5 cm), enabling deeper spatial diffraction around edges and exciting wall molecules less rapidly (lower heat absorption).",
        ],
        "ans": 3,
        "explanation": "Official Course Quiz Question. A 2.4 GHz wave has a wavelength of ~12.5 cm compared to ~6.0 cm for 5 GHz. Longer wavelengths diffract more effectively around obstacles and suffer significantly less molecular resonance absorption when passing through common building materials.",
    },
    {
        "id": "L5Q3",
        "q": "A mobile device moves from a distance of 2 meters away from a Wi-Fi router to a distance of 6 meters. Assuming ideal free-space propagation, how does the surface area of the expanding wavefront change, and what happens to the power density received by the device's antenna?",
        "options": [
            "Surface area increases by 3x; power density drops to 1/3 of its original value.",
            "Surface area increases by 6x; power density drops to 1/6 of its original value.",
            "Surface area increases by 9x; power density drops to 1/9 of its original value.",
            "Surface area increases by 12x; power density drops to 1/12 of its original value.",
        ],
        "ans": 2,
        "explanation": "Official Course Quiz Question. The surface area of an expanding spherical wavefront is A = 4πd^2. Tripling the distance (from 2m to 6m, ratio = 3) increases the spherical surface area by 3^2 = 9x. Since total power is spread over 9 times the area, power density drops to 1/9.",
    },
    {
        "id": "L5Q4",
        "q": "Resonance is often described as an 'energy bridge' between electromagnetic waves and physical matter. Which statement correctly distinguishes how resonance behaves in a tuned copper antenna versus inside a wet drywall wall?",
        "options": [
            "Resonance transfers energy into organized electron current in an antenna, but prevents energy transfer entirely inside a wall.",
            "Resonance transfers energy into organized electron motion inside an antenna (useful signal), while transferring energy into random molecular agitation inside the wall (heat loss).",
            "Resonance converts electromagnetic energy into heat in both cases, but the antenna recovers that heat using thermoelectric generators.",
            "An antenna captures energy via diffraction, whereas a wall absorbs energy via inverse square geometry.",
        ],
        "ans": 1,
        "explanation": "Official Course Quiz Question. In an antenna, resonance couples EM wave oscillation into organized alternating electron current (useful RF signal). In dielectric materials like moist drywall, resonance couples wave energy into the rotational/vibrational oscillation of polar water molecules, dissipating the energy as heat.",
    },
    {
        "id": "L5Q5",
        "q": "What is the primary difference between Passive RFID tags and Active RFID tags?",
        "options": [
            "Passive tags have an internal battery and transmit continuously, while active tags have no battery.",
            "Passive tags have no internal battery and draw operating power from the reader's incoming RF electromagnetic field via backscatter, whereas active tags possess their own battery to transmit signals over long distances.",
            "Passive tags operate on optical light, while active tags operate on sound waves.",
            "Passive tags can store gigabytes of video, while active tags store only text.",
        ],
        "ans": 1,
        "explanation": "Passive tags have no internal battery; they are energized by the RF signal emitted by the reader and reflect data using backscatter modulation. Active tags have an onboard battery and transmitter, achieving ranges of up to 100 meters.",
    },
    {
        "id": "L5Q6",
        "q": "Why is Near Field Communication (NFC) restricted to an operational distance of less than 10 centimeters?",
        "options": [
            "Because higher distances are banned by international law to protect birds.",
            "Because NFC relies on magnetic near-field inductive coupling between coils, which decays extremely rapidly with distance (1/d^6 in near-field), providing intrinsic physical security against remote eavesdropping.",
            "Because smartphones lack enough battery voltage to broadcast further.",
            "Because NFC uses optical lasers that cannot travel through air.",
        ],
        "ans": 1,
        "explanation": "NFC operates at 13.56 MHz in the reactive near-field region using inductive magnetic coupling between the initiator's antenna coil and the target's coil. The magnetic field strength drops as 1/d^3 to 1/d^6, ensuring communication only happens when devices are tapped within centimeters.",
    },
    {
        "id": "L5Q7",
        "q": "What is the standard data exchange format used by NFC tags and devices to exchange contacts, URLs, or text?",
        "options": [
            "JSON",
            "NDEF (NFC Data Exchange Format)",
            "XML-RPC",
            "Protobuf",
        ],
        "ans": 1,
        "explanation": "NDEF (NFC Data Exchange Format) is the lightweight binary standard defined by the NFC Forum for encapsulating data (text records, URI records, MIME objects) inside NFC tags and peer-to-peer transmissions.",
    },
    {
        "id": "L5Q8",
        "q": "In Jetpack Compose, what is the core architectural principle that describes the relationship between UI and State?",
        "options": [
            "State is mutated directly by Views using setters.",
            "UI is a pure function of State: UI = f(State). When state updates, Compose automatically recalculates and recomposes the affected UI elements.",
            "UI components hold private global variables that are updated by background threads.",
            "UI layouts must be defined in XML and parsed by ViewBinding.",
        ],
        "ans": 1,
        "explanation": "Jetpack Compose is a declarative UI toolkit where the UI is modeled as a mathematical function of current state: UI = f(State). When state changes, Compose re-invokes the relevant @Composable functions with new parameters.",
    },
    {
        "id": "L5Q9",
        "q": "What is the difference between remember { mutableStateOf(x) } and rememberSaveable { mutableStateOf(x) } in Jetpack Compose?",
        "options": [
            "remember saves state to a remote cloud server, while rememberSaveable saves to RAM.",
            "remember preserves state across recompositions, while rememberSaveable preserves state across both recompositions AND Activity recreation caused by configuration changes (such as screen rotation) or process death.",
            "remember is deprecated and should never be used.",
            "rememberSaveable can only store integers, while remember can store any object.",
        ],
        "ans": 1,
        "explanation": "remember retains state across recompositions, but loses state if the Activity is destroyed and recreated (e.g., during screen rotation). rememberSaveable automatically saves and restores the state in the SavedStateHandle Bundle.",
    },
    {
        "id": "L5Q10",
        "q": "What is 'Recomposition' in Jetpack Compose?",
        "options": [
            "Re-compiling the entire Android APK whenever the user taps a button.",
            "The process of re-executing @Composable functions when their inputs or observed states change, updating the UI tree while skipping unaffected composables.",
            "Converting Kotlin Compose code into legacy XML layout files.",
            "A garbage collection pass that frees unused graphics memory.",
        ],
        "ans": 1,
        "explanation": "Recomposition is the execution cycle where Compose re-runs composables that observe state changes to produce updated layout trees. Compose employs smart skipping so composables whose parameters did not change are not re-executed.",
    },
    {
        "id": "L5Q11",
        "q": "What is Unidirectional Data Flow (UDF) in modern Android architecture with Jetpack Compose?",
        "options": [
            "Data flows in a circle between the Activity and the Linux kernel.",
            "State flows downwards from state holders/ViewModels into Composable UI functions, while events (clicks, gestures) flow upwards from UI composables to event handlers.",
            "All data flows exclusively from the user's touch screen to the database without stopping at the UI.",
            "A design pattern where only one Activity is allowed per application.",
        ],
        "ans": 1,
        "explanation": "Unidirectional Data Flow (UDF) dictates that State flows DOWN to composables, and Events flow UP to state holders. This decouples UI presentation from business logic and makes testing straightforward.",
    },
    {
        "id": "L5Q12",
        "q": "In Jetpack Compose, how does the order of Modifiers affect the rendered UI?",
        "options": [
            "Modifier order does not matter; Compose sorts them alphabetically.",
            "Modifier order is significant: chaining .padding(16.dp).clickable { } results in a clickable area that does not include the padding, whereas .clickable { }.padding(16.dp) includes the padding in the touch target.",
            "All modifiers must be placed at the very end of the function.",
            "Order only matters for text color, not layouts.",
        ],
        "ans": 1,
        "explanation": "Modifiers in Compose are applied sequentially from left to right (or top to bottom). Placing clickable before padding creates a clickable area that encompasses the padding, whereas placing padding before clickable restricts the touch target to the inner content.",
    },
    {
        "id": "L5Q13",
        "q": "Which of the following three layouts in Jetpack Compose corresponds to a vertical LinearLayout, a horizontal LinearLayout, and a FrameLayout respectively?",
        "options": [
            "Column, Row, and Box",
            "VerticalStack, HorizontalStack, and ZStack",
            "List, Grid, and Frame",
            "Table, Flex, and Canvas",
        ],
        "ans": 0,
        "explanation": "In Compose, Column arranges children vertically (like vertical LinearLayout), Row arranges children horizontally (like horizontal LinearLayout), and Box stacks children on top of each other (like FrameLayout).",
    },
    {
        "id": "L5Q14",
        "q": "Why is Infrared (IrDA) communication unsuitable for tracking student badges or automated library checkout systems?",
        "options": [
            "Infrared radiation causes severe headaches to students.",
            "IrDA requires a direct line-of-sight and precise alignment within a narrow optical beam; it cannot penetrate clothing, backpacks, or opaque barriers.",
            "IrDA operates on 2.4 GHz frequencies that clash with Wi-Fi.",
            "IrDA hardware is too expensive for universities to afford.",
        ],
        "ans": 1,
        "explanation": "Infrared uses optical light waves that cannot penetrate physical obstacles (backpacks, wallets, clothing) and requires strict line-of-sight alignment within a narrow cone, making it unsuitable for automatic walk-through identification.",
    },
    {
        "id": "L5Q15",
        "q": "What is the primary trade-off when selecting Ultra-High Frequency (UHF) RFID (860-960 MHz) instead of NFC for an access control system?",
        "options": [
            "UHF RFID allows long-range walk-through scanning without queuing, but suffers from accidental reads of nearby bystanders and higher cloning risks compared to proximity-locked NFC.",
            "UHF RFID cannot read more than 1 tag per hour.",
            "UHF RFID requires all students to carry active 12-volt car batteries.",
            "UHF RFID only works underwater.",
        ],
        "ans": 0,
        "explanation": "UHF RFID allows fast, long-range scanning (several meters) without physical tapping. However, its broad interrogation zone can accidentally read cards of students walking past outside the gate, and standard passive UHF tags lack the cryptographic challenge-response found in modern NFC credentials.",
    },
    {
        "id": "L5Q16",
        "q": "Can Composable functions in Jetpack Compose execute in parallel on multiple threads?",
        "options": [
            "No, Compose is strictly single-threaded on the Android Main thread.",
            "Yes, the Compose compiler can optimize recomposition by running independent composable functions in parallel on background thread pools, meaning composables must not mutate local variables across scopes.",
            "Yes, but only if the device has at least 8 GB of RAM.",
            "No, Compose uses GPU compute shaders exclusively.",
        ],
        "ans": 1,
        "explanation": "Compose can execute composables in parallel to optimize rendering performance on multi-core devices. Therefore, composable functions must be side-effect-free and must not mutate shared variables during execution.",
    },
    {
        "id": "L5Q17",
        "q": "What is a 'SideEffect' in Jetpack Compose, and how is it managed safely?",
        "options": [
            "An unwanted visual defect caused by GPU driver bugs.",
            "An operation that modifies state or interacts with the outside world (e.g., making a network call, showing a Toast) outside of a Composable's scope; managed using effect handlers like LaunchedEffect and SideEffect.",
            "A memory leak in the Android Linux kernel.",
            "A transition animation between two screens.",
        ],
        "ans": 1,
        "explanation": "A side effect is any change of state that happens outside the scope of a composable function. Because composables can be executed or recomposed at any time or skipped, side effects must be wrapped in controlled effect APIs such as LaunchedEffect(key) { ... }.",
    },
    {
        "id": "L5Q18",
        "q": "What happens if a Composable function reads a MutableState variable whose value changes frequently (e.g., during a scroll animation)?",
        "options": [
            "The app will crash due to stack overflow.",
            "Only the specific composables reading that state will recompose; Compose skips all parent and sibling composables that do not depend on that state.",
            "The entire Android operating system reboots.",
            "The screen turns black until the animation finishes.",
        ],
        "ans": 1,
        "explanation": "Compose tracks state reads granularly. If a state variable changes, Compose triggers recomposition ONLY for the specific composable functions that read that state value, leaving non-reading parent and sibling nodes untouched.",
    },
    {
        "id": "L5Q19",
        "q": "Which frequency band is used by Near Field Communication (NFC)?",
        "options": [
            "125 kHz",
            "13.56 MHz (High Frequency HF band)",
            "433 MHz",
            "2.4 GHz",
        ],
        "ans": 1,
        "explanation": "NFC operates globally on the unlicensed ISM radio frequency of 13.56 MHz, using magnetic induction across an ISO/IEC 18000-3 air interface.",
    },
    {
        "id": "L5Q20",
        "q": "In Jetpack Compose, what is the purpose of the LazyColumn component?",
        "options": [
            "A column that refuses to load data until prompted by the user.",
            "A performance-optimized list container that composes and lays out only the items that are currently visible on screen, functionally equivalent to Android's legacy RecyclerView.",
            "A column that introduces artificial 500 ms delays between text elements.",
            "A database querying tool used by Room.",
        ],
        "ans": 1,
        "explanation": "LazyColumn is Compose's equivalent of RecyclerView. Rather than instantiating and measuring hundreds of items at once (which a standard Column would do), LazyColumn only measures and composes items visible in the current viewport, ensuring smooth 60/120 fps scrolling.",
    },
]
