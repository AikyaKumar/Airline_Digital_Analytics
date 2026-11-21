
# Consent-Based Customer Data Collection
# Synthetic airline analytics simulation

# 1. Simulated customer consent preferences
customer_consent = {
    "essential": True,
    "analytics": False,
    "marketing": False
}

# 2. Simulated website events
customer_events = [
    {
        "event": "session_started",
        "category": "essential"
    },
    {
        "event": "flight_search",
        "category": "analytics",
        "origin": "FRA",
        "destination": "ZRH"
    },
    {
        "event": "select_flight",
        "category": "analytics",
        "origin": "FRA",
        "destination": "ZRH"
    },
    {
        "event": "booking_complete",
        "category": "marketing",
        "booking_value": 150
    }
]

# 3. Filter events based on consent
def filter_events(events, consent):
    collected_events = []

    for event in events:
        category = event["category"]

        if consent.get(category, False):
            collected_events.append(event)
            print(f"ALLOWED: {event['event']}")
        else:
            print(f"BLOCKED: {event['event']}")

    return collected_events


# 4. Execute consent filtering
print("\nCUSTOMER CONSENT:")
print(customer_consent)

print("\nEVENT COLLECTION RESULTS:")

collected_events = filter_events(
    customer_events,
    customer_consent
)

# 5. Display final collected events
print("\nCOLLECTED EVENTS:")
for event in collected_events:
    print(event)

print(f"\nTotal events generated: {len(customer_events)}")
print(f"Total events collected: {len(collected_events)}")
