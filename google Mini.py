import google.auth.credentials
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

# Set up credentials
credentials = google.auth.credentials.Credentials.from_authorized_user_file(
    existing_file('credentials.json')
)

# Start the assistant
with Assistant(credentials) as assistant:
    # Send a voice command to the Google Home Mini
    assistant.start_conversation()
    assistant.send_text_query('Play some music')
