from google.auth import default

creds, project = default()
print("Auth OK")
print("Project:", project)
print("Creds type:", type(creds))
