"""
Quick demo script for Agri-Sage Agent
"""

import asyncio
import sys
import os

# Add the current directory to path
sys.path.append(os.path.dirname(__file__))

from agri_sage_agent import GatewayAgent

async def quick_demo():
    """Quick demo without image processing"""
    agent = GatewayAgent()
    
    response = await agent.process_farmer_query(
        farmer_id="demo_farmer",
        location="Nakuru, Kenya",
        crop_type="tomato",
        query="My tomato plants have yellow leaves with dark spots. What is wrong and what should I do?"
    )
    
    print("Agri-Sage Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(quick_demo())
