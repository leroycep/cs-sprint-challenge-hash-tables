#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    destinations = {}
    start_ticket_dest = None
    for ticket in tickets:
        if ticket.source == "NONE":
            start_ticket_dest = ticket.destination
        else:
            destinations[ticket.source] = ticket.destination

    route = []
    current_dest = start_ticket_dest
    while current_dest != "NONE":
        route.append(current_dest)
        current_dest = destinations[current_dest]
    route.append("NONE")
    return route
