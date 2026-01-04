# Understanding the Problem
- [ ] Consider `S/P*L`, the number of spines per group times the number of leaves per group, as the number of edges between leaves and OXCs. In other words, to get from a specific leaf to a specific OXC, there are `S/P` edges to use. Any more and you'd have to start duplicating.
- [ ] The quantity `S/P` (which shows up a lot in the problem statement) is the number of spines per plane. Imagine drawing all `S` spines out, and all the ones that belong to one plane are of the same color.

# Observations
- [ ] In the sample test cases, many connections between the same two leaves are duplicated (at least _ times). That means that sometimes, it is necessary to create multiple paths between the same two leaves to spread that load evenly.