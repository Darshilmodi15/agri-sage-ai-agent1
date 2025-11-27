# Agri-Sage: AI-Powered Agricultural Assistant for Smallholder Farmers

## Kaggle Agents Intensive Capstone Project - Track B: Agents for Good

### 🎯 Project Overview
Agri-Sage is a multi-agent AI system designed to provide personalized agricultural advisory services to smallholder farmers in developing countries. Using natural language interfaces and computer vision, it delivers real-time advice on crop management, disease diagnosis, and market opportunities.

### 👥 Team Members
- **Darshil Modhi** - Lead Developer & AI Engineer
- **Het Chaudhari** - Data Scientist & Backend Developer

### 🚀 Problem Statement
Smallholder farmers face critical challenges including limited access to agricultural experts, delayed disease diagnosis, climate vulnerability, and market information gaps - leading to significant crop losses and economic hardships.

### 💡 Our Solution
A sophisticated multi-agent AI system that provides:
- Real-time crop disease diagnosis using computer vision
- Personalized farming recommendations based on local conditions
- Market intelligence and pricing insights
- Multi-lingual support via SMS/voice interfaces

### 🏗️ Architecture
![Architecture Diagram](architecture_diagram.png)

### 🛠️ Technical Features

#### Multi-Agent System
- **Gateway Agent** - Handles farmer interactions and session management
- **Diagnosis Agent** - Specializes in crop disease identification
- **Market Agent** - Analyzes pricing trends and market opportunities
- **Synthesis Agent** - Coordinates all inputs and generates final plans

#### Course Requirements Demonstrated
✅ **Multi-agent System** - Four specialized agents working in coordination  
✅ **Custom Tools** - Agricultural-specific tools for disease detection and analysis  
✅ **Sessions & Memory** - Persistent farmer context and personalized memory  
✅ **Observability** - Comprehensive logging and performance monitoring  
✅ **Effective Gemini Integration** - Powering natural language understanding  

### 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/[your-username]/agri-sage-ai-agent
cd agri-sage-ai-agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env file

# Run the agent
python agri_sage_agent.py
