# dupped Game Design Document
### gravity flipping fun

---

### Concept

2D High-Scoriented Arcade Game

You are a ball, your only button flips the gravity.

You fall to the floor at first, then flipped gravity makes you fall to the roof, and this cycle repeats.

There are capsules that float horizontally across the screen, there are two types:
	- Capsule: Slow, has walls on either side that will kill the player. These are worth less points, the player must fall through the middle of the capsule.
	- Side Capsule: Faster, these have a roof and/or floor that will kill the player. These are worth more points, as the player must keep flipping gravity inbetween the surfaces to not die.

Both have a small collider in the centre that, once touched, give the player points.

---

### Controls

Button: Flip gravity from up -> down, or down -> up.

Any keyboard input, any gamepad button input, is THE input.
