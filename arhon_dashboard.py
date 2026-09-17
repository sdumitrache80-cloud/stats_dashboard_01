import streamlit as st

# 1. SETUP & CUSTOM CSS
st.set_page_config(page_title="ARHON Synergy Matrix", layout="wide")

custom_css = """
<style>
.arhon-tooltip { position: relative; display: inline-block; color: #1f77b4; border-bottom: 1px dotted #1f77b4; cursor: help; font-weight: bold; }
.arhon-tooltip .tooltiptext { visibility: hidden; width: 280px; background-color: #2c3e50; color: #ecf0f1; text-align: left; border-radius: 6px; padding: 10px; position: absolute; z-index: 1; bottom: 125%; left: 50%; margin-left: -140px; opacity: 0; transition: opacity 0.3s; font-weight: normal; font-size: 13px; line-height: 1.4; box-shadow: 0px 4px 6px rgba(0,0,0,0.3); }
.arhon-tooltip:hover .tooltiptext { visibility: visible; opacity: 1; }
.flow-box { background-color: #2b2b2b; color: #ffffff; padding: 8px; border-radius: 5px; text-align: center; font-family: monospace; font-size: 13px; margin-bottom: 10px; box-shadow: 0px 2px 4px rgba(0,0,0,0.2); }
.pillar-header { background-color: #1e1e1e; padding: 10px; border-radius: 5px; text-align: center; margin-top: 10px; margin-bottom: 15px; border: 1px solid #444; }
.pillar-header h3 { color: #ffffff !important; margin: 0; padding: 0; }
.radiance-box { background-color: #f8f9fa; border-left: 4px solid #b0bec5; padding: 10px; margin-bottom: 15px; color: #000; border-radius: 0px 5px 5px 0px;}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def inline_tooltip(text, tooltip_content):
    return f'<div class="arhon-tooltip">{text}<span class="tooltiptext">{tooltip_content}</span></div>'

# 2. HEADER & RULES
st.title("ARHON: Attribute & Synergy Visualizer")

col_rules1, col_rules2 = st.columns(2)
with col_rules1:
    st.markdown("### 📜 THE SYSTEMIC RULES")
    st.info(
        "**The 1:1:1 Equilibrium Rule:** Every single one of the 30 Hardware attributes serves as a Primary Engine exactly once, "
        "a Secondary Engine exactly once, and a Cross-Discipline Edge exactly once across the entire 30-Software list.\n\n"
        "**The Synergy Formula:** Every Learned Skill is derived from three genetic engines: Primary [50%] + Secondary [30%] + Cross-Discipline [20%]."
    ) #[cite: 1]
with col_rules2:
    st.markdown("### 🧬 BIOLOGICAL CONSTANTS (Hardware)")
    st.warning(
        "**Universal Application:** Every single entity (Player Avatars and AI Agents) utilizes this exact 60-Stat biological architecture.\n\n"
        "**The Math:**\n"
        "- **Pioneers:** Start at a flat 3/10 in all Hardware stats. Gain exactly +10 points to allocate at 'Coming of Age'.\n"
        "- **Heirs:** Hardware is rolled 1 through 8 (Genetic Lottery 80/20 parent split).\n"
        "- **The Soft Cap (10):** Absolute zenith of baseline human biology. Cannot be raised past 10 via allocation.\n"
        "- **The Hard Cap (20):** 11-20 requires Ascension/Relics. This is 'Acquired Mastery' and does not pass to heirs."
    ) #[cite: 1]
st.markdown("---")

# Global UI Elements
tt_floor = inline_tooltip("Genetic Floor", "The unbreakable baseline dictated by your Hardware. Decay never drops a skill below this number.") #[cite: 1]
tt_synergy = inline_tooltip("Synergy Factor", "Your Hardware dictates how fast you learn the gameplay-driven Software arts/skills/attributes. Multiplies Gross XP.") #[cite: 1]

def draw_engine_block(name, icon, p_name, p_val, s_name, s_val, c_name, c_val):
    floor = (p_val * 2.5) + (s_val * 1.5) + (c_val * 1.0) #[cite: 1]
    syn = (p_val * 0.5) + (s_val * 0.3) + (c_val * 0.2) #[cite: 1]
    st.markdown(f"### {icon} {name}")
    st.markdown(f"<div class='flow-box'>({p_name} 50%) + ({s_name} 30%) + ({c_name} 20%) ➔ ⚙️ {name} Outputs</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#e8f4f8; padding:8px; border-radius:5px; color:#000; margin-bottom:5px;'><b>↳ {tt_floor}:</b> {floor:.1f} / 100</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#e8f8ec; padding:8px; border-radius:5px; color:#000; margin-bottom:15px;'><b>↳ {tt_synergy}:</b> {syn:.2f}</div>", unsafe_allow_html=True)

# Master Column Headers
col_h, col_m, col_s = st.columns([1, 1.6, 1])
with col_h: st.header("Hardware (1-10)")
with col_m: st.header("The Synergy Engine")
with col_s: st.header("Software (1-100)")

# ==========================================
# EXPANDER 1: THE BODY PILLAR
# ==========================================
with st.expander("🔴 THE BODY PILLAR", expanded=False):
    c1, c2, c3 = st.columns([1, 1.6, 1])
    with c1:
        st.markdown("<div class='pillar-header'><h3>🔴 BODY HARDWARE</h3></div>", unsafe_allow_html=True)
        str_hw = st.slider("Strength", 1, 10, 3, help="Exert physical force. Fuels: [P] Might | [S] Block | [C] Fortitude") #[cite: 1]
        agi_hw = st.slider("Agility", 1, 10, 3, help="Move quickly/balance. Fuels: [P] Stealth | [S] Evasion | [C] Reflexes") #[cite: 1]
        con_hw = st.slider("Constitution", 1, 10, 3, help="Physical hardiness. Fuels: [P] Fortitude | [S] Investigation | [C] Meditation") #[cite: 1]
        vig_hw = st.slider("Vigor", 1, 10, 3, help="Active strength/energy. Fuels: [P] Acrobatics | [S] Dodge | [C] None") #[cite: 1]
        coo_hw = st.slider("Coordination", 1, 10, 3, help="Fine-motor control. Fuels: [P] Dexterity | [S] Parry | [C] Acrobatics") #[cite: 1]
        sen_hw = st.slider("Sensory Acuity", 1, 10, 3, help="Nervous system speed. Fuels: [P] Parry | [S] Finesse | [C] Perception") #[cite: 1]
        end_hw = st.slider("Endurance", 1, 10, 3, help="Cardiovascular ceiling. Fuels: [P] Dodge | [S] Meditation | [C] Concentration") #[cite: 1]
        kin_hw = st.slider("Kinetics", 1, 10, 3, help="Burst speed/explosive power. Fuels: [P] Reflexes | [S] Might | [C] Intimidation") #[cite: 1]
        fle_hw = st.slider("Flexibility", 1, 10, 3, help="Joint mobility. Fuels: [P] Finesse | [S] Performance | [C] Deception") #[cite: 1]
        den_hw = st.slider("Density", 1, 10, 3, help="Bone mass/weight. Fuels: [P] Block | [S] Intimidation | [C] Discipline") #[cite: 1]

    with c3:
        st.markdown("<div class='pillar-header'><h3>🔴 BODY SOFTWARE</h3></div>", unsafe_allow_html=True)
        might_sw = st.slider("Might Proficiency", 1, 100, 1, help="Physical strength, power, and the ability to exert force. The learned leverage and application of raw Meta Strength.") #[cite: 1]
        dex_sw = st.slider("Dexterity Proficiency", 1, 100, 1, help="The skill, grace, and agility in physical movement, particularly the ability to use one's hands with precision and ease.") #[cite: 1]
        fin_sw = st.slider("Finesse Proficiency", 1, 100, 1, help="The execution of actions with highly refined skill, delicacy, and precise coordination.") #[cite: 1]
        acr_sw = st.slider("Acrobatics Proficiency", 1, 100, 1, help="The skill of performing feats of balance, agility, and bodily coordination.") #[cite: 1]
        ste_sw = st.slider("Stealth Proficiency", 1, 100, 1, help="The ability to move silently and remain unseen by others.") #[cite: 1]
        ref_sw = st.slider("Reflexes Proficiency", 1, 100, 1, help="The body's involuntary and rapid response to sudden stimuli.") #[cite: 1]
        par_sw = st.slider("Parry Proficiency", 1, 100, 1, help="To deflect an attack, usually with a weapon or your hand, to prevent it from hitting you.") #[cite: 1]
        blo_sw = st.slider("Block Proficiency", 1, 100, 1, help="A defensive move where you use a solid object—usually a shield—to stop an attack from hitting your body.") #[cite: 1]
        dod_sw = st.slider("Dodge Proficiency", 1, 100, 1, help="To move quickly to one side to avoid being hit by something or someone.") #[cite: 1]
        eva_sw = st.slider("Evasion Proficiency", 1, 100, 1, help="The act of avoiding or escaping something through cleverness, trickery, or physical movement.") #[cite: 1]

    with c2:
        st.markdown("<div class='pillar-header'><h3>🔴 BODY ENGINE</h3></div>", unsafe_allow_html=True)
        draw_engine_block("Might", "⚔️", "🔴 Strength", str_hw, "🔴 Kinetics", kin_hw, "🟡 Will", 3)
        draw_engine_block("Dexterity", "🪡", "🔴 Coord.", coo_hw, "🟡 Aptitude", 3, "🔵 Vitality", 3)
        draw_engine_block("Finesse", "🎯", "🔴 Flex.", fle_hw, "🔴 Sens.Acuity", sen_hw, "🟡 Intuition", 3)
        draw_engine_block("Acrobatics", "🤸", "🔴 Vigor", vig_hw, "🟡 Spatial", 3, "🔴 Coord.", coo_hw)
        draw_engine_block("Stealth", "🥷", "🔴 Agility", agi_hw, "🔵 Aura", 3, "🟡 Temperament", 3)
        draw_engine_block("Reflexes", "⚡", "🔴 Kinetics", kin_hw, "🟡 Wits", 3, "🔴 Agility", agi_hw)
        draw_engine_block("Parry", "🤺", "🔴 Sens.Acuity", sen_hw, "🔴 Coord.", coo_hw, "🟡 Lucidity", 3)
        draw_engine_block("Block", "🛡️", "🔴 Density", den_hw, "🔴 Strength", str_hw, "🔵 Conviction", 3)
        draw_engine_block("Dodge", "💨", "🔴 Endurance", end_hw, "🟡 Intuition", 3, "🔴 Vigor", vig_hw)
        draw_engine_block("Evasion", "🏃", "🟡 Wits", 3, "🔴 Agility", agi_hw, "🟡 Spatial", 3)
        
        st.markdown("### ⚙️ BODY DERIVED PHYSICS")
        st.markdown("<div class='flow-box'>(20kg Base) + (🔴 Strength × 3) + (🔴 Density × 2) ➔ ⚙️ Payload Limits</div>", unsafe_allow_html=True) #[cite: 1]
        encumb = 20 + (str_hw * 3) + (den_hw * 2) #[cite: 1]
        tt_encumb = inline_tooltip("Encumbrance Threshold", "Characters face a strict carrying limit of 70kg. Exceeding your specific threshold severely penalizes Agility and Endurance.") #[cite: 1]
        st.markdown(f"<div style='background-color:#fce8e8; padding:10px; border-radius:5px; color:#000;'><b>↳ {tt_encumb}:</b> {encumb} kg</div>", unsafe_allow_html=True)

# ==========================================
# EXPANDER 2: THE MIND PILLAR
# ==========================================
with st.expander("🟡 THE MIND PILLAR", expanded=False):
    c1, c2, c3 = st.columns([1, 1.6, 1])
    with c1:
        st.markdown("<div class='pillar-header'><h3>🟡 MIND HARDWARE</h3></div>", unsafe_allow_html=True)
        int_hw = st.slider("Intellect", 1, 10, 3, help="Reasoning/abstract. Fuels: [P] Intelligence | [S] Reasoning | [C] Charisma") #[cite: 1]
        wit_hw = st.slider("Wits", 1, 10, 3, help="Quick perception. Fuels: [P] Evasion | [S] Reflexes | [C] Reasoning") #[cite: 1]
        mem_hw = st.slider("Memory", 1, 10, 3, help="Recall information. Fuels: [P] Tactics | [S] Intelligence | [C] Wisdom") #[cite: 1]
        wil_hw = st.slider("Will", 1, 10, 3, help="Internal driving force. Fuels: [P] Concentration | [S] Deception | [C] Meditation") #[cite: 1]
        intuit_hw = st.slider("Intuition", 1, 10, 3, help="Subconscious processing. Fuels: [P] Wisdom | [S] Animal Handling | [C] Finesse") #[cite: 1]
        luc_hw = st.slider("Lucidity", 1, 10, 3, help="Clarity under stress. Fuels: [P] Investigation | [S] Concentration | [C] Parry") #[cite: 1]
        apt_hw = st.slider("Aptitude", 1, 10, 3, help="Pattern recognition. Fuels: [P] Learning | [S] Dexterity | [C] Intelligence") #[cite: 1]
        spa_hw = st.slider("Spatial Awareness", 1, 10, 3, help="Internal compass. Fuels: [P] Perception | [S] Acrobatics | [C] Evasion") #[cite: 1]
        tem_hw = st.slider("Temperament", 1, 10, 3, help="Emotional baseline. Fuels: [P] Deception/Discipline | [S] Persuasion | [C] Stealth") #[cite: 1]
        cal_hw = st.slider("Calculation", 1, 10, 3, help="Raw math processing. Fuels: [P] Reasoning | [S] Tactics | [C] Willpower") #[cite: 1]

    with c3:
        st.markdown("<div class='pillar-header'><h3>🟡 MIND SOFTWARE</h3></div>", unsafe_allow_html=True)
        intel_sw = st.slider("Intelligence Proficiency", 1, 100, 1, help="The capacity for logical thought, problem-solving, and understanding complex information.") #[cite: 1]
        reas_sw = st.slider("Reasoning Proficiency", 1, 100, 1, help="The process of drawing logical conclusions and making judgments from available facts or premises.") #[cite: 1]
        wis_sw = st.slider("Wisdom Proficiency", 1, 100, 1, help="The application of experience, intuition, and deep understanding to make sound judgments.") #[cite: 1]
        conc_sw = st.slider("Concentration Proficiency", 1, 100, 1, help="The ability to direct all mental focus onto a single task or thought.") #[cite: 1]
        disc_sw = st.slider("Discipline Proficiency", 1, 100, 1, help="The practice of self-control, focus, and strict adherence to rules or training.") #[cite: 1]
        learn_sw = st.slider("Learning Proficiency", 1, 100, 1, help="The active process of acquiring new knowledge, skills, or behaviors through study or experience.") #[cite: 1]
        perc_sw = st.slider("Perception Proficiency", 1, 100, 1, help="The ability to see, hear, or become aware of things through the physical senses.") #[cite: 1]
        willp_sw = st.slider("Willpower Proficiency", 1, 100, 1, help="The conscious and deliberate control over one's own impulses and actions.") #[cite: 1]
        tact_sw = st.slider("Tactics Proficiency", 1, 100, 1, help="The trained application of battlefield geometry and strategy in real-time scenarios.") #[cite: 1]
        inv_sw = st.slider("Investigation Proficiency", 1, 100, 1, help="The trained, methodical skill of searching an area to uncover hidden clues, tracks, or truths.") #[cite: 1]

    with c2:
        st.markdown("<div class='pillar-header'><h3>🟡 MIND ENGINE</h3></div>", unsafe_allow_html=True)
        draw_engine_block("Intelligence", "🧠", "🟡 Intellect", int_hw, "🟡 Memory", mem_hw, "🟡 Aptitude", apt_hw)
        draw_engine_block("Reasoning", "🧩", "🟡 Calculation", cal_hw, "🟡 Intellect", int_hw, "🟡 Wits", wit_hw)
        draw_engine_block("Wisdom", "🦉", "🟡 Intuition", intuit_hw, "🔵 Empathy", 3, "🟡 Memory", mem_hw)
        draw_engine_block("Concentration", "🧘", "🟡 Will", wil_hw, "🟡 Lucidity", luc_hw, "🔴 Endurance", end_hw)
        draw_engine_block("Discipline", "📏", "🟡 Temperament", tem_hw, "🔴 Endurance", end_hw, "🔴 Density", den_hw)
        draw_engine_block("Learning", "📚", "🟡 Aptitude", apt_hw, "🔵 Fervor", 3, "🟡 Intellect", int_hw)
        draw_engine_block("Perception", "👁️", "🟡 Spatial", spa_hw, "🔵 Resonance", 3, "🔴 Sens.Acuity", sen_hw)
        draw_engine_block("Willpower", "🛡️", "🔵 Conviction", 3, "🔵 Soul", 3, "🟡 Calculation", cal_hw)
        draw_engine_block("Tactics", "🗺️", "🟡 Memory", mem_hw, "🟡 Calculation", cal_hw, "🔵 Aura", 3)
        draw_engine_block("Investigation", "🔍", "🟡 Lucidity", luc_hw, "🔴 Constitution", con_hw, "🔵 Empathy", 3)

# ==========================================
# EXPANDER 3: THE ESSENCE PILLAR
# ==========================================
with st.expander("🔵 THE ESSENCE PILLAR", expanded=False):
    c1, c2, c3 = st.columns([1, 1.6, 1])
    with c1:
        st.markdown("<div class='pillar-header'><h3>🔵 ESSENCE HARDWARE</h3></div>", unsafe_allow_html=True)
        sou_hw = st.slider("Soul", 1, 10, 3, help="Incorporeal identity. Fuels: [P] Meditation | [S] Willpower | [C] None") #[cite: 1]
        spi_hw = st.slider("Spirit", 1, 10, 3, help="Prevailing mood. Fuels: [P] Leadership | [S] Charisma | [C] None") #[cite: 1]
        vit_hw = st.slider("Vitality", 1, 10, 3, help="Capacity for survival. Fuels: [P] Performance | [S] Fortitude | [C] Dexterity") #[cite: 1]
        fat_hw = st.slider("Fate", 1, 10, 3, help="Intervention. Fuels: [P] None | [S] None | [C] Diplomacy/Animal Handling") #[cite: 1]
        pre_hw = st.slider("Presence", 1, 10, 3, help="Magnetic weight. Fuels: [P] Charisma | [S] Leadership | [C] Persuasion") #[cite: 1]
        aur_hw = st.slider("Aura", 1, 10, 3, help="Spiritual footprint. Fuels: [P] Persuasion | [S] Stealth/Deception | [C] Tactics") #[cite: 1]
        res_hw = st.slider("Resonance", 1, 10, 3, help="Magical attunement. Fuels: [P] Diplomacy | [S] Perception | [C] None") #[cite: 1]
        convi_hw = st.slider("Conviction", 1, 10, 3, help="Unshakeable belief. Fuels: [P] Willpower | [S] Diplomacy | [C] Block") #[cite: 1]
        emp_hw = st.slider("Empathy", 1, 10, 3, help="Emotional connection. Fuels: [P] Animal Handling | [S] Wisdom | [C] Investigation") #[cite: 1]
        fer_hw = st.slider("Fervor", 1, 10, 3, help="Spiritual intensity. Fuels: [P] Intimidation | [S] Learning | [C] Leadership") #[cite: 1]

    with c3:
        st.markdown("<div class='pillar-header'><h3>🔵 ESSENCE SOFTWARE</h3></div>", unsafe_allow_html=True)
        cha_sw = st.slider("Charisma Proficiency", 1, 100, 1, help="A compelling attractiveness, charm, or magnetic personality that inspires devotion in others.") #[cite: 1]
        per_sw = st.slider("Persuasion Proficiency", 1, 100, 1, help="The social skill of convincing others to agree with an idea, take an action, or change their beliefs.") #[cite: 1]
        lea_sw = st.slider("Leadership Proficiency", 1, 100, 1, help="The capacity to guide, inspire, and organize a group toward a common goal.") #[cite: 1]
        for_sw = st.slider("Fortitude Proficiency", 1, 100, 1, help="Mental and emotional strength in facing difficulty, adversity, or physical pain.") #[cite: 1]
        int_sw = st.slider("Intimidation Proficiency", 1, 100, 1, help="The trained use of presence and physical threat to force compliance or induce fear.") #[cite: 1]
        dec_sw = st.slider("Deception Proficiency", 1, 100, 1, help="The practiced art of masking truth, manipulating intent, and maintaining a false persona under scrutiny.") #[cite: 1]
        dip_sw = st.slider("Diplomacy Proficiency", 1, 100, 1, help="The formal practice of negotiation, etiquette, and navigating the feudal hierarchies of Kosmegalo.") #[cite: 1]
        med_sw = st.slider("Meditation Proficiency", 1, 100, 1, help="The active, practiced methodology of centering the spirit to rapidly restore stamina and mental fatigue.") #[cite: 1]
        prf_sw = st.slider("Performance Proficiency", 1, 100, 1, help="The practiced art of storytelling, music, or distraction to capture the attention of a room.") #[cite: 1]
        ani_sw = st.slider("Animal Handling Proficiency", 1, 100, 1, help="The spiritual and practiced bond used to train, calm, and command beasts.") #[cite: 1]

    with c2:
        st.markdown("<div class='pillar-header'><h3>🔵 ESSENCE ENGINE</h3></div>", unsafe_allow_html=True)
        draw_engine_block("Charisma", "✨", "🔵 Presence", pre_hw, "🔵 Spirit", spi_hw, "🟡 Intellect", int_hw)
        draw_engine_block("Persuasion", "🗣️", "🔵 Aura", aur_hw, "🟡 Temperament", tem_hw, "🔵 Presence", pre_hw)
        draw_engine_block("Leadership", "👑", "🔵 Spirit", spi_hw, "🔵 Presence", pre_hw, "🔵 Fervor", fer_hw)
        draw_engine_block("Fortitude", "⛰️", "🔴 Constitution", con_hw, "🔵 Vitality", vit_hw, "🔴 Strength", str_hw)
        draw_engine_block("Intimidation", "⚠️", "🔵 Fervor", fer_hw, "🔴 Density", den_hw, "🔴 Kinetics", kin_hw)
        draw_engine_block("Deception", "🎭", "🟡 Temperament", tem_hw, "🔵 Aura", aur_hw, "🔴 Flex.", fle_hw)
        draw_engine_block("Diplomacy", "🤝", "🔵 Resonance", res_hw, "🔵 Conviction", convi_hw, "🔵 Fate", fat_hw)
        draw_engine_block("Meditation", "🕯️", "🔵 Soul", sou_hw, "🔴 Endurance", end_hw, "🟡 Will", wil_hw)
        draw_engine_block("Performance", "🎻", "🔵 Vitality", vit_hw, "🔴 Flex.", fle_hw, "🔴 Coord.", coo_hw)
        draw_engine_block("Animal Handling", "🐺", "🔵 Empathy", emp_hw, "🟡 Intuition", intuit_hw, "🔵 Fate", fat_hw)

# ==========================================
# EXPANDER 4: THE MACRO & PHYSICS ENGINE
# ==========================================
with st.expander("⚪ THE MACRO & PHYSICS ENGINE (Radiances & Derived)", expanded=True):
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='pillar-header'><h3>⚔️ P2 TACTICAL RADIANCES</h3></div>", unsafe_allow_html=True)
        st.write("Useable as Battle Auras on the P2 tactical battlefield.") #[cite: 1]
        
        tt_ctrl = inline_tooltip("Control", "Useable as a Battle Aura on the P2 tactical battlefield.") #[cite: 1]
        cap_ctrl = (luc_hw + mem_hw + wit_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🟡 Lucidity + 🟡 Memory + 🟡 Wits) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_ctrl} Capacity:</b> {cap_ctrl}</div>", unsafe_allow_html=True)
        
        tt_cmd = inline_tooltip("Command", "Useable as a Battle Aura on the P2 tactical battlefield.") #[cite: 1]
        cap_cmd = (den_hw + tem_hw + fer_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🔴 Density + 🟡 Temperament + 🔵 Fervor) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_cmd} Capacity:</b> {cap_cmd}</div>", unsafe_allow_html=True)
        
        tt_auth = inline_tooltip("Authority", "Useable as a Battle Aura on the P2 tactical battlefield.") #[cite: 1]
        cap_auth = (spi_hw + wil_hw + sou_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🔵 Spirit + 🟡 Will + 🔵 Soul) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_auth} Capacity:</b> {cap_auth}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='pillar-header'><h3>👑 P3 MACRO RADIANCES</h3></div>", unsafe_allow_html=True)
        st.write("Spendable Macro-Currencies for Realm Laws & Diplomacy.") #[cite: 1]
        
        tt_legit = inline_tooltip("Legitimacy", "The recognized right to rule and hold land; prevents vassal rebellion.") #[cite: 7]
        cap_legit = (mem_hw + aur_hw + int_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🟡 Memory + 🔵 Aura + 🟡 Intellect) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_legit} Capacity:</b> {cap_legit}</div>", unsafe_allow_html=True)
        
        tt_pres = inline_tooltip("Prestige", "Worldly fame used to declare war, change state laws, and attract guilds.") #[cite: 7]
        cap_pres = (vig_hw + end_hw + pre_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🔴 Vigor + 🔴 Endurance + 🔵 Presence) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_pres} Capacity:</b> {cap_pres}</div>", unsafe_allow_html=True)
        
        tt_fav = inline_tooltip("Favor", "Personal social currency representing vassal and liege goodwill.") #[cite: 7]
        cap_fav = (tem_hw + emp_hw + pre_hw) * 10 #[cite: 1]
        st.markdown("<div class='flow-box'>(🟡 Temperament + 🔵 Empathy + 🔵 Presence) × 10</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>⚪ {tt_fav} Capacity:</b> {cap_fav}</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='pillar-header'><h3>⚖️ GLOBAL PHYSICS & MAGIC</h3></div>", unsafe_allow_html=True)
        
        tt_hit = inline_tooltip("Hit Recovery Speed", "The physical recovery speed from kinetic staggering.") #[cite: 1]
        hit_recov = den_hw + agi_hw + vig_hw #[cite: 1]
        st.markdown("<div class='flow-box'>(🔴 Density + 🔴 Agility + 🔴 Vigor)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>{tt_hit}:</b> {hit_recov}</div>", unsafe_allow_html=True)
        
        tt_fert = inline_tooltip("Dynastic Fertility", "The biological probability of dynastic reproduction.") #[cite: 1]
        fertility = con_hw + vig_hw + fat_hw #[cite: 1]
        st.markdown("<div class='flow-box'>(🔴 Constitution + 🔴 Vigor + 🔵 Fate)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>{tt_fert} Probability:</b> {fertility}</div>", unsafe_allow_html=True)

        tt_mr = inline_tooltip("Magic Resistance (MR)", "Acts as the binary gate against magical cloaking, manipulation, and lethal damage. Unscathed if MR > MD.") #[cite: 1, 7]
        mr_cap = (apt_hw * 2.0) + (intuit_hw * 1.0) + ((wit_hw + luc_hw) / 2.0) + (conc_sw * 0.1) #[cite: 1]
        st.markdown("<div class='flow-box'>(Aptitude*2 + Intuition*1 + Wits&Lucidity/2) + (Concentration*0.1)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>{tt_mr}:</b> {mr_cap:.1f} / 100</div>", unsafe_allow_html=True)

        tt_md = inline_tooltip("Magic Damage (MD)", "Represents the offensive penetration power of a spell. If MD > MR, the target suffers Instant Execution.") #[cite: 7]
        md_cap = (wit_hw * 2.0) + (luc_hw * 1.0) + ((int_hw + pre_hw) / 2.0) + (learn_sw * 0.2) #[cite: 7]
        st.markdown("<div class='flow-box'>(Wits*2 + Lucidity*1 + Intellect&Presence/2) + (Learning*0.2)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='radiance-box'><b>{tt_md}:</b> {md_cap:.1f} / 100</div>", unsafe_allow_html=True)