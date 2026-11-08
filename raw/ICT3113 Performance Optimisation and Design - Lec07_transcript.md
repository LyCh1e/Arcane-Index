# ICT3113 Performance Optimisation and Design
## Lecture 7 — Performance Testing — Re-recorded Lecture Transcript (Verbatim)

*A/Prof Donny Soh — ICT Cluster, Singapore Institute of Technology*

*Note: auto-generated speech-to-text; mis-hearings are left as recorded (e.g. "Genita"/"Geometer" = JMeter, "soken"/"soup test" = soak test, "PSTEM" = presumably the lecturer's results output, "Benny Schmuck pest" = benchmark test).*

---

Hi, good day to everybody. So, I realized that somebody very kindly told me that there were some issues with the audio in the previous
recording. Hence, I'll be redoing this recording. Thank you so much for your patience, and I'll start.
So, I would consider this to be one of the critical lectures of the entire session. The reason why? Because, like, we are linking the theoretical part to the vertical portion.
So, in the theoretical portions, we learned about things like, the metrics, the percentile utilization, and then, in the lecture 3, we talked about workload.
lectures 4 and 5, there were a lot of math formulas that were there. So, in this lecture, we're going to be linking up… linking up the
the theoretical part, the theoretical part with, 6 different performance tests. So they'll be doing, load testing, soken testing, can't remember the rest, but we'll go along there in the second part. And I would… I would… I would treat this as…
is quite critical, because these are some tests that AI cannot run for us. You know, AI can… can… can write a lot of tests for us, they can write some tests for us, I mean, they can write some tests for us, they can help us to analyze the results of the test, but they cannot run for us.
If they run it in their own sandbox, it is typically not accurate, because the testing environment is different, so, you know, it will not be accurate if they… if they kind of, everything we do it.
I mean, they can run it for us if we allow them control over our samples, over our testing environment, but then that will be…
that would require a certain level of control, so I think that would still not be the most…
likelihood of that happening in the near future where you'll be graduating is lower, so I would still be expecting you to be running your own performance test. I would expect AI to help you.
craft sort of this test, but I will still expect you to be able to analyze the results.
Obviously, to understand
If, really, the test is exactly what you are looking to assess, and then to understand what are the areas within the test that we need improvement, they may help you to craft the test, but you have to decide whether, is this test really…
suitable for managing that portion. And finally, I actually believe that you will be the one that will be executing the test on the back.
So
So this lecture will be split into three parts. So, part one, we'll be looking into the performance requirements documents. So there are about four documents that we need that…
Typically, we'll be requiring, for this lecture, we'll be… well, and also for this module, we'll be only going through three of them.
The requirements plan, the measurement plan, and the test plan.
And we'll put them in the form of,
of a template. So we can follow a fixed template, and from that template onwards, right, you can
You can… you can then see how… how… how to easily, I would say, write such requirements, yeah.
After all, if they fall on the template, it should be quite… not so difficult to manage.
Let's go through part one.
So this is the structure of…
of the requirements, there are… in the template, that was proposed by Bondi, there are 10 sections in total.
Okay, so we have the requirements number, we have the title of the performance requirements, we have the statement, what this requirement is supposed to do. In fact, 0.3 is slightly the most critical part of the entire performance requirements.
Because you will need to ascertain that he needs to run
like, below a certain number, you know, and maybe in a certain condition, everything. So, 0.3 is likely the most critical part.
You may have, no, no supporting commentary in .4, some percentile, quantiles.
quantities, and 0.6, and other requirements, assumptions, but all these, right, they all are meant to support point number 3, which is
How the requirement, or what is the actual requirement?
So these are… The explanations of…
all the… of the individual points. So, for example, in…
Climate number, performance 01, the title of it, or what this is supposed to entail. The statement will be the most critical thing you can tell.
95% of everything shall complete within a certain time. How is it measured by? And in what condition.
esto inventor.
So you can tell point 3 is…
It's really… seems to be quite…
Quite, quite detailed, in what it needs to…
be testing for. And the rest of it is… is just to justify what point 3 is.
So, for example, point 4 is to support whatever commentary there is to support what is point 3.
The point 5 is when we order with reference papers or research papers that have similar, similar, similar…
similar… test conditions.
Point 6 is how we, in fact, got these numbers. So, some of these numbers, you may be able to back-calculate based on the workload. You'll be able to calculate based on, you know, wherever
whatever resources
compute resources that you may have. Yeah, so 0.6 is where you derive them from. So, remember, 0.5 is whatever precedent that is there, so maybe another company is doing a similar one with
such a response time. And maybe for you, yourself, you are able to say that, this is the amount of workload that I expect to…
To get, like, 10 requests per second.
And, yeah, 0.7 and 8, yeah, I think nothing much. 0.9 is how you…
What tools we'll be using in order to
To work and to measure, this performance requirement.
So, this is the template pattern. So, the template pattern here states that, okay, so first you have a condition.
been… And for example, in how many of the cases?
You know, the system shall have a mean response time of no more than 200 milliseconds.
So, so this is for the response time.
This for the throughput.
Okay. In the response time, we have certain It does.
So when you write the performance, so-called subject, lots of people, sorry, what is the… when you write the performance…
a statement, but one statement, you should be using
All of these editors to craft the performance statement.
So, for instance, in the case of something, like, where, you know, for example, in the case of
For example, 11-11 in the first 10 minutes of 1111.
the ye…
maybe the add-to-cut operation must not have, or rather shall have a mean response time of maybe, no more than 200 milliseconds. And maybe there are…
They are… the one is the add to cart, maybe you have another one, which is maybe the checkout.
must have a 95% percentile response time, maybe of, no more than maybe, 50 milliseconds. So, so that, so in…
Such cases, what we do is we'll just take from individual sections, we'll join them together, and easily we can form quite a nice something.
Performalistic migrating.
And the target one, the one on top, is the performance statement for response time.
That is the other performance statement, which is for the throughput.
So, for the throughput, throughput performance statement, what… similarly, what we do is, we have various different
haters on top, and then we kind of join them together. So maybe in… How many of the cases?
the checkout.
The checkout operation shall have a mean throughput of… No less than… Maybe, 1,000…
No orders per meet… per second.
So, similarly, we're just drawing some of these
These things together to make it, to make sense of them.
Okay, so I'll give you one example here.
So, we write these requirements so they can be tested, and the requirement is the ordering system shall be fast and scalable, and shall handle peak loads without noticeable startup.
Okay, so I would ask that you pause the video first, and try to work it out based on the
based on the patterns that were presented in the previous slide here, okay? So, please pause the video for the time being, and try to work out the statement yourself.
Thank you.
Okay, so I will continue on the…
section, so please pause the video if you had thoughts. That was, I'll continue.
So this line can, in fact, should be broken into two parts.
So, the first part is where it talks about the ordering system, Shall be fast.
Okay, so this pasta is, it's a very… It's a very, rough…
Very, you know, not a very nice word, because there's no meaning, there's no quantifiable meaning.
So, when it comes to fast, this is in fact, belong to the response time.
And then the second part, shall handle peak loads without no signal disable slowdown. This… Follows to the…
throughput. So, this entire line, in fact, should be broken into minimally
two different performance requirements. The first will be towards the order creation response time, and the second should be towards the true performance.
There may be a third, which is a scalable. So the scalable one can…
become itself as well, another requirement, but this one is actually a bit harder to take, to write, and I don't cover… it's not… it may not be able to fall under either one of the templates.
Yeah, so, so I, I did not, I did not cover this, for this time around. Yeah, so, just, just take note there. There's a scalable part which, was not included in, one of the templates.
But we'll focus on the response time as well as the throughput for today.
So in the response time, what we have is the… the main thing will be the statement.
So, 95% or something, Shell, and complete within something.
And this is the rest of the scenario that… Ben.
That, we have, indicated. But the main, main thing is, see, 95% of something.
Shall complete within 200 milliseconds.
Meeting go back to the previous slide.
So, 95% of something shall complete at one minimum of less than 100 minutes. So, remember, this entire thing.
It's exactly what we see over here.
And the rest of it is just the quantifiable… some of the qualifiers that we put the requirements undone.
Second, we have the following. The other one would be in terms of the throughput. Similarly, some of the service here shall proceed at least how many orders, which may be considered to be the peak load at, a certain, error rate.
And then this is the rest of the scenario.
not increasing by more than… So…
So this, this one will be part of the scenario, and, we can get the peak load.
By… by maybe, calculating or estimating what does it mean
When the system means it's going to be a pick and book.
So, this will be the final step for this section.
So, good performance requirements pass the same checks as the functional one. So, we have talked a bit about what are some good functional kind of requirements, or some good metrics in the early lectures. So, in this aspect, the
The performance requirements should fall with the same standard as that of functional requirements.
So I think, I think this will be the end of the first, section. The next section will be quite exciting, meaning that
reason because we will really be going through, 6 different, demos. You'll be… I'll be running
some videos on… maybe about 4 of them, and you will be able to see in…
you know, how these demos are being run, but importantly, the results that come out from PSTEM, also. And hopefully, this will benefit you, you know, as you are going forward for your career.
Thank you, I'll see you in the next section.

So in this portion, what we're going to go through is the second part, where we'll be sharing about the various different tests that we're going to be running.
So, first, we talked about the difference between closed-loop systems and open-loop systems. So, by default, our geometer looks at closed-loop system, where each user
sends a request, we wait for the reply, and then after that, it sends the next request. So, in our load, this would be N divided by response time and think time, and, this is what typical geometer standard track group does.
For now, the rest of the tests that we'll be doing, we'll be doing something called the test, where, you know, arrivals, or rather the requests arrive at a certain rate, whether or not the previous, has been answered or not.
And, this is also how real traffic, behaves, where customers do not stop arriving because the last one is pending, and this is known as the open model track group.
in the genita.
No? Okay, so it went back into a bit of 2016, where, where we have the launch of Pokemon Go. You see, in the launch of Pokemon Go, it was such a phenomenal that,
I think they never managed to recreate, this bus, that happened during that period of time. And they plan for 5 times of the expected load, and they still… and in the end, actually, they got 50 times the object estimate.
And they would never be… have been able to capture this amount, because the… the… the, the, the…
the… The traffic that…
that they… they got was so much more than what they expect… so much more than what they expected, so, yeah. So… so the question now I have is, you know, I have for you is that, what performance tests might have, caught this
So, I'll leave you maybe, one…
Maybe you can pause the video first, and think through what performance tests might, have been able to court… might be able to catch, this…
This, this situation. Okay, in, in today, okay, maybe I, I, I can also say what are the performance tests that you'll be going through.
Yeah, so we'll be going through load testing.
Stress testing.
some tests.
regression test.
Benchmark and PEPT index.
So, these are the 6 different tests.
that we'll be going through today. And if you think back to, the Pokemon, which of these
test…
like, would be able to have caught. So I give me, I give you maybe, pause the video, rather, and you can think through, and I can, you know, and we'll go through after you unpause the video.
So, the answer here would be stress test.
So, if you do load testing, you are going to be testing according to the expected load.
Even if you do it multiple times of the expected load, which is 5 times the expected load, the load test would still pass. So, even if you have done the load test properly, and you deem that the load test passed, you'll also not have caught this situation. And what might have caught this situation would be…
Probably the stress test. Like, the stress test, what we do is we intentionally, stress test the load to make sure that, you know.
that, if things go wrong, things, hopefully will not break. Yeah, so, of course, on hindsight, it's easy to say, this very easily, but, but, likely, it was, you know, likely they have done it as well, but the stress test…
We'll be able to highlight where, I think, parts that will break, given this situation.
Okay, so the first test we're going to go through is that of the load test. The load test, you'll test an expected load to see whether is it steady or not, and whether the system, does it meet the performance requirements under a certain, under a certain, no, under a certain load, lah.
And then, what we'll do is, we'll set the arrival rate using the WorkNote model, and then, over,
it will be X number of requests that comes in per second, and then we'll run it long enough for it to be listed.
Then we record both the response time, and then as well as to be able to measure the P50, the P95, P99, and the CPU, and all the other memory usages all around that. We want to see the response time, the throughput, the average rate.
And if the…
Whether the test passes or fails, it depends on what was in the requirement. What was in part one, also what was in the requirement.
Okay, so when we're doing this processor, we're going to be seeing four command line windows.
So, on the top, left, it will be the service that we are running. So, it will be the service that will be, taking in the requests, from, the so-called the clients. And then, on the bottom left.
will be the generator of the request. So, here, we are going to see that, for instance, here, will be, I think a rate of, 10…
request, per second. So a new order, 10… 10 requests per second, or every order, every 100 milliseconds on average, and, it will run for about 3 minutes.
On the top right will be, the monitor, so we were… there are two forms here. One is single request, and the other one is monitor, or PY. Single request, right, helps us to calculate, on average, what is the response time when we run a single request.
on the server. And then Monitor will then, will start to monitor the various instrumentations, writing into command line.
Okay, writing it to, CSV file. Now, on the bottom right, we will then, display the CSV file in real time. Maybe every other few lines, you know, we start to display one or two various different, forms, so-called lines from the CSV file.
This is how you look like.
Okay, so this will be the screen, for demo one.
So, yeah, so I'm going to be starting to run the demo. So, on the top left, we have, we now start the application, which is Python.abbp. Now, we notice that, the
Flask server is now running. Okay, so you see that the server is running, the…
I don't know if I'm done.
Then we go to the top, top le- top right.
In the top right, then we will start to run the single request.
So, the reason for running this single request is to ensure that the…
To measure, to measure what is the response time, per one requester.
After we are done here, we start to create a monitor script. We run a monitor script, and this monitor script actually records down the resources that are being consumed, and then it will write them into a CSV file.
P?
So now it's starting to write me to the CSV file. I think next we go to the bottom, bottom right.
At the bottom right, we will start to… Continuously… Output in…
latest few lines from the CSV file, but on the bottom left.
Right now, we start to create the load, and what we are doing is we're going to be sending in a rate of 10 requests per second, sending it for a period of 3 minutes in total.
So, in the top.
left corner, you can see that the request is moving. The request is moving largely because, like, we are sending in requests, from the… from the… from the node, which is the bottom left.
Now, we view what's happening on the bottom right. Bottom right, it is, you know, coming up with the figures of
No,
Let's take a screenshot. Coming up with the figures of, what is the timestamp, the CPU usage, percentage usage, the memory use, memory available, and the memory for the hook as well.
I think, yeah, I think we are almost done with Demo 1.
I think… I think I do need to run through the end of… Dammit, let me see… yeah.
Oh yeah, let me also analyze the data. Analyze… this would show us the amount of load that was being
Paste in.
Which is 10 requests per second. The throughput here is almost the same.
And we have the P50, which is 70 milliseconds.
120 milliseconds, and the P99 150 milliseconds. So if the request, if the performance requirement was 200 milliseconds, our load test, shows a great success.
So our P50, EP95P99 all shows a response time of below, so-called, below 200 milliseconds.
Let me show… go to the next slide.
Did he help.
So, monitor file, this is on the file that was created on the top right and the bottom right.
shown on the bottom right, it shows you the CPU percentage that's being used, the memory that was being used, and the memory available. So we're using some of these metrics, right, in some of the later tests to come. For this test in particular, we are not using this. I mean, it's good to monitor and to see, but there's nothing outstanding that we are able to see,
Over here. Nothing out of the ordinary, you know.
Again, this is the part that is interesting here. So, in this, section, we see, the, as I was saying earlier, the,
The load that was being sent over, which is 10,
We know that P50 is 70 milliseconds, and this is the corresponding times for the 95 and 99. Error percentage 0, which is very, very good, so none of the packets, resulted in error, to 2.09.97, which is very similar to the, the error rate of 10.
And the CPU, CPU usage, I think, and, and, and, and, and the ratio between the sun and the end, which is, okay, which is, nothing, nothing out of the ordinary for this, so…

Okay, in, stress test 2, that's where we… we test the system beyond its capacity.
So, in Test 1, we test it, that it's within the load that we expect. In Test 2, we would, we would, test it intentionally beyond. So, what we do is that we start the system at the load whereby
Who is expected to perform, to be able to perform, and then, over time, we start to slowly step up the arrival rates, and to see
which are the… which is the point where the system actually starts to break. And then we plot, kind of a need, where we realize, oh, at this certain point of time.
That's where the aerobics climb, and that's probably where the system, really can't, is unable to, to, to support that, the load that we are pushing it towards.
So I'm going to play the demo as well. So, first, we will start the demo.
are the surveys.
Thereafter, what we'll do is… We would then…
I believe we also, run,
Yeah, so this shows that the script is working. We also do a single request to know what is the response time.
And so we calculate the response time, here.
And then now we're going to start the monitoring script to start to write the data onto the CSV file.
Here we start the load. So, notice, what is happening is that we're gonna run, the load of, 5 requests per second for 1 minute, followed by 10 requests per second for 1 minute, followed by 15, 20, 25, and 30.
Yeah, so we're going to, measure, really, how the system performs according to, this loader.
Yeah, so I'm going to steal the video as well, so we don't go through all the five units here, and then we'll be looking into how the system is really performing. I think we're going to see on the bottom right corner.
So, bottom right corner, you have this chart over here that says, at which, you know, at which, interval, rather at which.
at which, load that was there, what is the error rate, and, what is the P90, P95 as well. This graph is… is hard to read here, so what I'm going to do is I'm going to switch over to the… to the… to the… to the slides. So this is, better.
Okay, so, at… at P, at the load, when the load is equal to 10, it was as per normal. So what we started was when we started at load equals to 5.
So we check.
the throughput.
And although it's 5, everything is still okay.
P95, P50 are no issues.
We grew up.
to 10?
Still looking.
No concerns over here.
Yeah, the error is still, relatively low, still at zero.
Okay, now, but then, notice one thing.
Notice that our P95?
I just climb up
our P50 also has climbed up significantly. So, it is likely that
If you look at, you know, how the system is performing, at this point of time, we likely have, passed a certain
a certain, a certain, a certain, need, where, you know, where now our P50, P95 is, beyond a certain amount.
If we want… if we increase it anymore at P15, we realize that the average rate starts to climb up.
Same thing for the P95 and P50, airways climb up. The throughput is, you can say that you can hit a certain ceiling of 12.
And, when it goes to a runway of 20, similarly, it's about 12, and not every week is out of, every… every 3 packets, one is, you know.
Corn.
Same thing at 25, now it's at 40% error rate.
At 30, now it's at 50%, hardly. Half of it, half of it has, has, you know, it's been rejected.
Yeah. So, the interesting thing that you may find a little bit strange is that as the P50, as the error rate goes up, unfortunately, one thing is that the P50 also goes down.
And there's a reason why that is happening, it's because, right, these refusals are also being, taken into consideration when we're calculating the P50.
So, although the P50 seems to be going down here, you know, some of you may think, this seems to be a good sign, but actually it's not. It's just that we are taking the rejected, rejected things.
you know, rejected, requests in, as well, yeah. So, that's the…
That's the reason why we see a drop in this P50.

known as a soup test. A soup test, occurs when you are running a test, and it's supposed to hold a load, and it's supposed to hold a load for over a long period of time. We want to pick a load that is below the knee, and so that, you know, if, things,
If things go wrong, it is because of something that occurs in the memory, or something like that, and not due to saturation.
And to hold it for a long period of time. And, yeah, and some of the things we want to watch out for is, for instance, a memory light rising in the straight line, and, you know, there's no clear at all, which means that there probably is some memory leak here and there.
Okay, so I will not be, showing you the demo, because, no.
There's nothing much to show here.
It's just running, and then you'll just be seeing something that goes rising over a period of time. But let me explain to you what is happening here.
So, in this service that you're running, we are going to be making a request.
For every request that is there, something is going to be added onto the memory. So there's going to be a database that's been kept in the process memory. So naturally, the longer it runs for, the more memory the process will be using, and then it will slowly get built up.
So, on this chart that we see over here, the blue chart, the blue, semi-speed line is the response time, the P50 response time, and, over the period of 10 minutes, we actually see the P50 response time, quite,
quite stable. There's no big variations that really happened to the P15 response time, so the resources during that time is still being kept in check, so as what we expect, because we are running it below, below the load test.
Yeah, and however, what we see is when we measure the memory slope, we see a gradual growth in the memory usage. And as what we saw earlier, as what we discussed earlier, that is also to be expected, and the reason why is because, wherever we are doing these tests, we realize that, you know.
The memory that is being utilized is not being released, so it's still kind of memory. So, in process memory, and hence, it's not surprising that as we start to utilize, or rather, as we
continue to run, the test here, the memory, then starts to, gradually get, long, get, get used up again over time, and over some period of time, this thing would, probably, you know, just crash.
Yeah, and the key thing to highlight here is we show that, here, the memory usage actually goes up over time, but one key thing, and the P50, it stayed flat, but one key thing to highlight here is neither the
Neither demo 1 or Demo 2 would have captured this phenomena, and the reason is because it ran for… in this, both cases, it ran for too short a time, and both of them, they focused more towards the response time, and not so much on the memory.
And, in this situation, this test tree, which is the Soak test, would be able to
Catch such an error.
In test number 4, You will have the performance regression test.
So, what this means is that, maybe…
The original, system had,
series of performance, you know, experiments that have been run, and then we make some changes onto the system. And with the new system, we test again to see if… have there been any
Any changes, or rather any… any, yeah, any changes, any negative changes, to the performance of the system or not?
And, of course, it's likely that if you were to change, something like, for instance, animal requirements, the performance of the system would naturally, be… be not so good, lah. That's typical of it. But the key thing also is that
We want to ascertain if, of these changes, are there any… any… any issues that we want to highlight and catch early?
The flip side of it is that assume that you have, you know, done everything up already, and then, you know, everything seems to be working well, functionally, everything seems to be working well, and then you realize that, oh, the functional test actually performs really, really bad.
And then you want to then decide, oh, where is the issue coming from? And that's where you will get a headache, because you… you will have to test various different components to understand whether, you know, it's anything that is, you know, going, haywire or not, which is the part that's going wrong.
And that may also have, other further downstream effects. So this performance regression test tests to see whether this change that was being done, did they make, the process slow or not?
Okay, so, the demo over here is that, you have, two builds, Build A and Build B.
So, in this, so-called, in this, you know, in this, example, what we have is, build A is the build, is the blue lines, and build B is the red color lines,
And here, we see that, over… for the P50, build A,
In Build B, I mean, of course, Build B is, is a little bit higher than Build A over time, but, but it's still pretty much, consistent. Oh, yes, for the P95, Build B does seem to take significantly, more time as compared to, Build A.
Yeah, I'm gonna show the, the demo here.
So first, we activate the Build A.
And then we run the server for build A.
So, these steps are rather similar.
After running the steps for block A,
What we do is we, again, we measure that of a single request.
And then we start to run, maybe some of the, tests that It's going for…
for view A.
And then, what we see is, we run it for…
5, requests per second for 8 minutes.
Okay?
Here, we get the responses, for build A.
A, so here we have the, demo A, running completed, so it's, 5, yeah. Now we're going to continue the test, and, now I'm going to run for.
Demo B. So, here you can imagine that Demo B is the updated, updated, no, is the, it's the application with, with more features, so we've, we have updated it that way. So we first set the build to, to build B.
And after that, we start the service…
Yeah, first of all.
Okay, don't do it again. I think we need to do the single, single response time.
Yeah, single request, okay, seems okay.
And now we're going to start monitoring for view B.
King.
We're going to run the same, load test, which is, you know, a rate of, 5 requests per meg per second for a period of 8 minutes, and then we're going to, to show the, the outputs.
As well, for building.
So, here we…
No. The example that we will highlight will be, similar to what we saw earlier. Let me pause this first.
Yeah, so we will compare the load test between that of Build A and Build B as well.
Okay, the numbers is a bit, small to see, but what I want you to focus on is the following.
You'll notice here that… the…
The rubber weeds are similar.
Okay? The throughputs here are also very, very similar.
Okay, what we see… Here is, the P50.
Yeah, it's increased by a bit.
But the P95 has increased by a lot.
Same thing for the P99.
So it does show a slight significant increase in terms of the response rate for the P95 and P99, and that may warrant us to really dig a little bit deeper into what is really going on with these two builds,
Okay, so this is, kind of the purpose of the… of the regression, test.
We'll go on to the next stage now.
It reaches the Benny Schmuck pest.
Benchmark test is where we… we measure the performance against a standardized load.
So in this case, we're going to do, use the hashing look. So we define what is the task, and then we keep it identical across various different candidates, the same request, and then we want to see, you know, how much
The performance actually changes as we, as we, change the…
The data, or change the load that is being, sent over to the system.
Hey, maybe before we show the demo, maybe it'd be good to just highlight what Intense, in fact, is.
So, we are going to have, you know, three different settings on the token hash, on the token hashing, or rather the, yeah.
The first will be… Maybe,
hashing at 25,000 iterations. The second will be hashing at 100,000 iterations, and the third will be hashing at 400,000 iterations.
So, for all 3 instances, we are going to be sending the identical load, which is 5 requests per second. This button, every time we send.
So, one of it will be, 25,000 iterations, another one, 100,000, then the next is 400,000. Okay, so, this is to, just to let you understand, what the… what the… what the test is talking about.
So, in this example that we see on the screen, we see that when we hash at 25,000, the response time is about 110 milliseconds. 100,000, the P95 is a bit higher, which is at 480.
And, when it comes to 400, 400, thousand, so-called, you know, the P95, goes on to a high of, 20 seconds. But then, there's only one measure. The other measure they run into is the useful, the throughputs.
The throughput of the first two, is still, at 5, which is very similar to that of the throughput of, of the weights, but then at the…
400,000 mark, we see that the trooper has dropped by quite a bit, indicating that the error is very, very high.
Let's look at the demo here.
So, in the demo. So, first, we have, the 25,000 iterations.
They're going to set the… Team, team… The, the service to one.
Oh, it lasts right there.
And now the service is running.
Can I do the… Well, we're just going to start the monitoring.
Now I'm going to assign the load. The load will be 25.
Thousand first?
Then we're going to, showing the outcome.
Okay, I don't think I want to show all the three ones, but they're all going to be the same, so I'm going to skip ahead here, all the way to the end.
At the end, I will analyze the load.
And now we can view the summary at this point. Okay, we can view the summary.
of, yeah.
Okay, so you can see… the… The bottom of it is…
You know, similar across all three.
A variable rate here is, yeah, so the throughput here is standard… is, able to match the arrival rate, but the throughput here has, fairly,
decreased, so the throughput, actually, you know, has gone down by quite a bit. Ever rate, skyrocket, skyrocket as well.
The P15.
T15.
is slow.
is relatively, okay, but here, again, yeah, it's gone up.
No, me too, actually.
P95, okay, you know, over here, he has gone up by 4 times, and here it goes up to 30 seconds again.
Here, again, is, how do you put it? It's, is, is, I don't know, yeah, it's gone up by about, 7, 6.
times, and now it goes up to 20 seconds. So, can tell that here, all the responses are all
not really, not really, not really working. At high iterations, actually the response is, is not really, working, properly at, at all,
What is likely also happening is that
You notice that all of this is at 20.
About 20-ish millisecond.
So I, I'm also, suspecting that at this period of time, probably, probably, the request,
was ready… maybe had a timeout of 20 seconds, and maybe waited for 20 seconds and was too long, but then we just died, yeah.
And, just was abandoned. Yeah, so, luckily, this is, occurred, and probably a huge number of requests were in this category, which is why the number is, 20 over here.
Let me go ahead with,
Oh, the last one. So the last test is to see if the test itself is correct or not.
Yeah, so the log here will be very valuable, and this is to ascertain, to see, whether, you know, is the performance test really testing the correct thing or not.
Yeah, so, no, yeah. So, no, we will send the request by hand.
After that, we will check, if the assertion in the plan is similar, and we would check to see if, you know, if there are any errors that may come up or not.
And these errors may be very hard to catch, and what we will do is we would have to go into a little bit of detail to see, you know, within the plan, although it seems to be running as per normal, is it, in fact, you know.
Generating, or rather, returning us the right manufacture or not.
So, Demo 6 has, no actual run demos, but we're going to extend, this, over the slides.
So, what happens is, there is, a build where maybe you're going to run it for maybe n number of iterations. Like, here, let's assume that it's just 100… 100,000 iterations, but there was a change that was being made
And in this change, there was a file that you were supposed to write to. However, the file is missing.
So that is, or rather that the path that was
that it was supposedly to point to is not there. So what happened… what is happening is that, when it goes to…
Trying to, complete the request.
The… the…
order couldn't be written into the, into the log, couldn't be written into the database. And it will catch the… so the server actually catches the error. And when it returns, 200, HTTP status 200, which states that, oh, everything is fine.
So, when this happens, and if you were to see, like, you know, how the test is being run, we would…
Have the forced impression that
Actually, everything is going well, you know, that, you know, oh, seems that, the order is progressing well. My P50P95P99s are all doing well. Success is 100%. There's no, no, no, no, no, no, no, nothing to doubt.
That, that, that, you know, there's something that is really, incorrect over here.
Yeah, why? Because, like, it was written in a way whereby if there's an error there, even though there's an error there, in this case, it is still returning a 200, and the error is not in court.
So, in real life, this might be quite hard to catch.
But what you would be able to suspect during this process is when you start to do, maybe your load test.
No tests, I think it was too hard, it was too fast. When you start to do your stress test, you will then, start to see, how come…
my…
I'm able to scale to a huge amount, but it doesn't seem to be taking up additional requests at all.
And that's where you then start to suspect them.
Maybe there is something, that is wrong with, you know, some of the
Some of, the, some of the…
Some of the other. Maybe there can be something that is wrong with, some of the configurations.
So, in this demo 6, this test is called the pipe test. So what we do is.
when we are writing the test out, we need to ensure… well, not ensure, need to test to see whether, if there are any, call them assertions, and…
If, let's say, there's a certain response that is replied over here, where there's error, where there's no such file or directory, we can do an assertion to see whether… what kind of response is being replied by the server. And
If we are able to note that, then it will give us, in fact, a much clearer picture of what errors are, in fact, are hiding behind the tester. That seems to suggest that everything is working well, but actually, there are quite a number of… actually, every one's an error here lah.
Okay, so these are the 6 different, tanks that I hope
is… I think it would be useful for… for you to understand and appreciate lah. So, actually, I spent quite a lot of time
just to, you know… I spent some time, I spent some time, to organize, some of these demos, and then to run them, and then to hopefully be able to demonstrate to you, very nicely, how these demos,
illustrate some of these things that we have been talking about in transit.
So I hope, I hope these are useful. Actually, I shared with you also very, frankly, this is the first time I include this in my class, so if there are anything that you think I can improve on, please let me know. I'll be happy to see how I can turn improve from there now.
So, the next thing that, so then after this will be part three, and then after part three, what I will also look into is that how we can…
Organize some of these.
issues that have emerged, and then, maybe, hopefully, show in a stepwise fashion how can we diagnose this concept… these errors out, and then, further on, how then to resolve them. All that will occur in, likely in our next lecture.
Thank you.

Hello, and welcome back. This is the final part of this pretty long lecture. This section talks more about the test plan. How do you really write up the test plan?
So… Let's just roll right into it.
Okay.
So the test plan is an experiment, and you usually, unless you really allow your agent to
take over your entire, or rather the bulk of your testing environment, which I doubt we are there yet at this point in time, you would still likely be running this test lab. So, because of that, whenever you run it, you
And every time you run it, you want the results or something.
To be the same, it can be bad all the time, but at least it must be consistently bad all the time. So it must be reproducible, it must be ambiguous, meaning that
Different people that read it, hopefully, they'll interpret it in the same manner.
Control. Nothing else is running.
Meaning that it's really, you're able to control the environment, it can be dedicated. In this situation, what this…
What is written here, it means that it's more of a dedicated system, where, you know, on this laptop, everything else, nothing else is running other than the test.
Validated instruments, this goes back to demo number 6, where I talked about the…
The, pipe clean… the pipe clean test, testing to see if it's the instrument itself
Correct, not recorded. So everything to be kept, just to… just to…
Just to ensure that, you know.
Then, if there's traceability that you need, or auditing that's required, at least you know where to look for the information.
The final line here says, you may want to consider running every…
Every experiment, a couple of times.
So, you know, if you run it 3, 4, 5 times, and you get consistently the same results, it really does tell you that your
Your experiment is reproducible.
So, human beings here, I think, I think they have,
They have a role here to play.
So they need to provision whatever hardware, software, also the tools.
the scripts. I think the scripts, you know, at least the AI can still help out, but…
after development, maybe a way really is to… is to run it, and then to ascertain that it's running properly. Rather than having the agent, you know, just running script after script after script, and not being analyzing it enough, you likely…
May need to review the results every single time the script is completed.
Test data, going to be holistic instrumentation, and, yeah, to deal with…
What the tests, find.
So, you know, whatever issues that may emerge from it, we may need to then carry out the steps to address those issues.
So… this…
was in line with what we said, maybe all the way in Lab number one, where we first ran the…
First vendor… the source code. After that, we ran the source code with the portfolio. We realized that
The time it took up, took,
Multiple times that of it, but really to appreciate that, you know, whatever you are measuring, it also competes with the system that is under testing.
So, on this part, I want to talk a little bit about the Duh.
the, the lab that we did with Jane Meter, I'm not sure if you remember.
So, that time when we did the lab, we did the entire lab on, most of it on our own laptop.
And then, there was one… some experiments that we did by…
by running a server of a Google Cloud,
And then, after we started to…
pinged that server, and we measured the response time from that server. Okay, so that is a more reasonable setup, where you have a client side, which is your computer, or your laptop, then you have a server side, which is something else.
Further down that, lab, we…
combine both, where your laptop serves as both the client and the server. Okay, I want to say that
That is typically not the correct book.
But we put it in the lab in this manner so that it's easier. In the past, right, B…
We had to set up.
Two separate laptops.
So one, I think, as a server, one, I think, as a client. And, you know, to set that up, right, we usually…
About more than… Well, one whole lap, just to set up.
The entire server and client interface.
And, you know, it turned out to be more like a networking exercise, networking lab, rather than performance requirement. So that's why I decided that, you know.
Doing that is…
It's a bit too painful. So instead of doing that, everything will be on the same laptop. But I… I urge you to…
I want to remind you, lah, that typically that's not the right way also. Also, your server dragons should be on different laptops, and then, yeah, then your… it should be measuring different things lah. For our lab, we did it in that manner because of our convenience. Just because of convenience, that's all.
So, the test environment must match it in structure, but not the size, meaning that it can be smaller, and typically, many times it's smaller also, because we want to test it first on a smaller environment.
to see whether is it… is it feasible on the small environment, and if it's fine, then we scale it up to a bigger, and finally… finally, to the production environment. So… so… so… so just to let you know that…
Okay, good. The size…
should be smaller, but the structure should be very similar. If not, hopefully, almost the same. So you can…
And try to reproduce how the production environment will be working at, but at a smaller scale.
So, yeah, it… There are two ways… yeah, yeah, yeah, social media. There are two ways of, of…
Dealing with the…
changing the size of your test, so you can either take… you can either do the scaling up or scaling down. I'll talk more about those two techniques, later on. And, this is the… the image on the left, right, shows you the… the…
The current system that we are talking about, which is we have a load that's coming from a single source.
This single source goes through 3 separate web servers, but all 3 separate web servers, they access the same database.
Okay, so once again, the image on the left shows you the current production environment, which is a single source, single load source coming in, and this load source is going to three separate web servers.
All three support servers, they are accessing a single database server.
Okay, so there are two, two options here, lah, four ways to change the capacity, largely two options. So, we have it scanning up or down, and then scanning in or out, okay? So, again, I would say scanning up or down, or scanning in and out.
Scaling up or down means that I do not change The number of machines.
But I make it more or less powerful.
Scaling up meaning making the machine more powerful, scaling down, meaning that making the machine less powerful, okay? So, scaling up or down, that's one. And we typically call this vertical scaling.
With Guskin.
Then the other option is what we call horizontal scaling, where we do not change the…
how powerful the machine is, but we change the number of machines up. When you say scaling out, it means that we're adding… we will add more of the similar machines. Scaling in will be removal of machines. So, in this case, if you… from pre-service, cut it down to just one.
We call it a scaling in of the machines.
So these are the two typical ways how we change, you know, change the capacity to a smaller capacity, by both scaling down and also scaling in.
So, this is… let's, take this example. So, here we have, three servers, server 1,
It's a tool.
symmetry. So remember… Our experiment earlier.
Where we have 3 servers.
No? I think so.
This, the one on the right is wrong. I thought I removed the thing, maybe, but it's still there.
So… We have two web servers.
Okay, and then now it corresponds to these three web servers here.
Okay, so each web server is the same, which has 12 CPU cores, So, if you…
If you want to reduce the amount of resources that you want to utilize for testing, option A still says that we scale it in.
Meaning that instead of 3 servers, we just use one server, okay? In this one single server, what we do is that the load that this server takes will also be the same.
So, instead of, three servers, we have one, but we still have trial calls, and the…
The request load will, in the same way, be 100 requests per second, and the amount of requests per call would still be 8.3 requests per second per call.
So, the same load per call as in the production. So, nothing… so we are really able to test, you know, how much each call is, is… is… will be undergoing, and, you know, how, how, you know… and this would be a very good estimate of how we'll be, like, in production time.
So, let's look at the… let's look at option B. Okay, if you scale down, One server.
So, let's say, in option B, what is happening is that you are first doing scanning in one server. After that, you are somewhat… not in addition to that, you are scanning down as well.
And in this situation, from 12 cores, you are going down to just 4 calls.
Okay, so the parts I read, because, like, the… the test for option B is wrong.
Being wrong because…
In the 4 cores that we are scaling it down to, you are still feeding the four calls with 100 requests per second, and that will cause each call to go up.
The request go up by 25 requests per second.
Okay, so the equivalent is not there to the actual production. So, actual production, we are only expecting 8.3 requests per second per core, but here we are scaling in, scaling down, and increasing the number of requests per core.
To 25. So by right, what needs to be done is, we need to cut down as well the number of requests to the server per second, to likely to be about 33.3 requests per second, and then once we do that, it will then correspondingly
We decreased the request per second per call down to the same as 8.3.
Which is the same as that of the… in the actual production server.
So…
So, the… one of the final slides, this is a playbook, which… which states that once a person, given the amount to scale in, scale down, you're supposed to write a step-by-step indication of how
the test should be run, and it is known as a playbook. With the playbook, somebody can…
Can take the entire thing and be able to just… just run it.
Hopefully, with little supervision or, you know, helpful.
the original person.
And…
there'll be several load generators that you'll be meeting in your career. So, we have used JMeter, I've introduced JMeter.
I, I know my… actually, my engineering, so-called team, right, they like to use, locusts, right? They say that it's easier to use, but I did not… I did not introduce, locusts
for… for this time around, yeah. So maybe the next time, we will be able to consider doing that, yeah, but there are… there are a few other such load… load… load simulators or load generators that you want to be…
familiar or aware with. I think another common one is also
Log Runner. Yeah, so Lock Runner, I've never used it, personally before.
Yeah, so, but I don't know whether we'll be able to, like, to introduce it one day at the course, yeah.
But probably, it is similar, like, the way the different load generators are, they're largely quite simple.
So…
Finally, we'll be talking about the user types. So when you use load runners, or registration, we use load animators, what we want to consider is, what are the type of load that we are generating?
So, for instance, are we generating that kind of, let's say we are… we are doing a load for… a load for a…
e-commerce sites. What kind of users are we…
generating? Are we generating, the certain percentage of users that come in to just do browsing? A certain percentage of users that come in, and they do…
How to put it? The, the, the, here to… Make up the case.
Or are they coming to just search and to compare prices between various different platforms?
So, you know, so the load model allows you to… or rather, before you do the load model, first you want to ascertain what kind of users are really coming to your website.
And then after that, to be able to decide, you know, based on
whatever data that you have gathered, how then
to segment between the kind of users that you have, and then their behavior. And knowing their behavior, will that allow you to then be able to simulate what will be the flicking time, the time between requests.
the pacing time, you know, like, how fast do they typically enter into your website? And then after that, the low profile will be, you know, do they usually come, you know, some people, during lunchtime, they may like to do browsing.
or… or, you know, some, I know.
I see no… maybe during office hours, they're also doing some purchasing or what. So it happens, it happens. Yeah, so, you know, and also, maybe after hours, there'll be a certain profile of users that come in as well. Yeah, or maybe when doing the travel time.
Before work, from 8 to 9, you know, while they're commuting, maybe they're just browsing, or…
For whatever things to… to just…
sea of things to buy, whatever. So, what is the profile… the shape of the profile of such users? And these can also be replaced into the load generators.
So…
The scripts. Actually, from all those… all these profiles, all these user types, or what? Then you come up with a script.
Now, this script is really a description of how the users behave. So, when I ask you in the lab, or maybe in the project, whereby, you know, a person comes in.
It thinks for a few seconds, and then it clicks another website. That is trying to simulate how the person is behaving within the website.
And… And, this is how we…
We ascertain whether, you know, is it able to
support a certain kind of behavior. So, remember, no functional test cases, they are really just testing if
Brother Ken.
Can a piece of software… Do we correctly or not?
But then, when it comes to performance tests, right, you are really going to see whether
Are you able to… to… Is it able to perform well every single time?
may not be the best analogy, but, you know, we always say when we go to, you know, if you go on stage to… either to speak or to perform something or whatever, we always need to practice a lot. One thing that we… we like to remind ourselves is, you know, we don't practice until we get it right.
That's not… that's the bare minimum. Don't practice until you get it right. You practice until you don't get it wrong.
Yeah, so it's similar to performance testing. So we… we test to ensure, you know.
That various things are being covered, so that we don't get things wrong.
Functional test, probably, if you ask me, is I'm testing the things out, right?
But we also want to test where things don't go wrong, yeah.
That helps. So, this… I think this is the final slide, where we link back everything to… everything together. So.
We have, was sharing earlier, we have the metrics in Lecture 2, workload, we have performance… workload estimation.
NOFA and 5, we have performance models, all your formulas, all your… all your formulas are here. Then, in this lecture, we really go into how to do the performance test, what it actually is.
I think we have one or two more lectures on performance testing, and, that will be on, on database. And, maybe, I'll see what else I can provide in.
And in the… in the final assignment, I would like to go a little bit into the diagnostics. How then do we measure, after measurement, how then do we improve?
So, I think that's the end of the lecture today, and thank you so much for bearing with me over the last few weeks, and I hope you… hope you enjoyed the short sharing, and hope you managed to learn something from this lecture. Thank you so much.
