from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "sticky_notes.txt")

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

@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the sticky note file.
    
    Returns:
        str: All notes as a single string separated by line breaks.
             If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes or "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Retrieve the latest note from the sticky note file.
    
    Returns:
        str: The latest note. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."