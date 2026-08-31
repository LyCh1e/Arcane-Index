# ICT3112 Software Verification and Validation — Lecture 1 (Live Transcript)

**Module**: ICT3112 Software Verification and Validation  
**Lecturer**: Ryan Fraser Kirwan  
**Type**: Live lecture recording / transcript  
**Coverage**: Module introduction, software quality, V&V fundamentals, reliability metrics, defect density, customer metrics

> Raw transcript — immutable. See wiki/sources/ict3112-svv-l1.md for structured index.

---

Hey!
Alright.
Hopefully we're recording.
Hi, everyone.
Let's see… How is life?
It's, your final year, right?
Wait, I can't remember what schedule you have.
Let me put it onto the chat.
Have you had other classes today?
Yeah, long time no see. Let me share my screen, sorry.
Alright.
Dude.
Two more online at… oh, okay.
Oh, we're the first one, right? Did you have one… you had one this morning, no?
First one, okay, that's cool.
Alright, I'll try and make it painless. Actually, week one is normally painless, I think, for my modules, at least.
Alright.
I'm assuming everything is visible.
How many are we expecting? I guess… you guys said, like, a hundred and something? Less? More?
Maybe I change the class list.
Okay, that's not right, student…
Okay, technically 109 of you, although… Maybe… might be some tests.
accounts in there, I don't know. Okay, maybe there's 190 of you. Okay, that's cool.
So we're… we're not quite at the halfway stage of, people joining, but, that's okay.
Alright.
I'll just wait one more minute, and then if I pass, we'll just get stuck into the lecture. I think this lecture will be nice and painless. As I say, it's really just introductory. Most of the module will kind of kick off from week two.
For those of you who did Maths 2, which I think is most of you…
Yes, the rats are back.
Oh, you're sending a direct message, but yeah, rats are back.
And they will be infesting your lives once more. I'm making some changes.
So, I… I did, create…
this module a long time ago, and then I was not teaching it last year, and so I'm in the process of…
redoing, revamping, particularly the lab sessions. I have finished the… at least half of the labs, or probably more, but I will… I didn't release the PDFs, so I'll release them later today.
But,
I wanted to get everything out in advance. Unfortunately, that's not the case, but I think, basically, this week, most of them will be out. Next week, all of them should be out. Regarding the content itself, I think…
All of that is pretty much out already.
Alright. Okay, so it's 5 passed.
This is recorded, so I'm not expecting everyone to join, but we have reached the 50% threshold, so we've effectively passed our…
Degree, we've got a passing grade, in terms of attendance, so I will get started.
Right. So, this module is software verification and validation. The module code
has changed a little bit over the years, but I believe it is 3112.
at the moment, but I literally just removed it from my slides because it does seem to change a bit frequently, and I don't have the wrong module code on my slides by accident. The first half of this module is what I'll be taking, and that is just the first 6 weeks.
And I'll break the introduction of how this 6 weeks is going to work today.
So…
Today's lesson, a really, module introduction, as I say. I'm going to talk you through the plan. Now, some of this is much
Much more of a plan than normal, as in, Best laid plans don't always…
come to fruition, so we will see. I'm going to implement some new technology, some new ideas, and we'll see how they go, so please bear with me. It's all meant to be for the greater good, but we will see. Today, I'm going to cover also a bit of motivation behind verification and validation. I obviously think, and the university thinks it's very important.
And…
Yes, AI. Hey, if you chat… if you chat to everyone, then everyone can read, and I won't seem like a crazy person talking to you directly on the chat. But I do have the chat open on the side. If you want to send me messages, tell me that I'm muted or whatever, please, please do that. But I want to cover some motivation
behind the module, and then talk about software quality. So, generally speaking, we… we want quality software.
We buy and want quality software, but how do we actually measure what is quality? And so we're going to look at some traditional metrics.
Of quality, like, how do we understand and measure quality in a quantified way?
And there are a variety of ways of doing this, as you can imagine, and some of which I want us to be able to apply ourselves.
And we will cover some scary equations. However, any equations that we cover.
at least the complicated formulas from the MUSA models, they will be given to you in any assessment that you would be needing to use them. That includes the rats. So, like with my maths module, I'm not super keen on forcing students to memorize equations, but more be able to apply them thoughtfully.
And that's what we're doing here as well.
So, we're going to cover some metrics, look a little bit at, quality standards, though that's a bit more brief, as those are quite,
dynamic in nature, and really just give an introduction to software VMV in terms of some more definitions as we go through.
So, the first half is going to be my approach to team-based learning. It's going to be very much like the Mathematics 2 module that you would have done previously, and I'll pass, I'm assuming, if you're here, which is great, well done.
the… rats and T-rats, the iRats and T-rats will be back, by popular or unpopular demand.
I'm slightly reducing the percentage.
And as you can see in the slide here, I have these kind of asterisks around the 20% and the 15% for the lab assessments and the rats.
And that's because…
I am a little bit dubious about some of the technology I'm planning to use. I'll explain it a bit more. And I want to leave my options open so that I can fairly assess you if things
don't pan out as intended, right? So, the asterisks are there for, an escape clause should things go pear-shaped, but the
idea that we're going to embark on is having the five IRAT TRAT sessions.
very much like your maths stats portion that I covered.
And we're going to try and assess that about 25… sorry, 20% now for those. So each assessment, each question is not worth very much, but the idea is by doing incremental learning, we are going to absorb a lot of the materials better, and that is the general goal.
The way I'm going to run this module this time.
opposed to years ago when I used to run it, I used to do…
teams, and I used to make…
The rounds during the labs and try and talk to everyone and get them to explain their code.
And do assessments live in the labs.
As you can imagine, logistically, this is a bit of a challenge, and it certainly took…
I mean, sometimes extra hours Per, days of labs, and…
students weren't happy because sometimes they were delayed. Thankfully, some of them were very understanding, but effectively, I… I don't have the capacity to do a rigorous assessment like that myself anymore. Hence, we are bringing in a new friend.
It is an AI. It is called AI Orate, and you may have heard of it. It is produced in-house.
in, Stella, our learning division, our learning… Why is it? Student…
teaching and… I can't remember the acronym, it's quite bad, but anyway, it's an in-house system. It obviously harnesses, some of the latest LLMs.
And I've been playing around with it, it's pretty good.
And what we're going to attempt to do
And more details will obviously follow explicitly once we try and get it out for next week, is the goal. But…
It's going to interview you on your code, and it's going to be tied to your Dropbox
And so what's going to happen is, you're going to complete your code for your first lab, which you won't need to do this week, so don't worry, and then it's going to…
Examine you, or interview you on that code, and do a general assessment of your knowledge and understanding of the code through an interview.
Now…
The caveat is that I am not accepting its assessment as is. I'm defining it, I'm defining the rubrics, etc, and I've been fine-tuning it and going through the assessment several times already to see how it works.
Some tweaks here and there, but generally speaking, I think it's quite good. And so what's going to happen is it's going to interview you, and you're going to be submitting that
As, effectively, your lab assessment.
And I will then review all the transcripts to assign the marks. Now, this will still take me
Probably more time than it did going through one-on-one in the labs, but the one-on-one in the labs is just not logistically possible, and
probably wasn't as thorough. So I will spend a lot of time reading transcripts, probably, like, a short novel, I guess, each week to make sure that the marks line up. And, especially so this first run of it, where I want to make sure it's actually doing its job properly.
The percentage over all these planned 4 assessments, possibly 5, but let's say 4,
is only 15%, so the percentage is not meant to be huge. It will be a reasonable time investment for you guys, of course.
But the lab materials themselves will be assessed in the theory as well, so it's not that you're doing the labs only for these lab assessments. These lab assessments are just to ensure you have understanding of the code.
You can obviously understand the reason for this.
you can almost certainly use AI to do whatever you want to do regarding development of software, and specifically in this case, software testing, which is what we're focusing on.
But your understanding is the only thing which kind of separates you from a company hiring Claude, opposed to hiring you, right? And so, what I want to try and ensure is that despite using these tools, which I encourage.
You also have the fundamental understanding to debug, maintain, and explain.
And that's the goal. I want you to have and develop and have valued those skill sets, because ultimately, when you go into the workforce.
They don't… regard your ability to, you know, prompt Claude
As, you know, the most important thing you're bringing to the table. They think your critical analysis, your ability to
build maintainable, explainable software solutions is really more valuable, and so I think
I'm going to try and shape the assessments that way, and we'll see how it goes. But a bit of a long-winded way of saying we are using AI interviews for the lab assessments that will begin next week.
And provisionally 20% for the IRAT CRATs, and then 15% for the laboratory, assessments of your code, okay? What I've also generally done with this module is, because it's flipped like mass, I tend to give you the first lab sessions, as in
time, give you that time just to get ahead of the content. So, start viewing the online materials, start developing your labs, and get ahead of the curve so you're working one week ahead of the assessments. And that's what I'm trying to do here as well.
that's… that's generally what we'll try and do. Keep this week lab-free, so you can focus on catching up on everything, and really start and kick off the assessments next week. So, that is the plan.
If you do have questions relating to that, please dump them in the chat, and I will… I will get to them.
But I'm going to elaborate more on the details of each of the sessions. So… First, though.
more of an introduction. I know I kind of went through some more specifics first, but I think it's important that you understand that I'm trying new things here, and I'm going to do my best to assess you fairly, and just being very honest and upfront about it, I think, is the best way forward, and hopefully we will get something really valuable out of this.
But I want to introduce more the module.
the reasons behind the module, and then also, I'll try and distinguish between the topics in the first and the second half, and, you know, what the fundamental difference is.
But why V&V? Why verification and validation in the first place? I think one thing, you've probably seen images like this before, I think it's pretty appropriate. Whenever you're building a system, you have a plethora of stakeholders, right? You have a lot of different perspectives and opinions.
And… In order to ensure that you deliver what is expected, you have to account for
the differences in how the customer explained something, how the consultants described it when selling it, you know, how, what the customer actually needed, opposed to what they're asking for. So, here we just have a comical, you know, image of all the different ideas and perspectives of the system.
But what we want to do in verification and validation is come up with some ways of measuring
that we've met, we've verified the specification of our system, so we've met the needed criteria, and validated with… validated it with the clients, with the stakeholders, so that they agree that we have delivered what they asked for. So verification and validation is really…
A way of trying to ensure contract completion, With our stakeholders.
So it cannot be that we go in a way and develop a system, and then we try and say, hey, look, we've done it, and they're like, well, this isn't what I want. You know, this is not a desirable outcome. We obviously want to define in advance
if possible, and have a way of demonstrating that we have verified the system, it works as to specification, and validate it with the client, so that when we hand it over, they are happy with it. And so that's what VMB is attempting to do. It's attempting to find a formal way of ensuring we reach the desired quality.
Of the product that we are handing over.
So… The basic analogy I like to give is, This shirt,
Verification is effectively, does this shirt meet specification? So when we're talking about verification, it's the specification. Does it have two sleeves? Is it the correct size? Size large? Is it blue? Are there any buttons missing? So this is the verification steps that we want to perform to ensure it meets specification, whereas the validation is
Does it actually fit the customer, let's say? Is it comfortable?
to drive in, if that's what they're using it for. Does it match their eye color? Is it affordable? So, validation is all more about the customer satisfaction, the client satisfaction, or more broadly, the stakeholder satisfaction, and how we meet those standards. Whereas verification is more that it meets the technical specifications for a system. And so you'll see that these are quite distinct, but both
very important aspects of developing software. We want to verify it, is it correct? And we want to validate it, is it what they want?
Okay, so try and just keep these thoughts, with you in mind. I think I've messed up the animations here a little bit, but…
The two distinct parts of this module, David Sana, the program leader for SE, will be taking the second half, and that'll be focused more on the formal
side of V and V. Now, for us, what we will be working on is, quote-unquote, the informal side. Now, it doesn't mean we're just making things up, it's just more to say that
what we're trying to do is verify software through, like, limited coverage, so we'll do software testing and things like this, that's the main focus. But testing in itself is not a, you know, a cover-all. Like, we can't cover all exhaustive test cases for any reasonable-sized software system.
Okay? We just can't have that many test cases. So, it's generally a limited amount of, let's say, simulation of systems to ensure it works correctly. We might do spot checks on specific parts of the system to ensure the most important parts run smoothly.
And we will design our various different test vectors or use cases to ensure the flow through the systems work. But this is not, like, a formal, exhaustive approach to ensuring the quality of the system, and hence we refer to this as informal VNV.
Now, on the second half, and I won't delve too much into this, because of course David will be taking this.
But this is what we consider, like, formal verification and validation. And that's where we move in to use more formal mathematics, like horror logic, a lot of different types of logical languages, and we try to specify systems mathematically and
prove properties of systems mathematically. And this is much more important in your kind of, like, mission-critical systems, where any failure is a disaster and things like this. And we can say this much more formal, because this is rigorous and mathematical in nature. And so these are the two distinctions in the module.
I think, generally speaking, it's fair to say that the software testing side, the informal side, is much more what you're likely to encounter in the workforce and in the big bad world.
The formal side, may be a bit more specialized, but I believe having the formal knowledge, like, understanding how these processes work is actually very instructive for how you perceive, you know, debugging or, you know, error handling or testing in your actual development work going forward. So I think both are extremely valuable, and just to separate them, the first half we will consider informal, and that's the first
6 weeks.
Right.
So, as mentioned, this is the schedule for the first 6 weeks, and I will cover the schedule for the second.
We are introducing software quality today.
From week two, we're going to be starting our IRATs and TRATs. I will have, and I believe I have already specified what those are going to be on. I will lay it out in advance, like in mathematics, the subject's covered for each, so that you know in advance what you need to be studying.
And we will also be doing our lab assessments.
As mentioned, we're using this AI
or rate system to interview on your code. My initial plan is to…
have this, you can… you do it in the laboratory sessions themselves, but I'm still working out the tweaks. We might try and do it asynchronously as well. I just want to make sure that it's not AI interviewing AI, right? So…
Obviously, some… some concerns to address there. But this is… this is the general plan. If you notice in part
in the week 6 at the bottom, I do have Consultation Labs slash lab assessment 5.
I do have some…
additional materials in the labs that I'm playing around with adding, and then building an assessment for.
We'll see if I have time. The idea is to build something in the assessment, in the lab itself, which is useful for you guys, and then I want to assess it as well. We will see about that one, though. So, depending on how the other weeks go, it will be either added or omitted, depending on how things work out.
Okay, so a little bit of variability, unintentional, but necessary as we work through some new technologies. And then this is the second half of the module.
This is what David, plans to go through. It may be subject to change, but as of now, he's introducing formal methods, and you're going to be using FRAMAC and formal verification in your laboratories.
He's gonna have a quiz in week 10, and then a final evaluation quiz in week 13, and I believe this is, as of this weekend, what this schedule will look like, but of course, I'm not going to elaborate too much on this, because he will be conducting this half of the module.
Right.
Now, the percentages… As I mentioned, some of this has the asterisk, because it's provisional, but
Actually, I didn't… for the exam, it shouldn't be a provisional asterisk. It is 30% for the exam, so we are having an exam, which is MCQ and short answer. That kind of formalized setting of the exam is a good way of ensuring people's knowledge is actually their own. So that will be there.
And then the lab assessments, should have the asterisks, which for my half will be
the 15%, and then the 20% for the IRATs and T-rats.
This is provisionally what the percentages will look like. As I say, the lab assessments might have a bit more…
variability, depending on how well or poorly they go. And then for the second half, there'll be 35% for the quizzes and assessments. I'm not sure exactly how David's breaking that down yet, so I'm just…
putting it out there, it's 35%. Effectively, this module is symmetrical, 35% CA first half, 35% CA second half, and a 30% exam, which splits 15-15. So each half is equally weighted.
I guess the only thing to possibly consider as a difference is, for your exam, you'll be 6 weeks removed from the first half, so you might have to revise and refresh yourselves a little bit more with that, whereas the second half, you'll be going into the exam, from the second half material, so maybe a little bit fresher.
Okay.
Oh, and I think I noted there, the laboratories also have some content in them as well, so there's some
Notes and reading related to the theory in the labs to make it relevant to that particular lab, and so that's obviously accessible as well.
Right, so just like with the rats, we plan to do something similar with our time, so we have our sessions from 11 to 1.
Last, I recall, to the zeroth minute, you'll be revising.
You will have the IRAT, which will be about 20 minutes. Then we will do a team division in groups. This will work more generally, so previous…
years, I had done groups.
for the discussions, set groups, and I had groups for the labs. That won't be happening this time.
there won't be assigned groups you can work with and help whomever and discuss together. I'll open breakout rooms and set them randomly, and you can discuss in those rooms to help each other learn. I'm totally fine with that. The reason I'm trying to do it
More open this time is because
when we conduct the online AI assessments, it's going to be per individual, and so I don't need to go and talk to you in various groups. I hope you support each other in the labs regardless, but there won't be a team element, other than your own choice of discussion partners.
And then you'll do your TRAT after having a discussion, generally less time. These times may vary slightly, but just to give you the idea of the flow, and then, like before, there'll be about 50 minutes, possibly a little bit longer, possibly a little bit less, where I will go through the intended solutions.
for those questions, such that you can work out what you got right and got wrong, and understand what was the correct or intended answers. And if there's any, you know, clarifications or challenges or otherwise, you can follow up in that session or via email afterwards, and I will address them, just like in mathematics.
Okay, so that's the general flow, that's the general plan. That will start from next week, of course, not starting right now. And as I say, this is, I think, a very effective way to get that incremental learning, kind of forcing you to absorb
digest and regurgitate. Bit of a disgusting analogy, sorry, but regurgitate some of the materials in those assessments each week. Times will vary slightly.
I think… I'll try and start the IRATs a little bit closer to 11. I will put out the…
the calendar timers, in your LMS as well, so that you know exactly when it's starting.
So a question in the chat. Try and write your questions to everyone, because then I don't have to… okay, we are… are we using… effectively, you're saying, are we using Respondus? So, I think you know that we're not using Respondus, because it was discontinued, right?
So, we're using, of course, Examiner, which has gone through a whole
slew of fixes, since you would have last used it, so I'm hoping it's much more stable. Obviously, I… I'm not working for Examiner teams, so I can't guarantee any of that, but yes, we will be using Examiner for the quizzes.
And I will…
set them up accordingly, and hopefully we don't encounter issues, and if we do, we'll try and solve them.
Oh, just double checking, because it still says…
And Lectures, thanks. Oh yeah, sorry, yeah, it's possible that I,
Yes, I was pining for the use of Respondus and may have left it in, here, as you can see. But, yes, I should update that to Xaminer, my bad. So, just to fill you in, though, this is something that I didn't… I wasn't really informed of initially, but when they changed from Respondus, not that Respondus was perfect at all, but…
We were under the impression that this was… a intended…
you know, decision to change technologies. But what transpired later is I realized, after discussions with the teams.
the… Responders didn't want to continue their contract with SIT. So Examiner was…
a necessary choice. So it wasn't that the university was trying to disrupt things, actually, at all, or change things. It was actually simply that, Respondus discontinued their contract.
and they need to find a new system, and that's where Xaminer came in. And just like the initial years of Respondus, it was quite temperamental, obviously, with Xaminer, I'm sure you know, but…
things should be getting better and smoother, and yes, I will update the slides on this as well, but…
Yes.
We will not be using Responders, possibly ever again.
But, yeah, just to let you know that it was not a… it was not a case of switching something that worked for something new, it was more that thing decided not to… it basically broke up with us, right? It said, sorry, I found someone else, and then, you know, we were left with…
Examiner, okay? That's… that's what happened. Very sad, very sad breakup story. Okay.
Right, so, when creating this course many years ago, I was trying to use a lot of the formal
metrics and textbooks. Now, I wouldn't recommend reading these, necessarily, because I'm referencing only what's still somewhat relevant, particularly when we're talking about metrics of reliability and applied software management.
These are just, or were used at least, to inform of the different quality metrics that we have been using in software. These are more kind of classical approaches. The model checking book, I think, is still pretty good, but this is more relating to the formal methods stuff, and it will inform you in that area.
But model checking is a particular flavor of formal verification that may not be covered, actually, anymore. But I still think the book is quite instructive on formal methods.
And then one thing that I still refer to, and it's still relevant, is, the software testing primer. Now, it does have some
possible dated terms, and obviously doesn't consider the prevalent use of AI in the same way, but the software testing primer is still a relevant source, it's a free online source, which can give you a good idea of the general
purview, the general landscape of testing, why it's used, different types of tests, and it's quite a short read, so this is something that I think is quite informative and still useful, and that you can use to kind of further your knowledge, should you be interested.
And also, just, oh, yeah.
Testing is effectively the search for truth. You can hope that your software works, or that you can know it works through testing. The no is maybe a little bit strong here, but that is a quote from the book.
I think…
Generally speaking, what I try to do for all the theory is I've aligned the theory with the international standards for quality testing, testing foundations.
qualifications or certifications. And so, my idea was that once you…
do this module, you can effectively do the foundational test or certification from the international, standards for quality software testing.
And that is still aligned. The theory has not changed in the last few years, the theory is the same. The practice obviously has changed and become more automated, and hence, we have changed the labs more than the theory itself. But…
A lot of the, theory is still, linked to software testing primer and the actual certifications in the area, which are still valid.
Okay.
Annie Hugh, oh, yeah.
Anyhow,
what I've highlighted here are effectively the learning outcomes for this particular lecture, and I'm highlighting them because next week I'm going to be assessing you on this lecture. Okay, the IRAT, TRAT will be just on this lecture. Very nice, just on this lecture. So.
What we're trying to understand is explain the necessity of ensuring software quality in software engineering, explain intrinsic software quality metrics, customer-orientated metrics, explain and distinguish between the factors contributing to poor quality software, understand the definition of software quality and software quality assurance, and apply software quality metrics in software quality assurance.
So…
regarding to quality or regarding quality, these are the things I want you to understand. And specifically on software verification and validation.
We want you to be able to distinguish between the two. We've basically covered that already. We're going to look at static and dynamic. These are the two broad strokes.
types of VNV in software, and then understand the definitions of VMV is also useful. But generally speaking, these are quite broad learning outcomes. I'll flash this slide again at the end, just to see if you've taken away any of these, but
Ultimately, I think this is a very modest set of learning outcomes for today's lecture.
So…
First, the motivation. Now, I mentioned a little bit of the introduction, kind of the motivation, but interestingly, this whole kind of field
Came about through… big software failures, and so…
Back in the, olden days, pretty much… prehistoric, right?
We started building software into our systems. We started using electronics to govern systems where most things were previously manual.
And, of course, as you can imagine.
things started going wrong. We started getting errors for all sorts of reasons, and this… gave birth to…
a lot of the theories, practices that we're covering today and going forward, as software systems became more prevalent in day-to-day lives. And this is obviously no more… no less true today than it was then. In fact, it's more…
true today. We use software systems for almost everything, and so ensuring their quality through verification and validation becomes more meaningful. But just to give you some examples, so…
Two classical examples I'd like to cover, because they're really at the initial stages of this field. So, the THEREC 25 radiation overdosing from 1985 to 1987. So, in cancer treatments, radiation therapy was obviously a useful tool, still is today, and the THREC machine was using software to administer radiation doses.
But…
unfortunately, I mean, unfortunately, probably doesn't even do this justice, but there were at least 6 cases of overdoses of radiation due to software issues. And when we talk about overdoses, these were hundreds of times over the dose.
And what was effectively happening, there was a race condition from the value being written and the value being read, and we were…
Overdosing patients, and unfortunately, three…
definite fatalities caused by this, likely more. And so this is one of the first cases where they're realizing, actually, how do we ensure this type of thing doesn't happen? Like, how do we verify this software actually doesn't do this?
And so they looked into, they had an investigation, they realized the code wasn't independently reviewed,
There was never testing of things in combinations.
So two separate, you know, threads, let's say, trying to communicate over shared resources. These weren't, properly simulated or tested, and this led to the race condition issues. So this is one of the kind of first
Really, big-scale investigations into software quality and lack… or lack thereof, and then how this kind of shaped… shaped the field going forward.
Another example, which is also quite prevalent, is…
in, the European, Ariane 5 space mission, which in 1996 cost more than $500 million, which was an awful lot at the time.
Basically, due to data conversion from a floating point to a 16-bit signed integer, it changed the trajectory of the rocket, causing it to explode. Thankfully, this was not a manned mission, but a huge financial cost for what is simply a data conversion issue.
And so this was another situation which brought to the forefront, how are we actually testing these systems? What type of rigorous processes do we have in place to ensure these things don't happen? Now, obviously, these are big, kind of mission-critical, or extremely financially valuable.
tools, and any failure is catastrophic in finance or in loss of life. But for general case systems, this is also true. We want to ensure software quality, and so a lot of the principles and practices of verification and also validation, to some extent here, are
indeed, important in any software we develop as well. But these are kind of the initial types of catastrophic failures that led to the need for types of quality controls, yeah.
Okay, and then just about on the finance side, some of these are a little bit older, but it's a 2024 reference in here, but just to give you some idea and not dwell on things, like, the actual cost
even, like, you know, 20-plus years ago, is huge. I mean, about $60 billion then, presumably much more now. I probably should have updated this slide, sorry about that, but…
Even then, there was an estimated, like, one-third of this kind of loss based on poor software quality or software failures. An estimated one-third of that can be actually just improved by having standard testing in those systems, or a moderate level of testing.
And…
This has been a continuing problem throughout the industry, the software industry. You must know yourselves, when you run your software, you get the blue screen of death, or you get some sort of issues. You kind of think, oh yeah, I mean, this is just common. Obviously, software crashes, systems crash.
But ultimately, if your car breaks down, that's actually quite…
a rare occurrence, hopefully, and you're like, wow, this is terrible, why is the car breaking down? It's brand new, or whatever it might be. But with software, we're like, oh, it's brand new, of course it's gonna crash, of course it's gonna fail, and we've kind of accepted a lower level of standard, and actually, these collective failures of software have huge economic impacts, if not, you know,
Impacts on human well-being and health as well, depending on where the systems are used.
So, a lot of interesting articles and sources, you know, over the years of…
Estimates on how much this costs, but…
No doubt these estimates are only increasing and set to increase further as software systems become more prevalent in almost everything we do. Hence, the cost of poor quality systems and software failure becomes a bigger impact on global GDP and the economy at large.
So there's… there's really strong motivation for
learning, understanding, and building in strong verification and validation practices in your software. Because your software not failing, your software being of a higher quality means it's going to be sold, maintained, and
be much more effective in the long run than other alternative solutions. So there's a lot of motivation why to focus on this field, particularly for yourselves under this particular program.
And… Some of the big investors in this area.
I'd like to cover NASA, because NASA and European Space Agency, other space agencies, Chinese Space Agency, I'm sure, is very interested in this as well. But, NASA, for decades now, has been running formal methods, symposiums, where
They really focus on how to formally analyze and assess systems, ensure that they are not going to crash and fail. And even now, obviously, a lot of these space missions have issues, but, the…
investment in this area, in terms of research and otherwise, is extremely high, and will continue to be so as well. And they have their own definitions of verification and validation sourced from their website here.
But effectively, they align with the universal definition. So verification of a product shows proof of compliance with the requirements, effectively meeting all the shall statements, or the must statements. And validation, the product shows that
The validation of a product shows that the product accomplishes the intended purpose in the intended environment, and so these are alternate definitions, but effectively saying the same thing about verification and validation.
Okay, so the way I like to simplify it for this module is verification, are we building the product right? Okay, is it following its specification? And validation, are we building the right product? Okay, are we building the product right, or are we building the right product?
Yes, it's a simplification, but I think it effectively conveys the difference between the two. So validation, effectively, are we building what the user really requires, what the user really wants, or really needs, you could say? And then, are we building the product right? Are we building it to the specification, the agreed specification, the technical scope of the project?
So, there are a lot of definitions you'll find from, you know, NASA and otherwise, and IEE, etc.
But this is the kind of synthesis into a single sentence definition to make your lives a little bit easier to conceptually identify the two. Okay, so are we building the product right, and are we building the right product? It's a good way to categorize these two.
Okay, so in the, you know, IEEE Book of Knowledge, you know, you'll find a lot of these
landscapes, of all the different, you know, validation, verification tools, and this VIN diagram is used there, and I think it quite instructively encompasses where testing fits into the picture. So, verification and validation.
You know, goal analysis, prototyping on the validation side, and verification. We have proofs of correctness, things like this, robust analysis.
But then somewhere in between, we have this overlap with our testing, or we have acceptance testing, like UAT with customers, that's actually validation. We have, unit testing, that is more verification. Is it meeting the technical requirements, specification for the code? And then in between, we also have, like, regression testing, which
can be a bit of both, and system testing, obviously, that does some verification, but also validates the end-to-end testing with the client's needs in mind as well. So I think this is a good general picture of, like, where testing fits into the broader picture of validation and verification, and that's because testing is the informal
focus of this half of the module. But validation and verification span beyond just testing, but testing does encompass a nice subset here for your reference.
The other thing to talk about is the types, the general types of verification and validation. So, we have two types, thankfully, very easy to remember. We have static and dynamic. So, static is when we're trying to…
Verify and validate the system without executing code.
And so this can be, like, AI document analysis on the requirements, things like this. But also, in your IDEs, like, any, you know, squiggly lines that come underneath your code is effectively a form of static analysis with the, you know, automated compilers and the IDEs telling you, oh, this variable's never referenced.
Or, you know, some sort of issues, like it can't find such and such. So.
that is also a way of statically, ensuring quality through verification and validation, okay? And then the dynamic side is, you know, much more simple to describe. Effectively, this is when we're actually executing tests, executing the code, i.e. software testing as the primary example here.
And we do this to find errors or issues that we can then correct. And effectively, static and dynamic analysis and verification and validation are what we're trying to use across the board. So when we're developing software, we're trying to ensure that our requirements for the system are not inconsistent. We want to analyze them to ensure they're aligned with the client, validate them with the client.
verify them, ensure that they're internally consistent. We use the static analysis on the code we write to ensure there's no errors before we even compile and build the code.
Or before we at least ship the code. And then, dynamically, we also want to build, run the system, do use case testing with the system to ensure that dynamically the system is also being verified and validated as well. So we have static and dynamic as the two kind of classifications of verification and validation. Quite straightforward in terms of
There are scopes.
Effectively, another summary table. Static testing is done without executing the program. Dynamic testing done with executing.
Static testing is focused on preventing defects, so it's more in the ensuring that we're not building defects into the system with our, kind of, documentation or otherwise, and dynamic is more testing what we've developed to ensure we can find the defects and correct them.
Static can be done from the very start, obviously, from the documentation stages, whereas dynamic, we actually need some sort of system to be able to test it.
Generally, static analysis can be lower cost to prevent defects, and that's simply because if you can find possible defects, inconsistencies, or otherwise, before developing the code.
Obviously, it's going to save you money than trying to correct it later in both, maybe, the documentation and, of course, the code itself.
And then, static can be time-consuming, because analyzing the, documentation, you know, is… is more tedious, and obviously we use AI tools to…
analyzed as well, but we still need human oversight to do it thoroughly and properly. Now, at least, maybe that will change. Whereas dynamic, we can automate a lot of these things, so we can create tests, yes, manually or automated, and then run them automatically for detecting
defects or otherwise. So these are just the, kind of, the general comparison points for static and dynamic. I think in terms of what you want to understand is just the general principles of where they come into play in verification and validation.
I don't want… I wouldn't need you to memorize any particular sentences that I'm writing here. This is more just to give you a general understanding.
So that if questions come up, like in MCQ style, you can identify the ones that make the most sense.
Or if you're asked an exam question, you can
form some sort of general description that aligns with the idea behind each. And that's really true of most of the things I'm going to cover.
Okay.
So now we're gonna cover the big…
Topic of today, which is really software quality.
So when we're talking about software quality, we're effectively discussing something which is hard to… to quantify a lot of times. And so when you say, oh, my software is of high quality, like, what does that mean?
And over the years, Different academics, different research, different organizations have come up with measurements
that we use to assess quality. And these measurements.
aren't necessarily mutually exclusive, like, they can all be applied, together. And we're going to look at some of the more useful ones, some of the more classic ones, in this module, at least in the start of this module, and we can use these as, like, a framework to understand how we might express or prove
Or assess the quality of our software systems in a more objective way.
So… As mentioned.
Quality becomes a big, important factor in the early days of software use in mainstream and mission-critical systems.
And trying to understand how we can build quality systems becomes a big topic in the early days of the software engineering landscape. And so, yes, effectively, any,
Errors or things we can learn from past mistakes becomes wisdom later, and this is what we hope to achieve in the quality space, is learning from previous mistakes and building better quality systems.
Now, the first thing we're going to look at before we go into much of the measurements is…
Or are some of the factors that contribute to poor software quality?
Now, what I've decided to do this year, I have previously used the following list.
Which is…
A pretty, extensive, but some maybe a little bit loose terms that categorize, let's say, causes for poor quality software.
But what I've decided to do this year is harmonize, with, DORA, which is DevOps, Research Assessment, which is, like, Google's, kind of.
big, research…
organization within the space, and trying to align with more their broad categories of factors that relate to poor quality software. And it's more so that we can all be talking on the same terms.
And it's also because a lot of these terms, such as, like, human factor or communication failure, are a little bit, tight, and actually, generally, I think the categories are, or can be expressed
in different ways and more broadly. So I'm going to move this list of 9 to a list of 6, so that hopefully is good news for some of you. But what I'm trying to do is…
talk in a more harmonized language with what is latest today. So, we're talking now about these factors. So, people, communication, and organization culture would be one factor.
Planning, workload, change pressure, another. Requirements, architecture and design. Implementation, maintainability.
Configuration dependencies and software supply chain, and then finally, verification, delivery, and operational feedback. I guess validation somewhere.
could fall in there as well. But these are broadly aligned with a lot of the,
research that comes out of DORA and, some of the ISO standards. So I'm trying to just simplify what you need to take away from this, and then also harmonize.
Suffice to say that each of these factors, as described here, this is just a description of that domain.
memorizing it, I guess, will be easier in some sense. You know, if you're asked to give examples of these, you can just regurgitate the words used, but generally speaking, if you can explain
Some sort of equivalent description of any of these.
that is also, like, worth marks, let's say, if you're in an exam setting or otherwise. Like, if you can talk about, you know, communication, organizational culture in maybe different terms, but meaning the same category, that's totally fine. Again, I'm not trying to…
trip you up on word memorization here. I'm trying to make these categories self-explanatory as well, so it literally says some of the factors in the name. It's not meant to be.
Misleading in the name itself.
And so, just an example of something that may overlap a lot of these
Quality factors, so some sort of defect, like you could have an ambiguous late requirement, which is implemented hurriedly and merged without adequate review, and released after incomplete regression testing.
So, that will be an example of a defect that spans multiple categories, and so any of these categories can obviously introduce their own defects and issues.
But they are not mutually exclusive categories. Of course, we can have defects which span all these different categories. So these are really the factors.
the categories here, which will influence the quality of our software, and these are things that we want to pay attention to, and what we're going to do is cover just a general breakdown of each of these, which I want you to kind of grapple with and understand going forward.
Okay, so first, one of the most straightforward ones is people, communication, and organization. And I think I'm just going to cover these six, and then we'll go into a kind of small break, so bear with me, just focus for a little bit longer, and then we'll all make it through. So people, communication, and organization culture.
This one is, again, as I say, probably the most straightforward.
So the skills, communication, ownership, the working culture.
These determine how, kind of, information is shared, decisions are challenged, and risks are managed. And you can imagine that an organization culture in and of itself
can be detrimental, somehow, to quality. If you aren't allowed to challenge different decisions or otherwise, this can lead to poor quality things slipping through as well. So, these are all factors which can contribute to poor quality software.
Some of the specific contributing conditions I'm going to highlight in each of them, but vague, incomplete, or misunderstood communication.
You will experience this a lot. This is one of the biggest challenges.
Is to communicate clearly about the system that you're developing, the system you need to develop.
Because effectively, communication is, I'm trying to make some sense of, like, what's in my brain, all those fuzzy kind of thoughts, and articulate it in a way that your brain can comprehend, and we have the same idea. And it's actually extremely difficult. Of course, as humans, we communicate all the time.
But in software engineering.
communication has to be precise, right? It's not just so we can get an idea, a general idea, like, a lot of times we have to have precise, shared ideas, and so communication is a big part of
where we could introduce possibly poor quality, software. So ensuring, as best we can,
Clear and precise communication. And for the people issues, we might have gaps in knowledge or experience, which leads to, obviously, poor development. Unclear ownership, this is a big thing. Relating somewhat to people on culture, like, who takes ownership of certain implementations.
Handover, this is another big thing. Who's handing over? How are things handed over? How is that communicated?
And then…
on the people level, a lot of companies' work can be very stressful, there can be fatigue, additional or excessive cognitive load, which can really be detrimental to a quality software development. And then, as I mentioned from the top, the actual culture of the organization can be really detrimental if
Things cannot be challenged, things don't need to be explained or justified. Obviously, that is ripe for defects and issues to seep into the software.
Okay, so planning our workload.
This is obviously another issue. So, if you have unrealistic schedules, excessive simultaneous work, late changes, you don't have enough time for analysis, design, review, and testing.
Now, this one, again, a lot of the projects you do, you'll have tight timeframes, so if you have unrealistic deadlines, this can lead to poor quality, too much work simultaneously.
Poor quality, large changes delivered in one batch. That's a big recipe for disaster. Late changes happens a lot of the time. You display your kind of prototype, and the client says, oh, actually, can you change this? And it needs to be sent back by the next day, or something like this.
And, then, you know, changes of different platforms or infrastructure, last minute, oh, can it function on this platform as well? Oh, I also want to have an iOS version or something like this.
A lot of things…
Around planning and time constraints, will be fitting into here, and this is obviously a big deal when you're trying to meet the schedule of another industry partner, etc, and having insufficient planning or inaccurate planning will obviously lead to a poorer quality system.
And then a big one, requirements. I think requirements almost is one of the most important things, requirements engineering and specifying the correct requirements. And this also relates to the architectures chosen and the design of the system.
So, all of these three, if they're not adequately done with all the stakeholders' needs taken into account, then this is obviously a problem for producing a low-quality system.
A lot of issues here, ambiguity, as in, as I mentioned, that translation, almost back onto the communication, but if I have a requirement which is ambiguous, this is a factor in a poor quality.
Misapplication of technology. Technology changes all the time, all the time, and a lot of times we may neglect new technologies, which might have been more appropriate, or we may reuse only what we're familiar with, which might be less appropriate than other options.
So ensuring the highest quality means ensuring we choose the most appropriate technology,
Sometimes we go through the path of least resistance, so choosing what is maybe the easiest solution, but maybe not the most feasible solution in the long term.
And then, maybe, if we're talking about architecture or design specifically, we might design things poorly, so things are a bit too tightly coupled together, so one change requires a cascade of changes.
We might make invalid assumptions, more relating to the requirements, which lead to poor quality systems later, and
inconsiderate… inadequate consideration of failure and recovery for the system. So, again, a lot of this category is more about the…
Requirements being maybe not formally or precisely defined, and then the resulting architecture and design being poor.
I think this is possibly becoming a bit worse now that we're using AI to do a lot more, like, vibe coding and development work, and what you find is that tends to be, like, an incremental thing, where you'll be like, oh, can you do this? And then, you know, make this change, and you… you end up with quite, like, a cumbersome
code, which is not designed particularly well, but it works. And this is obviously a lower quality software, it will become slower and harder to maintain.
And then, one of the more obvious ones is implementation and maintainability. This is obviously a big factor which can contribute to poor quality software.
So, implementation decisions in the actual codes can make it difficult to understand and maintain, leading to lower quality. We don't have sufficient error handling, exception handling. We can,
Have, inaccurate boundary conditions on our inputs, so they can put in
Values which will break the system.
Unsafe concurrency and resource handling, kind of related to what we talked about earlier, but if we have multiple parts of the system which are communicating through a shared database or otherwise, obviously, if we don't have this done in a safe and consistent way for race conditions or otherwise, this can be an issue.
And then, as I just mentioned, AI-generated code is accepted without adequate review. I think this is a very big problem right now. Possibly as things get maybe better, this becomes less of an issue, but certainly the case that right now, AI is great at developing, you know, small-scale
Software, and if you're a software developer, you maybe have a lot of different agents working as your employees, as it were, to develop your systems.
But because AI is still based on large language models at the moment, a lot of these are obviously… well, these are probabilistic in nature, which means we don't have the precision that we necessarily want, and it will lead to, you know, inaccurate
Development, or low-quality development, especially if we do this in more of a piecemeal, incremental development.
And then configuration dependencies and software supply chains. This is another factor in poor quality. This one is more,
We want to ensure we have a reproducible configuration and a consistent and tested use of third-party tools. We also want to make sure we have things like proper version control, of course. That probably goes without saying, but that is a low-quality system if it doesn't have proper version control.
We also want to ensure we have the environment figured correctly and realistically, and the other one is dependencies. We will have so many dependencies in our systems, we're all using external resources and libraries and otherwise, and APIs.
But we want to ensure that we have the checks and balances within our code to account for when those don't necessarily work, or we want to make sure we keep those updated. But these are definitely a factory source
Of defects, which will lower the quality of our software.
So that's something to consider. And then finally, the verification side. We want to ensure we have a systematic review process, a testing process.
So that we can find where all the errors are and reduce the bugs, reduce the defects, increase the quality of our software. So, some issues are generally when you're
when you're kind of, like, building a system, you'll think of maybe only the positive path behaviors, so you'll just test all the positive use cases, as it were, and not consider what if the users do something counter-intuitive or somewhat destructive, and by not testing or neglecting those negative or, external,
I guess, unusual use cases. You might miss a lot of things.
You want to ensure you have realistic test data for your particular environments and setups, you know, something akin to how the system will be actually used.
And then, you want to ensure,
That any failures, are actually worked on and used to improve, not just a temporary fix, but improve the underlying root cause, to improve the quality of the system going forward.
So each of these are factors, these are basically categories which
If not given sufficient attention, can lead to
failures and defects, and essentially lower quality software. And so, I'm elaborating these here, some of the contributing conditions, but none of this is
required as a memorization exercise. This is more if you're asked to speculate on some
important categories to consider, some important factors to consider in software quality. You might want to talk about, let's say, planning and workload changes, or people in communication, and then give some of the general concepts. And as mentioned, these are not mutually exclusive categories in the sense that we can have defects which span a lot of them, but they are quite logically distinct categories in terms of, you know, the verification and testing is somewhat distinct from people
Communication, even though there's conceptual overlap as well.
Okay.
So…
as with much of this module, what I've been trying to do over the years is keep standardized with
the ISO, the International Software… the International Standards, and I'm trying to keep in harmony with the IEEE definitions, and I think we've broadly managed it, and as I've said, I've just updated the previous factors.
To ensure that we are talking the same language, broadly speaking. So, similar here, we have what the IEE defined as quality is the degree to which a system, component, or process meets the specified requirements.
And it also defines it as degree to which the system, component, or process meets the customer or user needs or expectations. And you can kind of see how this is pretty much talking about verification and validation under quality. And then the difference between defining quality
And software quality assurance is… software quality assurance is actually the planned systematic process, so the process for ensuring quality, whereas the software quality itself is more of, like, a measurement of how much quality is in the system.
So software quality assurance is the planned and systematic pattern of all actions necessary to provide adequate confidence that an item or product conforms to established technical requirements.
or two, a set of activities designed to evaluate the process by which the products are developed or manufactured. So again, a small distinction here, but when we're talking about software quality.
We're talking about possibly measuring it in terms of verification and validation, at least in IEEE terminology, and this is more a metric, a measurement of quality, whereas software quality assurance, SQA,
is related to the actual processes in a company, in a development team, that ensure quality. So those are two distinct things. One is to measure the level of quality, and one is to ensure that we meet, we have quality in our systems.
Okay.
We've reached… The, the first milestone of today. So we're at Mini Quiz 1.
Now, MINI quiz one?
We'll be preceded by Mini Quiz 2, but it is a very mini, mini, mini quiz.
Now, this quiz is, 100% of your grade. No, this quiz is worth nothing.
Other than giving you a distinct advantage by, hopefully retaining the information. So, this is just repetition of some of the things we've covered. Now, I know half of you are probably asleep, and the other half of you might not be listening. So, with that in mind.
we will have a little quiz here. The idea is write up or type up your answers as you go. Don't just skip ahead, don't just look at the answers, don't just wait for them to arrive.
In an assessment.
You want your brain to be able to recall information, especially for MCQs. You just want it to be able to see this, recognize, oh yes, this is the thing we discussed.
If you do not exercise your brain at recalling this type of information, it will not be good at recalling this type of information, right?
it will just learn to do whatever you do with it. So, that is just my motivational pitch.
But, effectively, if you just train yourself to look up the answers, Your brain will not…
learn what those answers are. It just learns, oh, I need to look up the answers.
If you train your brain to try and recall the answers.
it will maybe be bad at that initially, but through practice, it will get better, and then when you come to your assessments, lo and behold, you'll try and think of something, and it will be there, opposed to thinking, oh god, where's my laptop? I want to look something up.
So anyway, the best way of doing this is actually to write down and type up your answers as well, because you may delude yourself into thinking that you remembered stuff maybe when you didn't, and by typing it up, and then we go through the answers, you will actually realize
Whether you, in fact,
got the answer correct, opposed to just thinking, yeah, I was kind of thinking something like that, because we do that a lot, but actually it might not be the case.
Okie dokie.
So, mini quiz.
TOK.
What is the difference between verification and validation?
Okay.
Three marks.
Imaginary marks, but some sort of measurement of how well you're doing.
Two, how many factors?
Contributing to poor software quality, or, sorry, I've repeated stuff here, poor software quality software. Can you name or describe? Okay, so,
remove that extra software, but how many factors contribute to poor software quality can you name or describe? We covered 6 of them just now.
Can you name or describe them?
And… 0.54 each.
And then provide a definition of software quality. I just provided you with a couple, but you can come up with your own, provided they seem reasonable.
And then, lastly, provide a definition of software quality assurance.
Okay, so we just talked about software quality, software quality assurance, and how they're distinct.
So let's see if you can come up with short definitions. I've tried to assign marks here which somewhat mirror maybe what you might get in an exam in terms of a marking scale. Maybe not quite, but almost.
And that should just give you an idea of…
You know, how your answers will be measured here.
So I'm gonna give you, like, 5 minutes or so.
Maybe a little bit longer to just go through, these.
you know, type up your answers. Try not to look at the notes we just went through, because then
ultimately, you're not training your brain to do anything. The whole point of this is to see what you can actually remember. And by…
thinking about it, and then we go through the answers, you'll start to crystallize, those, synapses in your brain will start to link together, and you'll start to associate the memories accordingly. If you just look things up, again, all you're doing is short-cutting that process, and
When it comes to an assessment, you will not be able to recall things.
Okay, so I'm just gonna give you 5 minutes, and I'll be back in a couple minutes.
Alright, how is it going? What is the difference between verification and validation?
How many factors contributing to poor quality software?
How many factors contributing to poor software quality?
Can you name or describe?
I think you can remove either of those softwares, actually, and it works. And then provide a definition of software quality, and then provide a definition of software quality assurance. As we just went through, they're distinct.
Alright, so I'm assuming that most of you, if you're attempting this, have attempted it somewhat, and so let us proceed with some of the
answers. Or all of the answers, even.
Right.
So what is the difference between verification and validation?
Verification, okay, are we building the system right? And validation, are we building the right system? So, are we building the product right, or are we building the right product?
Does it conform to the specification? That's verification, or validation, is it really what the user actually wants? You can describe these in a variety of ways. Obviously, I gave some different definitions, and then I kind of
gave you what I think are the most terse and easiest definitions. But anything similar to this, anything aligned with this would get you the marks.
I think maybe three marks is possibly a little bit generous. If this… if this was an exam question, which I guess is unlikely to be, but you might have exam questions which are somewhat, definitional and simple, might be more like a two-mark question, or maybe a one-mark question, even.
Okay.
So…
This slide is a bit all over the place. But how many factors contributing to poor software quality can you name or describe? So these are what we covered earlier. We're talking about people, communication, organization, culture.
I think, you know, if you talk more generally about communication, that probably covers that one sufficiently, but I think more interesting parts of it relate to organization culture as well. And then planning, workload, scheduling, if you mentioned scheduling, things like this.
for the second one. For the third one, requirements. In requirements, engineering, and issues might sufficiently cover that, I think. And then, obviously, that leads into architecture and design, which are also specific ways you can introduce poor quality.
Implementation, maintainability, again, poor implementation, poor coding conventions, you know, poor maintainability practices in terms of
the way you're doing your development. And then, configuration dependencies. Dependencies, I think, is a big issue.
A lot of us build systems which rely on external APIs, tools, or otherwise, and ensuring that we have robust
frameworks in place to support those, and as they change, alter the codes accordingly. That's a real way to introduce poor quality into our system. And the last one, which is a little bit obscured by the marks here, sorry about that, is more about
verification and, testing. So this is really…
Do you have sufficient, test infrastructure to ensure that things are analyzed and developed, sorry, released?
After they have met certain standards for quality. So all of these, and the last one you can maybe just talk about testing more specifically to cover that one. So all of these requirement, sorry, all of these factors,
I think you can describe each of them in a slightly different way, but effectively, these are the six factors, or the six categories of factors for
Affecting, quality of a system, and possibly introducing a lower quality into our software system.
And then, software quality?
As I mentioned, you can just use the one we went through, the degree to which the system meets its specification, and the user needs. I wrote OR here because I introduced both of these. But software quality can be discussed of… discussed in terms of the verification and also the validation.
And then, software quality assurance, as mentioned, we're looking at the processes in place. So, if you mentioned just the processes.
In the development lifecycle, or in the company, to…
try to ensure high-quality software. Something along these lines will be fine. I'm giving the precise definitions here, but these are the… these are exactly the type of questions where you can write your own explanations, and providing they align in terms of the meaning, then you're getting all the marks as well.
Okay.
So, if you're playing along at home, you could have got 10 marks there. Congratulations if you got all 10. And generally, repeat to learn, so, learn to repeat, I think, is a general good approach to, trying to solidify certain knowledge in your brain.
Okay.
I say time for a break, but we don't have time for a break, so let's skip that one. That quiz was effectively the break. So…
I think we should be able to get through the second half on time, and finish with a quiz, which will give concrete examples where you can assess whether you're able to do these quality calculations, or calculate these quality metrics. And that is, in fact, what we're going to cover now. So, we talked about factors.
of… categories, in fact, that were factors in poor quality software.
But as I mentioned from the top, measuring quality is actually something we're very interested in. How do we actually measure the quality of software? And this is where software quality metrics come in. And there's a variety of companies, of academic research, which looked at ways of trying to evaluate, objectively, at least.
give a metric for quality of a system, particularly a software system. And we're going to discuss a number of these here, and…
Most of which I'm not going to ask you to memorize anything specifically, but more being able to apply some of these and understand why they may be used.
So… One point… Which I think I quite like this.
Is when a measure becomes a target, it stops being a measure. This is kind of Goodhart's Law, I believe. Edwards Deming… Edwards Deming.
paraphrase this, but I think this is a really powerful statement, and it relates to your academics as well, if you think about it. So.
Ultimately, if we look at an academic setting, it used to be you go to school, you study stuff, and then, you know.
that's… you're assumed that you're learning it, and, you know, you go on to do work. But at some stage, they wanted to understand, well, how much are people learning? How come this person knows stuff, this person doesn't know anything? So they started introducing exams and assessments.
And so, you can imagine back in the day, like, when I was studying, let's say, a module, I had, like, a textbook.
1,000-page textbook, and anything in that textbook is examinable, and then you go through the course, and then the exam is some…
Selection of questions within that textbook, right?
It's not an absolute… it's not asking you about every single page, there's not enough time, so you effectively have an exam, which is like some random selection of knowledge that you probably should know, and based on how well you do, it's a measure of
You know, your knowledge, let's say.
Okay, fair enough.
But what happened is, over time, as we started assessing people's learning, Through this measure.
it stops becoming a good measure, because instead of just focusing on trying to learn a subject, and then you're tested on it, you start realizing, well, I'm only going to be valued based on how well I score in this measurement, so instead, what I'm going to do is I'm going to look at all these past papers, and I'm going to try and map
exactly what type of questions are likely to come up, and I'm going to just study only those things. I'm going to just really gear all my studies towards the exam questions.
And then you might score very well on the metric, but actually the 80% of the module which was not tested in the exam, you don't know, right? And so what happens similarly in software
is, let's say, our target becomes, okay, how many passing tests do we have? And this is actually a real example from…
about 6 or 7 years ago, I had a capstone student, and they were…
they were really into testing, and they… their boss basically said something similar. They were like.
how many passing tests do you have? And they were… they were using this as some sort of metric for the quality of their… of their job, of, like, how well they're doing.
I think how…
think how easy this would be to exploit, right? So I'm developing some software, and I'm being assessed on, like, the number of passing tests that I have.
well, I just add more passing tests, right? I'll just add tests which I don't really need, or are kind of redundant or repetitive, but I get, like, way more tests. And so if the measurement of success is, you know, the focus, it starts becoming a good measurement.
because software testing is meant to be, like, you do some software testing, and generally speaking, you test broadly across the system, and, you know, you find certain defects, and you realize, okay, we've got this many defects, per this many lines of code, this is generally pretty good. But now, if you're just… you're thinking, okay, we…
the actual amount of tests passed is really what indicates quality. People will just change their behaviors to meet the metric and not actually focus on what the metric is meant to be measuring.
And so, this principle applies in academics, applies in testing, but when the measure becomes a target, it stops being a measure. And it's something to bear in mind whenever you're doing testing. Your goal is not to produce passing tests. Your goal is to find defects.
And assess the quality of your software.
And, yes.
the proportion of passing tests should be some measurement of that, but if that becomes your goal, it will be… it will cease to be a useful measure. So I think this is a really instructive quote, possibly more broad than just testing, but something to bear in mind as we go through.
Right.
So… Two levels of metrics.
The first of which we're going to focus on a lot more. This is the intrinsic software quality metrics, so we'll look at availability, failure intensity, and then defect density. So, the first one more about reliability, and the next one more about the density of defects, and that's more about process improvements, software quality assurance processes. And the last one is
More general, we're not going to focus on it too much in this module, but just to be aware, obviously, we can look at the quality as assessed by the customer, and so we can look at the problems posed by the customer, and the satisfaction derived from the customer for our systems.
So…
Reliability relates to how long a system can run before encountering a failure, and then defect density will be, like, the rate or the number of defects in software relative to its size, okay? So these are general quality metrics, and there's a variety of ways of performing these.
Which gives you some idea of how high quality or low quality a system is.
Basically, how…
Often does it run without failing? And then, how many defects are there in the amount of code that's being shipped with this system?
Okay, so we're gonna focus on availability first.
And this one, a little bit straightforward, but some… some equations, okay? Generally, these equations, I think these ones specifically, are quite intuitive and simple. Some of the later ones, a little bit more complicated, but again, we will give you, any of them.
Any of the complicated equations in an assessment, you will have them.
So you won't need to memorize the equations. So, for availability, let's consider some of these acronyms, because in Singapore, acronyms are everywhere. So, MTTF, or is the mean time to failure. So, that's the average operating time from a restoration or startup until the next failure of a system.
So it could be, let's say, 200 hours, and that means we can expect
failure every 200 operating hours for a system, okay? Meantime 2 failure.
Mean time to repair. So this is the average time to restore a system after failure. So it might be 10 hours. So it takes 10 hours to fix the system and get it running again after failure.
Now…
No, I have a note for this, so… And then, next, MIN time between failures is simply the addition of those two, okay? Because…
how long the system runs for until a failure is one measure, then how long it takes to repair it is the other, and so the mean time between failures is actually the addition of those two, okay? So the duration until failure, then the repair.
is the total time between, failures. Okay, so mean time between failures is given as, in this case, based on these numbers, 200 plus 10. From the previous two examples would give 210 hours.
Very straightforward so far.
Now… As I mentioned, a slight note here.
It is definitely true in a lot of modern systems and DevOps and engineering contexts that mean time to repair is very small, right?
Maybe you just have to, like, reboot one of your servers, or reboot your system, or whatever, whatever it might be.
But mean time to repair might be in seconds or minutes, whereas mean time to failure might be, like, thousands of hours. And so, effectively, you might find that mean time between failures essentially becomes mean time to failure, and that makes it, like, you know.
Very, very high availability for the system. It's almost like 100% just below every time. And that… that is actually pretty much…
a reasonable situation to occur for a lot of modern software systems. But availability can be measured to a very high amount of decimal places as well, so it's not, still not,
a, you know, unusual if you have a very high availability and it's still not being sufficient for a certain context. And we'll come to an example in a minute. But for the context of this module, because we're looking at systems more broadly.
Mean time to repair is not necessarily negligible, particularly if there's hardware components or a lot of different factors involved. To repair a system might take a significant portion of time, and so we're just going to consider that as an explicit factor in our calculations, as it should be in this classical interpretation. But it's just a note that
You know, it is true in purely software and smaller systems that mean time to repair might be very negligible.
In relation to mean times of failure.
So, availability is effectively the mean time to failure divided by the mean time between failures.
And so if mean time to repair is like before, we have 200 divided by mean time between, which is 210 from before, gives us an availability in a percentage of 95%. So 95% of the time, the system is available. Now, as mean time to repair gets very small, obviously, as I said, this will be close to 100%.
But not quite reaching it.
But, if we look at… The air traffic
control systems in the US. This is, an old,
textbook slide, but I believe a similar policy still exists. They have a categorizations for availability, and
Ultra availability, is considered 99.99999 available, right? So, it's really, just an extremely small amount of downtime for the air traffic control systems is considered acceptable.
And as you can see, even if MING to repair gets very small, a lot of systems, mission-critical systems, require an extremely high availability. If you have, like, hospital systems, if you have any kind of medical systems, you don't want the system to have, you know, even
even it going out for, like, a few minutes can be catastrophic. So, despite the availability percentages possibly getting very high and close and tending to 100%,
we still distinguish in the very high ends, because what we're talking about is systems which could be mission critical going down for any proportion of time, which could be very dangerous. So, assessing quality in terms of availability is used in a lot of these mission-critical systems, because availability of a system
is indication of a higher quality or high quality system. So this is one measure, availability, quite straightforward, mean time to failure divided by mean time between failures, which is the summation.
of mean time to failure plus mean time to repair. So, pretty straightforward equation for this one, and that gives us availability, which is related to reliability.
Okay.
So the next one is probably the more complicated of the things we'll cover today, but as said, don't let the equations scare you, just understand the basic principles, and the equations will be given to you. Okay, so now we're going to look at failure intensity.
So, failure intensity… is a rate.
And it is the number of failures.
Right? That you get in a section of time. And so, the basic, equation is lambda tau, so these are kind of the Greek alphabet, so lambda tau.
You don't need to remember the Greek names, just what it looks like, I guess. But the lambda tau denotes failure intensity, and effectively.
Its hash number here is the number of failures from time tau till time delta tau, so delta tau is the difference in time.
Divided by that difference in time. So it's basically, we take a time interval, how many failures you get divided by the time interval. Quite straightforward, actually. And this gives you a rate.
Now, it's not a probability, it is a rate, so it can be exceeding 1, but this is considered failure intensity, so it's the rate of failure of a system.
Okay, that is failure intensity.
And so the factors we're going to look at now, are how we calculate failure intensity with different models, and use this as a measure of quality.
Now, a slight side note,
Not fundamentally changing what we're talking about, but it is important to note that whenever we're talking about time in our calculations.
There are two concepts of time in this case. So there's execution time, which is how much CPU time was used by a test, or cumulative processor time consumed while executing software, maybe a little bit more precise, kind of rephrased it.
And so we might say something takes, like, 5 hours of execution time on a particular specification.
But we might also talk about time, of course, in the more traditional sense of calendar time, or elapsed, or wall clock time, so that is the time used,
time taken to complete a test, let's say. So from 12 to 5, maybe 5 hours of clock time, okay? So we have execution time and calendar time, as I'm calling it here, possibly also clock time, you could say, as well.
Now…
5 hours in each of these may not be equivalent in certain situations. So, for example, execution time versus calendar time. We might have a situation where we have a multi-threaded system, right, running in parallel, such that the calendar time
let's say it takes 10 minutes, but… or 10 hours, whatever units we're using here. But the CPU time would actually be much greater. It's just that we've multi-threaded the system, so it's actually, you know, running
two CPUs worth in the same calendar time. But this actual execution time is longer than the calendar time. And similarly.
if we're using a system where the CPU time is, you know, 1 hour, but the calendar time is maybe 2 hours, because the CPU isn't always being… always executing the actual test, because there are I.O. operations, there's all sorts of things going on, which is obviously very common of modern PC usage.
And in which case, the calendar time for a running test is actually longer due to the general use of the system.
So, there's different situations which can result in either one of these not being equal to the other. Generally speaking, when we're talking about time, I will not try and be particularly nuanced or obfuscate this, it's just more that you want to be aware of this distinction. And then also to consider, that when we're defining
time, we should be precise, we should talk about a particular environment, setup, hardware, etc, when we're talking about, you know, CPU time, or calendar time, or time in general, so that things can be reproducible
going forward. So, just to note, execution time and calendar time or clock time are not necessarily equivalent, when we're talking about time for these systems.
Okay, but generally speaking, when I ask you to do these calculations, you can just assume time is time, and I won't, like, make you have to work out which one we're talking about.
Okay.
So, when we're talking about failure intensity.
A lot of the models and calculations in this area rely on certain observations or assumptions. Now, I've added the word assumptions here.
The idea is that when a system fails.
We then fix the corresponding faults or errors.
And after doing that, we are assuming that there are now fewer faults remaining in the system. That is, failure intensity will be smaller after we fix every fault.
This seems pretty reasonable, okay? It's just simply the case that if we would remove one error, we have less errors.
It is, in fact, an assumption, though, because, as you'll know, when you are fixing an error, you may unfortunately introduce errors, right? Like, there is an underlying assumption about this, let's say, observation.
But for these models, this is the overarching assumption, and it's a reasonable one, that when you reduce
you fix… you find an error, you fix the error, you're reducing the total failure intensity in the system. So that's the assumption by which these calculations and models are run, and as I've added the note here explicitly, they assume perfect debugging.
Which is, you know, correspond… correcting a fault, responsible for an observed failure reduces the expected failure intensity.
But it's not necessarily true, it is an assumption, because when you fix, you may introduce errors. But going forward, this is the assumption we're making.
Okay.
So, two classic ways of calculating this, and these are good frameworks to understand and possibly bring in to bear if you want to talk about failure intensity as a reliability metric. So, we have two models we're going to look at, and again, don't be scared of the equations. We have the basic Muslim model and the logarithmic model.
Each of these measure failure intensity.
Okay, the rate of failure.
The basic model assumes that you have a constant, decrease with every
error that's fixed. Every failure, sorry, that's fixed.
In your model over time, in your system over time, whereas the logarithmic model
Has… funnily enough, it has a logarithmic… it has a reduction in the decrease in failure intensity over time.
And so both of these will represent At a particular starting point.
how long it may take until we get to a point of, like, stability of relatively little or no errors in the system. So this can be a good way of analyzing your system and then projecting into the future at what point it might be stable for a release based on the data that you have. And that's kind of what these are used for, right? So you're trying to get to a failure intensity which is, reliably, you know, low.
Okay, but these two distinct models, they're…
similar, come from the same, people, but they are, slightly different in their use cases, and one, I guess, slightly more complicated, but ultimately doing similar jobs.
Now, I think the easiest way to visualize is just have a graph and understand them from the graph.
So, we have our lambda, so this is our lambda. We have all the terms here. Lambda is failure intensity that we looked at previously. Lambda zero
is our measurement of the failure intensity at the initial point, right, that we decide to start this model, this calculation. So lambda zero is the initial failure intensity that we've measured.
We have mu, which is the average total number of failures at a given point in time, okay? So at any particular time, we can expect a certain average number of failures to have occurred.
And then V0 is a predicted total number of failures over infinite time, and this is an estimate that we might use based on historical data, and it's used in the basic model. So how do these plot on our graph?
So our graph, we have failure intensity on the y-axis, and on the x-axis, we have mean failures, alright?
This is what the basic model looks like.
It is linear. As mentioned, it has a constant decrease.
The logarithmic one is a log curve, okay? So it slopes down and tends to zero.
Both of them, we map out initially with an initial failure intensity, and then we project out over time to see at which point
we get to pretty much zero failures, okay?
And both of them have slightly different estimates at different times in our axes, and that's what we'll just look at now.
So… The basic model.
For our lambda tau failure intensity, it is our initial failure rate multiplied by 1 minus the average expected failures divided by the total number of expected failures, okay? Straightforward equation, actually, in this case.
And then the average number of failures, mu tau at a certain time, a little bit more complicated equation, but it's the total number of failures.
In brackets, then 1 minus the exponential of the negative.
Lambda zero failure intensity divided by total number of failures times by tau, that particular time. So again, don't need to memorize this, you just need to be able to plug this into your calculator and understand why it's used.
So one is to calculate the failure intensity, and one is to calculate how many failures at that point in time can we expect on average, right? So the latter one is quite useful for forecasting when the system might be ready for deployment.
Okay.
So… Let's look at a concrete example. So assume a program will experience 100 failures in infinite time.
It has now experienced 50 failures, okay?
The initial failure intensity was 10 failures per CPU hour. So this is the initial information, and then from that, I might ask you to do some calculations. So the first one is we will calculate lambda tau, again, that's failure intensity. So we plug the numbers into our equation. Okay, we're not 50 over 100, 1 minus that.
Times by 10, we get 5 failures per CPU hour. That is our failure intensity.
Now, for the slightly more complicated
complicated equation. We have the mu tau, which is the average number of expected failures at a particular time. So, if we look at this at 10 CPU hours, so we run the system for 10 CPU hours, what can we expect? So, we plug in the numbers again.
And you can do these calculations yourself, we should expect to get 63 failures.
Alright?
And, just as an exercise in comparison, we'll do this also with a logarithmic model to show you the differences, but for this model.
If we run it for 100 CPU hours, we'll get
you know, 99.99… some… 99.95, I can't remember the exact number, but basically 100 failures as an estimate here.
And so, what we see is.
As we increase the hours, of course, we're reducing the number of expected failures, oh, sorry, we're increasing the number of failures.
But then the number of expected failures going forward, will obviously be almost zero, as this model only predicts up to 100 failures. And so this can give us an idea that the system, after 100 hours, will
be basically stable, because we would have accumulated all possible, all predicted, sorry, not all possible, but all predicted errors at that point, okay?
Now, for the logarithmic model.
Same idea. We have a slightly new parameter here, theta, which is called the decay parameter, and this is normally in the literature either 0.01 or 0.02. I'm going to use 0.02 here, if I remember correctly. But we have, again, failure intensity, and then we have
The average number of failures, all the terms are the same, theta is the only new one.
For the average number of failures at a time tau, we give it as a different equation. It obviously has LN, which is the natural logarithm. You'll have that button on your calculator, I'm sure. And this is obviously just to make it logarithmic, plus 1 to ensure it calculates non-zero for the initial point. And so we have the average
Number of failures at the time tau is equal to 1 over the decay parameter times by the natural logarithm of the following. Okay, so again, we'll just go through some examples. You don't need to memorize the equations. I'm speeding up a little bit, of course, you might have noticed. I want to get through all this.
So, let's say we have the initial failure intensity, 10, like the previous example, but now we have the decay parameter at 0.2. Again, 0.02 or 0.01 are the common ones chosen. It has now experienced 50 failures.
Okay, so failure, intensity, we can plug in the numbers, we get 3.68. But the more interesting comparison, let's say.
After 10 CPU hours, we'll actually predict 55 failures, okay, and that's because we have this kind of sharper decline in the predicted number of failures.
Compared to the 63 of the basic model.
But then, for 100 hours, we actually predict more failures, and that's because the logarithmic model tends to zero, but never gets to zero. And so what happens is, over time, the logarithmic model will continue to predict failures, right? And that arguably makes it somewhat more realistic.
Okay.
So… There's been different thoughts on, like, which one of these is more useful, under which circumstances, but…
I believe the general consensus is that the basic model
Is actually quite good for, like, a stable or fixed release.
And that is because it assumes that the errors, or the bugs or otherwise, are kind of evenly distributed and somewhat unrelated. And that is to say that I fixed this bug and it has an equal equivalent impact on the reduction in failure intensity.
So faults contribute similarly, and it produces comparable reduction of failure. And so when a system is very stable, that's generally the case, that the bugs are a little bit distributed and, you know, all likely to be encountered, equally likely to be encountered, and removing one has a fixed
impact. Now, the logarithmic model might come into more use
when the fault exposure is uneven, and this is very useful in, like, the early days of a system. So you can imagine you build a system which has
let's just simplify. It says, like, 10 main use cases or user flows, but only 2 of them are kind of used all the time. And…
you'll find that those two user flows will be used all the time, and all the bugs associated with that will happen very quickly. But once you start fixing those bugs, the majority of the failures of the system will stop, right? Because most people are just using those two use cases. So if those become bug-free very quickly.
then your actual failure intensity goes down much more quickly, like in the logarithmic model, right? And this is very true of normal systems, but over time, you'll continue to get bugs, because there'll be more fringe use cases.
used less often, and bring up those bugs, and they have lower impact on the failure intensity changes. So the logographic model is quite good in the more early stages, uneven.
our fault, distribution. And… Also, in those situations, you…
You would use it where you would expect a larger initial improvement with the bug fixes, because you're fixing bugs in those most used areas of the system.
Either way, both give you some idea, some measure of failure intensity as a metric of reliability, and more used is understanding your average amount of expected failures after a certain amount of time, and this can be used for when you're releasing some sort of product, some game, or otherwise.
you know, at what stage in the future, based on our current data, would we expect to have a very low failure intensity, a very low, you know, we've basically experienced the majority of our failures, and we're kind of stable. And so these models can give you that type of
Map, roadmap for, reliability.
Okay, so as I just mentioned, we can decide if things are ready to release, if we need more testing, or we could look at availability like we did, and have we achieved the requisite availability metric, which is the other one we just looked at for release.
A good point also is that any bugs that we find
In these early stages before release, are much cheaper to
fix than after release, when we have to deal with customers and other, additional problems when things are actually launched. So generally, getting bugs, getting issues out the way early saves us money in the long run, which is why, focusing on software quality in the very inception of projects is important.
Okay, so the other one, which is quite simple that we'll get through, is defect density. And so, other than reliability, we can also look at the process of developing our software, and are we actually improving that because we're having less defects in the code, or are we giving
and adding more defects to the code, hence getting worse. So.
A brief look at defect density.
Defect density is, as said, we're looking at the proportion of defects relative to the size of the code. You can also do this with function points, but traditionally we do this with K lock, or lines of code. K is thousands of lines of code, which is more useful in some cases.
And we're effectively just trying to understand, how dense
Really packed defects are into our code.
Now, for a lot of IDEs and otherwise, they will measure your lines of code, and you just go by that measurement and stay consistent. But it is worth mentioning.
This is, just to give you an idea, of course.
Simple function, hello, hello world would have been nicer, maybe, but…
5 logical, 5 physical lines of code, 2 logical, 1 comment line. How is this being counted in your IDE? How are you counting lines of code?
Can also do it with function points.
essentially, as long as you're consistent with your measurements in a particular language, then there's no issue. Obviously, different languages, different lines of amounts of code.
comparisons are meaningless. When you're talking about lines of code in your own development process, you need to be consistent. Counting code in the same way. You might talk about comments as well, because you have to maintain them, let's say. So…
You're talking about lines of code in a particular language, in a particular way of calculating them, and then when we calculate defect density, it becomes relative to that same, same framework.
Okay.
So how do… how might we use this?
We… Might want to do a check of what is our current
Defect density, how many defects did we release into our code per line of code?
And then, in our next release, did we improve the amount of defects we released? So you're using this as an assessment of the quality assurance process, right, rather than just the quality of the software, but the process. So this is an assessment of the process, or can be an assessment of the process.
When used in this way.
Okay.
So…
More acronyms here, but this one is also quite straightforward. We have SSI, which is Shipped Source Instructions. We have CSI, which is Changed Source Instructions.
And whenever you release a new version of the code, you have the original ship source instructions, plus the changed, minus deleted code, minus changed code, and that gives you the total new amount of code in a release.
But actually, when we're doing our calculations.
what we're normally doing is actually just looking at the release-to-release defect density and comparing the two. So in this example here, we have the initial release, where the change source instructions are the same number as the source instructions, chip source instructions, because it's the first release, so 50,000 lines of code.
Let's say we introduce 100 defects.
Okay? Then… The defect entity.
Okay, in this case, would just be 100 divided by 50, so we get 2 defects per thousand lines of code.
And then for our next release, okay, let's say we're changing 20,000 lines of code.
And we then have added… we find out we added another 36.
Defects… so the defect density of our new release is 36 over 20, which is actually 1.8. So…
We've actually improved the rate of defects in our code. And this is…
Possibly due to changes we've made in the development process, but this is something we can analyze to try and ensure we have good quality assurance in our development of our software systems. Okay, so we can look at the defect density in each of our releases, compare them.
see if we're going in the wrong or right direction, and make changes to the process accordingly. And then based on the other calculation… oh, yeah, so we would do the calculation, like, the original minus
The new divided by the original, and that gives us the percentage change from the original, so we've actually got a 10% improvement in defect density from release 0, or release 1 to release 2, or 0 to 1.
Okay, and aside.
From the previous calculations, you can also, obviously, calculate the new number of lines in the code by considering the new changed, minusing the deleted lines, and getting a new total of lines of code.
depending on the question, I might ask you to calculate how much code is in the new,
Release, and then…
assuming, all the defects were previously fixed, how many defects are in the new release, something like this. I might ask you some questions, so that calculation
possibly can be useful. But the general use of this is comparing initial release to the next release, and looking at whether our defect density is improving or getting worse, and using this as a measure of quality for our quality assurance processes.
Okay, and just briefly, I think this is the last thing to cover,
Before we get to the MINICRIS 2, which I will probably have to leave with you.
That you can do in your own time. But we can also look at quality in terms of the customer's perspective and customer metrics, so more on the kind of validation side of quality, let's say.
Sorry, I'm just sneezing.
So, two of the ones I want to highlight is we may look at the customer problems metrics, or customer satisfaction metrics. Both quite straightforward.
ultimately, we have the problems, and we can measure these by the problems per user month, okay? So, we have the total number of problems reported by customers divided by the total of licensed months of the software, and this basically gives us some idea of
a basic metric that's used to indicate quality through customer problems, okay? So it's the proportion of problems encountered per month, or the PUM. And this is one basic measure from the user perspective, the validation perspective of software quality.
And then the other side of things, we also have satisfaction metrics. So these are more common, and we have our general Leichhardt scales, and so there's a lot of frameworks used by different industries here, but effectively, regardless of the model, where it's HP, IBM, or similar adapted models.
Effectively, you… Also assess the quality.
By doing surveys with the users.
And they will give a satisfaction score, you know, 5 very satisfied, 0 very dissatisfied. And this can give you another metric for quality, which relates to the validation side from the customer. So we can look at the satisfaction metrics or the reported problems, as distinct from the intrinsic metrics, which are the measurements of bugs and reliability availability that we talked about earlier.
Okay, we will not…
give sufficient time for this, but I'll just briefly go through this, and I'll upload this quiz version so you can go through it in your own time. But, just briefly as we go through…
Mini Quiz 1, MiniQuiz 2 now.
So, I ask you to say which each…
which of these are? So we have failure, we have the mean time to repair, we have the mean time to failure, we have the mean time between failures.
And you have to identify each of them here, although I've kind of just done that for you. Then I give you an example calculation for the basic Musa model, a determined failure intensity, and the number of failures expected after 5 CPU hours, given these values.
And then, I also am asking you for, the ship source instruction, code size, and the defect rate change.
Okay, a lot of percentages to process here as well, numbers to process. All these examples, I would recommend going through them just to practice for yourself, and I will upload these answers. So each of these, quite straightforward, repair time and failure time, time between failures.
And then, each of these, I'm giving you the calculations and the answers
these also, okay? So I'm just blitzing through these, but I'm going to upload them.
Ultimately, these are just practice that might serve you well for next week, because we're almost certainly going to be asked some of these metrics and asked to do some of these calculations.
And a good metric for yourself is today we basically had 30 marks of questions, approximately, and see if you can get 30 out of 30 before your next week's quizzes, and I'm sure you'll be in a good spot.
And a summary… Of what you're meant to go away with today.
I want you to understand software quality in software engineering, why it's necessary. I want you to understand some of the metrics. We looked at, intrinsic metrics, those calculations we looked at earlier, and then we looked at the customer metrics very briefly, but that's another way of evaluating quality. Kind of looking at it in terms of a verification, almost, and a validation angle, almost. And then I want you to be able to distinguish between the factors contributing to poor
To poor software quality. Again, I've added an extra software here, I'll remove that. But…
There are certain factors, 6 of them that we covered, and these are broad categories that we need to consider that can lead to bad quality, and so how we might want to mitigate or prevent
bad quality by dealing with those factors. I want you to understand the definitions of software quality and software quality assurance. Those are two things we looked at, which are a bit distinct. And then I want you to be able to apply the quality assurance metrics that we went through.
And for verification, of course, I want you to be able to distinguish between the two, and then look at, or understand the differences, basically the differences between static and dynamic, and understand the definitions of verification and validation.
All right, that is one hour. I will upload all these slides with the quizzes involved, and you can do the assessments and make sure you are comfortable with that.
So, I'll deal with some questions here…
a Hyprof, which represents BLASS radius in terms of how much
is affected every failure, something like small bug, like.
text output typo versus app data loss, or, leakage level. Oh, great question. So, we're not explicitly looking at, kind of, the, so-called… well, you're referring to it as a blast radius, but the impact of
the significance of each failure or bug. But it is worth noting that some failures are more catastrophic and more damaging than others. For this, we're just looking at quantifying failures themselves.
And the classification of those is not… is, like, implicit in the metrics, so however the company wants to define a failure.
Would be, you know, under their own purview.
Profsa Company, is using AI to co-author their code, and each developer produces 50,000, plus,
lines of code. Would locks still be a good way to quantify errors?
Quantified defects per errors. I mean, if you're dealing with thousands of lines of code, it depends on the language.
I mean, ultimately, you can scale it depending on the language. A lot more modern languages generally produce less lines of code, but if you're talking about defect density, you just want to have a consistent measure so you can understand whether you're improving the development process or not. So it's not so much that
you're trying to compare with other companies or other, you know, different languages, you're just trying to find a consistent measure to understand whether your own practices are actually improving the number of defects that you push out into the code or not. So, a good question, but I think it's more a case of
what language are you using, and what is the actual goal in this case? And it's almost certainly for internal process improvements and reflection on the defects being added. Hyprof may check if lab attendance is compulsory, if the lab assessments can be done at home.
I think I mentioned the idea originally was to have them done in the lab, but I'm still working out the…
the nuances of this new system.
I will release the labs later today, actually. Not all of them, but at least the first one, probably the first two.
we are going to run the assessment next week. One idea is to have it in the labs, and one idea is to just have it asynchronous, done by the end of the week.
I'm still playing around with the actual assessment itself, I don't want, you know…
these to be redundant, and just having AI talk to AI, so I do want some sort of oversight.
let me just say, I will… I will formalize this. The lab attendance is not mandatory. There's no lab this week, but next week, I will be there for any questions, concerns that you have. But let's just say that
If the assessment's meant to be done in the labs, then of course you'll need to be there.
Okay, oh, another question. Oh, so Prof, with this one, you mean big errors could be, quantified the same as small errors?
I mean… Yes, in this case, they could be. I think…
What we're talking about for these measures are measuring errors without defining
or measuring defects or failure. We're measuring system failures, let's say, without defining or distinguishing between,
what a system failure is. But for your case.
you know, a typo and an output wouldn't necessarily be considered a system failure, whereas the latter probably would. But I guess the threshold of what constitutes that would be dependent on how that company is defining it.
For what we're presenting, it's actually just the framework for the measurement itself.
But I think it's a great, it's a great question, because ultimately, it will be determined by whomever is applying this metric what constitutes a failure of the system in their particular context.
So, yes, I guess I'm saying they could be counted as the same, but a lot of what these are considering, like, for the
failure intensity, they're talking about system failures. They're not necessarily talking about,
You know, output inconsistencies or other minor,
Bugs, etc. They're talking about actual failures.
Yeah.
But it's a great… it's a great question, and not necessarily addressed by these metrics, but…
Yes, certainly each to their… each will classify things a bit differently, I guess.
Okie dokie,
If you have any additional questions, you can follow up. I'll put out more details on exactly how things will transpire in terms of the lab assessments going forward, but as I mentioned, please bear with me, I'm trying out some new things, so we'll see if it works out okay. Provisionally, labs are on next week.
I expect you to be there, but if you need to be there, I'll tell you. Yeah.
That's a fair way of putting it.
Okay, enjoy the rest of your day. Hopefully this trimester goes great, and I will see you in the coming weeks.
