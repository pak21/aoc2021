# AoC 2021 review

## HERE BE SPOILERS

Don't read this unless you want to be spoiled from here to Christmas.

## [Day 1: Sonar Sweep](https://adventofcode.com/2021/day/1)

Probably going to skip over most of the early ones pretty quickly, not much to
say about them really.

I wondered if this was going to be a lead-in to a more complicated partial sums
puzzle on a future day, particularly as there was a vaguely interesting 2D
partial sums puzzle in a previous AoC (*TODO*: find puzzle)... but it wasn't a
lead-in.

## [Day 2: Dive!](https://adventofcode.com/2021/day/2)

Nothing interesting here, unless you maybe want to think of it as a _really_
simple VM.

## [Day 3: Binary Diagnostic](https://adventofcode.com/2021/day/3)

Bit twiddling is one of those areas which I'm always surprised how many people
have just never done but even given that this felt overly fiddly, particularly Part
2. The [stats page](https://adventofcode.com/2021/stats) bears this out, with
around about 1/3 of the people who completed Day 2 not managing this one.

## [Day 4: Giant Squid](https://adventofcode.com/2021/day/4)

Fairly fun if not particularly deep.

## [Day 5: Hydrothermal Venture](https://adventofcode.com/2021/day/5)

On the day, this certainly didn't grab my enthusiasm, nothing really interesting
in it. Looking back, I wonder if you can think of it as a precursor to the now
infamous Day 22...

## [Day 6: Lanternfish](https://adventofcode.com/2021/day/6)

Absolutely classic AoC puzzle. Part 1: trivial. Part 2: a few orders of
magnitude later, the trivial approach doesn't work any more. I think these
puzzles are great, they make you think about your data structures and
algorithms, and I've seen them teach other people stuff as well.

## [Day 7: The Treachery of Whales](https://adventofcode.com/2021/day/7)

Not quite sure what this puzzle was about really. There is some vaguely
interesting maths behind it (Part 1 is the median of the positions, Part 2 is
close to but not exactly the average of the positions) but it's so trivial to
brute-force you may as just well do that.

## [Day 8: Seven Segment Search](https://adventofcode.com/2021/day/8)

I have mixed feelings on this one: I really like the overall structure with
Part 1 being a really big clue as to how to do Part 2, but Part 2 itself didn't
really hit the mark with it being much more a logic puzzle than anything even
programming-adjacent.

The stats page shows this as dropping about 1/4 of the player population, so
again probably a miss overall.

## [Day 9: Smoke Basin](https://adventofcode.com/2021/day/9)

This is a great puzzle. Part 1 checks you can parse the input and gives you the
first steps (pun intentional), Part 2 sends you off to one of the classic
computer science algorithms. More like this please!

## [Day 10: Syntax Scoring](https://adventofcode.com/2021/day/10)

Running through Part 1, I had high hopes for this one - while bracket matching
is a bit of an overused theme in the programming puzzles world, a fairly gentle
intro is a good thing, particularly early in the month.

But then Part 2 didn't really add anything at all to the puzzle - if you've
solved Part 1 with the "canonical" solution of a token stack (and I imagine most
people will have done), it's trivial. (And also minus a small amount more for
the whole "find the median" bit, which adds nothing to the puzzle).

## [Day 11: Dumbo Octopus](https://adventofcode.com/2021/day/11)

Once you've done a couple of years of AoC, you know there's going to be a
cellular automaton problem at some stage, and probably more than one. The rules
for this one were slightly fiddly, and again hoping for Part 1 to be a lead in
for an interesting Part 2... but again, Part 2 fell a bit flat just being "brute
force it for a few hundred cycles".

That said, some clever people did go very deep on this automaton and found
[some interesting behaviours](https://www.reddit.com/r/adventofcode/comments/rft2it/2021_day_11_cyclic_octopi/).

## [Day 12: Passage Pathing](https://adventofcode.com/2021/day/12)

In what is a running theme here, Part 1 of this was nice: a relatively tidy
pathfinding algorithm - just more classic computer science type things (and a
nice lead in for the upcoming Day 15 and Day 23). Again though, Part 2 was
fiddly rather than insightful - just a different constraint on the set of
available moves which didn't really feel like it added much.

## [Day 13: Transparent Origami](https://adventofcode.com/2021/day/13)

While this wasn't particularly deep, I think it was a fine puzzle for the middle
section of AoC - and again maybe (at a stretch) one making you think about
spatial transforms before Day 19?

## [Day 14: Extended Polymerization](https://adventofcode.com/2021/day/14)

If you liked Day 6, you'll like this one. If you didn't, you probably won't. Not
much more to say about it than that I think.

## [Day 15: Chiton](https://adventofcode.com/2021/day/15)

Another classic CS problem. While the first part may have been reasonably
brute-forceable with just a breadth/depth first search, I suspect you'll need
full Dijkstra for Part 2.

## [Day 16: Packet Decoder](https://adventofcode.com/2021/day/16)

Meeeuh. Just. So. Fiddly.

Unpacking hex to bits. 5 bit chunks for numbers. Two different length types. It
feels like there's the core of an interesting problem in here, but it's just so
wrapped up in tedious bits than it wasn't enjoyable.

## [Day 17: Trick Shot](https://adventofcode.com/2021/day/17)

This one felt odd: writing the actual simulation was pretty trivial, so the
problem pretty much came down to working out some bounds for the initial
velocity - but even then the search space was small enough that you could just
brute force it. Not sure if I'm missing something on this one - maybe my physics
background meant that the fact I was able to get 3 of the limits meant that it
was easier than it was for others?

## [Day 18: Snailfish](https://adventofcode.com/2021/day/18)

At one level, this is an interesting parsing/tree manipulation problem. At
another level, the "explode" step feels unnecessarily complicated - maybe
there's a data structure other than a simple binary tree I missed here, but
_all_ the complexity in the problem was implementing explode. Once that was
done, split was simple... and then Part 2 was trivial.

## [Day 19: Beacon Scanner](https://adventofcode.com/2021/day/19)

The first of this year's hard problems.

I guess the question about this one is whether it's a programming problem or a
physics problem. Looking back now with a week or so's hindsight, I think it's
probably on the edge - generating the rotations is pretty much a physics/maths
problem, but generating the tree (maybe DAG?) of connections is much more a
programming problem. I enjoyed it whatever, even if it took 4 hours...

## [Day 20: Trench Map](https://adventofcode.com/2021/day/20)

Yes, well... one of the things I've always liked about AoC problems is that
other than scale, there's generally no "tricks" in the input which aren't in the
test cases. Until this one... yes, I know there are plenty of hints in the
rubric but all the same it felt cheap rather than interesting - and there's
nothing particularly interesting in the automaton itself either.

## [Day 21: Dirac Dice](https://adventofcode.com/2021/day/21)

See Day 14 (and from there to Day 6). All the same comments apply again.

## [Day 22: Reactor Reboot](https://adventofcode.com/2021/day/22)

A puzzle that generated some controversy, in particular a fair amount of
grumbling on the AoC subreddit that it required specialist knowledge to solve.
I don't really agree with that - of the two common approachs to the problem, the
"just slice the big cuboid into little cuboids" is IMO obvious if somewhat
tedious to code, while the "negative cuboid" approach I took isn't something I
think I've ever been taught, but worked out on the fly. I'd call it a good
problem.

## [Day 23: Amphipod](https://adventofcode.com/2021/day/23)

While in general I'm a fan of pathfinding problems, this one didn't really hit
the spot - just a perfectly standard Dijkstra with a horribly, horribly
complicated function to find the possible next states. With hindsight, pretty
much ignoring the grid entirely and just having individual structures for the
hallway and each side room would simplify it a bit but I think it would still be
a bit of a mess.

## [Day 24: Arithmetic Logic Unit](https://adventofcode.com/2021/day/24)

The now expected reverse engineering problem; again always causes debate as to
whether it's "really" a programming problem or not. I personally think it's
programming-adjacent enough to be included, but that view certainly isn't
universal. While I went the full reverse engineering route, that turned out not
to be the only viable strategy - a bunch of people essentially simulated every
possible input in parallel and got the answers that way.

Perhaps my only slight knock on this one was the fact that Part 2 wasn't
interesting once you'd done Part 1.

## [Day 25: Sea Cucumber](https://adventofcode.com/2021/day/25)

And the now expected relatively easy Day 25. Just a simple cellular automaton,
nothing really to comment on here.
