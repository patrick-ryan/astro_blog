---
pubDate: 2023-12-11
title: Overengineering
description: Triggered about overengineering
tags:
  - meta
  - tech
  - rant
---
I'm tired of hearing this term. This includes phrases like "Putting the cart before the horse", "Keep It Simple Stupid", "You Ain't Gonna Need It", and especially "**Don't let perfect be the enemy of good**". Heaven forbid I need to "timebox" my task so that it doesn't commit "scope creep".

> I'm pretty sure "Perfect is the enemy of good" is one of the catchphrases I dislike most; it's truly meaningless to me. There is always a tradeoff between time and quality, but this phrase suggests the tradeoff involves a binary choice between sufficient and unattainable quality. In other words, there is no such thing as high quality products. At its best, it is a strawman argument to be taken as a compliment, as they are inferring that the idea you just proposed is "perfect".

I think these phrases were created because engineers were building stuff that wasn't actually needed, that customers weren't paying for. That's well enough, I'm not personally inclined to work on things that aren't requested in my day job. That should be pretty natural, but maybe engineers occasionally develop an internal conception of the user's or platform's needs that diverges from reality, so there may need to be boundaries on that, especially when the value gain is not higher than that of shipping the product before the deadline.

> And I have no problem with that.

If that was what "overengineering" was considered to be today, I'd have no problem with that. The problem is this term and its friends have been morphed into something altogether different.

Now, "overengineering" means adding complexity to the system. Why implement a new way of doing something when you can just muck around within the current constraints of the system? According to this philosophy, every feature or every system component or every evolution shall not introduce a new level of abstraction, otherwise that is exploding the scope.

Some people suggest to hold off adding new layers of abstraction and new methodologies until we implement the simple approach first and "reassess" later. This is fancy words for saying that we are taking on technical debt that will likely never be addressed until something breaks.

But every abstraction is a best guess on the representation of the system and how the system will evolve; the codebase could not exist without it being introduced in the first place. Deferring additional abstraction for "more information" is just generally a weak stance: at best, it means you don't really understand how this system could evolve, and are afraid of the consequences of premature prediction.

For most cases however, I will bet the reason is really: you are afraid of abstraction. If there is not a scheduled time when you know more information will be available that will be crucial to the design of the system or application, and no way to defer work until that point, then you know it's probably a good idea to keep the implementation minimal. You need that specific point in time, because by that point you should plan out a rewrite of the code to be accurate to the system needs and planned evolution, and without such a contract the codebase is doomed to the "prototype-phase" quality that your KISS philosophy landed you on. There is no such thing as a tech-debt sprint.
