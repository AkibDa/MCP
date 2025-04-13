from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = "notes.txt"

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")
            
@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.
    
    Args:
        message (str): The note content to be added.
        
    Returns:
        str: Confirmation message indicating the note was saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"
