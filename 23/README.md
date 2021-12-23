# Optimisation thoughts

In terms of number of moves executed, I think this is not essentially as optimised as it can be. The only real change that could
be made would be to move towards a more structured representation of the state (e.g. with the siderooms represented as stacks
and the hallway as a set(?)) which would then allow for a more efficient determination of the available moves - e.g. we could
simply ignore creatures not at the top of a sideroom stack, rather than going in and working out they can't move every time.
