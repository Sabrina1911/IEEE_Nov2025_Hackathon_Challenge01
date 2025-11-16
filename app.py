import streamlit as st
from st_audiorec import st_audiorec
import os
from datetime import datetime
import json

# Simple lookup for key northern & southern locations (for Option B map)
CITY_COORDS = {
    # Northern regions / communities
    "Nunavut": {"lat": 63.1543, "lon": -75.3412},
    "Iqaluit": {"lat": 63.7467, "lon": -68.5170},
    "Yukon": {"lat": 64.2823, "lon": -135.0000},
    "Whitehorse": {"lat": 60.7212, "lon": -135.0568},
    "NWT": {"lat": 64.8255, "lon": -124.8457},
    "Yellowknife": {"lat": 62.4540, "lon": -114.3718},
    # Southern / urban centres
    "Toronto": {"lat": 43.6532, "lon": -79.3832},
    "Ottawa": {"lat": 45.4215, "lon": -75.6972},
    "Vancouver": {"lat": 49.2827, "lon": -123.1207},
    "Calgary": {"lat": 51.0447, "lon": -114.0719},
    "Edmonton": {"lat": 53.5461, "lon": -113.4938},
    "Winnipeg": {"lat": 49.8951, "lon": -97.1384},
    "Montreal": {"lat": 45.5019, "lon": -73.5674},
    "Barrie": {"lat": 44.3894, "lon": -79.6903},
    "NB": {"lat": 46.5653, "lon": -66.4619},  # New Brunswick as a province tag
}

# --- Paths for local assets ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# ✅ Single cover image for the home page (LOCAL FILE)
COVER_IMAGES = [
    {
        "path": os.path.join(ASSETS_DIR, "echo_cover_main.png"),
        "alt": "An elder and youth together, and a young person connecting by laptop",
    },
]

# 🔧 Turn the map on/off (for screenshots keep this False)
ENABLE_STORY_MAP = False

# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="Echo of the North",
    page_icon="🧭",
    layout="centered",
)

# 🔤 Global font + DARK THEME for every page
st.markdown(
    """
    <style>
    * {
        font-family: "Times New Roman", "Times", serif !important;
    }

    /* 🌌 Dark background for the whole app */
    body {
        background: radial-gradient(circle at top, #020617 0, #020617 40%, #000000 100%);
        color: #e5e7eb;
    }

    /* Main content card */
    .block-container {
    background: #020617;
    border-radius: 18px;
    padding: 1.5rem 2rem;
    margin-top: 1.5rem;        /* ✅ add this line */
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.9);
   }

    /* Make all headings / labels / text clearly visible */
    h1, h2, h3, h4, h5, h6,
    label,
    .stMarkdown, .stText, .stCaption, .stCheckbox, .stRadio, .stSelectbox {
        color: #e5e7eb !important;
    }

    .subtitle {
        font-size: 18px;
        color: #e5e7eb;
    }
    .tagline-small {
        font-size: 14px;
        font-style: italic;
        color: #cbd5f5;
    }
    .footnote {
        font-size: 12px;
        color: #9ca3af;
    }
    .role-pill {
        display:inline-block;
        padding:6px 14px;
        border-radius:999px;
        background:#111827;
        font-size:13px;
        color:#e5e7eb;
        margin-bottom:4px;
    }

    /* Aurora-style banners on dark */
    .nl-banner-elder {
        display:inline-block;
        padding:8px 18px;
        border-radius:999px;
        background:linear-gradient(90deg, #22c55e, #22d3ee, #60a5fa);
        color:#022c22;
        font-size:13px;
        font-weight:600;
        box-shadow:0 0 18px rgba(59, 130, 246, 0.6);
    }
    .nl-banner-youth {
        display:inline-block;
        padding:8px 18px;
        border-radius:999px;
        background:linear-gradient(90deg, #f472b6, #fb7185, #facc15);
        color:#4a044e;
        font-size:13px;
        font-weight:600;
        box-shadow:0 0 18px rgba(236, 72, 153, 0.6);
    }

    /* Hero image cropping */
    img[alt="An elder and youth together, and a young person connecting by laptop"] {
        max-height: 360px;
        width: 100%;
        object-fit: cover;
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ensure folders exist
os.makedirs("mock_data", exist_ok=True)
os.makedirs("assets", exist_ok=True)
REFLECTIONS_PATH = "mock_data/reflections.json"


# ----------------- SIMPLE ROUTER + ROLE STATE -----------------
def go(page: str):
    """Update current page in session state."""
    st.session_state["page"] = page


# Initialize page once
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Who is using the app right now?
if "user_role" not in st.session_state:
    # Two main modes: Elder vs Youth/Family
    st.session_state["user_role"] = "Elder / Knowledge Keeper"

# Last recording path
if "last_recording" not in st.session_state:
    st.session_state["last_recording"] = None  # raw audio file path

# Selected story for detail view
if "selected_story" not in st.session_state:
    st.session_state["selected_story"] = None


# ----------------- HELPERS FOR REFLECTIONS -----------------
def load_reflections():
    """Load reflections per story (simple dict: {key: [..]})"""
    if not os.path.exists(REFLECTIONS_PATH):
        return {}
    try:
        with open(REFLECTIONS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_reflections(data: dict):
    with open(REFLECTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ----------------- HOME / WELCOME -----------------
def show_home():
    st.markdown(
        "<h1 style='text-align:center; color:#e5e7eb;'>Echo of the North</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='subtitle' style='text-align:center;'>Preserving Canada’s northern voices beyond the internet.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='tagline-small' style='text-align:center;'>For northern communities where elders carry the stories and youth carry the future.</p>",
        unsafe_allow_html=True,
    )

    # ----- Single cover image just under the title -----
    current_cover = COVER_IMAGES[0]
    if os.path.exists(current_cover["path"]):
        st.image(
            current_cover["path"],
            caption=current_cover["alt"],
            use_column_width=True,
        )
    else:
        st.warning(
            f"Cover image not found at `{current_cover['path']}`. "
            "Make sure the file exists in the assets folder."
        )

    st.write("")

    # -------- Who is using the app today? (Elder vs Youth) --------
    st.markdown(
        "<p style='text-align:center; font-size:15px; color:#e5e7eb;'>Who is using Echo of the North today?</p>",
        unsafe_allow_html=True,
    )
    current_role = st.session_state.get("user_role", "Elder / Knowledge Keeper")

    # Our own visible label
    st.markdown(
        "<p style='text-align:center; font-weight:700; color:#e5e7eb;'>Choose your role</p>",
        unsafe_allow_html=True,
    )

    # Centered selectbox instead of radio (always clearly visible)
    left, center, right = st.columns([1, 2, 1])
    with center:
        role = st.selectbox(
            "I am using Echo of the North as a…",
            options=["Elder / Knowledge Keeper", "Youth / Family Member"],
            index=0 if current_role.startswith("Elder") else 1,
            label_visibility="collapsed",  # we already show our own label above
        )
    st.session_state["user_role"] = role

    # Role-specific banner
    banner_label = "Voices of the North" if role.startswith("Elder") else "Echoes of Home"
    banner_class = "nl-banner-elder" if role.startswith("Elder") else "nl-banner-youth"
    st.markdown(
        f"<p style='text-align:center; margin-top:4px;'><span class='{banner_class}'>{banner_label}</span></p>",
        unsafe_allow_html=True,
    )

    # Small pill to reinforce selection
    st.markdown(
        f"<p style='text-align:center;'><span class='role-pill'>Mode: {role}</span></p>",
        unsafe_allow_html=True,
    )
    st.write("")

    col1, col2 = st.columns(2)
    if role.startswith("Elder"):
        record_label = "🎙 Share a New Story"
        explore_label = "📚 Listen to Story Library"
    else:
        record_label = "🎙 Add Your Memory / Reflection"
        explore_label = "📚 Explore Story Library"

    with col1:
        st.button(
            record_label,
            use_container_width=True,
            on_click=go,
            args=("record",),
        )
    with col2:
        st.button(
            explore_label,
            use_container_width=True,
            on_click=go,
            args=("gallery",),
        )

    st.write("")
    st.button(
        "🎥 Watch the Journey",
        use_container_width=True,
        on_click=go,
        args=("journey",),
    )

    st.write("---")
    st.markdown(
        "<p class='tagline-small' style='text-align:center;'>Designed for remote Indigenous communities across Nunavut, Yukon, NWT, and Northern Ontario.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='footnote' style='text-align:center;'>Even when youth move south, their roots stay connected here.</p>",
        unsafe_allow_html=True,
    )


# ----------------- SCREEN 2: RECORD STORY -----------------
def show_record():
    st.button("← Back to Home", on_click=lambda: go("home"))
    role = st.session_state.get("user_role", "Elder / Knowledge Keeper")

    # Role badge
    st.markdown(
        f"<span style='font-size:13px; padding:5px 12px; border-radius:999px; "
        f"background-color:#111827; color:#e5e7eb;'>Mode: {role}</span>",
        unsafe_allow_html=True,
    )

    banner_label = "Voices of the North" if role.startswith("Elder") else "Echoes of Home"
    banner_class = "nl-banner-elder" if role.startswith("Elder") else "nl-banner-youth"
    st.markdown(
        f"<p style='margin-top:10px;'><span class='{banner_class}'>{banner_label}</span></p>",
        unsafe_allow_html=True,
    )

    st.title("Record a Story")

    if role.startswith("Elder"):
        st.markdown("**Whose voice are we preserving today?**")
        st.write(
            "Ask an elder to share a memory, a legend, or a winter story "
            "in Inuktitut, Cree, or Ojibwe."
        )
    else:
        st.markdown("**What memory or reflection would you like to add?**")
        st.write(
            "As a youth or family member, you can record a response, reflection, "
            "or your own version of a story you grew up hearing — even if you now live in the city."
        )

    st.write("---")
    st.markdown("### 🎙 Tap to start recording")

    audio_bytes = st_audiorec()  # returns raw WAV bytes or None

    if audio_bytes is not None:
        st.markdown("### ▶️ Preview your recording")
        st.audio(audio_bytes, format="audio/wav")
        st.write("")
        st.write("")

        st.markdown("### ✅ When you're happy with it")
        _, c2, _ = st.columns([1, 2, 1])
        with c2:
            if st.button(
                "Save recording & go to Transcription",
                type="primary",
                use_container_width=True,
            ):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"mock_data/story_{timestamp}.wav"
                with open(filename, "wb") as f:
                    f.write(audio_bytes)
                st.session_state["last_recording"] = filename
                st.success("Recording saved locally.")
                go("transcribe")

    st.info("All recordings stay on this device to respect community ownership.")


# ----------------- SCREEN 3: TRANSCRIPTION (MOCK) -----------------
def show_transcription():
    st.button("← Back to Record", on_click=lambda: go("record"))
    st.title("Transcription & Translation")

    audio_file = st.session_state.get("last_recording")
    if not audio_file:
        st.warning("No recording found. Please record a story first.")
        return

    st.markdown("#### Story Title")
    title = st.text_input("Story Title", value="The Winter of 1979")

    col_lang, _ = st.columns([1, 2])
    with col_lang:
        language = st.selectbox("Language", ["Inuktitut", "Cree", "Ojibwe"])

    st.write("---")
    col1, col2 = st.columns(2)

    demo_original = (
        "(Demo) [Offline AI transcription of your recording would appear here. "
        "You can edit this text to match the elder's exact words.]"
    )
    demo_translation = (
        "(Demo) It was the coldest winter we remember, when the snowbanks hid the houses."
    )

    with col1:
        st.markdown(f"**Original ({language})**")
        original_text = st.text_area(
            "Original text",
            value=demo_original,
            height=180,
        )

    with col2:
        st.markdown("**English Translation**")
        translation = st.text_area(
            "English text",
            value=demo_translation,
            height=180,
        )
        st.caption("Prototype: using a lightweight offline AI model (simulated here).")

    if st.button("Save to Story Library", type="primary"):
        story_record = {
            "title": title,
            "language": language,
            "region": "Nunavut",
            "audio_file": audio_file,
            "original": original_text,
            "translation": translation,
            "recorded_by_role": st.session_state.get(
                "user_role", "Elder / Knowledge Keeper"
            ),
        }
        stories_path = "mock_data/stories.json"
        existing = []
        if os.path.exists(stories_path):
            with open(stories_path, "r", encoding="utf-8") as f:
                try:
                    existing = json.load(f)
                except json.JSONDecodeError:
                    existing = []

        existing.append(story_record)

        with open(stories_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)

        st.success("Story saved to your local library.")
        go("gallery")


# ----------------- SCREEN 4: GALLERY -----------------
def show_gallery():
    st.button("← Back to Home", on_click=lambda: go("home"))
    st.title("Community Story Library – Canada’s North")

    stories_path = "mock_data/stories.json"
    if not os.path.exists(stories_path):
        st.info("No stories saved yet. Record a story to see it here.")
        return

    with open(stories_path, "r", encoding="utf-8") as f:
        stories = json.load(f)

    st.markdown(
        "Stories recorded in Nunavut, Yukon, and beyond — accessible from anywhere in Canada."
    )

    if st.button("🔗 Connect from Anywhere"):
        st.info(
            "Moved to Toronto, Ottawa, or Vancouver? You can still listen, learn, "
            "and add your memories to these stories."
        )

    st.write("---")

    if not stories:
        st.info("No stories saved yet. Record a story to see it here.")
        return

    for idx, story in enumerate(stories):
        lang = story.get("language", "Unknown")
        region = story.get("region", "Unknown")
        header = f"{story['title']} · {region}"
        with st.expander(header):
            st.markdown(
                f"<span style='display:inline-block; padding:4px 10px; "
                f"border-radius:999px; background-color:#111827; "
                f"color:#e5e7eb; font-size:12px;'>🗣 {lang}</span>",
                unsafe_allow_html=True,
            )
            st.write(f"**Region:** {region}")
            if "recorded_by_role" in story:
                st.write(f"**Recorded by:** {story['recorded_by_role']}")
            st.write("**Original:**")
            st.write(story["original"])
            st.write("**English Translation:**")
            st.write(story["translation"])

            if os.path.exists(story["audio_file"]):
                st.audio(story["audio_file"], format="audio/wav")

            if st.button(
                "Open Story Detail",
                key=f"open_detail_{idx}",
            ):
                st.session_state["selected_story"] = story
                go("story_detail")


# ----------------- SCREEN 5: STORY DETAIL + MEMORY THREAD -----------------
def show_story_detail():
    story = st.session_state.get("selected_story")
    if not story:
        st.warning("No story selected. Please choose one from the library.")
        if st.button("Back to Library"):
            go("gallery")
        return

    st.button("← Back to Library", on_click=lambda: go("gallery"))

    title = story.get("title", "Untitled Story")
    st.title(title)

    meta_role = story.get("recorded_by_role", "Unknown")
    language = story.get("language", "Unknown")
    region = story.get("region", "Unknown")
    st.markdown(
        f"**Original language:** {language} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"**Region:** {region} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"**Recorded by:** {meta_role}"
    )

    st.markdown(
        f"<span style='display:inline-block; margin-top:4px; padding:4px 10px; "
        f"border-radius:999px; background-color:#111827; "
        f"color:#e5e7eb; font-size:12px;'>🗣 {language}</span>",
        unsafe_allow_html=True,
    )

    audio_file = story.get("audio_file")
    if audio_file and os.path.exists(audio_file):
        st.markdown("### 🎧 Listen to the story")
        st.audio(audio_file, format="audio/wav")

    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Original Text")
        st.write(story.get("original", ""))
    with col2:
        st.markdown("#### English Translation")
        st.write(story.get("translation", ""))

    st.write("---")

    st.markdown("### 🧵 Memory Thread – Voices Across Canada")
    reflections = load_reflections()

    audio_key = story.get("audio_file", "")
    primary_key = audio_key or title

    if primary_key not in reflections and title in reflections and audio_key:
        reflections[primary_key] = reflections.pop(title)
        save_reflections(reflections)

    story_reflections = reflections.get(primary_key, [])

    listener_locations = sorted(
        {
            r.get("location", "").strip()
            for r in story_reflections
            if r.get("location", "").strip()
        }
    )
    if listener_locations:
        locations_str = " · ".join(listener_locations)
        st.markdown(
            f"<p style='font-size:14px; padding:6px 10px; "
            f"border-radius:999px; background-color:#111827; "
            f"color:#e5e7eb; display:inline-block;'>"
            f"Recorded in <strong>{region}</strong> · "
            f"Heard in {locations_str}"
            f"</p>",
            unsafe_allow_html=True,
        )

        import pandas as pd

        points = []
        if region in CITY_COORDS:
            c = CITY_COORDS[region]
            points.append({"lat": c["lat"], "lon": c["lon"]})
        for loc in listener_locations:
            if loc in CITY_COORDS:
                c = CITY_COORDS[loc]
                points.append({"lat": c["lat"], "lon": c["lon"]})

        if points and ENABLE_STORY_MAP:
            st.caption("Where this northern story is travelling today:")
            df_points = pd.DataFrame(points)
            st.map(df_points, use_container_width=True)

    if not story_reflections:
        st.info("No memories have been added to this story yet.")
    else:
        for ref in story_reflections:
            who = ref.get("name", "Community Member")
            where = ref.get("location", "")
            by_role = ref.get("by_role", "")
            text_val = ref.get("text", "")
            ts = ref.get("timestamp", "")

            header_line = f"**{who}**"
            if where:
                header_line += f" – 📍 {where}"
            if by_role:
                header_line += f"  ·  _{by_role}_"

            with st.container(border=True):
                st.markdown(header_line)
                st.write(text_val)
                if ts:
                    st.caption(ts)

    st.write("---")

    st.markdown("#### Add your memory or reflection")
    current_role = st.session_state.get("user_role", "Youth / Family Member")
    default_name = (
        "Youth listener" if current_role.startswith("Youth") else "Community member"
    )

    if "memory_form_seed" not in st.session_state:
        st.session_state["memory_form_seed"] = 0
    seed = st.session_state["memory_form_seed"]

    name = st.text_input(
        "Your name (or how you want to be shown):",
        value=default_name,
        key=f"memory_name_{seed}",
    )
    location = st.text_input(
        "Where are you listening from? (e.g., Toronto, Nunavut, Vancouver)",
        key=f"memory_location_{seed}",
    )
    text = st.text_area(
        "What does this story mean to you?",
        placeholder="Type a short reflection about how this story connects to your life...",
        key=f"memory_text_{seed}",
    )

    if st.button("Add My Memory to This Story", type="primary", key=f"add_memory_{seed}"):
        if not text.strip():
            st.warning("Please enter a short reflection before adding.")
        else:
            new_ref = {
                "name": (name or default_name).strip(),
                "location": location.strip(),
                "text": text.strip(),
                "by_role": current_role,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            story_reflections = reflections.get(primary_key, [])
            story_reflections.append(new_ref)
            reflections[primary_key] = story_reflections
            save_reflections(reflections)
            st.success("Your memory was added to this story.")
            st.session_state["memory_form_seed"] += 1
            st.session_state["selected_story"] = story
            st.rerun()


# ----------------- SCREEN 6: WATCH THE JOURNEY (VIDEO PAGE) -----------------
def show_journey():
    st.button("← Back to Home", on_click=lambda: go("home"))
    st.title("Watch the Journey")
    st.markdown(
        """
        This page is a small **Journey Hub** for Echo of the North —  
        showing how Indigenous stories and youth journeys travel between
        northern communities and southern cities.
        """
    )

    st.write("---")

    st.markdown("### 🌍 Story + Journey Panel")
    videos = [
        {
            "title": "Indigenous Canada – A Story to Tell",
            "url": "https://www.youtube.com/watch?v=OzpKdPEBLfQ",
            "desc": "A short documentary capturing the resilience and storytelling traditions of Indigenous peoples across Canada.",
        },
        {
            "title": "Language Keepers – Reviving Our Words",
            "url": "https://www.youtube.com/watch?v=QKTh0U4RJnc",
            "desc": "A look into how Indigenous communities across Canada are reclaiming and teaching their ancestral languages.",
        },
    ]

    selected = st.selectbox(
        "Choose a journey to explore:",
        options=[v["title"] for v in videos],
    )
    chosen = next(v for v in videos if v["title"] == selected)

    st.video(chosen["url"])
    st.caption(chosen["desc"])

    st.write("---")

    st.markdown("### 🪶 Heritage & Skills Discovery Deck")
    st.caption("Each journey suggests a simple action that keeps culture alive in everyday life.")

    with st.expander("🎧 Learn 5 words from this story in your language"):
        st.write(
            "Try learning words like **snow, home, wind, family, fire** "
            "in Inuktitut, Cree, or Ojibwe — and teach them to a friend."
        )

    with st.expander("🎨 Try a northern craft using recycled materials"):
        st.write(
            "Make a small snow-catcher, bead pattern, or symbolic object using "
            "recycled materials (bottle caps, cardboard, leftover fabric)."
        )

    with st.expander("🎙 Interview an Elder using your phone (for your community only)"):
        st.write(
            "Ask an Elder: *“What is one story you wish more youth remembered?”* "
            "Record it safely with their permission — this prototype could one day store such clips offline."
        )

    with st.expander("🏙 Capture your city soundscape"):
        st.write(
            "If you're living in the south, record **15 seconds** of city sounds that remind you of home "
            "and describe why in the Reflection section of a story."
        )

    st.write("---")
    st.markdown(
        """
        **What this page represents for the roadmap:**
        - A future space where **local elders’ videos** and **youth journey clips** live together  
        - Guided actions that help youth **practice language, craft, and reflection**  
        - A bridge between **northern roots** and **modern city life**, built into the same app  
        """
    )


# ----------------- ROUTER -----------------
page = st.session_state.get("page", "home")
if page == "home":
    show_home()
elif page == "record":
    show_record()
elif page == "transcribe":
    show_transcription()
elif page == "gallery":
    show_gallery()
elif page == "story_detail":
    show_story_detail()
elif page == "journey":
    show_journey()
