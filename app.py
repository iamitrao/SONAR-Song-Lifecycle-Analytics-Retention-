import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

# --- Page configuration ---
st.set_page_config(page_title="Spain Top 50 Analysis", layout="wide", initial_sidebar_state="expanded")

# --- Custom Styling (Streamlit aesthetics) ---
st.markdown("""
<style>
/* Base Dark Theme overrides to make it look nice */
.stApp {
    background: linear-gradient(135deg, #0e1117 0%, #171d2b 100%);
    color: #e0e6ed;
    font-family: 'Inter', sans-serif;
}
/* Making the stat boxes look cool */
div[data-testid="metric-container"] {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(108, 92, 231, 0.3);
}
div[data-testid="metric-container"] label {
    font-weight: 600;
    color: #a29bfe;
    font-size: 1rem;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    font-weight: 800;
    font-size: 2.2rem;
    color: #ffffff;
    background: -webkit-linear-gradient(45deg, #a29bfe, #00cec9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
h1 {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    background: -webkit-linear-gradient(45deg, #fd79a8, #a29bfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-bottom: 20px;
}
h2, h3 {
    font-family: 'Outfit', sans-serif;
    color: #dfe6e9;
}
hr {
    border: 0;
    height: 1px;
    background-image: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
}
</style>
""", unsafe_allow_html=True)

# --- Data Loading ---
@st.cache_data
def load_data():
    df = pd.read_csv('/Users/amitrao/Desktop/internship 2nd project/processed_spain_top50.csv')
    df['date'] = pd.to_datetime(df['date'])
    with open('/Users/amitrao/Desktop/internship 2nd project/kpi_results.json', 'r') as f:
        kpis = json.load(f)
    return df, kpis

df, kpis = load_data()

# --- Pre-processing for Selectors ---
min_date = df['date'].min()
max_date = df['date'].max()
stages = df['lifecycle_stage'].unique().tolist()
album_types = df['album_type'].unique().tolist()

# --- Sidebar Filters ---

st.sidebar.title("My Filters")

date_range = st.sidebar.date_input("Pick a Date Range!", [min_date, max_date], min_value=min_date, max_value=max_date)
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

stage_filter = st.sidebar.multiselect("Phase of Song", stages, default=stages)
explicit_filter = st.sidebar.radio("Has Swearing?", ["All", "Clean", "Explicit"])
album_filter = st.sidebar.multiselect("Is it an Album or Single?", album_types, default=album_types)

# --- Applying Filters ---
mask = (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date)) & \
       (df['lifecycle_stage'].isin(stage_filter)) & \
       (df['album_type'].isin(album_filter))

if explicit_filter == "Clean":
    mask = mask & (df['is_explicit'] == False)
elif explicit_filter == "Explicit":
    mask = mask & (df['is_explicit'] == True)

filtered_df = df.loc[mask]

# --- Dashboard Layout ---
st.title("Spain Top 50 Songs Analysis Project")
st.markdown("Welcome to my project! This dashboard shows how long songs stay on the Spain Top 50 chart and other interesting stats I calculated.")

# -- KPI Summary Metrics --
st.header("My Key Findings (KPIs)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Average Time on Playlist", f"{kpis['Average Days on Playlist']:.1f} days")
col2.metric("Time Needed to Peak", f"{kpis['Entry-to-Peak Time (days)']:.1f} days")
col3.metric("Daily Churn (Songs Replaced)", f"{kpis['Average Daily Playist Churn (%)']:.2f}%")
col4.metric("Songs That Survive > 30 Days", f"{kpis['Retention Stability Index (>30 days %)']:.1f}%")

st.markdown("<hr>", unsafe_allow_html=True)

# --- Visualization Modules ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Where are the songs at right now?")
    stage_counts = filtered_df.groupby('lifecycle_stage')['song_id'].nunique().reset_index(name='count')
    fig_pie = px.pie(stage_counts, names='lifecycle_stage', values='count', hole=0.6,
                     color_discrete_sequence=['#a29bfe', '#fd79a8', '#00cec9', '#ffeaa7', '#fab1a0'])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font_color='#dfe6e9', legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5))
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    st.subheader("How Long Do Songs Survive? (Explicit vs Clean)")
    song_survival = filtered_df.groupby(['song_id', 'is_explicit'])['date'].count().reset_index(name='days_in_period')
    song_survival['Type'] = song_survival['is_explicit'].map({True: 'Explicit', False: 'Clean'})
    fig_box = px.box(song_survival, x='Type', y='days_in_period', color='Type',
                     color_discrete_map={'Explicit': '#fd79a8', 'Clean': '#00cec9'})
    fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#dfe6e9',
                          yaxis_title="Total Days on the Chart")
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("Songs Entering vs Leaving the Chart")
flow_df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]
entries = flow_df[flow_df['days_since_entry'] == 0].groupby('date').size().reset_index(name='New Entries')
exits = flow_df[flow_df['days_to_exit'] == 0].groupby('date').size().reset_index(name='Exits')
flow = pd.merge(entries, exits, on='date', how='outer').fillna(0)

fig_flow = go.Figure()
fig_flow.add_trace(go.Scatter(x=flow['date'], y=flow['New Entries'], mode='lines', name='Songs Coming In', line=dict(color='#00cec9', width=3)))
fig_flow.add_trace(go.Scatter(x=flow['date'], y=flow['Exits'], mode='lines', name='Songs Dropping Off', line=dict(color='#fd79a8', width=3)))
fig_flow.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#dfe6e9',
                       hovermode="x unified", yaxis_title="Number of Tracks")
st.plotly_chart(fig_flow, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("My Timeline of the Top 20 Longest Charting Songs")
top_songs = filtered_df.groupby('song_id')['date'].count().nlargest(20).index
timeline_df = filtered_df[filtered_df['song_id'].isin(top_songs)]
lifecycle_timeline = timeline_df.groupby('song_id').agg(Start=('date', 'min'), Finish=('date', 'max'), Type=('album_type', 'first')).reset_index()

fig_time = px.timeline(lifecycle_timeline, x_start="Start", x_end="Finish", y="song_id", color="Type",
                       color_discrete_map={'single': '#a29bfe', 'album': '#ffeaa7'})
fig_time.update_yaxes(autorange="reversed", showticklabels=False) 
fig_time.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#dfe6e9')
st.plotly_chart(fig_time, use_container_width=True)
