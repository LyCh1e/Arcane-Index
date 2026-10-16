# Human Aspects of Security: Phishing, Pharming & Social Engineering

*Cyber Security Fundamentals — Dr Peter Loh*

## 1. Introduction: People as the Weak Link

- "It's completely secure.." — a claim often heard about systems with strong technical protections.
- The problem arises **when users are added** to the system.
- Users are seen as the **"weak link"**: why attack a system with good technical security when you can get in through the user?
- Recommended reading referenced: Kevin Mitnick, *The Art of Deception*.

---

## 2. Phishing

**Definition:** an attempt to extract credentials by pretending to be a legitimate organisation or individual.

### What attackers want
- Usernames and passwords
- Banking account numbers
- Credit card information
- Access to / control of systems (IT and OT networks)

### Lessons from the Examples

| Example | Key lesson |
|---|---|
| **1** | Legitimate companies will not ask for personal information, nor supply a link in an email. They ask you to log into their site **directly from your browser** and check your account. |
| **2** | Typos in an "official" message are a warning sign. Clicking the link leads to a site built to steal **email credentials**. |
| **3** | Poor use of English. The attachment can be submitted to **virustotal.com**, which flagged possible malicious links in the file. |
| **3 (links)** | Shortened links hide the real destination. Hover to check, and use link-checking tools: checkshorturl.com, urlvoid.com. |
| **4** | Same approach: hover over links and check them with checkshorturl.com, urlvoid.com, scanurl.net (the example used an is.gd shortened link). |
| **5** | A genuine email from a professional enterprise will **not ask you to do authentication-based tasks**. |
| **6 (non-phishing)** | A **genuine** email does not ask you to update your password or particulars by clicking a link. Extra precaution: open links inside a **VM**. |
| **7** | Phishing, identified from the **message header**: the "Received" line shows it came from an unrelated domain (cnsmtp03.com), not Microsoft/Outlook. |
| **8** | Awkward phrasing; asks the receiver to log in "as soon as possible"; "PayPal Support" sending from an outlook.com address. Confirmed by viewing the **message source** and checking the "Received from" information. |

### Spear Phishing
The attacker targets **you specifically**:
- They know a bit about you (your **online profile**)
- They know your name, so the email is **personalised**
- Use of **URL shorteners** to hide the actual link
- May contain a **malicious payload**
- Warning signs: **inconsistent message headers** and **suspicious URLs**

### Spotting Phishing in General
- **Not personalised** — legitimate businesses use a personal salutation (except in spear phishing)
- The "from" address displayed **doesn't match** the full message details ("Received from"), e.g. a misleading or different domain name
- **Awkward phrasing and spelling errors** (less likely from a professional enterprise)
- **Sense of urgency** — a need for fast response, or unrealistic threats ("click NOW or else...")
- **Links to click** — hover, don't click; watch for deceptive URLs redirecting elsewhere or "shortened" links
- Asks for **private personal or financial info**
- Compels you to **validate or confirm your account** by entering authentication information

> These signs are **not mutually exclusive** — several often appear together.

### PhishTank
- A website where people submit **suspected phishing sites** (phishtank.com).
- Provides an **API** so developers can check sites against known phishing sites.

---

## 3. Pharming

**Definition:** a cyber attack that **redirects a website's traffic to another, fake site**.

**Two main routes:**
1. Changing the **hosts file** on a victim's computer
2. Exploiting a **vulnerability in DNS server software**

**Core idea:** tamper with name resolution so that the domain name of the target application points to an **attacker-controlled server**.

### How it works
1. You type a URL with a domain name.
2. The request goes to **DNS**, which translates the domain into an **IP address**.
3. Your browser connects to that IP address and loads the website.
4. In pharming, DNS is **"poisoned"**, e.g. your local DNS cache is corrupted through a malware infection or attack.
5. You type the **legitimate address** but are sent to the attacker's phishing website.

- Pharming is **less common** than phishing.
- **Spotting a fake site:** check the **URL** shown in the browser address bar.

---

## 4. Social Engineering: No-Tech Attacks

- Social engineering attacks **exploit basic vulnerabilities in human psychology**.
- Course analogy: the TV show *White Collar*, where FBI consultant Neal Caffrey is a brilliant social engineer who evaded the FBI for years.

### The Five Techniques

#### 4.1 Authority
- People **respect authority**, even something as simple as a **uniform** (e.g. a fireman or cable guy).
- The attacker poses in a position of authority or as a service provider, so the target feels they should trust.
- **Types of authority** that can be exploited:
  - **Legal** — based on government and law; generally applies to law/safety enforcement officers
  - **Organizational** — defined by an organization; typically a supervisory hierarchy
  - **Social** — within a social group (co-workers, college friends, any gathering of people); the attacker asks or pressures the target for information

#### 4.2 Charm (Empathy)
- Make people **like or sympathise** with you — people **want to help**.
- Used in the lecture for **social engineering passwords** and in the context of **CSRF**.

#### 4.3 Pretext
- The attacker creates a good **pretext**: a **fabricated scenario**, and prepares for expected questions.
- Used to steal victims' personal information or targeted objects.
- More advanced attacks try to trick targets into doing something that abuses an organization's **digital and/or physical weaknesses**.
- Example: Neal Caffrey gave a pretext to police officers to get them to do something they wouldn't normally do, helping him break into a car.
- A pretext is an **elaborate lie**: the attacker may impersonate people in positions of authority, or create a situation that makes people inclined to help.
- Charm is sometimes categorised as pretext, since there may be **no definitive dividing line**.

#### 4.4 Baiting
- Uses a **false promise** to pique a victim's **greed or curiosity**.
- Lures users into a trap that steals personal information or infects their systems with malware.
- **Physical baiting:** leaving malware-infected flash drives in conspicuous areas.
- **Online baiting:** enticing ads leading to malicious sites, or encouraging downloads of a malware-infected application.

#### 4.5 Reciprocation
- **Reciprocity** is the expectation that you will treat others the way they treat you.
- People don't want to be indebted; it is human nature to feel **obliged to return a favour**.
- The attacker manipulates the victim into feeling **grateful or obligated**, or into compliance by promising future benefits or supplying something they need or want.
- Also known as **Quid Pro Quo**.
- **Classic experiment:** in 1974, sociologist Philip Kunz (Brigham Young University) sent Christmas cards to 600 strangers. Within 5 days, **more than 200 replied**, even though they didn't know him.
- Providing a **pretext** to entice an interaction — the main approach is reciprocation.

### Discussion Prompts in the Slides
The Authority and Pretext sections each ended with a **"Mitigation?"** discussion prompt and a **real-world example** slide. These were image-based, so no written answers appear in the slide text. Think about how you would defend against each technique, for example verifying identity through a separate channel before acting on a request.

---

## Summary

- People are the **weakest link** in the system.
- **Phishing** — various examples of phishing and non-phishing emails, and how to spot a potential phishing email.
- **Pharming** — redirecting web traffic via the hosts file or DNS cache poisoning.
- A **fake website** can be used in conjunction with pharming; know how to recognise one.
- **Social engineering (no-tech attacks)** — Authority, Charm, Pretext, Baiting, Reciprocation.
- Social engineering attacks exploit basic vulnerabilities in **human psychology**.
- Next lecture: **Network Security** (and an ACW2 briefing).

## Key Takeaways
- Attackers go after the **user** when the technology is strong.
- **Phishing red flags:** impersonal greeting, mismatched sender/"Received from" domain, poor spelling and grammar, urgency or threats, suspicious or shortened links, and requests for credentials or financial info.
- **Defences:** hover over links without clicking, check suspicious links and files with tools (urlvoid, checkshorturl, scanurl, virustotal), inspect the **full message header**, never log in through emailed links, and report to PhishTank.
- **Phishing vs. pharming:** phishing tricks the *user* into visiting a fake site; pharming silently redirects the *traffic* via the hosts file or DNS, so the URL you typed was correct but the destination is not.
- The five social engineering levers map to psychological tendencies: **obedience to authority, liking/empathy, trust in a believable story, greed/curiosity, and the urge to repay favours**.
