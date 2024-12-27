import sys
import streamlit as st
from src.market_data_multi_agent.crew import MarketDataMultiAgent

# Streamlit UI for Market Data Multi-Agent
def main():
    st.set_page_config(page_title="Market Data Multi-Agent", layout="wide", initial_sidebar_state="expanded")
    st.title("📊 Market Data Multi-Agent Dashboard")
    st.markdown("### Professional UI for Market Data Analysis")

    # Initialize session state
    if "raw_markdown" not in st.session_state:
        st.session_state.raw_markdown = None

    # Sidebar inputs
    st.sidebar.header("🔍 Input Settings")
    market_segment = st.sidebar.text_input("📈 Market Segment", "AI and LLMs")
    market_size = st.sidebar.selectbox("🌍 Market Size", ["Global", "Regional", "Local"], index=0)
    lang = st.sidebar.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Chinese"], index=0)

    # Process Request
    if st.sidebar.button("🚀 Run Analysis"):
        with st.spinner("Running Market Data Multi-Agent..."):
            try:
                inputs = {
                    'market_segment': market_segment,
                    'market_size': market_size,
                    'lang': lang
                }
                
                # Run the crew
                result = MarketDataMultiAgent().crew().kickoff(inputs=inputs)

                # Store the result in session state
                st.session_state.raw_markdown = result.raw

            except Exception as e:
                st.error(f"Error processing request: {e}")
                st.session_state.raw_markdown = None

    # Display results if available
    if st.session_state.raw_markdown:
        display_results(st.session_state.raw_markdown)

# Display results in Markdown format
def display_results(raw_markdown):
    if not raw_markdown:
        st.error("❌ No result available. Please try again.")
        return

    st.markdown("### 📜 Analysis Results")
    st.markdown(raw_markdown, unsafe_allow_html=True)

    # Download button for Markdown
    st.download_button(
        label="💾 Download Markdown",
        data=raw_markdown,
        file_name="market_data_analysis.md",
        mime="text/markdown",
        key="markdown_download_button"
    )

if __name__ == "__main__":
    main()
