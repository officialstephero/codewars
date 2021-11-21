def queue_time(customers, n):
    t = 0
    ticket = [0]*n
    if n < len(customers):
        while customers:
            if customers:
                for j in range(n):
                    if ticket[j] == 0 and customers:
                        ticket[j] = customers.pop(0)
                while ticket.count(0) == 0:
                    t += 1
                    ticket = [i - 1 for i in ticket]
        return t + max(ticket)

    elif n >= len(customers) and customers:
        return max(customers)
    else:
        return 0
    