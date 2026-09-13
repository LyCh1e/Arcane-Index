---
type: raw
source: live lecture transcript
module: INF2005 Cyber Security Fundamentals
lecturer: Dr Tan Kheng Leong
topic: Lec02 — Steganography (preceded by cryptography recap)
week: 2
format: spoken lecture, speech-recognition transcript
status: verbatim — do not edit
---

Kelesta or Lecture. Good afternoon, everyone.
All of… all of you have some fun during the lab.
Doing encrypting and decrypting.
Any of the teams, try the challenge.
I published in this, XI.
Whereby you need to decipher and then extract out contents within their ciphers.
Anyway, I tempted.
No.
Okay, that's fine. Okay, let's, recap on what we have learned last week on cryptography.
Right? So remember, there are two types of, crypto systems, especially when it involves keys. Symmetric keys…
Right? So, isymmetrix cryptography is basically, there's only one key.
So, it's used for encryption and decryption.
So, that's why it's called a private key cryptography, because there's only one single private key.
Right? Remember… What we have learned, which CRST system we use, Deaths and crippled deaths.
Right, but because it's easy to break, so they came up with the latest… nowadays we are using AES, Advanced Encryption System.
Okay? Guys, remember that the number of bits is a concern. As you increase the bids, then it's more secure. Of course, if you increase the number of beads.
The encryption and decryption time also increased.
Okay? They are typeless.
asymmetric keys, right? Asymmetric key means that they are a key pair, okay? So you have a public key.
And a private key.
Whether it's used for encryption or decryption, it can be reversed, right? Remember, we talked about how it's used, how to do it for confidentiality?
If you want to have a computer ID, you encrypt it with the other person's public key.
Right? Then the other puppy, you'll use his or her private key to decrypt.
But if you want to use for authentication.
Means that you use your private key, to encrypt
That's why we don't say, when you use a driver key, we don't say encrypt, we call sign. Okay, you're signing it because you want to
authenticate to the other person when they decrypt it.
Using your public key, that this message is usually from you.
Okay? And… The most commonly used asymmetric key cryptography is ISM.
Okay? Reverse Samuel Edmonds.
The three names of the researcher.
Right?
And then the third one, Petography, is basically hashing. So this has, there's no key. It basically just hash a message
or a content.
Right? Into a fixed length.
So you, yeah, you can hash not only just a message, but you can also hash a file.
Okay? So, what is the use of hashing the form? Anyone can tell me?
That's commonly YUE.
What's the purpose and advantage of hashing files?
Remember the CIA?
Right?
Haching is actually, you try to prove the integrity.
Okay? So where do we usually use this?
as you're downloading any applications to install, right, how to ensure that this application you're trying to install is not malware. So you notice that if you go to any download site, right, the proper one.
If you want to download, they also provide you a hash.
Hash string.
Okay, to ensure that when you download it, you want to ensure that it's,
not tamper with. You can actually hash this file, this downloaded file, and see whether the hash values matches.
Okay, if it matches, so you can be quite assured that this file is saved, it's as what is claimed by the provider.
Okay?
Right? So…
A symmetric key and symmetric key, they are… what I've taught you are basically the usually used one, but there are others. So if you take a look at this link that I provided.
Okay, there are others. Yes, the most common one, really, nowadays we are using. So, yeah, CHA, right? CHA.
Then you also have RC, right? RC5, RC6, and so forth.
Okay? So, you can see that these are still considered as secure.
Can't go fish.
Simpons…
Right? And so forth. And there are not so secure ones, right? The desks and triple deaths I mentioned, and others grow fish as well.
Okay? And now, of course, for this, asymmetric key, Right?
So… RICA is the most common one. You also have an elliptic curve.
And Diffie Human, everyone still remember Diffie Human? We use it for key exchange.
Right?
So basically, right, there are artists…
symmetric key and asymmetric key cryptography that I didn't mention, but it's good to know as well, right?
Okay, now the next question is, like, where do you can see these three cryptography being used together?
Symmetric key, asymmetric key, and hashing.
So the most commonly used one, right, which you use every day.
is your… in your browser, right? Remember the HTTP, HTTPS, okay? So let's see if we check this out, right? This is SHIP S with an S means that it has a valid
digital certificate. So what is that? So you take a look at it itself, right, and see that this connection is secured.
So you go deeper, you can see that it has a certificate, which is valid, and what is this?
Subjugate… So you can see that it's actually provided
Who is issued to, and who is the issuer, right?
And then, look at this, right? It's actually using SHA-256.
And…
green coffee, it's not stated here. Can you guys go into the… So Croity portion.
Right? Then you can see further on this, okay? So if you roll this again… We are a certificate.
Alright.
Okay, so this is not stated, it's using RSA. Okay, let's look at our…
SIT website.
Hmm?
So you can see that, okay, he also has a valid
Distance certificate, so we go inside, same thing, right? Secure connection.
Look at the certificate itself.
Okay, so here it's issued by Amazon, and using RSA2048.
Okay? And it's also using SHA-256.
Let's look at… Any other security?
also immune juice.
So you look at it.
From the security… on this… Right? So you can see from here what you notice here.
Okay, so if these are TLS.
And then also AES128.
Everyone still remember, what is this? AESS
This is a symmetric key cryptography system that's used.
Okay, so you can see that from a single browsing of any website, as long as you have a certificate, like, digital certificate.
Right? That have enabled you to send messages, like, browse securely over the channel, right? It's using not only just
Duh.
A symmetric key, but also symmetric key and hashing.
Right? So the ash is actually, yeah, forwarding through the protocol.
University is called SSL.
secure socket layer, but because it's not secured, right, because of some flaws in the blood bleed, in a sense, right, now it has been replaced by TLS.
Okay? Transport layers of priority.
Okay?
So, now the question comes, right, since you already have a symmetric key, why you still need to have
symmetric key, okay? So a symmetric key is already there, right? Why do you need to have additional or symmetric key cryptography? So, it's actually… is it duplicate?
Anyone can tell me why?
You have both of these together.
When one is good enough to do encryption and decryption.
Okay, the question… the answer is very straightforward, right? So let me ask you, right, between these,
Symmetric key and asymmetric key. When you're doing the encryption and decryption.
Which one will take a longer time?
Symmetry key or asymmetric key?
Okay, so if you, right, you have tried before, so basically, if you are using a symmetric key, the time taken will be much longer than symmetric key.
Okay? Because of using a public key and private key. So therefore, when you are doing, you know, doing a browsing.
Right? In this DSC certificate, not only is there, right, not only is there this, asymmetric key, right, the public key, right? Of course, the private key, remember, the owner needs to keep it so the server you have a copy safely kept in their, right, storage.
So that's why, if you look at
This itself, right? You can see that it's actually, look at the certificate itself, it only provides the public key.
Okay? So how this protocol works is very straightforward, right? First of all, when you browse to any server, right, any website.
Right? Your browser, you'll ask, you'll check whether he has a valid certificate.
So, if you check that it's a valid certificate, then you'll get the public key from the server.
Okay? So once, your browser receives the public key from the server, you encrypt, right? You encrypt
A session key, which is a key, right?
Using the server's, puppy key.
Right? And then send to the server. And then what do the server do?
the server, you decrypt it using its private key. So this part is actually using the asymmetric key cryptography, right?
the session key has been provided, right, secure it, right, means it's encrypted, and then the server has decrypted it and has the session key, right? And then the next, right, whenever you're doing any browsing of the website itself.
The content will be encrypted, but you'll not be encrypted
using a symmetric key, but using symmetric key, okay? Using A, yes.
And what's the key? The session key that we provided earlier.
everyone clear on this? Right? Now, of course, the hashing part is actually, again, is to ensure integrity, and also for digital signature.
Everyone clear on this?
So you can see that, right, the three choreography in action.
Just when you are doing browsing using HTTPS.
Okay? Right.
Okay, that's about a recap. So, the three important points for you.
tweeted coffee systems.
Okay, let's look at our class schedules. Now we are in week 2, so next topic I'm going to cover will be STEM photography, right? And also later, I'm going to brief you on your ACW1.
Okay, so after a briefing of the ACW1, right, which you're going to demo in week 5, the next three lab sessions will be for you to work on ACW1.
So there will not be any lap.
right, tutorials for you to call them, but basically you work in your team, right? So you can go to the lab.
Venue as a project work, or it can work anywhere you wish. And if you have any questions to ask, right, you can arrange for a consultation.
Okay.
Right?
So, let me talk about this, stenography. First of all, ask you to look for someone, right? This WAI is missing, right? So, where is he?
Here.
Anyone can find you?
Okay? Of course, if you keep browsing, stuff from top to bottom, scan, scan, scan, scan, scan, scan, scan, eventually you can find him, right? So he's just right over here.
Right?
So… Because it's so crowded, right, in a way, it's hidden from sight.
So, basically, it's hiding in plain sight, right? If you don't…
scan it properly, right? So you can actually miss your eye… your sight, right? So, ultimately, this is, stemography is to basically to be unnoticed or inconspicuous.
Right? By staying visible, but at the same time, you mask your presence, right? You're somewhere there, but somehow no one noticed your presence, right? So it can also be your…
Camouflaging, right?
Yan blend into the environment. That's why you are, in a way, if someone wants to look for you, you can be visible, but if no one, right, just casually look around, you actually don't notice your presence.
Okay? And so this is what standography is, the practice of concealing messages or information within text or multimedia.
Yep.
Right? So another type of, in the olden days, I…
Instead of a standard Raffi, right?
The way they hide text is into a… text into a text is basically something they call as a… as caustics.
Ascotic is simply just like a poem, but in the poem itself, there's a hidden message, or hidden words.
Right? So, in this, through the Looking Grass novel, published in 1871, right, see how old it is, right, the final chapter has a poem, right? A book Beneath a Sunny Sky. It's actually an acoustic
Right? Which actually lists down the real name of the author, at least. Right? So if you look, I have time to look into this book itself, and see that
the whole, right, the start of the poem, starting with A, L, I, C, E, right, and then follow through. Actually, the whole poem itself, the first letter itself, can form up the at least, right, the author's full name.
Hmm?
So, of course, it's one way of doing it, right? There are other ways also, right? Some also use… using a text, they have a stencer, right? The stencils, whereby you can form out, right, which words, which letters, join in which letters, right? And then you can form out the words itself.
So there is this such a stencil subjector, which is used during the war, right?
of equipping and encrypting works itself.
Right?
So now the question is, is there an inference for what we will learn cryptography?
So what's the difference between standography and cryptography?
So, you can see from here, right.
As far as telegraphic goes, right, if you have provided this message, you wouldn't know whether it's there a hidden message.
Right?
Even during thorough analysis, you may not find
Right? But for cryptography, you can see that Right?
It's actually some message.
Some Jubberish Mahesh itself.
So, when you're provided this, you can actually be quite sure that actually this can actually be converted into a message, can be decrypted, because it's a gibberish. So, why would anyone send a gibberish message, right? So, it must be a cipher, right? Okay? So, simple to say, right? We talked about
Ellis and Bob communicating, right? Remember, we have an EV that is always used dropping, right? Men in the middle.
So, Eve… Ellie send them an image to Bob, and Eve received it.
When you look at this message, you think that, okay, this is just a normal image, nothing to be concerned about, right?
Even though there may be a message hidden inside.
Right?
But if, right, ELLI sends this cipher over to BOC, and…
EV intercepted it. So, if you look… if you look at this itself, definitely you'll know, right? This must represent a certain message, but somehow, Eve cannot decipher it.
Okay?
Okay, so of course, right, this is cryptography, and also hiding a message. The print text
Right? The best one, of course, need to be hidden.
Right? So… In a synergraphy, right, the message cannot be easily deducted.
And slim border radiography, right?
He shouldn't be able to break his rebook it to… Review the print text.
Okay, let's talk about process, right? So, of course, process is always your payload, which is something you want to hide.
And then the cover object. Together, right, the payload is embedded into the cover object, and then you produce YU a SHANON
Sago object, right? Which looks exactly, okay.
Exactly, okay, exactly the same as your cover object.
Okay? And your payload, okay, can be any mesh, any text, Image, or even other multimedia.
Your cover object as well, right, can be image, video, audio, or even text itself.
Okay?
So, payload is the one you want to hide, and your cover objects, like any media.
And the resulting one will be exactly the same as your cover object.
Okay? With the payload hidden.
So the concept of a standography is actually going by this security, by obscurity.
remember why I talked about this briefly last week, right? We are trying to Hide something, right?
By not reviewing how you hide it, or where you hide it.
Okay? So this is… remember, this is, right?
Actually, you are trying to hide something, maybe your money, somewhere in your house, right? Hopefully, hoping that no one will know, right, where you hide it, or how you're going to hide it itself, but you can only share it with someone you trust.
Who can actually retrieve for you?
Yeah?
So it's safe for stenography, right? You are provided an image, right? So you… you are the one, you are going to hide the image, so you are the one who knows how it's hidden, which part of it is hidden, and how much of the content is there.
Right? The start and end.
Because only you know. So since you know, right, you want to provide this message to someone else, you have to tell this information to the other person. Okay, this is hidden in which pieces, right? And then starting from which pieces to which pieces, and you extract out.
Okay? So the best, of course, if you are… Yes,
Just a small amount has been hidden.
Usually, you will not notice any difference, right? So if you look at these two, right? Can anyone see any subtle change?
Not really, right? Okay? But as you embed more, right, if you embed more message into the cover object, you'll notice, right, somehow you'll notice some difference.
Right? Everyone can see. Actually, you can see from here, there's some… there's some changes here, right?
Alright? So now this, the message is 50% heat in.
Right? So… 50% of the… Image has been used for hiding the message itself.
Okay?
So… How do we do it?
So now we're going to talk about the algorithm.
So, we are going to talk about the most common way of doing it.
Right? I think most of you also have thought of this, the LIS Seneca Bids Algorithm.
We know that in images, right, it's a colorful images, it's basically consisting of RGB channels.
Okay? So each of the channels, right, is actually 1 byte, and 1 byte is actually 8 bits.
Okay, so you have a red, green, and blue.
Right? So in bits itself, right, we arrange them in the most significant bits to the least significant bits.
Okay? So if you say that most maker means it's important, right? List makeance means that, right, if somehow you change it, it may or may not be a bit concerned.
Okay? So that's why this algorithm is trying to use these significant bits as…
The way to hide your payload itself.
So, if you look at this example, Self?
we are given a payload, okay? So, you know, I have to say, right, how we get into MANA. So, actually, you need a lot of conversion, right? So, image, right?
Mr.
see that it's, H is 8 bytes, and 8 bytes can change convert to bits itself.
Okay? So this can be image, but text also, similarly, ASCII can convert to binary as well, okay? And then you just need to replace each of these bits, starting from the most certain bits of the payload, and replace it with
Each of the lists, it could be of each of the pixels.
Okay? So actually, you're embedding, right, each of the bits Something for most certain bits, Of the payload into…
The lists and income bits of each pixels.
Okay, so each pixels, the list completes will be replaced.
Right?
Okay?
So that's why you can see from here, right, basically why you are doing the listing a bit is because the changes will be quite unnoticeable itself.
Okay, so if the payload is too large, of course, you go to the next
Listen, you don't be suss.
Okay? So, of course, you have to traverse through your RGB first, and then really have no more listen bits, then you go to the next one.
Okay?
Of course, now you think about it, right? As you go Right?
Nearer and nearer to the most screen beats, there'll always be a concern, right? Your measure will become more and more detectable, okay? So, there's always a balance between, right, what is the payload size and your cover object size.
Okay?
Right?
Okay, so there are two ways to our LIP algorithms.
Right?
One is using LISP replacement, and the other is LISP matching.
So, but one constraint about images is this LISP only works on lossless… lossless compression images, right? As you all know, right, when you compress any files, or even images.
Huh?
the ZIP, right, applications is always trying to optimize, right, optimize the file size. So sometimes they may omit certain bits itself, so they can save on the size. So if, right, if the
compressions, the algorithm is such that it's going to remove some bits, right, then this LISP substitution, right, replacement algorithm will not work. So therefore, one constraint is the LISP
algorithms only work on lossless compression images, which means that whether you compress or not compress, the bits itself will still be retained, right? There will not be any change or any data loss or modified during compression or non-compressions.
Okay? That's all these, PNG, TIFF, and…
VPM, like, the VMA itself, are examples that when we can use LSV and void them.
Okay?
So now, let's talk about these two algorithms, LIP replacement and LIP matching.
Okay, so LSP replacement, right, as the word replacement goes, right, basically, you just replace
the LIP bits with the payable bits. So let's say I'm trying to embed this G, right? G, right? From ASCII, I convert it to binary into this original data, which is the cover object.
Right? So first, right, I start from the most important bit of the payload, it is 0, so I replace it with, right.
each of the pixels. So each of these, right, are pixels in the image.
Example, okay? Example, this original data is image.
Okay, so I just replace it, 0, right, this is 0, and a 1, I just, right, no change, right, so we gain.
and 0, right, change to 0, and so forth. Okay, so you'll notice that
Some bits, some… these semicond bits are changed, some are not.
Right? Because some are the same as the payload, so it don't change.
So, in general, right, about average over 50% of the cover image pixels are changed.
Right? Because, yeah, some change, some doesn't change, right?
Any questions so far?
clear on about this, replacement, avoid them.
Andrew?
Quite straightforward, right? Okay, now we talk about the matching.
So matching is about… it's also the same thing, right? It's still about LSV, but then, okay, so that is actually deciding whether to plus or minus if the Bs are different.
Okay, so let's say this is a cover object, right?
So you have, different pixels, right? So you have 2, 4, 6, 8 pixels, and I'm trying to embed this character A into this cover object.
Okay, so what this does is, this matching does is, if, right, if the bits are the same, right, you just leave it at ease, don't do anything. If the bits are different, right.
You'd either do a plus one or minus 1, remnantly.
Okay? Doesn't matter where PRESS1 or minus 1, right?
So… What does this mean?
So, you can see from here, right? For example.
60, right? So there's 0, and you want to replace it with 1. So.
is different, right? Payload and payload and the cover object bits are different, okay? So you can decide whether it's plus 1 or minus 1.
So what's the effect?
Right? From 0, right, you want to change to 1, correct? Because they're different.
So either you plus 1 or minus 1, definitely you will be changed to 1.
Everyone still remember how you do binary addition and subtraction, right? Zero, right? Whether you're plus 1 or minus 1.
You'll still get BAC 1.
Correct.
Okay? So therefore, we have a choice of plus 1 or minus 1.
Eventually, your payload will still be embedded with a 1 as the least significant bit.
Everyone followed so far?
Okay, same for if it's 1, right? 1 to be… your payload is 0, right? So they are different. So you can do a plus one and minus 1. So 1 plus 1 or minus 1, you'll still get back your
This one can be as 0.
Right?
So it doesn't matter whether plus 1 or minus 1.
But notice from here, right? So let's take for this example, the 44.
Right? So, the payload is 0, and the least bit of this pixel is 1, right? So, if you do a plus 1, you can see that a few bits has been changed.
Compared to the rest, right? Compared to the rest, it's actually one big change.
Right? So actually, what do you think is the benefit about doing this matching?
Android, compared to the basement.
So the idea about this matching, right, is actually to create certain confusion, in a sense, right? So that the algorithm or the hidden message is harder to be analyzed, right? To be predicted to have a hidden message, right? Because you're doing a PRESS1-1 randomly, right?
So you're actually in… in a way, creating certain confusion, right? And then some of the bits change, right? And some bits… one bit change only, and some multiple bits have changed, right? So you're actually creating confusion, is there a pattern? Or, actually, there's no pattern.
Right? To someone, we're trying to analyze it.
Okay?
Cushions?
On this matching algorithm, Everyone fine?
Okay.
Let's talk about the…
briefly about the coding, okay? I'm sure all of you are very good in the coding, so even you get a chat GPT or GenAI to write it, you'll write something similar. So idea is still the same. You're using Python, right? You'll be using these computer vision libraries and NumPy for the mathematical
Multipations, aromatics, calculations.
Right? Simple as that, right? Of course, like I mentioned, right, all your data need to convert to binary. So this part is actually converting all your sort of datas to binary, whether it's a string, a byte, or integer, and other types you can do, right? You can never support.
Okay? And then the encoding part, remember how… what we talked about encoding is basically we try to encode, right, the…
the bits, the payload bits, into these technical bits of the cover objects, okay? Therefore, you can see from here, right.
Why is this, right? This pie is the one that is…
Right? You're zooming in to the LSB, right? This zoom this.
Okay?
So you're actually doing it from the right-hand side, the LSMBs, and then adding it on. Then you have RGB channels, right, for each of them, and you'll keep adding the data index accordingly as you keep changing, keep replacing your bits, your Listen bits itself.
Okay?
And then next, how you decode, right?
So, we are doing encoding, means that we are trying to replace, like, the bits inside. So, we are trying to embed our… your payload into the cover objects by encoding these bits into the cover objects.
bits of the payload into the cover objects. So we do the reverse is to decode, right? We need to extract out the bits from the SHANON objects.
And then format the… message?
Okay? So, basically, you are actually extracting out each of the pieces.
Right? The least single bits from here.
Right? And then, since you assume that it's going to be, certain characters itself, right, informing into 8 bits.
Right? To become a character.
Okay?
And now the question here is, like, what is the purpose of this?
Yeah, it's, HOI quo.
Why do we have this? Anyone can tell me?
No one right, Tim?
Very simple.
Very simple. If you…
Yes, and, right? So if you imagine that you're going to embed your message, right, your message most likely is going to be smaller than your cover object.
Right? Are you going to retrieve out every bit yourself? Right?
Not really, right? That is not very efficient, right? It's going to be… the performance will be key, especially if you have very large cover objects, right? So therefore, in your, right, in your embedding itself, right, definitely you need to embed certain
Terminator, right? The one, right, most commonly called terminator string, right? Or terminator characters.
to let your program know, right, if I keep something like this, I know that I've accepted all your… all the business itself sufficient for me to…
revert it into a message itself. I do not have to continue anymore.
Okay? Right? So, how, what you want to use is up to you.
Right? So this is just an example of just using 4 equals. You can use something much more efficient, right? Maybe just one or two characters.
Okay? But of course, when you want to choose your characters, be aware of, right, commonly used characters.
Okay, this is for matching, right? Remember the matching itself, basically, the important part is actually randomly decide whether to plus or minus.
Right? So the rest of the flow is actually the same. So this is the part whereby it's doing the random selection here.
Right?
And what is this, right? Equals to 0 and 255.
So, since you are going to do plus 1 or minus 1, you also need to check the extreme, right? If you say to the zero, you cannot do minus, right? It's best not to do minus. Imagine if you do a minus, right? A lot of bits will be changed.
then you're actually creating more obvious, right, sign to the observer that certain has been changed, right? Same for 255. Once you have a 255, right, of course you do a minus 1.
Okay?
Right? If not, then you can decide according to this side as when we selected.
Kit.
And the extraction, right, or the decoding, right, is the same. We just pick up from the… now there's no difference, let's pick up the last least significant bits, and then form it into a character.
Okay?
Alright, so let me show you a very simple program, right, which is doing this.
Right, it's a very quick stangle program.
Okay, so let me clear everything yellow.
Yeah, I'm going to open up the image.
Okay, so this original image… Right?
So, you know, I get X…
Right? There's nothing, right? So he'll tell you there's nothing.
Because the program knows how to do it, right? Okay? So I clearly…
Okay, so now I'm going to, add a secret message inside.
Hi, please. Christine.
Okay, now I'm going to hide the message.
Okay, and I'm gonna save this message.
surface image, okay? Let me save this into this, small.
Okay, this is what it is, right?
Okay, so I'm gonna clear this…
Okay, so I'm going to do a BAC again, right? So I'm going to open up the original one first, just to make sure that, right, it's there.
Okay, so there's nothing. So now I'm going to open up the one that I've hidden some message.
Okay, so I can see that it's… Mahesh is there.
Okay? So it's just a very simple application, right? Hi.
Right? And show it.
Right? In… later in your HEW one, you're going to do more complicated one.
Okay? And how to analyze this? Just to analyze, whether which… what algorithm are they using? Okay? So let me, show you…
A tool, right? Which also, some of you may have used this in your lab.
Called HEXA Editor.
Alright, so now I'm going to compare. I'm going to do analysis, right? And then compare these two images that I have, created. Original, alright?
Bond beef, staggom, right?
Okay?
So before I do this, I want to show you this, like, the file size.
Notice the fall size, the 2.
Yeah, the same.
Right?
Should be, right? Right? Most of the time, it should be, right? Unless something… certain header file or metadata has been changed, right? If not, it should be a change… should be the same, because you are just changing a bit, right? The B is originally there, so you're just doing a replacement, so the size capacity is already there, right?
Okay, so now I'm going to compare this.
Alright, so you can, so you can see, right, right, what has been changed. So I can just do an analysis.
Let me do a F6, okay? So I do a F6, and I can see all the…
Right? You can see… All the differences.
So what?
Right? See all the differences. You can see EEEF, right? Only one big change.
Right? E-E-E-F.
Right?
Okay? Then EAE9.
Right? So this is basically just to show that it's actually the last bit that's been changed, one bit only.
Okay?
Huh?
Hey, there's a question, will the hash of the file be different?
Okay, of course you'll be different, right? Because the BINT has changed.
Right? The size will remain the same, but when you hash it… remember hashing? Right? The best hashing of RIDM is that even you have a slight change, even one bit of change, your output will look totally different.
Okay? So that's the best… best hash algorithm.
Right? That is a… right? This is to prevent people doing reverse engineering.
Right?
YUAN clear about this?
As long as content has changed, The hashing will definitely change.
H?
Hey, since I've introduced you to DANISH, Alright.
now is to tell you about your ACW.
1, okay? So, if you look at the… Let's go to…
XI, okay?
Publish this… Hey, let me pop a ship now…
But I don't see it.
Okay? So, y'all… ACW1, it was basically, you'll be… you'll be…
writing, right? You'll be developing this stenography.
program, right? A GUI-based LSV replacement stemographic program. It can be window-based or web-based, okay? Some of you can use this,
like, JavaScripts, right?
Notes?
Or even window base, right, like what I showed you just now, just not what I showed you, the simple one is window base.
Okay? So we're going to demonstrate how you do it for image and audio.
Okay? Video is optional, right? You can take it as an innovation, right? Yes, especially if you're trying to embed it into the frame or the audio of the video.
Okay?
So…
optimally, right, you're going to develop starting from this week onwards until week 5, when you're going to have your own evaluation, okay? So plan for your demo to be not more than 25 minutes, with all members involved.
Okay? So I provided a demo plan for you to plan out, okay? And most importantly, it's a team effort. Everyone must contribute and sign this declaration of ONGE form together with your work distribution and contribution.
Okay? So, briefly about this, what are the scope?
Okay? So optimally, It's going to combine what we have learned last week and this week itself.
Okay? So, not only JUSTING Raffi, but also checking integrity, right? And also, you're going to have involving digital signature as well.
Okay?
Right? To ensure the authenticity of the… Receiver or senders?
Okay?
Alright, so I'll leave it to you to go through this.
Alright.
And essentially, I've given you some guide for you to… what to show.
Right? So, important thing is also you need to do a capacity check. Remember just now, right? If the payload is larger than the cover objects, what should you do?
Right? And also, you want to simulate, right, this stagger object being sent from one party to another party, and how you do it safely.
Okay? So this is actually putting what you have learned this week And last week, together, alright?
And this part, selectable, right? Selectable payload sub-location, right? So I'm going to… right? So this will be very flexible. Later, I will talk about certain
the content about why this is good itself, right?
You're able to select where to put your payload.
And of course, your innovation, right? If you have something innovation, there are certain marks for you as well.
Okay, right, so we have been to all the software engineering courses, so these are function requirements.
Right? Okay, so I'll give you some example of an optional challenge.
And a submission, right? Okay?
The source code, you'll be… Uploaded after your demo.
Okay, but before your demo, make sure you have provided your demo plan, declaration opportunities, and your contribution and distribution statement itself.
Okay? Alright, so one thing I want to emphasize is this contribution and distribution statement has to be also be signed.
So, everyone needs to be agreed on, right?
On who has contributed what.
Right? I think all of you will come to common consensus.
Right?
I hope, right, everyone is clear, right?
Responsible for certain things, and everyone, every team members recognize it.
Right? Pros and cons, okay? Those who have not contributed, I think other members will eventually, right, will enter certain things, right? Still, again, everyone needs to be agreed upon.
All the distributions.
Right, this is the rubrics, right, take a look.
I probably have a clearer version, right? If it's… if you have any doubts on this, right, I'll provide you a clearer version of this. But I think, optimally, right, if you meet all the objectives that I mentioned, right, actually, it's all
Super moment by Eagle Indexed.
Marking guides for you to see which range are you in.
Git?
So, use of JEN AI, right? I'm not discussing you to use JAI, right? In fact, I'm encouraging you to use it, right? But make sure when you generate the code, you understand the code as well, because you will be asked to explain.
Yeah, okay? Right? So…
Anything that you want to use for JEN AI, you can use it, right? But make sure you give this
credits to your JEI whenever you have used it.
Okay?
Questions?
Hmm?
No?
Okay? So you don't have, right?
We will take a 5-minute break before I continue the second part.
So now the time is… 2.48, so you'll come back at 253 primary spec.
Okay, let's continue.
Okay? Everyone back from a water break or toilet break?
Okay, so next, I'm going to talk about this, BID planes.
Okay, so you can see that we are still using the RGB channels.
Right? But I'm sure that you also have noticed about her, grayscale. Grayscale images.
So when grayscale images are used, actually, they resulted in high accuracy in the classifications. Because remember, right.
If you are putting into great skills.
They need to be very clear, right, in the contrasting.
when you use RGB, of course, the colors will make a very good contrast, but when it's in gray, right, black, gray, or white itself, right, the contrast has to be better, right? Therefore, grayscale images actually provide better, higher accuracies of qualifications than these RGB images.
Okay? So therefore, if you embed, right, if you embed hidden messages into Grayscale, sometimes it's easier to detect.
Okay? Because gratitude bid, play, and sell right store intensity.
Okay?
But…
Nevertheless, right, you also want to learn about how you can use the big plane as one of options to embed
hidden messages, okay? So what is big planes? So, if you look at this itself, right.
each of the channels, okay, each of the… all the RGB channels itself, right? Each of the pixels itself, right? Each of the pixels is actually 8 bytes.
Alright? So if I just look at this itself, right, each of the pieces, for example, green itself, right, each of the pieces are 8 bytes on green, right? So if I just basically focus on certain bits.
of tech.
channel, right? I can also do some embedding into that The self.
Which is quite splint.
Okay, so what do I mean itself? So you have an RGB, right? So each of these has a…
8 bits, right? Each of the channels have 8 bits. So if I say the zero blue be bits plane is all the LIP of the blue bikes in the image, okay? So you need to do some imagination, okay? So look at this blue itself, right?
Okay?
So, all the pixel itself.
Let's not talk about the RGB yet, let's focus just on the blue itself, right? So blue, if you just look at the image, it's just totally blue, right? Each of these images itself, I actually…
Having every pixels. And every pixels itself has 8 bits.
Alright.
Okay?
So, this is the whole image, right? The dimension, and this will be… for example, the image is…
Let's say for 100x100, right? 100 by 100 means that it's going to be 100 times 100 pixels.
Right? With 10,000 pixels.
So, if I just look at each of the pixels, only look…
Grouping them, right, taking out all the bits in one single bit only.
Right? So you're taking out one single beast only, right?
Means that each of these itself is just…
Either the least service, or the most service itself.
Okay? So I can just gather, right, the list, second bits of all the pixels, okay? So, in a way, I remember this is just one single pixel. Okay, let me show you this. So, one single pixel itself, right? So if I gather all the list bits of all the pixels of this image.
Right?
And then displayed will look something like this.
Everyone can imagine. So, this image is formed using all the
Listen bits, right, the last bit, the rightmost bits of all the pixels in the red channel.
Right?
So you can see that in a way, right? So as it progresses, right, moving forward to the most grits, you can see that the image becomes clearer and clearer.
Right? When you are in the least significant beast itself, there are a lot of noises.
Okay?
Right?
So, everyone can see the simulations now.
Right? As you move to the most income base, much clearer, okay?
the controls, the contrast, right, starts to show. But here, very noisy, right? So if you look into the grayscale format itself, same thing also.
Alright?
These single bits, as she progresses, you can see that the images.
Something to form.
Into the actual image itself.
Okay.
Right? So what is, like, what is… we intend to do, right? In that example, this orange, you know, color image, we put into grayscale, right? So as it progresses from first, second, third.
Alright, progressively going to hit and see that it's actually showing clearer.
Right? In the most memorized plane.
Hmm?
So this is just an introductory, right, for me to introduce you to another algorithm called this big plain complexity segmentation algorithm.
Okay, so what is this algorithm about?
Okay, so again, this is what I've introduced you earlier, right? So I'm going to split this image into different bits of planes.
Okay? So this is actually just single one color.
Okay? So, for example, red color.
And then… I'm going to divide them into complex or non-complex region.
So how do I… what do I… how do you classify as complex or non-complex regions?
Right? So you can see that this is, alright, for example, these are all white.
Right? WWWWW, right? And this is checkered, right? White, black, white, black, white, black. So look at this cell, right?
So it is, right?
Both pieces white, and this is checkered.
Right? For example, if I pick up any of the segments from here, any region from here is put this way. So to you, right, which is considered as complex?
The left or the right?
So, obviously, it's the right, right? Because you have a…
alternates, right? So, imagine if you embed your payload inside.
Probably can hide better than a purely white or pairing back itself.
Okay? So I'm just showing it to extreme, okay? So this is what is meant by complex or non-complex regions.
So, needless to say, we embed our payload into the complex region.
Alright, hopefully without image deteriorations.
Okay.
Right?
So…
If you understand that, then the algorithm always goes this way, right? Similar to what I explained just now, right? You're still, again, replacing bits itself, so you're going to get… but this time you're using big plane itself. So you're going to get through… go through all the big planes, right? All your…
per second, third, okay? And then, while you have more spaces in the column big brain for you to embed your payload, you're going to get the next compact segment.
Okay, only embed using the complex segment, and then get your payload.
And then embed your payload into the complex segments.
Okay?
And if… if your payload is not, right, if your payload is not complex enough, right, remember the else is if it's complex, L's not complex, you conjugate it with, metrics, for example, this, to make it complex.
And hide it again into the current complex segments.
Everyone follow so far?
So…
Bottom line is, you're actually embedding your payload into the complex seminars. So you keep… if you have more payloads to embed, then you go to all the big planes, look for complex seminars, and then embed it.
Right?
So, of course, when you reverse it, you have to remember, okay, so that's complexity about this algorithm. You have to remember where have you embedded this complex sentence, so it can do, right, a reverse engineering.
On top of that, you also must know which part of the payload you have conjugated.
Again, very complicated process, right? So if you're forward, and when you're doing embedding, it's very complex, your reverse also will be similar. Plus, you need to remember how you do it.
Right?
Again, back to the principalities, it's actually, again, secrecy, right, secret by obscurity.
Right? You must know how the way to do it, which is algorithmic in a sense, right? Algorithmic in a sense. The steps to do it, how you do it, and then what you want to…
You code it, or extract it, you have to do the reverse, same way of doing it.
Okay?
They took an example, right, look at this exhibition hall.
So, obviously, this is HP logo, right? This HP sign itself, or screen itself, is considered non-complex. It's as good as white color, right? Okay, so wherever you embedd, right, if you zoom in, probably you can detect something.
And this, right, this is very good, right, because it's lighting, and we…
As a human, we don't know whether the shape is right or wrong.
Alright? So it's very good to embed it.
Right? But in front of this, right, well, it may seem like this can be complex, but if you embed it.
And you zoom in, sometimes it can also detect certain, right, certain…
and normality, because we know how a face looks like. So if it's a high resolution, if you embed something inside here, someone, like, zooming into this may detect something, right? Maybe this face itself, right? How come it's distorted somehow?
Right? Or missing one, or hair, or whatever, or certain parts of the, yeah, of the facial, or the body itself, right?
Okay? So…
whether it's complex or not, right, it depends. But, of course, we won't be able to, all the time, go to analyze the whole image and then decide where it is. So there's a better way to do that, in the sense that, okay, to how to find this,
How to find these noisy regions?
Right?
So this is the… how we do that. Basically, we do some calculation, right, some estimation.
Okay, so we are going to change, right, you're going to calculate a segment change value.
So, assuming that there are A bugs in segments, okay? So, A bugs are A bits, right? Okay? So…
can see that how these 8 bits change, right, can be alternate, right, to make it complex. Of course, not overall 111 or all 00, right? We are looking for complex. So, maximum value of, this, right.
For more complexity, you do an alternate, right? Essentially 7.
So, if you do this for each of the eight bikes, Okay?
So we have 8 bytes, right? Apex and segments. So, total, right, you have a total of, 7 changes.
Right? So you can see from here, right?
And invites in the segments.
Okay? So each of these can change, alternate, right?
So it can be 7 times alternate change.
Right?
Then, you also need to consider, right.
Whether it's this horizontal variation, or
Vertical variations. Therefore, it comes true to it.
Okay? So, therefore, there are a total of 112.
Variations, number of changes you can have.
For all these bits itself.
In a segment.
Okay? So this is the worst, worst, worst case, right? Most complex, okay? So you want to decide whether you want to decide on which is considered as complex segments, you can use, sort of, like, a threshold.
Right? So if, your complexity calculation, right, this calculation itself is greater than a certain threshold, then you consider it as complex.
Okay?
So, typically, it's about 0.3.
Everyone follow this?
Right? So this is a gauge in a program, right? When you're analyzing an image itself, you want to identify all the complex segments, right? Of course, you don't visually do it, use your program, right?
get invites… Right? Each of the segment itself, and then calculate the…
Change variations, right, delete change variations, and then compare it to a threshold and see whether this is… meet the complex segments criteria that you want.
Okay.
Okay, next, talk about standard analysis.
Okay?
Right?
So, basically, again, right, this is, same as CTON analysis. In CRTO analysis, we are trying to, right, detect how to reverse it, how to decipher a ciphertext spec.
So, same thing for stack GAN analysis. We are trying to discover whether there's a hidden objects, hidden messages inside an object, right? Hopefully, it's a stacked object, and then you can detect it.
And then use certain analysis… second analysis methods to try to extract out the message itself.
Okay? So you can actually separate them, the payload and the…
Cover objects separately, and then you can read into the payload itself.
Okay?
So, basically, right, that's the objective.
But it's easier said than done, right? As you can see, right, when you're given an image itself, it's not easy to detect.
Whether that's a human message. One way of detecting, of course, right, if you change the one, these circumstances, right, sometimes the image becomes not so smooth.
So, therefore, there are some certain filters, for example, it's back and white filters, right? It can be applied into the…
object itself, right? A single object, and hopefully it will give you some visible result. For example, this. That would be quite ideal, right? If you apply a filter to an object, you actually show the result in this, so you can actually be able to
Right?
I have a first card, say, okay, Bobby, there's some message hidden inside here.
Okay?
Right? But most of the way of detecting it, of course, we want to have an original image, and then compare to the…
Suspected one.
All right.
Then you can detect it, for example, seeing what's a color change using any of these color change. For example, this cell.
Right.
go into RGB, then detect whether any changes inside, so…
Right? Or we can do a difference.
Before and after, and see whether it totally go into a
white color or black color. If it's not, it's other colors, needs to say that it's actually tattoo. Doesn't…
Subtract to zero.
Right? It means that SHANTEMBs has been changed.
Then you can say that all of this has… this is actually, right, has been templated with. There's probably something inside these stagger objects itself.
Okay? So on its own, if we were just a staggered image itself, right, it's quite difficult.
Right? That's why Research has also come up with certain algorithms, right? For example, this statistic
train using these histograms that they seek to analyze, right? So, initially, when you're doing their preliminary
analyzing, right? You'll see that, okay, before and after, you can see a spike.
In a histogram.
So probably that can give them a hint. If you are given a standard object, and do this, histogram analysis, right, getting the statistic of it, if there are certain spikes, maybe that is a preliminary, right?
Right? Si that, Bobby, there's certain things hidden inside.
Right? Same order, right?
images itself, right? For example, it's color images itself. You can do it for all the colors.
Right? But ultimately, I can see that even before and after.
Before, there's already some spikes, right? And after, the spikes goes higher.
Right?
So… Without the stagger object, if you are given this, alright.
There's actually no way of telling, right? If you're only just given one.
one of the object, stable object, or the cover object, right? Spike doesn't mean, in a way, right, sometimes doesn't mean anything.
Okay? So therefore, some of the researchers also come up with their own algorithm. So these are just some of the techniques.
Right? I'm not going to go into, because it's going to be a very…
CHIM, right? Very deep mathematics way of doing it, but you can see that none are very, right.
Good.
Either they are computational heavy, right, or they are more sensitive.
Or they, have, more false positives.
Okay? Means that you detect it wrongly, which has become a waste of effort itself.
Right, when you see, okay, this maybe is, but actually it's not.
Okay?
Right? So, next…
Why is it applied? So, I've just changed upon this article, so I think it's good for you to read. It actually happens. People still use kong Raffi for
espionage kind of, behavior, right? So this is, one example of, the…
person, like, spying for China in America.
Okay, so this person is interested. So, more interesting is how he did it, right?
So, if you look at this itself.
Look at the articles I've provided. Page 6 is where it mentioned about the… how he did it.
Hang?
Okay?
can see that it's actually not using LSV.
So what it does is, right, you actually use an image called DONGPEG, right, and then… Basically, he…
convert it into binary. It lists out all the binaries, which lists the binary codes for this image itself.
Okay? And then… Type 88.
At the end of this MARK course, And then next E, right?
and bid… The payload, okay, which is this itself.
Into this, after this binary code itself, or this image itself.
Okay? Then after it's done, you just end with 88. So, needless to say, right, this is just to indicate the start and the end of the payload itself.
Okay, so why… how… how does this work? So, even, right, anyone looking at this, so how does this work is, in images, right, images, most of the time, the image header, you define what is the image size.
A was image capacity, and then sometimes they also have a terminator in the image to indicate that this is end of the data.
Okay? So what this person does is actually… is actually embedding the payload after the terminator data.
Okay? So therefore, when anyone, like, maybe the security or IT team are trying to look into this image, is still able to view it, because ultimately the header is still correct, it's still able to extract from the start to the terminator of the image.
Right? And then it's played onto the… any of the editors, right, or the viewers.
Okay? And then the rest of the content is still there.
Alright? Okay? So he's still able to do that, but of course, if you think about it, right.
If you are the…
You're trying to do an analysis of this image itself, it's easy for you to detect.
How can you detect? First of all, it's what?
The file size we have CH.
Right? So, if you are very alert itself, right, you look at this image itself, the image is only, maybe 1024 by 1034, right? Why is the size so large? Because you can multiply, right? If you do a rough estimation, right, if the size doesn't quite right, right, it also gives you an alert.
Right? And of course, if you look into the file itself, of course, you discover more.
Okay?
So that's why you can see that LSV itself, right, is even… is effective.
It's more effective than doing this way, right? This person probably doesn't know about LSP, right?
Okay? Alright, so, this is just an example of, Just to show, right?
Setting… TING still is, woeful.
trying, right? When you tend to do it.
Okay, so that's about what I want to talk about in Standard Wealth Feed.
Okay?
So, I think I'll leave it to you to go through this.
So, the next step here will be assessed control.
And, the subsequent lab…
In week 2, 3, and 4, book on your ACW1. You have questions, come look for me, right, or email me, or arrange a consultation.
If you have, any questions to ask, or anything about your groupings, or ACW1, right, you can still stay behind and ask me, right? So…
If not, right? So, that's it for today. I will end early, just for you to have
Or maybe some discussion on ACW1.
Okay? Thank you, everyone. See you next week.
Mine?
