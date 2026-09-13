---
type: raw
source: live lecture transcript
module: ICT3113 Performance Optimisation and Design
lecturer: A/Prof Donny Soh
topic: Course Overview + Performance Metrics (Lecture 1)
date: 2026-08 (approx)
format: spoken lecture, speech-recognition transcript
status: verbatim — do not edit
---

Hey, thank you so much for your time today, thank you for joining us on this very nice
Monday afternoon, I'm your instructor for this module. I'm Donny, and some of you may have met me last, early this year, when we were doing our machine learning. I hope, hope you guys managed to enjoy the course, and very happy and honored to be teaching everybody again, and always my joy to be
Teaching year 3, learners or students here.
And I can share with you that I… after this module, I…
I, I, I, I somehow, somehow or another, I teach.
software engineering more than my own applied AI students, and
some of them, I… I still get to meet when they go for IWSP. That is, something that is very, very, very nice, and
It's always my joy to… to see you guys, pursue on to your final year of your studies now, and then…
In a very short amount of time, you'll be moving on to your IWSP.
So, this, course has been… has gone through many iterations over the last, over the many years.
i.e.
Since we are still waiting for people to stream in, I started teaching this module
when I was a part-time
teacher at SITS. So I started off as a part-time teacher. That was 9 years back. And I taught this module for, I think, 1 to 2 times when I was a part-time teacher.
During that… during that time,
some, like, 7 years ago, they asked me if I was, open to…
To teaching for full-time or not.
then I took up the challenge, and I converted to a full-time I think 7 years back.
I've been teaching this module the last 7 years as well.
And…
And many things have changed over the last several years, but I think the last one, two years, were…
Things were changed the most.
Naive.
I think in… especially in your position that you are in right now, it is,
It's a challenging time.
And I urge you to…
to, you know, to treasure every, every moment, of, of learning, to, you know, to be ready, next year, when you go for your IWSP, and, to start preparing for your IWSP, as early as you can.
Okay, so I'll start to share my screen now. Hopefully, but one of my…
Right? My hope is also that whatever I teach here will be…
will be useful for you as you go out for your internship, as you go for your career. Hopefully, this will be
Something that you would be able to apply into your workplace.
Okay, so I have some simple slides to share in the actual one, where I talk about the course overview.
So, like, what the module is about, the module is about measuring, modeling, optimization, and deployment, being able to understand, what the system is doing. And especially in today's age of AI, no, we generate code, and we generate code very frivolously, you see. Like, we just generate and then
You sometimes don't even know what happens. Well, not sometimes, many times, after you generate, we don't read through the code as well.
No, it may work at a very small scale, but then as you…
As the scale of it gets larger and larger, you may find your systems
are not performing as well. So that is where you need to do things, preemptively. Being able to preemptively know that some of these
Some of these, these systems aren't able to perform as well under load, and then being able to catch them before they go on to, either production or even to UAT.
Okay, and then, to model, model predicting behavior before it happens, we'll be doing not a lot of modeling, but we will be doing a lot of measurement.
And after that, how to optimize, caching, indexing, algorithmic, changes, verified, again, by the first phase of measurement, and then, maybe a little bit of deployment here and there. And we'll be doing some, Docker and Kubernetes along the way over the last, two, three weeks of the program.
So these are the various different learning outcomes, and I'll just leave you to read through them.
What will happen is we'll be going through a metrics and workload identification over the first 2-3 weeks.
And thereafter, modeling using Q's, letters law, various different execution models, and we will also be looking into how we can write performance documents. Those will all fall under our measurement model.
And, we also want to find out how we can apply this in the AI space. So, many times.
Most of the jobs that you go in, they will go in with the… with the…
Expectation that you will be able to, at least be able to perform some parts relevant
Some parts of your workflow must be already AI-enabled, invaluable to write certain AI agents, being able to understand
how these things work. I think those are often the plus, and I want to be able to incorporate such things into the model this trimester. We did a little bit of that last trimester, but I think this year, I am re-looking at this and diving again.
A little bit change will… your midterm will be in week 6.
Okay, so we'll do the midterm before the last week of…
In… during the last week of the… of the…
During the last week of the… of this… of this half of the trimester. Okay, get ready for that.
And then, we'll be doing, you know, revision. I, I would… I would work with APA to, to check.
whether our exam is week 13 or week 14. If I'm not wrong, it is week 14. And, there'll be two sub… two project submissions as well. Sorry, it's missing here. Week 8, there'll be one, project submission. Week 13, there'll be another project submission.
So for this week, there's going to be no labs.
So, no labs for this week. We'll start, labs from next week onwards, where we'll be doing, some simple profiling, and then we'll be profiling with, profiling your Python programs, and then thereafter.
We'll be doing some J meter, load testing, some simple modeling. Actually, to me, the first…
Few weeks, to me, are pretty, pretty essential. So, they really need to…
To show… to show you some parts of
performance measurement, where we typically don't do, yeah, so I hope you can be, you know, be able to join the sessions and be able to learn from those sessions, okay?
the…
the next half of the… of the program is going to be a little bit interesting. Okay, so I am currently trying to get everybody enrolled into an online course.
So, I don't know if you have heard of this online course before. Let me… let me see if I can get you…
The name of the online course.
So, I am currently, sITs are… Coordinator for this program.
However…
I… we are still working out the legal part of it. So, AIC. So, I'm trying to get everybody enrolled into this program.
And…
parts of this course, I will point you to doing parts of this program, and then, when you complete it, you'll be considered as, as a credit bearing towards this course.
If we can't get it in time, I would then take some material from here, and then I will, I will… I will make it more relevant for this, for this module. But I'm hoping to…
to use this as something to really spearhead or kickstart whatever, you know, AI journey that you will be expected to be part of lah. This program is…
Yeah, I expected to complete this by right in about 3 months, but, I mean, being ICT students, I'm sure you can do this faster, so maybe 1-2 months would be… would be fine. And then…
The nice thing about this is after you complete this 3-month program, right, you are…
Given this master phase, where you will have access to a $600 subscription credits.
Oh, so you can start to use this for your coding assistance, and hopefully these will all help to make you a lot more employable during your IWSP.
If we can't get this in time, what I'll do is I would… I will take the material… I will extract some materials from there, and then I would be able to…
Customize it towards this module.
There's going to be another part of Docker, which is Docker Kubernetes, and this will be done with another external, external, another external…
course, module, which is from Dell, so you'll be doing two modules, one in, Locker 1 and Kubernetes. For the lectures on that, on those two weeks, I'll see what is the best way to do it. Why? Because, like, those modules by itself already has the…
lecture there already, so I don't know whether to I… so the last few years, what we've been doing is that we invited somebody from Dell to come in to give a little bit, like, a overview of motivational, like, why do we do Docker, and why do we do Kubernetes? I…
I actually find those sessions, they're nice because you get to see another face other than me, but then the actual content there.
I think it's…
It's good lah, it's just that, you know, it's more motivational rather than… rather than instructive, so I'm wondering whether to what… do I want to do that, or should I just, you know.
do something else for those few weeks now. So, for that, I will leave… I'll let you all know very soon. But I can tell that the course
I'm trying, also trying very hard to make the course, entire course, applicable for…
For, for… applicable towards some of the more…
Later, later, tech investments that have, been coming on for the last few months.
So, week 1, week 2 to 5, we'll be focusing on the fundamentals, performance metrics workload, performance modeling.
And then, after that will be more towards, more performance engineering for AI workloads, and this will be more towards the Agentic AI side, and then after that, deployment.
Okay.
Okay, I think that's about it for…
the start of this OER assessment done. So there is going to be assessment.
midterm in week 6, there'll be 25%, finals will be 35%, there's going to be a 35% for project. Likely there'll be a part 1, Part 2, so part 1 to be submitted in week 8, Part 2 submitted in week 13. You will have time for your part two, because
The later part of this week, most of our lectures or stuff may be done on a, like a,
done online, so you will have some time, to, to do your project, so not to worry. There's going to be a 5% that is set on root formation. So, what will happen will be, maybe, tomorrow or after today, I will be releasing out the
the project specs, and then I would, have you all to form your own groups. And your groups must be within your own tutorial group, yeah. So, this is to ensure that you form your groups on time. There were a few times that we did it where
Where either the learners couldn't form their groups, and it… And they were just not.
I don't know, but not, not, not that, not that,
motivated somehow to do it, so… so after we… we instituted this, I think, I think we managed to…
Accelerate things by quite a bit, and…
Yeah, I think in today's age.
We, we need to move, faster, so…
So, the midterm will be from week… oh, sorry, sorry, not week to week one. So, we're going to be starting… I think my introduction will end in about 5 minutes' time, or even less than that. So, I'll start with the lesson proper immediately after this.
And then, we'll be, doing the… your midterm will cover from week 1 to week 5.
And the finals will be primarily week 8 to 12, but then we will also apply, things from week 1 to week 5. So, for example, we'll be doing things like, you'll be doing things like Litters Law, we'll be doing things like, maybe even measurement of, measurement of.
Measurement of what, measurement of, latency, measurement of, of, of your throughput, yeah, all these will all be there, so, both, so your finals will cover, essentially, the entire trimester.
So, I think this one, this one, I think, also important, also important.
So this week, we'll have an overview, and then we'll start immediately with performance metrics. There's… there'll be no labs this week, and next week we'll continue then on.
Okay, so, there has always been a lot of feedback on me, where I'm very easily distracted by the questions. So for this trimester, I'm going to make it a point that I will only answer questions at set.
periods of time. So, now is the time for question and answer. Yeah.
Yeah, so, yeah, so there is some question, like, what is the group size for project group? Before the 5, I'll release the details, soon, and then,
Yeah. So, in terms of cloud code, I am not sure whether do you have access to that or not.
Okay, what I have asked for is, I've asked for everybody access to Clock Code. I have… currently, my ask is only the $30 one.
So, what will happen is that every group You would.
Be able to claim
up to about $150, or… I can't remember the exact number, about maybe $150 or $200. I need to get the exact number, but… but you… everybody will be able to get, the KWOK code, but only the pro version.
Okay, we'll see how things go over this trimester. So, if I'm not wrong, you can sign up for the team version. The team version is $25 per pack, and then the amount of credits is also a little bit higher.
tokens that you have access to is also a little bit higher. So… so you can… so I would advise that, yeah, you can do that. So the faster you form your teams, the faster you can also, start to utilize this team.
Team Pro Coda.
I will release these details out very soon, yeah, so…
Yeah, so I'm not… I'm not sure… can I just check, any other module that you are doing, is paying for your clock code? Or is it everybody is still paying for themselves?
Okay, if there are no answers, right, I am going to assume that
That everybody is either paying for themselves or not using it.
Both of which I find, is an issue. Okay, yeah, so most of your… some of you are paying yourselves, some of you are not using it, which… both of which are of a little bit of an issue, but I guess it's fine.
So, hopefully this trimester, we would be able to provide you access to that.
So, I think that should be okay. Let me… let me just fix some of these, before I…
Before I forget week 1, this will be 1…
It should be a big blind… I will change… I will change this…
Later, are there any other errors that I need to fix?
I think this is fine.
I think the rice are fine.
Doing the rest of the fine.
Okay.
Okay, good. Okay, so now that is my last call.
Yeah, so I will not be able to sponsor, the school will be sponsoring now, yeah, so… but I've asked for them to sponsor the team account. I will check during the break how much did I actually asked for.
Yeah, so, but it is minimally $150 per team. Minimally, minimally. Oh, per team per month. So a few, a few criteria again. So it's, let's say minimally $150 per team per month.
You will only claim once, though, meaning that you will claim one time at the end of the trimester. So, you will not be claiming every single month, else our admin will have a very, very hard time
trying to… trying to counter-check your claims and claims and everything. So, you will claim at once.
Once… once a trimester.
and at the end of the trimester. But every month, the team has up to $150, per…
up to… TMOT, up to $150 per month.
The intention is that everybody should minimally be able to subscribe to the $30 one.
Any other questions from here?
B.
If there are none, okay, what I'll do is, I'll do a verbal lecture, maybe I'll talk for about 1 hour, thereabouts.
And then we're going to… we're going to, we're going to start… we're going to, have an early break, and then, we'll see each other again, next week on Tuesday.
This is on Monday, sorry. This is on Monday.
Okay, so once again, once again, this will be my final question I will answer before the end of the lecture. So, the way this works is that every team will subscribe to… I believe there is a Cropcode team subscription.
And then… You will add everybody.
You add everybody in, we are TMO, so… let me check.
Yeah.
So, maybe I need to have a small little disclaimer. I don't earn money from ProdCode. So, yeah. So there is… remember, there's this team… yeah, this team plan. So you have about 5 of y'all, so you can get…
each person, BIN is per seat. So, per seat, no, I think the price go up a bit. Yeah, the per seat is $30, so if you have 5 people, so you will be able to get, $150, so per team.
per month, it'd be $150. So, you will expand this and be curvingly for the next, 3-4 months.
And after that, you'll be able to…
He will be able to, to claim back.
by, through our APA process.
Must it be a clock team in order to…
Okay, so that was a very good question. Must it be a prop team in order to claim the reimbursement later? Or can each member in the team subscribe to their own individual prop code accounts? Okay.
The… you can subscribe to your individual ClockCode accounts, however, the claim will still be capped at $150 per month.
So that would be the criteria. So if you don't want to use this TEE account, I think it's still possible, yeah, but I think, yeah, please use your school account, then you'll be a little bit more official.
Yeah, but you have to also know something. If you don't use your TEE account, sorry, if you use your TEE account, right, when you do the claim, what will happen is that
You need to submit your credit card details, at least the screenshot of the credit card payment, you see.
And,
Yeah, so some people may not be comfortable with that, so I leave it to y'all to see how… what is the best way you want to do it.
No.
Yeah, so let's use this bullet kernel now.
I decided I need to use a school account.
Yeah, so yeah, I understand some of you already have your own Cropcode Pro subscription for $30 per month, yeah. So… so, yeah, so just take note, just take note. But I must also say that…
if they were to check, and they say that, how come your subscription starts earlier than
31st of August.
Then, there may be some questions that we have to answer.
Yeah, so it is, you know.
If they ask, if they don't ask them.
Then, no, yeah, but if they ask, Yeah.
Okay?
Any other questions on this?
I hope, I hope this is useful. Actually, actually, your… your… I have some people for my year one, year two that feedback to me that they want to use crop code in their…
India, school.
work, and I don't know if your feedback or not, but I… I personally think that this is quite important.
So, Tim?
If it's fixed at $150 per team, then there may not be issues. That's why I cannot promise lah. Yeah, because,
You know, I had had incidents where… where my… my own subscription, I had to prove it.
Yeah.
Yeah.
So, yeah.
So, yeah, so, I mean, I just shared a view lah.
Okay.
Okay, everything is fine, oops, sorry. Okay, no other questions, I'm going to start.
Okay, so today I've, already released this set of slides on, on my site. I updated it a little bit, I updated this a little bit, earlier this afternoon, or this morning.
Okay, so these are the learning outcomes, identified to the… okay, I just continue, you just read this yourself. I start off with an example, a case study of the Mars Climate Orbiter case study.
So, there was this mass orbital climat that was being brought to the moon. I think two different groups of people brought it to the Moon. One was NASA, and the other one was Lockheed Martin. And what occurred was that one of them used Newton.
which is the SI units, and the other use pounds, which is our imperial units. And the issue was also that they use both in the same system.
So it was the same system, and you know, although they use the same… they use the same system, but they key in the values with different units. Now, of course, what happened was that it crashed. So the same quantity, it actually…
The issue here is there's a lot of inconsistency, although everybody thought that they were using the same consistent units, but… but they were consistent only to themselves, and that was not… not made known across different
Different, two different teams, huh?
I actually have a story to share here. Not so much with my own self, but this is something that I see across various different organizations. So it's… everybody is now talking about AI, you know, AI adoption, everything.
For most people that are non-technical, they are largely dealing with a lot of problems, context engineering.
I, I started off as a…
as a VBA consultant, I don't know if many people… your learners may not know this, but
I started off, I didn't start from academia, so I started as, from industry. So I was in industry for…
for quite a number of years, 15, 15 years, thereabouts? And then I… I… I started off writing, writing,
with VBA, as a VBA consultant, so I wrote VBA scripts for people.
And one of my first clients was a major oil company. That time, they were the largest oil company… largest company in the world, rather. And
And when I went there, I… I was asked to revise some of their VBA scripts, and I realized that many of the VBA scripts had many errors in them.
So apparently, they were written by people that were not very technical initially.
Then… no, after they left, The errors persisted there, so nobody knew what the scripts were even doing.
And then, one day, the scripts broke. They couldn't work, and then they didn't know what to do with it. And then the processes started to break, because
what used to be done by scripts now had to be done by people, and the people that were running it didn't know how to
Fixed the scripts.
So that was where they asked me to come in to help them out.
Actually, really, I still remember it was my first assignment, was my first assignment with them.
And, when I went in, I realized that many of them were very buggy. And some of them, they were very buggy, and they've been running buggy code for maybe when you guys have seen.
Something is where I see a similar corollary with what we're seeing today. Today, we don't have VBS groups, but we have a lot of prompts, so everybody is learning their own prompts. Everybody is running their own prompt, so-called context engineering, whatever it is.
And I am also starting to see a huge fermentation, where within an organization, everybody seems to think that they are saying the same thing.
that they are prompting in the same way, but there's no standard, that everybody becomes their own expert, and there's no standard. And if a prompt is… has error, or if the prompt is not consistent, actually it
It can persist for a very, very long time. One day, your person leaves, or the problem is given to somebody else that doesn't know exactly what it's doing.
So, so, so, so we are actually seeing these cracks.
Starting to emerge in the industry, and…
And, yeah, so maybe just to underscore, as engineers ourselves, right, we actually have a, have a large part to play, even though we are saying that, no.
code generation is automatic manner. But although code generation is automatic, I always believe that our value doesn't come from writing code. Our value comes from giving solutions. So we are here to solve people's problems.
And the particular way we solve the problems is the technical way. So maybe other people solve it by the back belt, I don't know, some Sigma, Sigma thing, or maybe they do it by, another, another Kanban, or whatever they do. But our, our way of solving people's problems is through technical.
Yeah, so, you know, so although we are seeing a lot of big shifts in the technology right now, but it doesn't mean that
just because you don't need to write code, it can't be done. I don't think that's the point also. I think the way we solve people's problems now becomes very, very different.
So, okay, so to end off this, this example is that, is that, oh, the, the interesting thing is that this issue was, in fact, noticed by
two different… navigators. So, two of them, actually.
You know, found this out, and wanted to flag this out, but then…
they are… their voices were… were dismissed. So this is an ironic case, which, you know.
It goes to show, you know, many times, the, the… You know, the metric.
Is, is there, and just because you are able to… to see the CHIN coming towards you, doesn't mean that people will also listen.
Anyway…
Yeah, so there's a performance metrics. A metric is what can be measured, and a standard way of measuring, yeah, like, for example, a distance between two points, you measure with a meter, and then you use a tape, tape, tape, tape measure to do that.
These are the various different, points that you… that is, that… that we want metrics to have. Linearity should behave in a very linear fashion, reliability, repeatability is… I'll leave you to… to read these, different…
Metrics are calculation, Du femme…
You know, characteristics of metric side yourself.
So I have one question here.
Which of the following best illustrates a violation of the reliability property of a performance metric?
Yeah, I'll give you maybe, one minute to think about this. I'll start at, like, 3.35.
Okay, so it's 3.35.
So, a benchmark A…
Scores, let's look at A. Benchmark score doubles when system resources double, but actual usage… user performance only improves it slightly. Does it fall under reliability?
Reserve on the reliability.
This likely, doesn't fall under reliability. This seems to fall, Under, under…
Under, maybe more of linearity? Linearity, yeah, so it's not really reliability.
So, not here.
Two independent lines of the same benchmark on the same hardware, Gives, different scores.
So there's… Blackley is under… Repeatability, so it's not reliability also.
Different labs use the same dashboard name, But calculate the metric differently?
So this, we're behind the… Consistency…
So, a metric, consistently reports higher scores for System A than System B, but in real-world usage, System B outperforms System A. There's, probably more of reliability, huh?
Okay, so here, the answer should be, question, choice number D.
Okay, let me go on. So, I have the answers here, the innovative PWD consistency.
So, okay, now we have,
This, this is a very heavy slant.
So, we have metrics, and we group metrics into 3 different parts.
Okay, so the first metric, we call it the outcome metric. So, so what is the eventual outcome that comes out of this, whatever system that we're doing? So, for example, the response time is an outcome metric.
Okay, so, when the user gets when the demand side and the supply side actually meets, what is the outcome?
So, now we come to the demand.
The demand is what is the work that is offered to the system.
counted at the entrance. So, for example, what is the arrival rate? So, the demand that's required. So, for example, there was this recent craze, like, about this, for example, there's this some funny soft toy, I also don't know what Laboo Boo, I don't know what this funny soft toy, right? Then you have a lot of people queuing up for this soft toy.
So what we call that is that the arrival rate, the demand there.
is actually very, very, very, very high. Also, that is… you can think about it as the demand-side automatic.
Then after that, we have the supply side of the metric. The supply side of the metric is how much is the system able to provide. So, doing that, that funny soft toy.
situation, the supply was very low. So the supply was very low, there was not enough to give out, and then the demand was very, very high. So what happened was that it resulted in the response waiting time to be very, very long.
Okay?
So, so these are the three parts where we can see the outcome, the demand side metrics, and the supply side metrics. So in the supply side metric, here we call it, one of them we call it, for example, in the throughput. Throughput is, how much
Well, in this example, how much soft toys is the battery able to come out within a set amount of time?
During my entire delivery, what I will try to do is, I will have one example that is a little bit more frivolous, then I will have two other examples. One example would be more in the manufacturing space, and the other example would be more in the healthcare space. And why I put these three examples is because
One of our…
the industries that hire us a lot is the manufacturing side, followed by the healthcare side. So, I think it may be good to, you know, see how your skills can be applied into other industries as well.
So let's say this example of this lithography scanner.
So, the little graphic scanner, it has the supply side throughput.
Maximum throughput of 150 wafers, per hour.
And let's say this, the demand, the arrival rate of, whatever that I need you to come up with me is 120, wafers per hour. If we put in the queue, if the throughput is, is, is higher than my demand, my arrival rate.
I will be able to meet the demand.
So, I have 20… 20… 120 wafers, demand coming in, comes to a queue, I'm able to deliver 120 wafers at all.
Okay, so the demand is 120 WAP per hour, my throughput will be the same, it's busy 80% of the time, 120 divided by 150, so, the work is, is stable, hence my arrival rate equals to my throughput.
I'm going through very fast today, so, so don't worry, but these things will be explained over this week and next week.
Okay, so if, let's say, my demand is higher, 188 wafers per hour, and my throughput is capped at 150, so what will happen is that this cube, every hour I have 30, that is, 30 wafers that will be, added on to the cube.
Okay, so my cycle time would increase for climb, and in this case, my response time will also increase.
So both sides agree only when my arrival rate equals to my, my throughput.
Okay, so in the LAUBU example, it's 5 people, and I, you know, I have 50 people queuing up, I only have 5, you know, so every hour, 50 people coming up. Every hour, I only have 5, so my queue will be 45, 45 will always be increasing by 45 every single hour.
So now, I go into a little bit more detail. So, we have the outcome, which goes to this outcome metrics over here.
Then we have the demand.
Where the demand, you can see the demand.
The demand side, which is the second, which is the demand over here, and then we have the supply.
Again, there's this coalition, by… by column.
Okay, so… we'll talk about the…
the outcome, which is the user experience metric. One of them that we want to look in is the response time.
So, the time taken for your page to load, for example, the time taken for you to start a selection, and then the time for it to get back the request.
It's the time that elapses between
the completion… the initiation, sorry, of the request, and its completion, okay? The initiation of the request, and its completion. This will be the…
Response time.
Okay, on the demand side, we have one key metric, which we call the arrival rate.
Aval rate is the number of units of work offered at a given amount of time. So, how many people are at the entrance?
At a given amount of time.
It says it's counted at the entrance, not at the end. Now, the exit is what we call the throughput.
The throughput is the number of units completed per unit time, which is counted at the exit. Okay, so a variable rate is at the entrance, throughput is at the exit. And then utilization, then, is how busy is it
During the time when it's between the entrance and the exit.
Here.
Go next.
So, we'll go on to the first response time. So, for example, you have,
you know, the time it takes for you to click on something to sing the web page shop. So maybe there's a think time, where the user decides what to do, and then you will click.
And then he will wait for the system to be ready for it, then he will serve, and then he will pack the response up, then go back to the user again.
Okay, so, there may be… there's some level of latency here, I'll just, you know, I'll just put it into, into one of, you know, I didn't put in the network latency around here, but, but you can consider network latency to be a little bit here, a little bit here. Oh, I didn't put it here.
But all this is counted as the… as the response time.
doing our labs on the J meter, like, what we'll do is that we'll be simulating this entire flow, whereby we'll be simulating, like, a person thinking, and after that, he will click on the page, and then you'll wait for it to come back, and then after that, you'll click on another link, and then you'll wait for it to come back. Then we'll measure the response time of the entire operation.
So, these are some of the metrics that people use, heuristic, like, how… how people work.
Consider, files also.
So the table, refers to a single response time. Okay, so this is where…
we, we, we, we, we go back to… not go back, we, we, we dive a little bit, a little bit deeper, where, okay, so we talked about 0.1, like, it's like a, you know, at…
It's, like, a hard threshold like that, but… but in reality, we don't really measure things like such hard threshold.
Or we measure things as a distribution. And normally, this distribution, we collect over, over thousands of requests. And what we usually have is that we want most of the requests to be very, very fast, and after that, right, there will be, there will be a tail that comes on.
So, like, when we go in our…
No, when we, when we, when we do our projects, or, like, you know, some of our projects, we always think, like, we want to…
we were always sometimes very worried about… and we should be, yeah, worried about sandbags, or whatever things like that. But in most of my industry projects I work in, like, I always ask the question, you know.
What is the most common Thing that happened.
So let's say, they want to build a certain workflow. So I will always ask them, what is the most common workflow that will occur, let's say? And then thereafter, we would focus on their workflow first.
Of course, once we got the workflow correct, right, then all the rest of it, can… How badina.
Once we get the workflow correct, then we worry about the rest of the 10, 20, 10, 10-15%, but the main, let's say, 80% of the workflow gets correct. Actually, if we can get 80% of the workflow correct.
And we can make the customer happier. If you can get 80% of the Buffalo correct, the customer will naturally become very, very happier. Yeah, so, to me, that is…
Really, really important. So, so back to, to this, especially most of it, we see that, oh, most of the time, we will have people that are able to get a very, very fast response time, and then the, the, the response time will then, will then store along the way, lah. Okay, so you would normally see this kind of a graph.
Whereby, no, you know, most of it, most of it will come at a very, very fast pace, and then there'll be a slow little, drop-off to, you know, to, to where it becomes very, very, very, very slow. Okay, and we always want to have, this to be, like, what, the 1%,
To be… to be maybe very, very long. So if you get the 1%, then… No. No.
Not very fortunate, not very fortunate.
Okay, I talked for quite some time, so let's do some exercise. Okay, so I'll give you maybe,
3… 3 minutes to do this.
So, we have this friend, that, you know, he's a procrastinator, and you know, he's asked to do our work.
This, and, you know, the instructor is the client.
There is the server.
Service time is the time he spent working on the lab.
Everything else is wait time, okay? So, he goes to the washroom, coins his hair, puts laptop, and what's his total response time?
there are some,
Some questions… no questions, some responses here.
Yeah, so… so we… we first, we classify each point.
Each point… what kind of time would that be?
So, let's classify them.
So for each, for the first one, The first one is the… the wait time…
Then again, and the wait time.
Innovate time… And then only… the service time is only the time Larry spends, in the lab.
So this becomes… The first service time.
Then it's, again, another week's time.
And then here… It's another, service time.
And this is completed. So after the thing is completed, this is actually,
not counted, lah. Oh, not counted. So the… the service time is actually the time that is being spent, actually working, lah.
So, in this situation, I… The service time is actually, pa 2, plus 8.
Which is, only, 10 minutes.
Boop.
And then if you combat the entire response time, it would be… This time, from here.
Oh, it is over here.
So this will all be considered as the response time. So the time where he is given the request.
To the time that the response is completed.
So this is not counted at all, because this is after completion already, or so this is not counted at all.
So his response time is only until…
Give you a mop.
So now, this is the healthcare… Ashton.
I have.
So in the same way, you can, try to calculate this.
Okay, I think this one is a little bit more straightforward, huh? Okay, this one… The first item…
Will be wait time.
Is our wait time.
This service, this wait time, the surveys…
The actual service time will be 10 plus 5?
is 15. Response time will be 25 plus 10 plus 15 plus 5.
Okay, this is other than this, 20, 30, 30, 35…
Correct, yeah, to 5. And then, what is the proportion of the visit they spent waiting? So, this would be the amount of time that's spent waiting.
It's, yeah, it's 40. So the proportion of the time
The SPAN weighting is 55, what's like 40 divided by 55.
Just about 73%.
Okay.
So, yeah, so this one… I have one note over here.
Which I think is… is nice. So most of the response time is overweight time, so the delay is Q-denominated. But, but, but some… some people like to say that, you know, you reduce…
If you reduce the consultation time, for example.
It's not necessarily that you only wait… you only reduce by 10 minutes, actually not true, no. If you reduce this, right, you actually can reduce this as well.
So that is one thing that many people, don't realize. Why I can… why I said? Because I… I do some, some simple work with, with some of the hospitals here.
And I know some of… one of the important tasks that they monitor is that the time it takes for a patient, once going into the A&E for the traging, for the traging, how long does it take for him to get to the… to the hospital bed?
Yeah, so they… that is a metric that is…
monitored quite stringently. I think they need to hit a certain standard, right? Yeah, so that is a number that they monitor very, very often.
Yeah, so… so, actually, when they talk about such things, like, it all goes back to such modeling once again. So, when I look into some of the performance statements, right.
they're actually very, very similar to what we do in IT. Maybe… maybe they come from a common queuing theory, and then we all borrow from there. Yeah, so I think there's a lot that we can apply elsewhere.
So I have done here, this is done.
Okay, so percentile.
So, I have these numbers that are there.
What's the mean response time? What's the median? What's the P90?
So this one, we all try, maybe,
Maybe you can try 1, 2, 3.
For the next, maybe 3 minutes?
Okay, let's continue. So, we, first question, what is the MIN response time? This one should be okay lah. We'll just add everything up.
And then just divide by 1, 2, yeah, it should be 10 numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, yeah, that should be 10. So just everything up, divide by 10, I'll give you the answer here.
Everything up, divide by 10, you will get 298.3. Okay, so the other thing you need to do is you need to sort the numbers from small to big, and then you get the, get the, get the median.
The median of… oops, sorry. The median of this would be, the fifth and the sixth number, the mean of the fifth and 6th number, so would be 1…
These two were together, divide by two.
The meeting will give you a 111 meeting.
And, P90 equals, there are 10, so the P90 will be a nice order value, which is this number, which gives you 120.
Okay, so far?
What?
So, so there is one final question that I didn't… Didn't answer.
Another question is then…
which one will you choose as your SRO, which is your service level objective? So you… you… you choose one that is,
that is… you won't get… will not get complained about. So, median is the one that is typical, which is, pretty…
Pretty low.
P90.
the expos… exposes where… The tail usually ends up.
Okay, so you can think about that. You want to
guarantee that most of the… 90% of your customers are happy, right? Then 120 will be your… 120 will be your service level, objective.
I'll go on… So, okay, Rena?
Let me pause for a while. So, you're okay, I'll continue on. Let me see how much…
Let me… I'll tell you what, I'll just go on for a few more slides, then, after that, I will… I'll stop already. I see your, your,
Let's see, many people are… starting to… my… my,
my retention rate is quite lower, so…
Yeah, that is what I will complete until…
this part, then I'll finish. I'll just do one to two more slides, and then I'll call it finish.
Yeah, so we have done the, the output level metrics. The other one will be the demand level metrics.
So, the demand level metrics, like, calculates the arrival rate. So, arrival rate is the number of units offered in a given amount of time.
So, for example, number of requests arriving at API per second, number of lots arriving at Little Gaffey 2 per hour, in the talk about healthcare, right, it will be the number of people arriving at your A and E per hour.
So, it's, how fast the demand actually comes, or how number of people queuing up at the store per hour.
Okay?
So, there's this exercise here.
Okay, so I'll give you maybe the next…
3-4 minutes to… to try this out.
Maybe I read through lah. So, Larry is enrolled in four modules.
Although 12 weeks are a trimester.
Each module has one lab per week.
So, it's about 4 laps per week.
And this is how he… Completes the lab.
Yeah.
And, in the language of SAIP, this is how the demand is, the normal workload is how much
labs does he have every week? So the arrival rate of his labs, is 4 weeks, 4 a week, 4 a week, okay? And the labs that he is able to complete is the throughput.
And then, so for example, if we can do 4 lats per week, that means that he is… his throughput is, 4 less per week, and week 9 to 12 is, 5 lats per week, which is also his maximum throughput.
So, we have these questions over here, you can try them out.
Thank you.
Okay, let's, start.
So… we have… This guy…
that is working on… so the arrival weight is 4 labs per week. So the first question is, what is the total number of labs?
It completed… completed in the trimester, so the… 4 times… Ball.
lies,
Tree,
1, 2, 3, 4… 5, 6, 7, 8.
Paul? Sorry.
Times 2, and 10, 9, 10, times 12, 4… And… Right.
But this would be 16.
This should be it.
This would be 20, so 24.
44. So the total number of labs she completed is, 44.
Average throughput of LAPS will be 44.
Do you buy it by?
12.
Okay?
So, duh…
the… the number of laps, the throughput is… the average throughput, rather, is 44 dB. Its maximum throughput here is 5.
Guest 5 letts per week.
And then the average throughput will be,
The demand, average throughput would be…
The shortfall is going to be 48.
Minus 4?
Which, minus 44, which is 4. So the percentage of 4 is 4… I'm true.
Okay?
Any questions so far?
You're all very quiet, but Mike.
D.
Okay, this is. Okay, good. Now, we have another similar one, so please try this out.
Okay, are you okay? Yeah, let me start.
So, here we have a semicor… Factory, that is… Looking at… 12,000 units per day.
Over a typical Friday work week, Monday and Tuesday, it runs at full capacity, so… 2002?
times 2.
And then on one… on one of the days… Dubic style.
So it's just, to half.
And then after that, there's, no, they force it to maybe run an extra shift.
So, 1400 times 2.
So what's the total output for the week? So there's…
2400 plus 600 would be 3,000.
3000 plus 2008.
201 Damn.
Okay, so the total output is 5,008.
The average throughput units per day, is 5,008.
You, bye, bye.
5.
First Fridays, 11, 6… Right? Oh, when I say zero. Yeah, I want to say zero.
Okay.
So, the average throughput, after they, you know, do the overtime, everything, is 1160. The average throughput, the shortfall, that's the percentage shortfall.
So we have, it's supposed to run at…
$6,000. It's similar to just some of the example lah, huh? You buy 6,000.
So it goes to 200.
That's what I'm pretty.
So, you can tell right now, like, how bad
The situation is, if a machine needs to break down, or any machine that breaks down.
It causes a lot, and you know, immediately there's a shortfall, even though they try to
They try to compensate by, by, you know, Doing an overtime, whatever.
Okay, I think everybody's fine. Okay, let's go on. Okay, so I won't go through this. Okay, now we do the last one, and then we will call you at day-to-day, you know, just about 15 more minutes, and then we should be done immediately.
The last one is, again, on the supply side. On the supply side… oh, not again, the last one is on the supply side. On the supply side is what the system is able to provide. So, would be, the throughput, like, for example, how many soft toys you can turn up, how many,
How many bowls of, no?
Noodles you can cook, you know? How many…
Things you can cook over a period of time, and then how much… and then also the utilization, the proportion of the time the device is busy, or when it's working.
So, for example, the number of bytes transferred per second, the percentage of time the CPU is spent executing instructions. So, if you open your laptop, you'll see that task manager, that'll be percentage busy, that's your utilization. Your RAM, that's occupied by its processes.
Okay, this part is… is a little bit more…
More… it's starting to get a little bit, technical already, because once we have passed through this
Service-side metrics that we start to…
I have some more formal definition.
Now, the formal definition we have.
The first is TAMCA, which is the arrival rate.
A variable rate lambda is the number of variables observed.
per unit time.
Inter-verb arrival rate is… The time that elapsed between consecutive arrivals.
So this time, The time spent doing a single job?
And the throughput is the job completed per unit time.
And then last one is the service rate, or the capacity. For a single server, for a single time, your, actually, your capacity equals to your 1 divided by your service time, meaning that when my utilization is
Or what, then, is my service rate? So what happens is my…
Maximum throughput when the… when the… when the… when… when my… when my… when my system is always busy.
If…
If, if for… if sometimes, like, you realize that for the machine, a mean interval time is equal to 1 divided by lambda, meaning that, the…
the time is always, busy, or maybe there's no queue, and it's able to, once it gets in the request, it comes out the request. So that's, for… it happens for long-running stationary… stationary workloads, okay?
But we don't, we don't worry about this for the time being. We would consider all this. Later on, we will have one example that highlights the difference between
In this basis, what is the sample mean of the, of the inter-arrival gaps?
So, right now, we have this example. There are 4 jobs that appear, ABCD,
So, for each drop, what is the… wait time?
The service time, and response time for each drop.
Okay, so I will explain what this means, so, for job A,
it goes at 0, and then it ends at 1. So, the time here… okay, I will just go at drop for job A lah. The wait time is 0.
The service time is 2.
And the response time is 2.
P.
Y'all try this.
question up. And then after that, we will call you a day-to-day.
Thank you.
Final question.
I'll just go through the first part.
Question number one.
So, so for B, The wait time is 1 unit.
The service time is 1, 2, 3, 4.
4, and then the total response time is… For C…
The wait time is 3.
Service time is 1 is 4, and for D, the wait time is 2.
Service time is 3, and the total time is 1.
Yeah, I hope you can get this.
So this is question number one.
Okay, let's look at question number two.
Calculate the arrival rate over this period of time for, like, I don't know, 10 seconds.
And then about 10 units of time zone. And then the 3 observed gaps in their MIN compared with 1 over, lambda.
Let's look at what lambda is first, lambda is my arrival rate. So, how many jobs arrive, so lambda…
Is my arrival rate.
Which is the number of jobs that arrive, within,
a unit of time, okay? And now we have,
How many jobs are here? We have… 4 drops that are here.
So we have 4 drops that are present.
And in these 4 drops, You have, over a period of 10… HAM units.
So lambda equals 2.
Dual point.
Oh.
So, by right, if you have lambda, which is how you evaluate, which is, like, 0.4 jobs, per second.
Your inter-arrival time is actually equal to 1 over lambda.
Which is… over 0.4… KGQuesto.
Kool 1 to 5.
Okay?
So your… actually, your inter arrival time Is equals to 2.5.
But what some people may see is that, may see is that
they see… actually, I, why, why, why, why, why is it 2.5, no? Some people may think, this takes 1 second, no, to, this job takes one second to 1 unit of time to arrive.
And this one, like, achieved it.
2 units of time.
To arrive.
Then this one, takes another…
2 units of time to arrive.
So, does it mean that my average inter-arrival time is… Warm. Lice.
Too.
Blast.
Too?
And then, after that, get the mean of them divided by 3.
And this will give me a 1.6-something number.
Does it mean this is how I calculate the average interval time? Actually, no, that is not correct. So, some people…
try to calculate the interval time like this, it's not correct. So we ought to calculate the interval time
Through the lambda, which is the number of jobs, divided by the amount of time.
That just gives us the lambda, and then we take the reciprocal of the lambda.
Okay, so this is one thing to…
To, to be mindful of.
Any, any questions so far?
Okay?
P.
So, last part… Last part will be, what is my, every shower.
Okay, my average service time. My average service time here, this one is, is a little bit of a frivolous example. We have 10 time units each time unit, and we have 4 jobs. So our average service time is simply equals to
2.5. And our service rate… Equals to the reciprocal of 2.5.
Which is, 0.4. So in this case, like, our arrival rate is equal to our service rate.
And you can tell that our server is always busy.
And the utilization here equals to 1.
Anybody, needs me to repeat any portion of, this example?
I think… I think, I think I'm… I'm good for today, Wendy lah. Yeah, it's been a… a long Monday.
AM… I don't… I think,
I think maybe I should have given you all a rest earlier. Next week, I will better manage the time.
So, thank you so much. One thing is, if you have any questions, please feel free to, to reach out to me. Yeah, I think, I think y'all have a lot of lectures today, and I'm the last one.
Yeah, so I think I'll give more…
More breaks, next time, in the middle, so that, y'all would be, less…
Nice to know. Yeah, but thank you so much for your time this evening, and next time, I will… I will, be able to space out better. Thank you again. I'll see you next week. Bye-bye.
