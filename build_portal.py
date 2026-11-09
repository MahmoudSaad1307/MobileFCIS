# -*- coding: utf-8 -*-
"""
Build Portal Script for FNI-421 Mobile Computing Study Portal
Generates d:\\Tech\\Summariez\\Mobile\\index.html
Architecture:
- Pure Python data serializer: imports all data modules, builds ALL_DATA JSON
- Injects ALL_DATA into one <script> tag
- JavaScript renders EVERYTHING dynamically via template literals
- Offline-ready, single-file HTML output with Tailwind CDN, Inter & JetBrains Mono fonts
"""

import json
import os
import sys

# Ensure local directory is in python module search path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

import data_lec1
import data_lec2
import data_lec3
import data_lec4
import data_lec5
import data_past_exams

ALL_DATA = {
    "course": {
        "code": "FNI-421",
        "name": "Mobile Computing",
        "instructors": "Dr. Soha Hussein & Prof. Mohamed Hashim",
        "institution": "FCIS — Ain Shams University",
        "term": "Fall 2025 / 2026",
    },
    "lectures": [
        {
            "meta": data_lec1.LECTURE_META,
            "summary": data_lec1.summary_sections,
            "memoryAids": data_lec1.memory_aids,
            "mcqs": data_lec1.mcqs,
        },
        {
            "meta": data_lec2.LECTURE_META,
            "summary": data_lec2.summary_sections,
            "memoryAids": data_lec2.memory_aids,
            "mcqs": data_lec2.mcqs,
        },
        {
            "meta": data_lec3.LECTURE_META,
            "summary": data_lec3.summary_sections,
            "memoryAids": data_lec3.memory_aids,
            "mcqs": data_lec3.mcqs,
        },
        {
            "meta": data_lec4.LECTURE_META,
            "summary": data_lec4.summary_sections,
            "memoryAids": data_lec4.memory_aids,
            "mcqs": data_lec4.mcqs,
        },
        {
            "meta": data_lec5.LECTURE_META,
            "summary": data_lec5.summary_sections,
            "memoryAids": data_lec5.memory_aids,
            "mcqs": data_lec5.mcqs,
        },
    ],
    "exams": {
        "mcqs": data_past_exams.exam_mcqs,
        "long": data_past_exams.exam_long,
    },
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MobileTutor — FNI-421 Mobile Computing Exam Portal</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        cyber: {
                            950: '#060a17',
                            900: '#0a1024',
                            850: '#0f172e',
                            800: '#141f3d',
                            750: '#1a274c',
                            700: '#223361',
                            cyan: '#00f0ff',
                            rose: '#ff3366',
                            emerald: '#00ffaa',
                            amber: '#ffb703',
                            indigo: '#818cf8',
                            purple: '#a855f7',
                            blue: '#3b82f6'
                        }
                    },
                    fontFamily: {
                        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
                        sans: ['"Inter"', 'system-ui', 'sans-serif']
                    }
                }
            }
        };
    </script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #060a17; }
        ::-webkit-scrollbar-thumb { background: #1a274c; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #223361; }

        /* 3D Flashcard Flip styles */
        .perspective-1000 { perspective: 1000px; }
        .transform-style-3d { transform-style: preserve-3d; }
        .backface-hidden { backface-visibility: hidden; -webkit-backface-visibility: hidden; }
        .rotate-y-180 { transform: rotateY(180deg); }

        /* Glowing accents */
        .glow-cyan { box-shadow: 0 0 20px rgba(0, 240, 255, 0.15); }
        .glow-emerald { box-shadow: 0 0 20px rgba(0, 255, 170, 0.15); }
        .glow-amber { box-shadow: 0 0 20px rgba(255, 183, 3, 0.15); }
        .glow-rose { box-shadow: 0 0 20px rgba(255, 51, 102, 0.15); }
        .glow-blue { box-shadow: 0 0 20px rgba(59, 130, 246, 0.15); }
    </style>
</head>
<body class="bg-cyber-950 text-slate-200 font-sans min-h-screen flex flex-col selection:bg-cyber-cyan selection:text-cyber-950">

    <!-- TOP STICKY HUD HEADER -->
    <header class="sticky top-0 z-40 bg-cyber-900/90 backdrop-blur-md border-b border-cyber-800 shadow-xl">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
            <!-- Brand & Course Badge -->
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-xl shadow-lg shadow-cyan-500/20 font-bold text-white">
                    📱
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-bold text-white tracking-tight text-lg">MobileTutor</span>
                        <span class="text-xs px-2 py-0.5 rounded-full bg-cyber-800 text-cyber-cyan font-mono border border-cyber-700 font-semibold">FNI-421</span>
                    </div>
                    <p class="text-xs text-slate-400 hidden sm:block">FCIS — Ain Shams University • Dr. Soha Hussein</p>
                </div>
            </div>

            <!-- Global Search & HUD Stats -->
            <div class="flex items-center gap-3">
                <!-- Search Button -->
                <button onclick="openSearchModal()" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-cyber-850 hover:bg-cyber-800 border border-cyber-750 text-slate-400 hover:text-slate-200 text-xs transition-all shadow-inner group">
                    <svg class="w-4 h-4 text-cyber-cyan group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    <span class="hidden md:inline">Quick Search...</span>
                    <kbd class="px-1.5 py-0.5 text-[10px] bg-cyber-950 rounded text-slate-400 border border-cyber-700 font-mono">⌘K</kbd>
                </button>

                <!-- Mastery Metric Pill -->
                <div class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-cyber-850 border border-cyber-750">
                    <div class="w-2 h-2 rounded-full bg-cyber-emerald animate-pulse"></div>
                    <span class="text-xs text-slate-400 hidden sm:inline">Overall Mastery:</span>
                    <span id="global-mastery-text" class="text-xs font-mono font-bold text-cyber-emerald">0%</span>
                </div>

                <!-- Reset Button -->
                <button onclick="resetAllProgress()" title="Reset study progress" class="p-1.5 text-slate-400 hover:text-rose-400 hover:bg-cyber-800 rounded-lg transition-colors">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                </button>
            </div>
        </div>

        <!-- 7 PRIMARY NAVIGATION TABS -->
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex overflow-x-auto no-scrollbar border-t border-cyber-850 gap-1 py-1.5" id="primary-tabs">
            <!-- Dynamically populated by JS -->
        </nav>
    </header>

    <!-- MAIN VIEW CONTAINER -->
    <main class="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-6">
        <div id="app-root">
            <!-- Dynamic view rendered by JavaScript -->
        </div>
    </main>

    <!-- SEARCH MODAL (CMD+K) -->
    <div id="search-modal" class="fixed inset-0 z-50 bg-cyber-950/80 backdrop-blur-md hidden flex items-start justify-center pt-20 px-4">
        <div class="bg-cyber-900 border border-cyber-700 rounded-2xl w-full max-w-2xl shadow-2xl overflow-hidden flex flex-col max-h-[80vh] animate-pop-in">
            <div class="p-4 border-b border-cyber-800 flex items-center gap-3">
                <svg class="w-5 h-5 text-cyber-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <input id="search-input" type="text" placeholder="Search course concepts, formulas, rules, MCQs, or exams..." class="bg-transparent border-none outline-none text-white placeholder-slate-500 w-full text-base font-sans" oninput="handleSearch(this.value)">
                <button onclick="closeSearchModal()" class="text-xs px-2 py-1 rounded bg-cyber-800 text-slate-400 hover:text-white">ESC</button>
            </div>
            <div id="search-results" class="p-4 overflow-y-auto space-y-2 flex-1">
                <p class="text-xs text-slate-500 text-center py-8">Type a keyword like <span class="text-cyber-cyan">"DEX"</span>, <span class="text-cyber-emerald">"FHSS"</span>, <span class="text-cyber-amber">"Compose"</span>, or <span class="text-cyber-rose">"diffraction"</span>...</p>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="border-t border-cyber-900 bg-cyber-950 py-6 mt-12 text-center text-xs text-slate-500">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p>FNI-421 Mobile Computing • Faculty of Computer and Information Sciences • Ain Shams University</p>
            <p class="font-mono text-slate-600">Built for Exam Excellence • Offline First</p>
        </div>
    </footer>

    <!-- EMBEDDED PURE DATA -->
    <script>
        const ALL_DATA = {DATA_JSON};
    </script>

    <!-- CORE JAVASCRIPT RENDERING ENGINE -->
    <script>
        // ── APPLICATION STATE ────────────────────────────────────────────────────────
        const STATE = {
            activeTab: 0, // 0..4: Lec1..5, 5: Simulator, 6: Past Exams
            activeSubTab: 'summary', // 'summary' | 'memory' | 'mcq' | 'flashcards'
            lectureMCQAnswers: {}, // { [lecId]: { [qId]: selectedOptionIndex } }
            examMCQAnswers: {}, // { [qId]: selectedOptionIndex }
            flashcardMastery: {}, // { [cardId]: true/false }
            simulator: {
                questions: [],
                currentIndex: 0,
                userAnswers: {},
                isSubmitted: false,
                filterLecture: 'all',
                questionCount: 20,
                timerSeconds: 45 * 60,
                timerInterval: null
            }
        };

        // ── STORAGE PERSISTENCE ──────────────────────────────────────────────────────
        function loadState() {
            try {
                const saved = localStorage.getItem('mobiletutor_state');
                if (saved) {
                    const parsed = JSON.parse(saved);
                    STATE.lectureMCQAnswers = parsed.lectureMCQAnswers || {};
                    STATE.examMCQAnswers = parsed.examMCQAnswers || {};
                    STATE.flashcardMastery = parsed.flashcardMastery || {};
                }
            } catch (e) {
                console.error("Failed to load local storage:", e);
            }
        }

        function saveState() {
            try {
                localStorage.setItem('mobiletutor_state', JSON.stringify({
                    lectureMCQAnswers: STATE.lectureMCQAnswers,
                    examMCQAnswers: STATE.examMCQAnswers,
                    flashcardMastery: STATE.flashcardMastery
                }));
                updateGlobalMastery();
            } catch (e) {
                console.error("Failed to save state:", e);
            }
        }

        function resetAllProgress() {
            if (confirm("Reset all quiz answers, simulator progress, and flashcard mastery?")) {
                localStorage.removeItem('mobiletutor_state');
                STATE.lectureMCQAnswers = {};
                STATE.examMCQAnswers = {};
                STATE.flashcardMastery = {};
                renderApp();
                updateGlobalMastery();
            }
        }

        // ── GLOBAL MASTERY HUD ────────────────────────────────────────────────────────
        function updateGlobalMastery() {
            let totalQuestions = 0;
            let correctCount = 0;

            // Lecture MCQs (100 total)
            ALL_DATA.lectures.forEach(lec => {
                lec.mcqs.forEach(q => {
                    totalQuestions++;
                    const answered = STATE.lectureMCQAnswers[lec.meta.id]?.[q.id];
                    if (answered !== undefined && answered === q.ans) {
                        correctCount++;
                    }
                });
            });

            // Exam MCQs (16 total)
            ALL_DATA.exams.mcqs.forEach(q => {
                totalQuestions++;
                const answered = STATE.examMCQAnswers[q.id];
                if (answered !== undefined && answered === q.ans) {
                    correctCount++;
                }
            });

            const pct = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
            const el = document.getElementById('global-mastery-text');
            if (el) el.textContent = `${pct}% (${correctCount}/${totalQuestions})`;
        }

        // ── SECTION RENDERERS (Strictly data-driven) ──────────────────────────────────
        const SECTION_RENDERERS = {
            definition(sec) {
                return `
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-5 hover:border-cyber-700 transition-colors shadow-lg">
                        <div class="flex items-center gap-2 mb-3">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyber-cyan shadow-sm shadow-cyan-500"></span>
                            <h3 class="text-lg font-bold text-white tracking-tight">${sec.heading}</h3>
                        </div>
                        <p class="text-slate-300 leading-relaxed text-sm">${sec.body}</p>
                    </div>
                `;
            },
            list(sec) {
                return `
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-5 shadow-lg">
                        <div class="flex items-center gap-2 mb-4">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyber-indigo"></span>
                            <h3 class="text-lg font-bold text-white tracking-tight">${sec.heading}</h3>
                        </div>
                        <ul class="space-y-2.5">
                            ${sec.bullets.map((b, i) => `
                                <li class="flex items-start gap-3 text-sm text-slate-300">
                                    <span class="flex-shrink-0 w-5 h-5 rounded-md bg-cyber-800 text-cyber-cyan font-mono text-xs flex items-center justify-center font-bold border border-cyber-700 mt-0.5">${i + 1}</span>
                                    <span class="leading-relaxed">${b}</span>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                `;
            },
            comparison(sec) {
                const headers = sec.table.headers;
                const rows = sec.table.rows;
                return `
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-5 shadow-lg overflow-hidden">
                        <div class="flex items-center gap-2 mb-4">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyber-purple"></span>
                            <h3 class="text-lg font-bold text-white tracking-tight">${sec.heading}</h3>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-cyber-800">
                            <table class="w-full text-left text-xs sm:text-sm">
                                <thead class="bg-cyber-850 text-cyber-cyan border-b border-cyber-800 font-mono">
                                    <tr>
                                        ${headers.map(h => `<th class="p-3 font-semibold">${h}</th>`).join('')}
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-cyber-850 text-slate-300">
                                    ${rows.map(row => `
                                        <tr class="hover:bg-cyber-850/50 transition-colors">
                                            ${row.map((cell, idx) => `
                                                <td class="p-3 ${idx === 0 ? 'font-semibold text-white font-mono' : ''}">${cell}</td>
                                            `).join('')}
                                        </tr>
                                    `).join('')}
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
            },
            formula(sec) {
                return `
                    <div class="bg-gradient-to-br from-cyber-900 to-cyber-850 border border-cyber-cyan/30 rounded-xl p-5 shadow-lg glow-cyan">
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-2">
                                <span class="text-xs font-mono uppercase tracking-wider text-cyber-cyan font-bold px-2 py-0.5 rounded bg-cyber-cyan/10 border border-cyber-cyan/30">Formula Box</span>
                                <h3 class="text-base font-bold text-white">${sec.heading}</h3>
                            </div>
                            <span class="text-xl">📐</span>
                        </div>
                        <div class="my-3 p-4 bg-cyber-950/80 rounded-lg border border-cyber-800 text-center font-mono text-cyber-cyan font-bold text-base sm:text-lg tracking-wide shadow-inner">
                            ${sec.formula}
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">${sec.explanation}</p>
                    </div>
                `;
            },
            rule(sec) {
                return `
                    <div class="bg-gradient-to-r from-cyber-amber/10 to-transparent border-l-4 border-cyber-amber bg-cyber-900 rounded-r-xl p-5 shadow-lg">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-cyber-amber text-lg font-bold">⚡</span>
                            <h3 class="text-base font-bold text-cyber-amber tracking-tight">${sec.heading}</h3>
                        </div>
                        <p class="text-sm text-slate-200 leading-relaxed font-medium">${sec.body}</p>
                    </div>
                `;
            },
            steps(sec) {
                return `
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-5 shadow-lg">
                        <div class="flex items-center gap-2 mb-5">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyber-emerald"></span>
                            <h3 class="text-lg font-bold text-white tracking-tight">${sec.heading}</h3>
                        </div>
                        <div class="relative border-l-2 border-cyber-750 ml-3 space-y-6">
                            ${sec.steps.map((st, i) => `
                                <div class="relative pl-6">
                                    <div class="absolute -left-[9px] top-0.5 w-4 h-4 rounded-full bg-cyber-emerald border-2 border-cyber-950 flex items-center justify-center"></div>
                                    <h4 class="text-sm font-bold text-white font-mono mb-1">${st.label}</h4>
                                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">${st.text}</p>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            },
            code(sec) {
                return `
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-5 shadow-lg">
                        <div class="flex items-center justify-between mb-3">
                            <div class="flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-cyber-blue"></span>
                                <h3 class="text-base font-bold text-white tracking-tight">${sec.heading}</h3>
                            </div>
                            <span class="text-xs font-mono uppercase bg-cyber-800 text-cyber-blue px-2 py-0.5 rounded border border-cyber-700">${sec.lang || 'code'}</span>
                        </div>
                        <pre class="bg-cyber-950 p-4 rounded-lg font-mono text-xs sm:text-sm text-cyan-300 overflow-x-auto border border-cyber-850 leading-relaxed"><code>${escapeHTML(sec.code)}</code></pre>
                        ${sec.explanation ? `<p class="mt-3 text-xs text-slate-400 leading-relaxed">${sec.explanation}</p>` : ''}
                    </div>
                `;
            }
        };

        function escapeHTML(str) {
            return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        }

        // ── NAVIGATION RENDERER ──────────────────────────────────────────────────────
        function renderPrimaryTabs() {
            const container = document.getElementById('primary-tabs');
            let html = '';

            // 5 Lectures
            ALL_DATA.lectures.forEach((lec, idx) => {
                const isActive = STATE.activeTab === idx;
                html += `
                    <button onclick="setActiveTab(${idx})" class="flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                        isActive
                            ? 'bg-cyber-800 text-cyber-cyan border border-cyber-700 shadow-sm font-bold'
                            : 'text-slate-400 hover:text-slate-200 hover:bg-cyber-850'
                    }">
                        <span>${lec.meta.icon}</span>
                        <span>Lec ${lec.meta.id}</span>
                    </button>
                `;
            });

            // Tab 6: Simulator
            const isSimActive = STATE.activeTab === 5;
            html += `
                <button onclick="setActiveTab(5)" class="flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                    isSimActive
                        ? 'bg-cyber-800 text-cyber-amber border border-cyber-700 shadow-sm font-bold glow-amber'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-cyber-850'
                }">
                    <span>🧪</span>
                    <span>All-Lectures Simulator</span>
                </button>
            `;

            // Tab 7: Solved Exams
            const isExamActive = STATE.activeTab === 6;
            html += `
                <button onclick="setActiveTab(6)" class="flex items-center gap-2 px-3.5 py-2 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                    isExamActive
                        ? 'bg-cyber-800 text-cyber-rose border border-cyber-700 shadow-sm font-bold glow-rose'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-cyber-850'
                }">
                    <span>📋</span>
                    <span>Solved Past Exams</span>
                </button>
            `;

            container.innerHTML = html;
        }

        function setActiveTab(index) {
            STATE.activeTab = index;
            renderPrimaryTabs();
            renderApp();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function setActiveSubTab(subTab) {
            STATE.activeSubTab = subTab;
            renderApp();
        }

        // ── RENDER SUB-VIEWS ─────────────────────────────────────────────────────────
        function renderLectureView(lec) {
            return `
                <div class="space-y-6">
                    <!-- Lecture Hero Banner -->
                    <div class="bg-gradient-to-r from-cyber-900 via-cyber-850 to-cyber-900 border border-cyber-800 rounded-2xl p-6 relative overflow-hidden shadow-xl">
                        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                            <div class="flex items-start gap-4">
                                <div class="w-14 h-14 rounded-2xl bg-cyber-800 border border-cyber-700 flex items-center justify-center text-3xl shadow-inner">
                                    ${lec.meta.icon}
                                </div>
                                <div>
                                    <div class="flex items-center gap-2">
                                        <span class="text-xs font-mono font-bold uppercase tracking-wider text-cyber-${lec.meta.color}">Lecture ${lec.meta.id}</span>
                                        <span class="text-slate-600">•</span>
                                        <span class="text-xs text-slate-400">${lec.mcqs.length} High-Yield Questions</span>
                                    </div>
                                    <h1 class="text-xl sm:text-2xl font-bold text-white tracking-tight mt-0.5">${lec.meta.title}</h1>
                                    <p class="text-xs sm:text-sm text-slate-400 mt-1">${lec.meta.subtitle}</p>
                                </div>
                            </div>
                        </div>

                        <!-- Sub-tab pill switcher -->
                        <div class="flex flex-wrap gap-2 mt-6 pt-4 border-t border-cyber-800/80">
                            ${[
                                { id: 'summary', label: '📖 Comprehensive Summary' },
                                { id: 'memory', label: '🧠 Memory Aids & Mnemonics' },
                                { id: 'mcq', label: `📝 MCQ Practice (${lec.mcqs.length} Qs)` },
                                { id: 'flashcards', label: '🃏 3D Flashcards' }
                            ].map(tab => `
                                <button onclick="setActiveSubTab('${tab.id}')" class="px-4 py-2 rounded-xl text-xs font-semibold transition-all ${
                                    STATE.activeSubTab === tab.id
                                        ? 'bg-cyber-cyan text-cyber-950 font-bold shadow-md shadow-cyan-500/20'
                                        : 'bg-cyber-800/80 hover:bg-cyber-750 text-slate-300'
                                }">
                                    ${tab.label}
                                </button>
                            `).join('')}
                        </div>
                    </div>

                    <!-- Content Area based on Sub-Tab -->
                    <div>
                        ${STATE.activeSubTab === 'summary' ? renderSummaryContent(lec) : ''}
                        ${STATE.activeSubTab === 'memory' ? renderMemoryAidsContent(lec) : ''}
                        ${STATE.activeSubTab === 'mcq' ? renderMCQPracticeContent(lec) : ''}
                        ${STATE.activeSubTab === 'flashcards' ? renderFlashcardsContent(lec) : ''}
                    </div>
                </div>
            `;
        }

        // 1. Summary View
        function renderSummaryContent(lec) {
            return `
                <div class="grid grid-cols-1 gap-6">
                    ${lec.summary.map(sec => {
                        const renderer = SECTION_RENDERERS[sec.type];
                        return renderer ? renderer(sec) : `<div class="p-4 bg-cyber-900 border border-cyber-800 rounded">${sec.heading}</div>`;
                    }).join('')}
                </div>
            `;
        }

        // 2. Memory Aids View
        function renderMemoryAidsContent(lec) {
            return `
                <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                    ${lec.memoryAids.map((aid, idx) => `
                        <div class="bg-cyber-900 border border-cyber-800 hover:border-cyber-cyan/40 transition-colors rounded-xl p-5 shadow-lg flex flex-col justify-between">
                            <div>
                                <div class="flex items-center gap-2 mb-3">
                                    <span class="w-6 h-6 rounded-lg bg-cyber-cyan/10 text-cyber-cyan font-mono text-xs flex items-center justify-center font-bold border border-cyber-cyan/30">#${idx + 1}</span>
                                    <h3 class="text-base font-bold text-white tracking-tight">${aid.title}</h3>
                                </div>
                                <div class="p-4 bg-cyber-950 rounded-lg border border-cyber-850 font-mono text-xs text-slate-200 leading-relaxed whitespace-pre-line shadow-inner">
                                    ${aid.content}
                                </div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            `;
        }

        // 3. MCQ Practice View
        function renderMCQPracticeContent(lec) {
            const answers = STATE.lectureMCQAnswers[lec.meta.id] || {};
            let correctCount = 0;
            let answeredCount = 0;

            lec.mcqs.forEach(q => {
                if (answers[q.id] !== undefined) {
                    answeredCount++;
                    if (answers[q.id] === q.ans) correctCount++;
                }
            });

            return `
                <div class="space-y-6">
                    <!-- MCQ Control Bar -->
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-lg">
                        <div class="flex items-center gap-4">
                            <div class="px-3 py-1 rounded-lg bg-cyber-850 border border-cyber-750 font-mono text-xs">
                                <span class="text-slate-400">Score:</span>
                                <span class="font-bold text-cyber-cyan ml-1">${correctCount} / ${lec.mcqs.length}</span>
                                <span class="text-slate-500 ml-1">(${Math.round((correctCount / lec.mcqs.length) * 100)}%)</span>
                            </div>
                            <div class="text-xs text-slate-400">
                                Answered: <span class="font-mono text-white">${answeredCount}</span> of ${lec.mcqs.length}
                            </div>
                        </div>

                        <!-- 20-Question Quick Jump Matrix -->
                        <div class="flex flex-wrap gap-1.5 max-w-full">
                            ${lec.mcqs.map((q, i) => {
                                const sel = answers[q.id];
                                let colorClass = 'bg-cyber-850 text-slate-400 border-cyber-750 hover:bg-cyber-800';
                                if (sel !== undefined) {
                                    colorClass = sel === q.ans ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40' : 'bg-rose-500/20 text-rose-400 border-rose-500/40';
                                }
                                return `
                                    <a href="#q-${q.id}" class="w-6 h-6 rounded flex items-center justify-center font-mono text-[10px] font-bold border transition-colors ${colorClass}">
                                        ${i + 1}
                                    </a>
                                `;
                            }).join('')}
                        </div>
                    </div>

                    <!-- Questions List -->
                    <div class="space-y-5">
                        ${lec.mcqs.map((q, qIndex) => {
                            const selectedOption = answers[q.id];
                            const isAnswered = selectedOption !== undefined;
                            const isCorrect = isAnswered && selectedOption === q.ans;

                            return `
                                <div id="q-${q.id}" class="bg-cyber-900 border ${
                                    isAnswered
                                        ? (isCorrect ? 'border-emerald-500/30 bg-cyber-900/90' : 'border-rose-500/30 bg-cyber-900/90')
                                        : 'border-cyber-800'
                                } rounded-xl p-5 shadow-lg transition-all">
                                    <!-- Question Header -->
                                    <div class="flex items-start justify-between gap-3 mb-3">
                                        <div class="flex items-center gap-2">
                                            <span class="px-2 py-0.5 rounded bg-cyber-800 text-cyber-cyan font-mono text-xs font-bold border border-cyber-750">Q${qIndex + 1}</span>
                                            <span class="text-xs text-slate-500 font-mono">ID: ${q.id}</span>
                                        </div>
                                        ${isAnswered ? `
                                            <span class="text-xs font-mono font-bold px-2.5 py-0.5 rounded-full ${isCorrect ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30' : 'bg-rose-500/10 text-rose-400 border border-rose-500/30'}">
                                                ${isCorrect ? '✓ CORRECT' : '✗ INCORRECT'}
                                            </span>
                                        ` : ''}
                                    </div>

                                    <!-- Question Text -->
                                    <h3 class="text-sm sm:text-base font-semibold text-white mb-4 leading-relaxed whitespace-pre-line">${q.q}</h3>

                                    <!-- Options -->
                                    <div class="space-y-2">
                                        ${q.options.map((opt, optIndex) => {
                                            const letter = String.fromCharCode(65 + optIndex);
                                            let optStyle = 'bg-cyber-850 hover:bg-cyber-800 border-cyber-750 text-slate-300';

                                            if (isAnswered) {
                                                if (optIndex === q.ans) {
                                                    optStyle = 'bg-emerald-500/20 border-emerald-500 text-emerald-200 font-semibold shadow-sm';
                                                } else if (optIndex === selectedOption) {
                                                    optStyle = 'bg-rose-500/20 border-rose-500 text-rose-200 font-semibold';
                                                } else {
                                                    optStyle = 'bg-cyber-950/60 border-cyber-850 text-slate-500 opacity-60';
                                                }
                                            }

                                            return `
                                                <button onclick="handleSelectLectureMCQ(${lec.meta.id}, '${q.id}', ${optIndex})" ${isAnswered ? 'disabled' : ''} class="w-full text-left p-3.5 rounded-xl border flex items-start gap-3 transition-all text-xs sm:text-sm ${optStyle}">
                                                    <span class="w-5 h-5 rounded-md font-mono font-bold flex items-center justify-center text-xs flex-shrink-0 mt-0.5 ${
                                                        isAnswered && optIndex === q.ans ? 'bg-emerald-500 text-cyber-950' : 'bg-cyber-800 text-slate-400'
                                                    }">${letter}</span>
                                                    <span class="leading-relaxed flex-1">${opt}</span>
                                                </button>
                                            `;
                                        }).join('')}
                                    </div>

                                    <!-- Detailed Explanation (Revealed once answered) -->
                                    ${isAnswered ? `
                                        <div class="mt-4 pt-4 border-t border-cyber-800 text-xs text-slate-300 bg-cyber-950/60 p-3.5 rounded-lg border border-cyber-850 leading-relaxed animate-slide-down">
                                            <span class="font-bold text-cyber-cyan font-mono uppercase tracking-wider block mb-1">💡 Detailed Explanation:</span>
                                            ${q.explanation}
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                </div>
            `;
        }

        function handleSelectLectureMCQ(lecId, qId, optIndex) {
            if (!STATE.lectureMCQAnswers[lecId]) {
                STATE.lectureMCQAnswers[lecId] = {};
            }
            STATE.lectureMCQAnswers[lecId][qId] = optIndex;
            saveState();
            const y = window.scrollY;
            renderApp();
            window.scrollTo({ top: y, behavior: 'instant' });
        }

        // 4. Flashcards View (3D Flip Animation)
        function renderFlashcardsContent(lec) {
            // Generate flashcards from summary definitions and rules
            const cards = [];
            lec.summary.forEach((sec, i) => {
                if (sec.type === 'definition') {
                    cards.push({ id: `fc-${lec.meta.id}-${i}`, front: sec.heading, back: sec.body, category: 'Definition' });
                } else if (sec.type === 'rule') {
                    cards.push({ id: `fc-${lec.meta.id}-${i}`, front: sec.heading, back: sec.body, category: 'Golden Rule' });
                } else if (sec.type === 'formula') {
                    cards.push({ id: `fc-${lec.meta.id}-${i}`, front: sec.heading, back: `${sec.formula}\\n\\n${sec.explanation}`, category: 'Formula' });
                }
            });

            return `
                <div class="space-y-6">
                    <div class="flex items-center justify-between bg-cyber-900 border border-cyber-800 p-4 rounded-xl shadow-lg">
                        <div>
                            <h3 class="font-bold text-white text-sm">3D Active Recall Flashcards</h3>
                            <p class="text-xs text-slate-400">Click any card to flip. Mark mastered cards to store your memory retention.</p>
                        </div>
                        <span class="text-xs font-mono bg-cyber-800 px-3 py-1 rounded text-cyber-cyan border border-cyber-700">${cards.length} Cards</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        ${cards.map((card, idx) => {
                            const isMastered = !!STATE.flashcardMastery[card.id];
                            return `
                                <div class="group h-64 perspective-1000 cursor-pointer" onclick="toggleCardFlip('${card.id}')">
                                    <div id="card-inner-${card.id}" class="relative w-full h-full transition-transform duration-500 transform-style-3d rounded-2xl shadow-xl">
                                        <!-- FRONT -->
                                        <div class="absolute inset-0 w-full h-full backface-hidden bg-gradient-to-br from-cyber-900 to-cyber-850 border ${
                                            isMastered ? 'border-emerald-500/40 glow-emerald' : 'border-cyber-750'
                                        } rounded-2xl p-6 flex flex-col justify-between">
                                            <div class="flex items-center justify-between">
                                                <span class="text-[10px] font-mono uppercase tracking-wider px-2 py-0.5 rounded bg-cyber-800 text-cyber-cyan border border-cyber-700">${card.category}</span>
                                                <span class="text-xs text-slate-500 font-mono">Card ${idx + 1}</span>
                                            </div>
                                            <div class="text-center my-auto">
                                                <h4 class="text-lg font-bold text-white tracking-tight">${card.front}</h4>
                                                <p class="text-[11px] text-slate-500 mt-2 font-mono">Tap to flip ↻</p>
                                            </div>
                                            <div class="flex items-center justify-between pt-2 border-t border-cyber-800/80">
                                                <span class="text-xs text-slate-400">${isMastered ? '✓ Mastered' : '○ Learning'}</span>
                                                <span class="text-xs text-cyber-cyan group-hover:translate-x-1 transition-transform">Flip Card →</span>
                                            </div>
                                        </div>

                                        <!-- BACK -->
                                        <div class="absolute inset-0 w-full h-full backface-hidden rotate-y-180 bg-cyber-950 border border-cyber-cyan/40 rounded-2xl p-6 flex flex-col justify-between overflow-y-auto">
                                            <div>
                                                <div class="flex items-center justify-between mb-2">
                                                    <span class="text-[10px] font-mono uppercase text-cyber-cyan font-bold">${card.front}</span>
                                                    <span class="text-xs text-slate-500 font-mono">Answer</span>
                                                </div>
                                                <p class="text-xs sm:text-sm text-slate-200 leading-relaxed whitespace-pre-line">${card.back}</p>
                                            </div>
                                            <div class="flex items-center justify-end gap-2 pt-3 border-t border-cyber-850" onclick="event.stopPropagation()">
                                                <button onclick="toggleCardMastery('${card.id}')" class="px-3 py-1 rounded text-xs font-mono font-bold transition-colors ${
                                                    isMastered ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-cyber-800 text-slate-300 hover:bg-cyber-750'
                                                }">
                                                    ${isMastered ? '✓ Mastered' : 'Mark as Mastered'}
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                </div>
            `;
        }

        function toggleCardFlip(cardId) {
            const el = document.getElementById(`card-inner-${cardId}`);
            if (el) {
                el.classList.toggle('rotate-y-180');
            }
        }

        function toggleCardMastery(cardId) {
            STATE.flashcardMastery[cardId] = !STATE.flashcardMastery[cardId];
            saveState();
            renderApp();
        }

        // ── 🧪 ALL-LECTURES SIMULATOR VIEW ──────────────────────────────────────────
        function renderSimulatorView() {
            const sim = STATE.simulator;

            // ── SETUP SCREEN ────────────────────────────────────────────────────────
            if (sim.questions.length === 0) {
                return `
                    <div class="max-w-2xl mx-auto">
                        <div class="bg-cyber-900 border border-cyber-800 rounded-2xl overflow-hidden shadow-2xl">
                            <!-- Setup Hero -->
                            <div class="bg-gradient-to-r from-amber-500/10 via-orange-500/5 to-transparent border-b border-cyber-800 p-6 sm:p-8">
                                <div class="flex items-center gap-4">
                                    <div class="w-16 h-16 rounded-2xl bg-cyber-amber/10 border border-cyber-amber/30 flex items-center justify-center text-3xl glow-amber flex-shrink-0">🧪</div>
                                    <div>
                                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">Exam Simulator</h2>
                                        <p class="text-xs sm:text-sm text-slate-400 mt-1">Instant feedback • Auto-advance • Timer • Full review</p>
                                    </div>
                                </div>
                            </div>

                            <div class="p-6 sm:p-8 space-y-6">
                                <!-- Scope Selector -->
                                <div>
                                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-widest mb-3">📚 Subject Scope</label>
                                    <div class="grid grid-cols-1 gap-2" id="scope-buttons">
                                        ${[
                                            { v: 'all',   icon: '🌐', label: 'All Lectures + Official Exams', sub: '116 questions in pool' },
                                            { v: '1',     icon: '📱', label: 'Lecture 1 — Intro & Android Stack', sub: '20 questions' },
                                            { v: '2',     icon: '📡', label: 'Lecture 2 — Modulation & Lifecycle', sub: '20 questions' },
                                            { v: '3',     icon: '📶', label: 'Lecture 3 — Wireless LAN & Intents', sub: '20 questions' },
                                            { v: '4',     icon: '⚡', label: 'Lecture 4 — Bluetooth, FHSS & Room', sub: '20 questions' },
                                            { v: '5',     icon: '🎨', label: 'Lecture 5 — Wave & Jetpack Compose', sub: '20 questions' },
                                            { v: 'exams', icon: '📋', label: 'Official Past Exams Only', sub: '16 questions' },
                                        ].map((opt, i) => `
                                            <label class="flex items-center gap-3 p-3 rounded-xl border cursor-pointer transition-all border-cyber-750 bg-cyber-850 hover:bg-cyber-800 hover:border-cyber-cyan/40 has-[:checked]:border-cyber-cyan has-[:checked]:bg-cyber-cyan/10">
                                                <input type="radio" name="sim-scope" value="${opt.v}" ${i === 0 ? 'checked' : ''} class="accent-cyan-400">
                                                <span class="text-lg">${opt.icon}</span>
                                                <div class="flex-1 min-w-0">
                                                    <div class="text-xs font-semibold text-white">${opt.label}</div>
                                                    <div class="text-[10px] text-slate-500 font-mono">${opt.sub}</div>
                                                </div>
                                            </label>
                                        `).join('')}
                                    </div>
                                </div>

                                <!-- Question Count -->
                                <div>
                                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-widest mb-3">🔢 Number of Questions</label>
                                    <div class="grid grid-cols-4 gap-3">
                                        ${[10, 20, 50, 100].map(cnt => `
                                            <button onclick="setSimCount(${cnt})" class="p-3 rounded-xl border text-center font-mono font-bold text-sm transition-all ${
                                                sim.questionCount === cnt
                                                    ? 'bg-cyber-cyan text-cyber-950 border-cyber-cyan shadow-md shadow-cyan-400/20'
                                                    : 'bg-cyber-850 border-cyber-750 text-slate-300 hover:bg-cyber-800 hover:border-cyber-700'
                                            }">
                                                ${cnt}
                                            </button>
                                        `).join('')}
                                    </div>
                                </div>

                                <!-- Mode Toggle -->
                                <div>
                                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-widest mb-3">⚙️ Feedback Mode</label>
                                    <div class="grid grid-cols-2 gap-3">
                                        <label class="flex items-center gap-3 p-3 rounded-xl border cursor-pointer transition-all border-cyber-cyan bg-cyber-cyan/10">
                                            <input type="radio" name="sim-mode" value="instant" checked class="accent-cyan-400">
                                            <div>
                                                <div class="text-xs font-bold text-white">⚡ Instant Feedback</div>
                                                <div class="text-[10px] text-slate-400">Shows correct/wrong after each pick</div>
                                            </div>
                                        </label>
                                        <label class="flex items-center gap-3 p-3 rounded-xl border cursor-pointer transition-all border-cyber-750 bg-cyber-850 hover:bg-cyber-800">
                                            <input type="radio" name="sim-mode" value="exam" class="accent-cyan-400">
                                            <div>
                                                <div class="text-xs font-bold text-white">🎓 Exam Mode</div>
                                                <div class="text-[10px] text-slate-400">Reveals answers only after submit</div>
                                            </div>
                                        </label>
                                    </div>
                                </div>

                                <button onclick="startSimulator()" class="w-full py-4 rounded-xl bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-cyber-950 font-extrabold text-base shadow-lg shadow-amber-500/20 transition-all font-mono tracking-wide">
                                    🚀 Launch Simulator
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }

            // ── RESULTS SCREEN ───────────────────────────────────────────────────────
            const answeredCount = Object.keys(sim.userAnswers).length;
            const totalCount = sim.questions.length;

            if (sim.isSubmitted) {
                let correctCount = 0;
                let streak = 0;
                let maxStreak = 0;
                sim.questions.forEach((q, i) => {
                    if (sim.userAnswers[i] === q.ans) {
                        correctCount++;
                        streak++;
                        maxStreak = Math.max(maxStreak, streak);
                    } else {
                        streak = 0;
                    }
                });
                const pct = Math.round((correctCount / totalCount) * 100);
                const grade = pct >= 90 ? 'A' : pct >= 80 ? 'B+' : pct >= 70 ? 'B' : pct >= 60 ? 'C' : 'F';
                const gradeColor = pct >= 75 ? 'text-cyber-emerald' : pct >= 50 ? 'text-cyber-amber' : 'text-cyber-rose';
                const emoji = pct >= 90 ? '🏆' : pct >= 75 ? '🎉' : pct >= 50 ? '📚' : '💪';

                return `
                    <div class="max-w-3xl mx-auto space-y-6">
                        <!-- Score Hero Card -->
                        <div class="bg-cyber-900 border border-cyber-800 rounded-2xl overflow-hidden shadow-2xl">
                            <div class="bg-gradient-to-r from-cyber-cyan/5 via-transparent to-cyber-cyan/5 border-b border-cyber-800 p-6 sm:p-8 text-center">
                                <div class="text-5xl mb-3">${emoji}</div>
                                <h2 class="text-2xl font-bold text-white">Simulation Complete</h2>

                                <!-- Big score badge -->
                                <div class="mt-5 inline-flex items-center gap-5 bg-cyber-950 border border-cyber-800 rounded-2xl px-8 py-5">
                                    <div>
                                        <div class="text-6xl font-mono font-extrabold ${gradeColor}">${pct}%</div>
                                        <div class="text-xs font-mono text-slate-500 mt-1">${correctCount} / ${totalCount} correct</div>
                                    </div>
                                    <div class="w-px h-14 bg-cyber-800"></div>
                                    <div class="text-center">
                                        <div class="text-4xl font-mono font-extrabold ${gradeColor}">${grade}</div>
                                        <div class="text-[10px] font-mono text-slate-500 mt-1">Grade</div>
                                    </div>
                                </div>

                                <!-- Stats Row -->
                                <div class="grid grid-cols-3 gap-3 mt-5">
                                    <div class="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-3">
                                        <div class="text-xl font-mono font-bold text-emerald-400">${correctCount}</div>
                                        <div class="text-[10px] text-slate-400 mt-0.5">Correct</div>
                                    </div>
                                    <div class="bg-rose-500/10 border border-rose-500/30 rounded-xl p-3">
                                        <div class="text-xl font-mono font-bold text-rose-400">${totalCount - correctCount}</div>
                                        <div class="text-[10px] text-slate-400 mt-0.5">Wrong</div>
                                    </div>
                                    <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3">
                                        <div class="text-xl font-mono font-bold text-amber-400">${maxStreak}</div>
                                        <div class="text-[10px] text-slate-400 mt-0.5">Best Streak</div>
                                    </div>
                                </div>

                                <div class="flex justify-center gap-3 mt-6">
                                    <button onclick="resetSimulator()" class="px-5 py-2.5 rounded-xl bg-cyber-cyan text-cyber-950 font-bold text-xs shadow-md shadow-cyan-400/20">↩ Retake</button>
                                    <button onclick="setActiveTab(6)" class="px-5 py-2.5 rounded-xl bg-cyber-800 hover:bg-cyber-750 text-white text-xs border border-cyber-700">📋 Past Exams</button>
                                </div>
                            </div>

                            <!-- Mini jump grid for quick review nav -->
                            <div class="p-4 flex flex-wrap gap-1.5">
                                ${sim.questions.map((q, i) => {
                                    const c = sim.userAnswers[i] === q.ans;
                                    return `<button onclick="scrollToReviewQ(${i})" class="w-7 h-7 rounded text-[10px] font-mono font-bold border transition-colors ${c ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40' : 'bg-rose-500/20 text-rose-400 border-rose-500/40'}">${i + 1}</button>`;
                                }).join('')}
                            </div>
                        </div>

                        <!-- Detailed Review -->
                        <h3 class="text-sm font-bold text-white uppercase tracking-wider font-mono">Detailed Answer Review</h3>
                        <div class="space-y-4">
                            ${sim.questions.map((q, idx) => {
                                const userChoice = sim.userAnswers[idx];
                                const isCorrect = userChoice === q.ans;
                                return `
                                    <div id="review-q-${idx}" class="bg-cyber-900 border ${isCorrect ? 'border-emerald-500/30' : 'border-rose-500/30'} rounded-xl overflow-hidden shadow-md">
                                        <!-- Header -->
                                        <div class="flex items-center justify-between px-4 py-2.5 ${isCorrect ? 'bg-emerald-500/10' : 'bg-rose-500/10'} border-b ${isCorrect ? 'border-emerald-500/20' : 'border-rose-500/20'}">
                                            <span class="text-xs font-mono font-bold ${isCorrect ? 'text-emerald-400' : 'text-rose-400'}">
                                                ${isCorrect ? '✓ CORRECT' : '✗ INCORRECT'} — Q${idx + 1}
                                            </span>
                                            <span class="text-[10px] text-slate-500 font-mono">${q.id}</span>
                                        </div>
                                        <!-- Body -->
                                        <div class="p-4 space-y-3">
                                            <p class="text-sm font-semibold text-white leading-relaxed whitespace-pre-line">${q.q}</p>
                                            <!-- Options summary -->
                                            <div class="space-y-1.5">
                                                ${q.options.map((opt, oi) => {
                                                    const isAns = oi === q.ans;
                                                    const isUser = oi === userChoice;
                                                    let cls = 'bg-cyber-850 border-cyber-750 text-slate-400';
                                                    if (isAns) cls = 'bg-emerald-500/15 border-emerald-500/50 text-emerald-300 font-semibold';
                                                    else if (isUser && !isAns) cls = 'bg-rose-500/15 border-rose-500/50 text-rose-300 line-through opacity-70';
                                                    return `
                                                        <div class="flex items-center gap-2.5 px-3 py-2 rounded-lg border text-xs ${cls}">
                                                            <span class="w-5 h-5 rounded font-mono font-bold flex items-center justify-center flex-shrink-0 ${isAns ? 'bg-emerald-500 text-cyber-950' : 'bg-cyber-800 text-slate-500'}">${String.fromCharCode(65 + oi)}</span>
                                                            <span class="leading-relaxed">${opt}</span>
                                                            ${isAns ? '<span class="ml-auto text-emerald-400 font-mono text-[10px]">✓ Correct</span>' : ''}
                                                            ${isUser && !isAns ? '<span class="ml-auto text-rose-400 font-mono text-[10px]">✗ Your pick</span>' : ''}
                                                        </div>
                                                    `;
                                                }).join('')}
                                            </div>
                                            <div class="pt-2 border-t border-cyber-850 text-xs text-slate-400 leading-relaxed">
                                                <span class="text-cyber-cyan font-mono font-bold">💡 Explanation: </span>${q.explanation}
                                            </div>
                                        </div>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>
                `;
            }

            // ── ACTIVE QUESTION RUNNER ────────────────────────────────────────────────
            const currentQ = sim.questions[sim.currentIndex];
            const currentAnswer = sim.userAnswers[sim.currentIndex];
            const isCurrentAnswered = currentAnswer !== undefined;
            const isCurrentCorrect = isCurrentAnswered && currentAnswer === currentQ.ans;
            const instantMode = sim.instantMode !== false; // default to instant

            return `
                <div class="max-w-3xl mx-auto space-y-4">
                    <!-- ── TOP HUD ─────────────────────────────────────────── -->
                    <div class="bg-cyber-900 border border-cyber-800 rounded-2xl p-4 shadow-lg">
                        <!-- Progress bar + counters -->
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-xs font-mono text-slate-500 w-20 flex-shrink-0">Q ${sim.currentIndex + 1} / ${totalCount}</span>
                            <div class="flex-1 bg-cyber-850 rounded-full h-2.5 overflow-hidden border border-cyber-800">
                                <div class="h-full rounded-full transition-all duration-500 bg-gradient-to-r from-cyan-500 to-blue-500" style="width:${(answeredCount / totalCount) * 100}%"></div>
                            </div>
                            <div class="flex items-center gap-2 flex-shrink-0">
                                <span class="text-[10px] font-mono text-emerald-400">${Object.entries(sim.userAnswers).filter(([i, v]) => sim.questions[i]?.ans === v).length}✓</span>
                                <span class="text-[10px] font-mono text-rose-400">${Object.entries(sim.userAnswers).filter(([i, v]) => sim.questions[i]?.ans !== v).length}✗</span>
                            </div>
                        </div>
                        <!-- Timer + Submit -->
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-2">
                                <span class="text-[10px] font-mono text-slate-500 uppercase tracking-wider">Time</span>
                                <span id="sim-timer" class="font-mono text-sm font-bold text-cyber-amber px-2.5 py-1 rounded-lg bg-cyber-850 border border-cyber-750">45:00</span>
                            </div>
                            <button onclick="submitSimulator()" class="px-4 py-1.5 bg-cyber-800 hover:bg-cyber-750 text-white font-semibold text-xs rounded-lg border border-cyber-700 transition-colors">
                                Finish & Submit
                            </button>
                        </div>
                    </div>

                    <!-- ── QUESTION JUMP GRID ───────────────────────────────── -->
                    <div class="bg-cyber-900 border border-cyber-800 rounded-xl p-3">
                        <div class="flex flex-wrap gap-1.5">
                            ${sim.questions.map((q, i) => {
                                const isCurrent = sim.currentIndex === i;
                                const answered = sim.userAnswers[i];
                                let style;
                                if (isCurrent) {
                                    style = 'bg-cyber-cyan text-cyber-950 border-cyber-cyan font-extrabold shadow-sm shadow-cyan-400/30 scale-110';
                                } else if (answered !== undefined) {
                                    style = answered === q.ans
                                        ? 'bg-emerald-500/25 text-emerald-400 border-emerald-500/50'
                                        : 'bg-rose-500/25 text-rose-400 border-rose-500/50';
                                } else {
                                    style = 'bg-cyber-850 text-slate-500 border-cyber-750 hover:bg-cyber-800 hover:text-slate-300';
                                }
                                return `<button onclick="setSimQuestionIndex(${i})" class="w-7 h-7 rounded text-[10px] font-mono font-bold border transition-all ${style}">${i + 1}</button>`;
                            }).join('')}
                        </div>
                    </div>

                    <!-- ── QUESTION CARD ────────────────────────────────────── -->
                    <div class="bg-cyber-900 border ${isCurrentAnswered ? (isCurrentCorrect ? 'border-emerald-500/50' : 'border-rose-500/50') : 'border-cyber-800'} rounded-2xl overflow-hidden shadow-xl transition-colors duration-300">

                        <!-- Question header stripe -->
                        <div class="flex items-center justify-between px-5 py-3 bg-cyber-850/80 border-b border-cyber-800">
                            <div class="flex items-center gap-2">
                                <span class="text-[10px] font-mono text-slate-500 uppercase tracking-wider">Question ${sim.currentIndex + 1}</span>
                                <span class="text-[10px] font-mono text-slate-600">• ${currentQ.id}</span>
                            </div>
                            ${isCurrentAnswered ? `
                                <span class="flex items-center gap-1.5 text-xs font-mono font-bold px-2.5 py-1 rounded-full ${isCurrentCorrect ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30' : 'bg-rose-500/15 text-rose-400 border border-rose-500/30'}">
                                    ${isCurrentCorrect ? '✓ Correct' : '✗ Wrong'}
                                </span>
                            ` : '<span class="text-[10px] font-mono text-slate-500">Select an answer</span>'}
                        </div>

                        <!-- Question text -->
                        <div class="px-5 pt-5 pb-4">
                            <p class="text-sm sm:text-base font-semibold text-white leading-relaxed whitespace-pre-line">${currentQ.q}</p>
                        </div>

                        <!-- Options -->
                        <div class="px-5 pb-4 space-y-2.5">
                            ${currentQ.options.map((opt, optIdx) => {
                                const letter = String.fromCharCode(65 + optIdx);
                                const isCorrectOpt = optIdx === currentQ.ans;
                                const isUserPick = currentAnswer === optIdx;

                                let btnClass, letterClass;
                                if (!isCurrentAnswered) {
                                    // Unanswered state
                                    btnClass = 'bg-cyber-850 hover:bg-cyber-800 border-cyber-750 hover:border-cyber-cyan/40 text-slate-200 cursor-pointer active:scale-[0.99]';
                                    letterClass = 'bg-cyber-800 text-slate-400';
                                } else if (isCorrectOpt) {
                                    // Correct answer — always highlight green
                                    btnClass = 'bg-emerald-500/20 border-emerald-500 text-emerald-100 cursor-default shadow-sm';
                                    letterClass = 'bg-emerald-500 text-cyber-950';
                                } else if (isUserPick) {
                                    // User's wrong pick
                                    btnClass = 'bg-rose-500/15 border-rose-500/60 text-rose-200 cursor-default opacity-80';
                                    letterClass = 'bg-rose-500/80 text-white';
                                } else {
                                    // Other unselected option after answering
                                    btnClass = 'bg-cyber-950/50 border-cyber-850 text-slate-500 cursor-default opacity-50';
                                    letterClass = 'bg-cyber-800 text-slate-600';
                                }

                                const tag = isCurrentAnswered ? 'div' : 'button';
                                const onclick = isCurrentAnswered ? '' : `onclick="selectSimOption(${optIdx})"`;

                                return `
                                    <${tag} ${onclick} class="w-full text-left p-3.5 rounded-xl border flex items-start gap-3 transition-all duration-200 text-xs sm:text-sm ${btnClass}">
                                        <span class="w-6 h-6 rounded-lg font-mono font-bold flex items-center justify-center text-xs flex-shrink-0 mt-0.5 ${letterClass}">${letter}</span>
                                        <span class="leading-relaxed flex-1">${opt}</span>
                                        ${isCurrentAnswered && isCorrectOpt ? '<span class="ml-auto text-emerald-400 text-lg flex-shrink-0">✓</span>' : ''}
                                        ${isCurrentAnswered && isUserPick && !isCorrectOpt ? '<span class="ml-auto text-rose-400 text-lg flex-shrink-0">✗</span>' : ''}
                                    </${tag}>
                                `;
                            }).join('')}
                        </div>

                        <!-- Explanation panel (shown after answering) -->
                        ${isCurrentAnswered ? `
                            <div class="mx-5 mb-5 p-4 rounded-xl ${isCurrentCorrect ? 'bg-emerald-500/8 border border-emerald-500/25' : 'bg-rose-500/8 border border-rose-500/25'}">
                                    <div class="flex items-center gap-2 mb-2">
                                        <span class="text-sm">${isCurrentCorrect ? '🎯' : '📖'}</span>
                                        <span class="text-xs font-mono font-bold ${isCurrentCorrect ? 'text-emerald-400' : 'text-rose-300'} uppercase tracking-wider">
                                            ${isCurrentCorrect ? 'Well done!' : 'Correct answer: (' + String.fromCharCode(65 + currentQ.ans) + ') ' + currentQ.options[currentQ.ans]}
                                        </span>
                                    </div>
                                <p class="text-xs text-slate-300 leading-relaxed">${currentQ.explanation}</p>
                            </div>
                        ` : ''}

                        <!-- Navigation footer -->
                        <div class="flex items-center justify-between px-5 py-3.5 bg-cyber-850/60 border-t border-cyber-800">
                            <button onclick="setSimQuestionIndex(${sim.currentIndex - 1})" ${sim.currentIndex === 0 ? 'disabled' : ''} class="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-cyber-800 hover:bg-cyber-750 text-xs text-slate-300 disabled:opacity-30 disabled:cursor-not-allowed transition-colors font-semibold border border-cyber-700">
                                ← Prev
                            </button>

                            <div class="text-xs font-mono text-slate-500">
                                ${answeredCount} / ${totalCount} answered
                            </div>

                            <button onclick="setSimQuestionIndex(${sim.currentIndex + 1})" ${sim.currentIndex === totalCount - 1 ? 'disabled' : ''} class="flex items-center gap-1.5 px-4 py-2 rounded-xl ${isCurrentAnswered ? 'bg-cyber-cyan text-cyber-950 shadow-md shadow-cyan-400/20 hover:bg-cyan-300' : 'bg-cyber-800 hover:bg-cyber-750 text-slate-300 border border-cyber-700'} font-bold text-xs disabled:opacity-30 disabled:cursor-not-allowed transition-all">
                                Next →
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        function scrollToReviewQ(idx) {
            const el = document.getElementById(`review-q-${idx}`);
            if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        function setSimCount(cnt) {
            STATE.simulator.questionCount = cnt;
            renderApp();
        }

        function startSimulator() {
            const scopeEl = document.querySelector('input[name="sim-scope"]:checked');
            const modeEl = document.querySelector('input[name="sim-mode"]:checked');
            const scope = scopeEl ? scopeEl.value : 'all';
            const mode = modeEl ? modeEl.value : 'instant';

            let pool = [];
            if (scope === 'all') {
                ALL_DATA.lectures.forEach(l => pool.push(...l.mcqs));
                pool.push(...ALL_DATA.exams.mcqs);
            } else if (scope === 'exams') {
                pool.push(...ALL_DATA.exams.mcqs);
            } else {
                const lecId = parseInt(scope);
                const lec = ALL_DATA.lectures.find(l => l.meta.id === lecId);
                if (lec) pool.push(...lec.mcqs);
            }

            // Shuffle pool
            pool = [...pool].sort(() => Math.random() - 0.5);
            STATE.simulator.questions = pool.slice(0, Math.min(STATE.simulator.questionCount, pool.length));
            STATE.simulator.currentIndex = 0;
            STATE.simulator.userAnswers = {};
            STATE.simulator.isSubmitted = false;
            STATE.simulator.instantMode = (mode === 'instant');

            // Timer
            if (STATE.simulator.timerInterval) clearInterval(STATE.simulator.timerInterval);
            STATE.simulator.timerSeconds = 45 * 60;
            STATE.simulator.timerInterval = setInterval(() => {
                STATE.simulator.timerSeconds--;
                const el = document.getElementById('sim-timer');
                if (el) {
                    const m = Math.floor(STATE.simulator.timerSeconds / 60);
                    const s = STATE.simulator.timerSeconds % 60;
                    el.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
                    if (STATE.simulator.timerSeconds <= 60) el.classList.add('text-rose-400');
                }
                if (STATE.simulator.timerSeconds <= 0) {
                    clearInterval(STATE.simulator.timerInterval);
                    submitSimulator();
                }
            }, 1000);

            renderApp();
        }

        function setSimQuestionIndex(idx) {
            if (STATE.simulator._autoAdvanceTimeout) {
                clearTimeout(STATE.simulator._autoAdvanceTimeout);
                STATE.simulator._autoAdvanceTimeout = null;
            }
            if (idx >= 0 && idx < STATE.simulator.questions.length) {
                STATE.simulator.currentIndex = idx;
                renderApp();
            }
        }

        function selectSimOption(optIdx) {
            const sim = STATE.simulator;
            // Prevent re-selection if already answered in instant mode
            if (sim.instantMode !== false && sim.userAnswers[sim.currentIndex] !== undefined) return;

            sim.userAnswers[sim.currentIndex] = optIdx;
            renderApp(); // Show instant feedback immediately

            // Auto-advance to next unanswered question after 1.6s (instant mode only)
            if (sim.instantMode !== false) {
                const nextIdx = sim.currentIndex + 1;
                if (nextIdx < sim.questions.length) {
                    if (sim._autoAdvanceTimeout) clearTimeout(sim._autoAdvanceTimeout);
                    sim._autoAdvanceTimeout = setTimeout(() => {
                        // Find next unanswered question from current position
                        let target = nextIdx;
                        for (let i = nextIdx; i < sim.questions.length; i++) {
                            if (sim.userAnswers[i] === undefined) { target = i; break; }
                        }
                        sim.currentIndex = target;
                        renderApp();
                    }, 1600);
                }
            }
        }

        function submitSimulator() {
            if (confirm("Are you sure you want to submit your exam simulation?")) {
                if (STATE.simulator.timerInterval) clearInterval(STATE.simulator.timerInterval);
                if (STATE.simulator._autoAdvanceTimeout) clearTimeout(STATE.simulator._autoAdvanceTimeout);
                STATE.simulator.isSubmitted = true;
                renderApp();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function resetSimulator() {
            if (STATE.simulator.timerInterval) clearInterval(STATE.simulator.timerInterval);
            if (STATE.simulator._autoAdvanceTimeout) clearTimeout(STATE.simulator._autoAdvanceTimeout);
            STATE.simulator.questions = [];
            STATE.simulator.userAnswers = {};
            STATE.simulator.isSubmitted = false;
            STATE.simulator.instantMode = true;
            renderApp();
        }

        // ── 📋 SOLVED PAST EXAMS VIEW ───────────────────────────────────────────────
        function renderPastExamsView() {
            const mcqs = ALL_DATA.exams.mcqs;
            const longProblems = ALL_DATA.exams.long;

            return `
                <div class="space-y-8">
                    <!-- Exams Hero -->
                    <div class="bg-gradient-to-r from-cyber-900 via-cyber-850 to-cyber-900 border border-cyber-800 rounded-2xl p-6 shadow-xl">
                        <div class="flex items-center gap-4">
                            <div class="w-14 h-14 rounded-2xl bg-cyber-rose/10 border border-cyber-rose/30 text-cyber-rose text-3xl flex items-center justify-center shadow-inner glow-rose">
                                📋
                            </div>
                            <div>
                                <span class="text-xs font-mono font-bold uppercase tracking-wider text-cyber-rose">Official Assessment Solutions</span>
                                <h1 class="text-2xl font-bold text-white tracking-tight mt-0.5">Mid-Term Fall 2025 & Department Quizzes</h1>
                                <p class="text-xs sm:text-sm text-slate-400 mt-1">Dr. Soha Hussein & Prof. Mohamed Hashim • 8 Graded Table MCQs + Step-by-Step Long Problems</p>
                            </div>
                        </div>
                    </div>

                    <!-- Section 1: Official Midterm Graded MCQs Table -->
                    <div class="bg-cyber-900 border border-cyber-800 rounded-2xl p-6 shadow-lg">
                        <div class="flex items-center justify-between mb-4">
                            <h2 class="text-lg font-bold text-white flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-cyber-rose"></span>
                                Official Graded Answer Key (Mid-Term Table)
                            </h2>
                            <span class="text-xs font-mono text-cyber-cyan bg-cyber-850 px-2.5 py-1 rounded border border-cyber-750">8 / 8 Graded Points</span>
                        </div>
                        <div class="overflow-x-auto rounded-xl border border-cyber-800 mb-6">
                            <table class="w-full text-center text-xs font-mono">
                                <thead class="bg-cyber-850 text-slate-400">
                                    <tr>
                                        ${[1, 2, 3, 4, 5, 6, 7, 8].map(n => `<th class="p-2.5 border-r border-cyber-800">Q${n}</th>`).join('')}
                                    </tr>
                                </thead>
                                <tbody class="text-white font-bold text-sm bg-cyber-950">
                                    <tr>
                                        ${['B', 'B', 'A', 'B', 'B', 'A', 'B', 'D'].map(k => `
                                            <td class="p-3 border-r border-cyber-800 text-cyber-emerald">${k}</td>
                                        `).join('')}
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- All 16 Past Exam & Quiz MCQs -->
                        <div class="space-y-4">
                            ${mcqs.map((q, idx) => {
                                const userChoice = STATE.examMCQAnswers[q.id];
                                const isAnswered = userChoice !== undefined;
                                const isCorrect = isAnswered && userChoice === q.ans;

                                return `
                                    <div class="bg-cyber-950/80 border ${
                                        isAnswered ? (isCorrect ? 'border-emerald-500/30' : 'border-rose-500/30') : 'border-cyber-850'
                                    } rounded-xl p-5 shadow-sm">
                                        <div class="flex items-center justify-between gap-2 mb-2">
                                            <div class="flex items-center gap-2">
                                                <span class="px-2 py-0.5 rounded bg-cyber-800 text-cyber-rose font-mono text-xs font-bold">Q${idx + 1}</span>
                                                <span class="text-xs text-cyber-cyan font-mono">${q.concept}</span>
                                                <span class="text-xs text-slate-500 font-mono">• Lec ${q.lecture}</span>
                                            </div>
                                            <span class="text-xs font-mono text-slate-400">Official Key: <strong class="text-cyber-emerald">${String.fromCharCode(65 + q.ans)}</strong></span>
                                        </div>

                                        <p class="text-sm font-semibold text-white my-3 whitespace-pre-line">${q.q}</p>

                                        <div class="space-y-1.5">
                                            ${q.options.map((opt, optIdx) => {
                                                const letter = String.fromCharCode(65 + optIdx);
                                                let style = 'bg-cyber-900 border-cyber-800 text-slate-300';
                                                if (isAnswered) {
                                                    if (optIdx === q.ans) style = 'bg-emerald-500/20 border-emerald-500 text-emerald-200 font-semibold';
                                                    else if (optIdx === userChoice) style = 'bg-rose-500/20 border-rose-500 text-rose-200';
                                                    else style = 'opacity-50 bg-cyber-950 border-cyber-900 text-slate-500';
                                                }
                                                return `
                                                    <button onclick="handleSelectExamMCQ('${q.id}', ${optIdx})" ${isAnswered ? 'disabled' : ''} class="w-full text-left p-3 rounded-lg border flex items-start gap-2.5 text-xs transition-all ${style}">
                                                        <span class="w-5 h-5 rounded font-mono font-bold flex items-center justify-center flex-shrink-0 ${
                                                            isAnswered && optIdx === q.ans ? 'bg-emerald-500 text-cyber-950' : 'bg-cyber-800 text-slate-400'
                                                        }">${letter}</span>
                                                        <span class="leading-relaxed flex-1">${opt}</span>
                                                    </button>
                                                `;
                                            }).join('')}
                                        </div>

                                        <div class="mt-3 pt-3 border-t border-cyber-850 text-xs text-slate-400 leading-relaxed">
                                            <span class="font-bold text-cyber-cyan block mb-0.5">Official Breakdown:</span>
                                            ${q.explanation}
                                        </div>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>

                    <!-- Section 2: Long Calculation & Architectural Problems -->
                    <div class="space-y-6">
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-cyber-cyan"></span>
                            Part B: Comprehensive Step-by-Step Solved Problems
                        </h2>

                        ${longProblems.map((prob, pIdx) => `
                            <div class="bg-cyber-900 border border-cyber-800 rounded-2xl p-6 shadow-xl space-y-5">
                                <div class="flex items-start justify-between gap-4">
                                    <div>
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-cyber-cyan/10 text-cyber-cyan border border-cyber-cyan/30">Problem ${pIdx + 1} (${prob.type.toUpperCase()})</span>
                                            <span class="text-xs text-cyber-amber font-mono font-bold">${prob.marks} Marks Total</span>
                                        </div>
                                        <h3 class="text-lg font-bold text-white">${prob.title}</h3>
                                    </div>
                                </div>

                                <div class="p-4 bg-cyber-950 rounded-xl border border-cyber-850 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
                                    <strong class="text-white block mb-1">Problem Context:</strong>
                                    ${prob.context}
                                </div>

                                <div class="space-y-4">
                                    ${prob.parts.map(part => `
                                        <div class="bg-cyber-850/60 border border-cyber-750 rounded-xl p-5 space-y-4">
                                            <div class="flex items-center justify-between border-b border-cyber-750 pb-2">
                                                <h4 class="text-sm font-bold text-cyber-cyan">${part.label}</h4>
                                                <span class="text-xs font-mono text-slate-400">${part.marks} Marks</span>
                                            </div>

                                            <div class="space-y-3">
                                                ${part.steps.map(step => `
                                                    <div class="p-3.5 bg-cyber-950/70 rounded-lg border border-cyber-800 text-xs space-y-1.5">
                                                        <div class="font-bold text-white font-mono flex items-center gap-2">
                                                            <span class="w-2 h-2 rounded-full bg-cyber-emerald"></span>
                                                            ${step.label}
                                                        </div>
                                                        ${step.formula ? `<div class="p-2 rounded bg-cyber-900 border border-cyber-850 font-mono text-cyan-300">${step.formula}</div>` : ''}
                                                        ${step.result ? `<div class="p-2.5 rounded bg-cyber-900 font-mono text-emerald-300 whitespace-pre-line leading-relaxed">${step.result}</div>` : ''}
                                                        ${step.table ? renderTableStep(step.table) : ''}
                                                        ${step.note ? `<p class="text-slate-400 italic">${step.note}</p>` : ''}
                                                    </div>
                                                `).join('')}
                                            </div>

                                            <div class="p-3.5 bg-cyber-900/90 rounded-lg border border-cyber-700 text-xs sm:text-sm text-white">
                                                <span class="font-bold text-cyber-emerald font-mono uppercase tracking-wider block mb-1">Final Model Answer & Grading Defense:</span>
                                                <p class="leading-relaxed text-slate-200">${part.answer}</p>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        function renderTableStep(tbl) {
            return `
                <div class="overflow-x-auto rounded border border-cyber-800 my-2">
                    <table class="w-full text-left text-xs font-sans">
                        <thead class="bg-cyber-800 text-cyber-cyan font-mono">
                            <tr>
                                ${tbl.headers.map(h => `<th class="p-2">${h}</th>`).join('')}
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-cyber-850 text-slate-300">
                            ${tbl.rows.map(row => `
                                <tr>
                                    ${row.map((c, i) => `<td class="p-2 ${i === 0 ? 'font-bold text-white' : ''}">${c}</td>`).join('')}
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            `;
        }

        function handleSelectExamMCQ(qId, optIdx) {
            STATE.examMCQAnswers[qId] = optIdx;
            saveState();
            const y = window.scrollY;
            renderApp();
            window.scrollTo({ top: y, behavior: 'instant' });
        }

        // ── SEARCH MODAL FUNCTIONALITY ───────────────────────────────────────────────
        function openSearchModal() {
            const modal = document.getElementById('search-modal');
            if (modal) {
                modal.classList.remove('hidden');
                document.getElementById('search-input').focus();
            }
        }

        function closeSearchModal() {
            const modal = document.getElementById('search-modal');
            if (modal) modal.classList.add('hidden');
        }

        document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                openSearchModal();
            } else if (e.key === 'Escape') {
                closeSearchModal();
            }
        });

        function handleSearch(query) {
            const container = document.getElementById('search-results');
            if (!query || query.trim().length < 2) {
                container.innerHTML = `<p class="text-xs text-slate-500 text-center py-8">Type a keyword like "DEX", "FHSS", "Compose", or "diffraction"...</p>`;
                return;
            }

            const qLower = query.toLowerCase();
            const results = [];

            // Search lectures
            ALL_DATA.lectures.forEach(lec => {
                // Search summary
                lec.summary.forEach(sec => {
                    const text = `${sec.heading} ${sec.body || ''} ${sec.formula || ''} ${(sec.bullets || []).join(' ')}`;
                    if (text.toLowerCase().includes(qLower)) {
                        results.push({
                            type: 'Summary Section',
                            title: sec.heading,
                            subtitle: `Lecture ${lec.meta.id}: ${lec.meta.title}`,
                            lecIndex: lec.meta.id - 1,
                            subTab: 'summary'
                        });
                    }
                });

                // Search MCQs
                lec.mcqs.forEach((mcq, i) => {
                    if (mcq.q.toLowerCase().includes(qLower) || mcq.explanation.toLowerCase().includes(qLower)) {
                        results.push({
                            type: `Lecture MCQ (${mcq.id})`,
                            title: mcq.q.slice(0, 80) + '...',
                            subtitle: `Lecture ${lec.meta.id}: ${lec.meta.title}`,
                            lecIndex: lec.meta.id - 1,
                            subTab: 'mcq'
                        });
                    }
                });
            });

            // Search Past Exams
            ALL_DATA.exams.mcqs.forEach(mcq => {
                if (mcq.q.toLowerCase().includes(qLower) || mcq.explanation.toLowerCase().includes(qLower)) {
                    results.push({
                        type: `Official Exam MCQ (${mcq.id})`,
                        title: mcq.q.slice(0, 80) + '...',
                        subtitle: `Concept: ${mcq.concept} • Lecture ${mcq.lecture}`,
                        lecIndex: 6,
                        subTab: 'past-exams'
                    });
                }
            });

            ALL_DATA.exams.long.forEach(prob => {
                if (prob.title.toLowerCase().includes(qLower) || prob.context.toLowerCase().includes(qLower)) {
                    results.push({
                        type: 'Solved Long Problem',
                        title: prob.title,
                        subtitle: `${prob.marks} Marks • Step-by-Step Walkthrough`,
                        lecIndex: 6,
                        subTab: 'past-exams'
                    });
                }
            });

            if (results.length === 0) {
                container.innerHTML = `<p class="text-xs text-slate-500 text-center py-8">No results found for "${query}".</p>`;
                return;
            }

            container.innerHTML = results.slice(0, 15).map(res => `
                <div onclick="navigateToSearchResult(${res.lecIndex}, '${res.subTab}')" class="p-3 bg-cyber-850 hover:bg-cyber-800 rounded-xl border border-cyber-750 cursor-pointer transition-colors">
                    <div class="flex items-center justify-between text-[10px] font-mono mb-1">
                        <span class="text-cyber-cyan">${res.type}</span>
                        <span class="text-slate-500">${res.subtitle}</span>
                    </div>
                    <div class="text-xs font-semibold text-white">${res.title}</div>
                </div>
            `).join('');
        }

        function navigateToSearchResult(lecIndex, subTab) {
            closeSearchModal();
            STATE.activeTab = lecIndex;
            if (lecIndex < 5 && subTab) {
                STATE.activeSubTab = subTab;
            }
            renderPrimaryTabs();
            renderApp();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // ── MAIN APPLICATION CONTROLLER ──────────────────────────────────────────────
        function renderApp() {
            const root = document.getElementById('app-root');
            if (!root) return;

            if (STATE.activeTab < 5) {
                const lec = ALL_DATA.lectures[STATE.activeTab];
                root.innerHTML = renderLectureView(lec);
            } else if (STATE.activeTab === 5) {
                root.innerHTML = renderSimulatorView();
            } else if (STATE.activeTab === 6) {
                root.innerHTML = renderPastExamsView();
            }

            updateGlobalMastery();
        }

        // ── BOOTSTRAP ────────────────────────────────────────────────────────────────
        document.addEventListener('DOMContentLoaded', () => {
            loadState();
            renderPrimaryTabs();
            renderApp();
        });
    </script>
</body>
</html>
"""

def build():
    print("Serializing ALL_DATA into JSON...")
    data_json = json.dumps(ALL_DATA, ensure_ascii=False)
    
    print("Injecting into HTML template...")
    # Replace {DATA_JSON} placeholder carefully
    output_html = HTML_TEMPLATE.replace("{DATA_JSON}", data_json)
    
    output_path = os.path.join(CURRENT_DIR, "index.html")
    print(f"Writing index.html to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_html)
    
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ Success! Generated index.html ({file_size_kb:.2f} KB).")

if __name__ == "__main__":
    build()

