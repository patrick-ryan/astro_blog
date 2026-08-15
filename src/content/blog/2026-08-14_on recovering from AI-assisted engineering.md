---
pubDate: 2026-08-14
title: On Recovering from AI-assisted Engineering
description: DESCRIPTION
tags:
  - tech
  - business
---
A little while ago, I decided to uninstall my AI tooling from my workstation. I believe that, while I never really gave the latest tooling a fair chance, this was the best decision for my long-term career as a software engineer.

To be honest, I've never really thought AI was a novel technology, or one that had much promise. My intention at work was to give it a fair chance and be able to speak about its capabilities in an intelligible way.

Today I hesitate to suggest to coworkers that the whole set of technologies is flawed, not because I have doubts in this belief, but because I am under the impression that these tools sow the seeds of their own destruction, and in the meantime the best convincing really comes from personal experience and reflection.

So I'm not here to convince you to drop AI tooling, but to collect some good software engineering practices, that some forlorn engineer can return to in the eventuality that they become depressed, lose faith in their engineering, or otherwise drop AI from their local stack.

# 1. How to look stuff up

Probably one of the easiest ways to interact with an LLM is by asking it "how does this thing work", where this thing can be any sort of technology or codebase or concept. You get an immediate response, and an immediate sense of conceptual understanding.

This is one of those innocuous requests, that end up being the most insidious. Why do research to answer a question when you can offload this whole activity at once? AI surely has better access to information, can scan more of it more quickly, and synthesize this information more capably?

If you've started asking these questions, you're already on the way to recovery!

Perhaps you were asked to explain a tech stack decision on a meeting, or describe what a particular technology is doing in detail. Or perhaps you receive a surprisingly in-depth code review. Or a bug ticket about some obscure interaction within the supply chain.

You could ask the LLM, but are you going to risk this rabbit hole? You got here by asking the LLM to summarize some concept for you. Is the LLM now going to be responsible for every branching thought from this original request? This is not sustainable, you will not enjoy being so dependent on tooling to answer basic questions, you will not seem very competent in your own right.

Start looking stuff up. "How do ternary operators work in Groovy?" Do a web search. Open a link to the language specification. Realize you opened a link to an [outdated document](https://opensource.net/ternary-operator-apache-groovy-7/), and go find the [more recent/authoritative version](https://groovy-lang.org/operators.html#_ternary_operator). Understand how the technology changes, how its informational content is structured, what qualities are most emphasized.

Maybe you find How-To guides, maybe an article with common pitfalls you were in the midst of falling into, a Best Practices guide, a "there is a better way now" answer in a forum.

You will find out that there is actually rarely a single answer to your question, or that your question is really a set of questions you realized you should have considered. But more importantly, you will know how to handle a simple question: how does this thing work? What alternatives are there? What are the tradeoffs of using the thing?

You will not just have confidence to answer these questions, but can cite references, and generate valuable discussion. You will be the person who "looked it up".

# 2. How to document stuff

With this and other related topics, I'm a big fan of the concept that [human attention requires human effort](https://tombedor.dev/human-attention-and-human-effort/).

Nobody wants to read your auto-generated book about how the div in your portal application does not appear fully centered on Safari (we have enough public documentation about div centering, thanks).

Did you make the mistake of generating a spec or overview that nobody has read? Maybe you drafted a ticket, or PR description, or Slack message, and got a thumbs-up emoji and that's it?

Your coworkers don't operate in a void, as it turns out. The documentation you may have provided, starts by defining the universe, and how the laws of physics are constant. But your coworkers are not looking for a lesson on cosmology, they care more about what's important to their lives at this point in time. The universe they currently operate in is the one within your specific team, tech stack, cross-team dynamics, etc.

So, when documenting something, start by asking: what is important to your team (or to your audience)?

Did you lack some understanding of how a technology or process fits into your team operations before this point? What background research is relevant to this topic, that may be relevant to other discussions of import to your team?

People like to read material that is relevant to them. When there is too much fluff, the average relevance starts to go down, as people assume the material is meant for a different audience, probably those with a lot of free time to spend.

In the act of documenting, like when you write something down, you will also build your working memory, and retain concepts more effectively. Writing is often an extension of thinking, you will build confidence in your subject matter, and you will more easily understand the gaps of understanding.

# 3. How to automate stuff

Look, I'm no Luddite here. You have shit to get done, and you want to get it done fast, and you don't particularly care how it gets done as it's just going to be repetitive, mindless work.

Maybe you want to generate 500 lines of bash for a single purpose, or convert some data schema into another schema, or generate a large number of tests.

Honestly, just write a python script or something. You can even write a script that writes a different script. Or consider looking up how to do whatever you're trying to do.

It's probably less hard to automate something than you think.

If you thought AI was the answer and suddenly got lost in the infinite abyss of prompting to build a script that scripts out a script that you can use to change your current directory smartly, maybe take a step back. Is this a problem that has been encountered before or even solved? Maybe a very similar problem at least?

Try building something. You seriously will have fun building the automation yourself. There is something deeply satisfying with it, and you can help build the greater community by sharing your learnings along the way.

"BUT THIS TASK IS URGENT AND I CAN'T SPEND ALL MY TIME ON AUTOMATION" - OK, stop yelling, you came to me in the first place... There is no silver bullet to all scenarios. Are you sure that AI is really going all that well for you in the pursuit of efficient use of time? What about instead, you break the problem down, automate the easy parts and fill in the gaps yourself?

People were writing shitty one-off scripts way ahead of this craze, and yes it's become a meme that you spend 20 hours automating a task that could only involve 20 minutes of real work. Weigh the tradeoffs, if it takes that long to automate the task by hand, it's more likely the AI doing it is going to be making mistakes along the way. Maybe try a simpler version that takes 2 hours of your time, and then you'll understand the problem boundaries more clearly and potentially find optimizations along the way.

Break your problem down, it always helps.

# 4. How to react to your coworkers using AI

This is kind of the final step of recovery. Maybe you started to notice that others aren't happy, they are having some existential crisis, they are not confident and are more unfocused.

There are signs, and leadership may expect you adopt some similar depression in order to "keep up" or "increase velocity" or (highly perversely) "use more of our token budget".

Counter this expectation immediately. Tell your manager you are morally opposed to AI, or it's against your religion or something. But also tell them that you work better and with higher quality without it. Be bold, and consider all your experiences thus far. There's no point hiding it, your manager will respect your being forthcoming.

But if you find a way to communicate this belief to the larger organization/community, I applaud you and hope the best for you! You are possibly bolder than I am. You basically just bashed the religions of the leaders of the societal apparatus that puts bread on your table... But damn it you got my respect.