def get_sdlc_phase(query):
  phases = {
    "first": "Requirement analysis",
    "second": "System Design",
    "third": "Implementation",
    "fourth": "Testing",
    "fifth": "Deployment",
    "sixth": "Maintenance",
    "seventh": "Disposal"
  }

  query = query.lower()
  for key in phases:
    if key in query:
      return phases[key]
  return "Please ask about a phase number from first to seventh."

def main():
  while True:
    user_input = input("Ask about an SDLC phase (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
      print("Goodbye!")
      break
    print(get_sdlc_phase(user_input))

print("SDLC Phases")
main()