const API_URL = "/api";

let selectedGenre = "All";
let selectedLanguage = "All";

/* ---------------- GENRE SELECTION ---------------- */
function selectGenre(btn, genre) {
    document.querySelectorAll(".genre-pill").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    selectedGenre = genre;
}

/* ---------------- LANGUAGE SELECTION ---------------- */
function selectLanguage(btn, lang) {
    document.querySelectorAll(".lang-pill").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    selectedLanguage = lang;
}

/* ---------------- VOICE INPUT ---------------- */
function startVoice() {
    const input = document.getElementById("promptInput");
    if (!("webkitSpeechRecognition" in window)) {
        alert("Voice input not supported");
        return;
    }
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.onresult = e => input.value = e.results[0][0].transcript;
    recognition.start();
}

/* ---------------- RUN ML ---------------- */
async function runMLRecommendation() {
    const query = document.getElementById("promptInput").value;
    const mood = document.getElementById("moodSlider").value;
    const quantum = document.getElementById("quantumToggle").checked;

    if (!query) {
        alert("Please enter movie description");
        return;
    }

    // Show loading overlay
    const overlay = document.getElementById("loadingOverlay");
    overlay.classList.add("active");

    try {
        const res = await fetch(`${API_URL}/recommend`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                query: query,
                genre: selectedGenre,
                language: selectedLanguage,
                mood: mood,
                quantum: quantum
            })
        });

        const data = await res.json();

        sessionStorage.setItem("lastResults", JSON.stringify(data));

        // Slight delay to let users see the spinner
        setTimeout(() => {
            overlay.classList.remove("active");
            window.location.href = "/results";
        }, 800); // 0.8s delay

    } catch (err) {
        overlay.classList.remove("active");
        console.error(err);
        alert("Backend not running. Start app.py");
    }
}


/* ---------------- CHATBOT ---------------- */
function toggleChat() {
    const win = document.getElementById("chatbot-window");
    win.style.display = win.style.display === "flex" ? "none" : "flex";
}

async function sendChat() {
    const input = document.getElementById("chatInput");
    const history = document.getElementById("chat-history");
    const msg = input.value.trim();
    if (!msg) return;

    history.innerHTML += `<div style="text-align:right;color:#60a5fa;margin:5px;">${msg}</div>`;
    input.value = "";

    try {
        const res = await fetch(`${API_URL}/chatbot`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        history.innerHTML += `<div style="text-align:left;color:#fff;margin:5px;">${data.reply}</div>`;
        history.scrollTop = history.scrollHeight;
    } catch {
        history.innerHTML += `<div style="color:red;">AI offline</div>`;
    }
}

/* ---------------- LOAD RESULTS PAGE ---------------- */
function loadResults() {
    const container = document.getElementById("resultsContainer");
    if (!container) return;

    const data = JSON.parse(sessionStorage.getItem("lastResults"));

    if (!data || data.length === 0) {
        container.innerHTML = "<p style='color:#aaa;'>No recommendations found</p>";
        return;
    }

    container.innerHTML = "";

    data.forEach(item => {
        const m = item.movie;

        container.innerHTML += `
        <div class="slide-card">
            <span class="match-score">${item.score}% Match</span>
            <img class="poster"
                 src="${m.poster || m.poster_url || 'https://placehold.co/300x450/222/fff?text=Movie'}">
            <div class="slide-info">
                <h3>${m.title}</h3>
                <p style="opacity:0.7">${m.language} | ${m.year || ""}</p>
                <p style="font-size:0.8rem;color:#8b5cf6">${item.reason}</p>
            </div>
        </div>`;
    });
}
